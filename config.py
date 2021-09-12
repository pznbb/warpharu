import os
class Config(object):

    WARP_ID = os.environ.get('WARP_ID', "None")
    USE_PROXY = os.environ.get('USE_PROXY', "False")
    PROXY_API = os.environ.get('PROXY_API', "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
    # old: https://api.proxyscrape.com?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all
    # new: https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all
    THREAD_COUNT = os.environ.get('THREAD_COUNT', "1000")
    WAIT_SECS_FOR_NORMAL_MODE = os.environ.get('WAIT_SECS_FOR_NORMAL_MODE', 17)
