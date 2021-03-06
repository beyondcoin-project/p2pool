import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'b7e2d781'.decode('hex')
P2P_PORT = 19333
ADDRESS_VERSION = 85
RPC_PORT = 19332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'beyondcoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'test'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('bynd_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'tBYND'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Beyondcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Beyondcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.beyondcoin'), 'beyondcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://test.beyondcoinexplorer.com/#/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://test.beyondcoinexplorer.com/#/address/'
TX_EXPLORER_URL_PREFIX = 'https://test.beyondcoinexplorer.com/#/transaction/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 1e8
