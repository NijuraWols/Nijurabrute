
	def __init__(self):
		self.useragent = "Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0" #header için
		self.contenttype = "application/x-www-form-urlencoded; charset=UTF-8" # header için
		self.link = "http://domains.yougetsignal.com/domains.php" # post isteğini yapacağım link
		self.key = "" # gönderilen boş bir değer
 
	def gonder(self,target): # fonksiyonumuz
		if target.startswith("http",0,4): # eğer gelen değerin ilk 4 karakteri http ise 
			return -1 # return -1
		self.hedef = target # gelen hedef
		self.values = [("remoteAddress",self.hedef),("key",self.key)] # list
		data = urllib.urlencode(self.values) # html olarak encode ettik
		req = urllib2.Request(self.link, data) # request isteğimiz
		req.add_header("Content-type", self.contenttype) # header eklendi
		req.add_header("User-agent", self.useragent) # header eklendi
		response = urllib2.urlopen(req) # isteğimizi yapıyoruz
		veri = json.loads(response.read()) # dönen değeri okuduk ve json'a ekledik
		if veri["status"] == "Fail": # status fail ?
			return -2 # return -2 
		return veri["domainArray"] # domainArray döndür

