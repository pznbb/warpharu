import os
class Config(object):

    WARP_ID = os.environ.get('WARP_ID', None) 
    THREAD_COUNT = os.environ.get('THREAD_COUNT', "999999999999999999999999999") 
