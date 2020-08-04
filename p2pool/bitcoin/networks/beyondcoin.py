import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 10333
ADDRESS_VERSION = 25
RPC_PORT = 10332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '12a765e31ffd4059bada1e25190f6e98c99d9714d334efa41a195a7e7e04bfe2')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('bynd_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'BYND'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Beyondcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Beyondcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.beyondcoin'), 'beyondcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.litecoin.net/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.litecoin.net/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.litecoin.net/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
