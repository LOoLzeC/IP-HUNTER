import requests,json,os,urllib,sys
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
def main():
	print W+"	==================================="
	print "	             IP-HUNTER "
	print "	        Created By LOoLzeC"
	print R+"	   _ _  _ _  _  _  ___  ___  ___ "
	print "	  | U || | || \| ||_ _|| __|| o \\"
	print "	  |   || U ||  \\ | | | | _| |   /"
	print "	  |_n_||___||_|\_| |_| |___||_|\\\\"
	print W+"	===================================\n	      "+B+"[+] "+W+"Coded By Deray "+B+"[+]\n"+W
	print B+"  1"+R+")"+W+" Mass Dumping HOST to IP With Weblist."
	print B+"  2"+R+")"+W+" Single Ip/hostname."
	print B+"  3"+R+")"+W+" Check My Public IP Adress."
	print B+"  4"+R+")"+W+" Generate Py Backdoors To Get Public Victim's IP Adress."
	print B+"  5"+R+")"+W+" Dumping Location From Public IP Adress."
	print B+"  6"+R+")"+W+" Mass Extract Page Links From Host."
	print B+"  7"+R+")"+W+" Info."
	print B+"  8"+R+")"+W+" Bye."
	print 
	choose=raw_input(''+W+'  choose#> ')
	if "1" in choose:
		host=raw_input(W+R+'  [+] '+W+'WEB LIST>>> ')
		try:
			word=open(host).readlines()
			hasil=len(word)
			print W+B+"  [*] "+W+R+str(hasil)+W+" HOST Loaded!"
			print W+B+"  [*] "+W+"Dumping IP from "+W+R+host+" "+W+"...\n"
			ww=open(host)
			for k in range(hasil):
				wordlist=ww.readline().replace('\n','')
				try:
					kkk=requests.get('http://ip-api.com/json/'+wordlist+'')
					OoO=json.loads(kkk.text)
					try:
						print W+R+"  [+] "+W+wordlist+R+" ========> "+W+"",OoO["query"]
					except:
						print W+R+"  [-] "+wordlist+" ========> Unknown!"
				except:
					print W+R+"  [-] Fuck ur connections!"
					raw_input(W+R+'  [!] '+W+'Press enter to menu...')
					os.system('clear')
					main()
			print W+B+"\n  [*] "+W+"Finished."
			raw_input(W+R+'  [!] '+W+'Press enter to menu...')
			os.system('clear')
			main()
		except:
			print W+R+"  [-] OH F*ck! List '"+host+"' Not Found Bitch."
			raw_input('  [!] '+W+'Press enter to menu...')
			os.system('clear')
			main()
		
	elif "2" in choose:
		target=raw_input(W+R+'  [+] '+W+'TARGET IP OR HOSTNAME>>> ')
		print 
		line="="*10
		print W+R+"  ["+line+W+" Host "+target+R+" "+line+"]"
		print 
		print W+B+"  1"+W+R+") "+W+"Get Ip From"+W+R+"",target
		print W+B+"  2"+W+R+")"+W+" Get Host+IP From"+W+R+"",target
		print W+B+"  3"+W+R+")"+W+" Get Host+IP+LOCATION from"+W+R+"",target
		print 
		pilih=raw_input(W+'  choose> ')
		if "1" in pilih:
			print W+B+"  [*] "+W+"Getting Ip From "+W+R+target+" ...\n"
			try:
				print R+"  [+]"+W+" IP :"+W+G+"", requests.get('http://ip-api.com/json/'+target+'').json()["query"]
			except:
				print W+R+"\n  [-] Fuck ur connections!"
				raw_input('  [!]'+W+' Press enter to menu...')
				os.system('clear')
				main()
			print W+B+"\n  [*] "+W+"Finished."
			raw_input(R+'  [!] '+W+'Press enter to menu...')
			os.system('clear')
			main()
		elif "2" in pilih:
			print W+B+"  [*] "+W+"Getting HOST from "+R+target+" ..."
			rr=requests.get('https://api.hackertarget.com/reverseiplookup/?q='+target+'')
			if "error" in rr.text:
				print W+R+"  [-] "+W+"Host => "+R+"Unknown!"
				print W+R+"  [-] "+W+"Please Input Host Without http or https"
				print W+B+"  [*] "+W+"Example : "+B+"site.com"
				print W+B+"  [*] "+W+"Byeee."
				raw_input(R+'  [!]'+W+' Press enter to menu...')
				os.system('clear')
				main()
			else:
				print W+B+"  [*] "+W+"Saving Host Result From "+R+target+" ..."
				name='reverse_from_'+target+'.txt'
				try:
					os.mkdir('reverse')
					filename=open('reverse/'+name+'','w')
				except:
					filename=open('reverse/'+name+'','w')
				filename.write(rr.text)
				filename.close()
				print W+B+"  [*]"+W+" Writted! Saved To :"+R+"",name
				print 
				print W+B+"  [*] "+W+"Dumping IP from List"+R+"",name
				buka=open('reverse/'+name).readlines()
				total=len(buka)
				print W+B+"  [*] "+R+s
