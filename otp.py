import time
import hmac
import hashlib
import struct

secret = b'MysecretKey'

time_step=300
current_time =int(time.time())
