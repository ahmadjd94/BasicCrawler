#!usr/bin/python3
#"this is basic recursive web crawler that will traverse every url\ link in  certain domain "


import  urllib.request as r
from bs4 import BeautifulSoup as bs 
import sys
import urllib.parse as parse


def scanner (soup):          #the function that will scan urls
	global unvisited,visited,inp
	#if f.closed:
	#	f=open(sys.argv[1]+".txt",'a')

	try :
		so = r.urlopen(soup)
	except:
		print ("there was an error openning the url make sure you enter the url in the following format http://example.com")
		return
	
	visited.append(soup)
	#f.write(soup+'\n')

	s =bs(so)
	init =s.findAll('a') #this line will find every <a> tag in a page 

	for i in init:
		st=i['href']
		
		if st[:len(inp)]==inp :
			print("correct url")
			#print (st)
			if st not in visited:
				unvisited.append(st)   #append the discovered ulr to the unvisited array if it belongs to the same domain
		#except :print ("unknown error ")
		else:
			st=inp+st
			print(st)
			unvisited.append(st)

	
	print("__\n")
	#f.close()
	
	

if __name__=="__main__":
	if len(sys.argv)<2:
		print ("""this is basic recursive web crawler that will traverse every url\ link in  certain domain 
			enter the url you want to scan in the following format example.abc """)
		sys.exit()

	inp =sys.argv[1]
	
	if inp[:4]!="http" or inp[:5]!="https":
		inp="http://"+inp
	
	unvisited=[]
	visited=[]
	dic={}
	count=0
	nam=sys.argv[1].replace('.','')
	nam=nam.replace('/','')
	nam=nam.replace(':','')
	#f=open(nam,'w')
	
	scanner(inp)
	for each in unvisited :  #visit each unvisited url in the unvisited list
		if each not in visited:
				print ("trying "+ each)
				
				scanner(each)

				#except:
				#	print('error traversing url'+each)
		else:
			print ("this node was visited already")


	
	print (unvisited,visited)





	
	








