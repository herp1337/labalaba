#!usr/bin/env python
# coding: utf8
#HeroBrine404
import urllib2,sys,os
# Set Colors ######
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
##################
def find(link,path):
	berkas=""
	daf=open(path,"r")
	dfr=daf.readlines()
	for x in dfr:
		tp=link+"/"+x
		try: 
			urllib2.urlopen(tp) 
		except urllib2.HTTPError as e: 
			print "%s[*]%s %s => %s"%(Y,G,tp,e)
			berkas +="[*] %s => %s\n"%(tp,e)
		except URLError as e:
			print "%s[*]%s %s => %s"%(Y,G,tp,e)
			berkas +="[*] %s => %s\n"%(tp,e)
		else:
			print "%s[*]%s %s => 200"%(Y,G,tp)
			berkas +="[*] %s => 200\n"%(tp,e)
						
	print "%s[!] %sComplete"%(Y,C)
	input=raw_input("%s[?]Do You Want Save Y/N: "%(Y))
	if input.lower()=="y":
		nama=raw_input("%s[?]File Name: "%(G))
		wibu=open(nama,"w+")
		wibu.write(berkas)
	else:
		sys.exit()