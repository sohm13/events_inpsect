import asyncio
import logging
import time
import sqlalchemy

from web3 import Web3
from web3._utils.filters import Filter
from web3.types import (
    LogReceipt,
     Optional
    )
from sqlalchemy import orm  

from schemas.sync_event import SyncEvent
from schemas.pair import Pair
from models.sync_event import SyncEventModel
from events import EthEvent, EventLogsId
from crud.sync_event import write_sync_events

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s  - %(message)s')
logger = logging.getLogger(__name__)






class BlockChainScan:
    poll_interval = 1

    def __init__(self, web3: Web3, pairs_for_scan: list[Pair]):
        self.w3: Web3 = web3
        self.pairs: list[Pair] = pairs_for_scan
        self.eth_event: EthEvent = EthEvent(self.w3)

    def handle_event(self, event: LogReceipt, db_session: Optional[orm.Session]):
        if event.topics[0].hex() == EventLogsId.Sync:
            event_rec: SyncEvent = self.eth_event.pars_sync_event(event)
            if db_session:
                write_sync_events(db_session, [event_rec])
            # logger.info(f'Block:{event_rec.block_number}, Pair:{event_rec.pair_address}, Reserves{[event_rec.reserve0, event_rec.reserve1]}, hash:{event_rec.hash}')
            logger.info(f'{event_rec.dict()}')

    async def log_loop(self, event_filter: Filter, db_session: Optional[orm.Session]):
        while True:
            for event in event_filter.get_new_entries():
                self.handle_event(event, db_session)
            await asyncio.sleep(self.poll_interval)

    def _scan(self, events: list[Filter], db_session: Optional[orm.Session]):
        tasks = [self.log_loop(event, db_session) for event in events]
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(
                asyncio.gather(*tasks)
                )
        finally:
            loop.close()

    def scan_sync_event_loop(self, db_session: Optional[orm.Session] = None):
        events = [self.eth_event.sync_event(pair.address) for pair in self.pairs]
        self._scan(events, db_session)



