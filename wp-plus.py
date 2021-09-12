#!/usr/bin/python

from pathlib import Path
from datetime import datetime
import urllib.request
import requests
import json
import random
import os
import string
import time
import threading
import ssl
from config import Config

fake_ssl_context = ssl._create_unverified_context()

def gen_str(str_len):
	return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_len))		    
def digit_str(str_len):
	return ''.join((random.choice(string.digits) for _ in range(str_len)))

def gen_request(warp_id):
	install_id = gen_str(22)
	body = {"key": "{}=".format(gen_str(43)),
			"install_id": install_id,
			"fcm_token": "{}:APA91b{}".format(install_id, gen_str(134)),
			"referrer": warp_id,
			"warp_enabled": False,
			"tos": datetime.now().isoformat()[:-3] + "+02:00",
			"type": "Android",
			"locale": "es_ES"}
	data = json.dumps(body).encode('utf8')
	headers = {'Content-Type': 'application/json; charset=UTF-8',
				'Host': 'api.cloudflareclient.com',
				'Connection': 'Keep-Alive',
				'Accept-Encoding': 'gzip',
				'User-Agent': 'okhttp/3.12.1'}
	return urllib.request.Request(f'https://api.cloudflareclient.com/v0a{digit_str(3)}/reg', data, headers)

# This mode doesn't use Proxy, thus doesn't support multithreading and bypass the 18sec wait.
def normal_mode(warp_id): 
	print("[i] No proxy mode selected, processing...")
	sucess_req = 0
	failed_req = 0
	while True:
		try:
			response = urllib.request.urlopen(gen_request(warp_id))
			response.close()
		except Exception as error:
			failed_req += 1
			print(f"[:(] An error occurred while sending request: \n{error}")	
		else:
			if response.getcode() == 200:
				sucess_req += 1
				print(f"[:)] Added 1 GB to the WARP ID.")
				print(f"[i] Total: {sucess_req} Sucess | {failed_req} Failed")
				print("[i] After 18 seconds, a new request will be sent.")
				time.sleep(int(Config.WAIT_SECS_FOR_NORMAL_MODE))
			else:
				failed_req += 1
				print(f"[:(] Error when connecting to server, server response: \n{response.json()}")
				print(f"[i] Total: {sucess_req} Sucess | {failed_req} Failed")
		time.sleep(1) # Wait 1 seconds before send a new request.

def threaded_proxy_process(thread_name, warp_id, proxies):
	def tprint(*args, **kwargs):
		print(f"{thread_name}: ",*args, **kwargs)
	tprint("Started.")
	sucess_req = 0
	failed_req = 0
	while True:
		try:
			req = gen_request(warp_id)
			proxy = random.choice(proxies)
			req.set_proxy(proxy, 'http')
			tprint(f"Using proxy: {proxy}")
			tprint(f"URL: {req.full_url}")
			response = urllib.request.urlopen(req, context=fake_ssl_context)
		except Exception as error:
			failed_req += 1
			tprint(f"[:(] Error: \n{error}")	
		else:
			if response.getcode() == 200:
				sucess_req += 1
				tprint("Added 1 GB to the WARP ID.")
			else:
				failed_req += 1
				tprint(f"[:(] Error, server response: \n{response.json()}")
			tprint(f"[i] Total: {sucess_req} Sucess | {failed_req} Failed")
		time.sleep(0.1) # Wait 0.1 seconds before send a new request.

def proxy_mode(warp_id):
	proxies = None
	with open("./http_proxies.txt", "r") as proxies_file:
		proxies = proxies_file.readlines()
	threads_str = Config.THREAD_COUNT # input("[?] How many threads do you want to use?: ")
	if threads_str.isdigit():
		threads = []
		for i in range(int(threads_str)):
			print(f"Creating thread {i}...")
			tiny_thread = threading.Thread(target=threaded_proxy_process, args=(f"T-{i}",warp_id,proxies))
			threads.append(tiny_thread)
			tiny_thread.start()
		print("All threads are running, starting main thread...")
		threaded_proxy_process("T-Main", warp_id, proxies)
			
	else:
		print("[:(] Invalid number of threads: %s" % threads_str)

print("[i] WARP+ Unlimited GB - ALIAPRO & teppyboy & HuzunluArtemis")
print("""[!] Proxies helps this script bypass the 18s cooldown before sending 
a new request, and also speed up the process by multithreading.
Note that this script reads proxies from 'http_proxies.txt' and
the proxy format is 'proxy':'port'""")

if not Config.USE_PROXY:
	print("[i] WARP+ Unlimited GB - Using Normal Mode")
	normal_mode(Config.WARP_ID)
else:
	print("[i] WARP+ Unlimited GB - Using Proxy Mode")
	print("[i] Using Prox API: " + Config.PROXY_API)
	print("[i] Thread Count: " + Config.THREAD_COUNT)
	# check and remove proxy file
	if os.path.isfile('./http_proxies.txt') or os.path.exists('./http_proxies.txt'):
		os.remove('./http_proxies.txt')
	# get proxy file
	r = requests.get(Config.PROXY_API)
	resp = r.text.replace('\n','')
	with open('./http_proxies.txt','w') as fd:
    		fd.write(resp)
	#
	proxy_mode(Config.WARP_ID)