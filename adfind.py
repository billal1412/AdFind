# copyright 2019 BILLAL
# Codded By Billal Fauzan
import sys,os
try:
	import requests,sys
except Exception as E:
	print ("[Err]: "+str(E))

def save(path):
	o = open("found.txt","a")
	o.write(path+"\n")
	o.close()

def banner():
	os.system("clear")
	print ("""\033[33;1m
    ___       _________           __
   /   | ____/ / ____(_)___  ____/ /
  / /| |/ __  / /_  / / __ \/ __  /
 / ___ / /_/ / __/ / / / / / /_/ /
/_/  |_\__,_/_/   /_/_/ /_/\__,_/ \033[32;1mBL4CK DR460N\033[0m""")

def crack(target,path):
	hasil = 0
	try:
		r = requests.get("%s/%s"%(target,path))
		if r.status_code == 200:
			print ("\033[33;1m[+] Found: \033[32;1m%s/%s\033[0m"%(target,path))
			save(target+"/"+path)
			hasil += 1
		else:
			print ("\033[33;1m[-] Trying: \033[31;1m%s\033[0m"%(path))
		return hasil
	except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError):
		print ("\033[33;1m[-] \033[31;1mConnection ERROR\033[0m")
		sys.exit()
	except requests.exceptions.MissingSchema:
		print ("\033[33;1m[-] \033[31;1mError: please use http:// or https:// \033[0m")
		sys.exit()
	except KeyboardInterrupt:
		print ("\033[33;1m[-] \033[31;1mExit? \033[32;1mOK\033[0m")
		sys.exit()
def buka(file):
	return open(file,"r").read()

def main():
	banner()
	print ("\n\033[34;1m[*] Input Hostname (Ex:https://google.com)\033[0m")
	target = raw_input("\033[37;1m[?]  adfind@localhist~#> \033[32;1m")
	y = raw_input("\033[37;1m[?] Path Default? (Y/n): \033[31;1m")
	if y in ["Y","y"]:
		op = buka("path.txt")
		for path in op.splitlines():
			crack(target,path)
	elif y in ["N","n"]:
		op = buka(raw_input("\033[37;1m[?] File Path: \033[32;1m"))
		hasil = ""
		for path in op.splitlines():
			crack(target,path)
#		print ("\033[32;1m[!] DONE\n[*] Total Path: \033[33;1m%s\033[0m"%(hasil))
		sys.exit()
main()
