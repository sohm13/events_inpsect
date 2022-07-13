from blockchain_scan import Pair, BlockChainScan
from web3_provider import MyWeb3
from db import get_inspect_session



if __name__ == "__main__":

    web3 = MyWeb3('bsc')
    web3 = web3.get_http_provider()
    db_session_inspect =  get_inspect_session()

    pairs = [
        Pair( address='0x16b9a82891338f9bA80E2D6970FddA79D1eb0daE', symbol='BUSD_WBNB'),
        Pair( address='0x8FA59693458289914dB0097F5F366d771B7a7C3F', symbol='MBOX_WBNB'),

    ]
    bsc_scan = BlockChainScan(web3, pairs)
    bsc_scan.scan_sync_event_loop()    
