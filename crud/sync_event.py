
from typing import List

from models.sync_event import SyncEventModel
from schemas.sync_event import SyncEvent

def write_sync_events(
        db_session,
        sync_events: List[SyncEvent],
) -> None:

    sync_event_models = []
    for sync_event in sync_events:
        sync_event_models.append(
            SyncEventModel(
                # **sync_event.to_dict()
                reserve0 = sync_event.reserve0,
                reserve1 = sync_event.reserve1,
                hash = sync_event.hash,
                block_number = sync_event.block_number,
                transaction_index = sync_event.transaction_index,
                pair_address = sync_event.pair_address,
                method = sync_event.method
            )
        )
    if len(sync_event_models) > 0:
        db_session.bulk_save_objects(sync_event_models)
        db_session.commit()
