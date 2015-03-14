import eventlet
eventlet.monkey_patch()

import os
import urllib3

TARGET_HOST = os.environ.get('TARGET_HOST', 'http://localhost:9200')
TARGET_PATH = os.environ.get('TARGET_PATH', '/test')

pool = urllib3.connection_from_url(TARGET_HOST)

for i in range(1000):
    try:
        pool.request('HEAD', TARGET_PATH)
    except:
        print('FAILED AT REQUEST %d' % i)
        raise
