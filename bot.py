try:
    from colorama import *
    import requests,json,time,os,binascii
    r = requests.Session()
except ImportError:exit('module not installed\nplease send command pip3 install -r requirements.txt')

readtimer = 'https://api.cc.lerjin.com/reading/timer'
obtreward = 'https://api.cc.lerjin.com/reading/obtainReward'
rwlist = 'https://api.cc.lerjin.com/reward/list'
oprw = 'https://api.cc.lerjin.com/reward/treasureChest/open'
spin = 'https://api.cc.lerjin.com/activity/spin'
init(autoreset=True)
merah = Fore.LIGHTRED_EX
kuning = Fore.LIGHTYELLOW_EX
hijau = Fore.LIGHTGREEN_EX
biru = Fore.LIGHTBLUE_EX
magenta = Fore.LIGHTMAGENTA_EX
cyan = Fore.LIGHTCYAN_EX
hitam = Fore.LIGHTBLACK_EX
putih = Fore.LIGHTWHITE_EX
reset = Fore.RESET

def tunggu(t):
    while t:
        print(f'[●         ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●        ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●       ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●      ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●●     ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●●●    ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●●●●   ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●●●●●  ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●●●●●● ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●●●●●●●] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        t -= 1

def banner():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        getpw = r.get('https://akasakaid.github.io/cpcp/bener.txt').text
        getpww = r.get('https://akasakaid.github.io/cpcp/info.txt').text
        info = json.loads(r.get('https://akasakaid.github.io/cpcp/info.json').text)
        ban = f"{kuning}____ _    _ ___  ____ _    ____ ___  ____ \n|    |    | |__] |    |    |__| |__] [__  \n|___ |___ | |    |___ |___ |  | |    ___]\n"
        print(ban)
        print(f'{putih}author {merah}:',hijau+info['author'])
        print(f'{putih}forum {merah}:',biru+info['forum'])
        print(f'{putih}versi {merah}:',kuning+info['versi'])
        print(f'{putih}pesan {merah}:',cyan+info['pesan'])
        print(' ')
        if not os.path.exists('.pw.txt'):
            with open('.pw.txt','w') as nulis:
                nulis.write('akasakaid gans')
        with open('.pw.txt') as file:
            data = file.read()
            password = str(binascii.unhexlify(getpw),'utf-8')
            if data != password:
                print(f'{putih}dapatkan password di',hijau+getpww)
                while True:
                    pw = input(f'{cyan}masukkan password {merah}: {putih}')
                    if pw == '':continue
                    if pw != password:continue
                    break
                with open('.pw.txt','w') as nulis:
                    nulis.write(pw)
    except KeyboardInterrupt:exit()
    except Exception as e:exit(e)
    except ConnectionError:exit(f'{merah}tidak ada koneksi internet , periksa koneksi internet anda !!')

banner()
try:
    if not os.path.exists('config.json'):
        uuid = input(f'{kuning}input your uuid {merah}:{putih} ')
        userid = input(f'{kuning}input your userid {merah}:{putih} ')
        token = input(f'{kuning}input your token {merah}:{putih} ')
        if uuid == '' or userid == '' or token == '':exit(f'{merah}tolong jangan mengkosongin bagian itu !!')
        with open('config.json','w') as file:
            isi = {"uuid":uuid,"userid":userid,"token":token}
            json.dump(isi,file)
except Exception as e:exit(e)
with open('config.json') as data:
    data = data.read()
    uuid = json.loads(data)["uuid"]
    userid = json.loads(data)["userid"]
    token = json.loads(data)["token"]

headers = {
    "Host": "api.cc.lerjin.com",
    "charset": "UTF-8",
    "device-type": "2",
    "api-version": "2",
    "external-version": "1.8.2",
    "device": "8.1.0",
    "version": "40",
    "timezone": "7",
    "token": token,
    "uuid": uuid,
    "app-id": "ClipClaps_google",
    "content-type": "application/json; charset=UTF-8",
    "user-agent": "okhttp/4.2.1"
}
print(f'{cyan}- '*25)
print(f"""{magenta}╔╦╗┌─┐┌─┐┌─┐  ╔═╗┌─┐┬┌┐┌
║║║├┤ │ ┬├─┤  ╚═╗├─┘││││
╩ ╩└─┘└─┘┴ ┴  ╚═╝┴  ┴┘└┘""")
print(f'{cyan}- '*25)
try:
    req = 0
    data = json.dumps({"spinType":"mega","token":token,"userid":userid,"_reqidx":req});req += 1
    r1 = r.post(spin,headers=headers,data=data).text
    r2 = json.loads(r1)
    if r2['msg'] != 'Success':print(merah+r2['msg'])
    else:
        tipe = r2['data']['reward']['type']
        jumlah = r2['data']['reward']['quantity']
        print(f'{putih}mendapatkan hadian jenis {hijau}{tipe} {putih}sebesar {hijau}{jumlah}')
except ConnectionError:exit(f'tidak ada koneksi internet , periksa koneksi internet anda !!')
except KeyboardInterrupt:exit(' ')
except Exception as e:exit(f'error : {e}')
print(f'{cyan}- '*25)
print(f"""{magenta}╦  ┬ ┬┌─┐┬┌─┬ ┬  ╔═╗┌─┐┬┌┐┌
║  │ ││  ├┴┐└┬┘  ╚═╗├─┘││││
╩═╝└─┘└─┘┴ ┴ ┴   ╚═╝┴  ┴┘└┘""")
print(f'{cyan}- '*25)
try:
    for __ in range(5):
        data = json.dumps({"spinType":"lucky","token":token,"userid":userid,"_reqidx":req});req += 1
        r1 = r.post(spin,headers=headers,data=data).text
        r2 = json.loads(r1)
        if r2['msg'] != 'Success':print(merah+r2['msg']);break
        else:
            tipe = r2['data']['reward']['type']
            jumlah = r2['data']['reward']['quantity']
            print(f'{putih}mendapatkan hadian jenis {hijau}{tipe} {putih}sebesar {hijau}{jumlah}')
except ConnectionError:exit(f'tidak ada koneksi internet , periksa koneksi internet anda !!')
except KeyboardInterrupt:exit(' ')
except Exception as e:exit(f'error : {e}')

try:
    data = json.dumps({"userid":userid,"token":token})
    r1 = r.post(readtimer,headers=headers,data=data).text
    r2 = json.loads(r1)
    if r2['msg'] != 'Success':exit(f'{merah}gagal login !!\nperiksa kembali uuid,userid,token, hapus file config.json , pastikan semua benar dah ulangi lagi program ini !!')
    day = r2['data']['day']
    aktifday = r2['data']['activeDay']
    videotime = r2['data']['videoTime']
    artikeltime = r2['data']['articleTime']
    timerr = r2['data']['config']['timerReward']
    versi = r2['data']['config']['version']
except ConnectionError:exit(f'tidak ada koneksi internet , periksa koneksi internet anda !!')
except KeyboardInterrupt:exit('')
except Exception as e:exit(e)

print(f'{cyan}- '*25)
print(f"""{magenta}╦  ╦┌─┐┌┬┐┌─┐  ╦  ╦┬┌┬┐┌─┐┌─┐
╚╗╔╝│ │ │ ├┤   ╚╗╔╝│ ││├┤ │ │
 ╚╝ └─┘ ┴ └─┘   ╚╝ ┴─┴┘└─┘└─┘""")
print(f'{cyan}- '*25)
funytime = 'https://api.cc.lerjin.com/funny/timer'
funyreward = 'https://api.cc.lerjin.com/funny/obtainReward'
try:
    a = r.post(funytime,headers=headers,data=data).text
    b = json.loads(a)
    datas = b['data'];hari = datas['day'];aktifday = datas['activeDay'];artikeltime = datas['articleTime'];versi = datas['config']['version'];video = datas['config']['timerReward']
    for vid in video:
        spesifik = vid['specific'];tim = vid['time'];tipe = vid['rewardType']
        data = json.dumps({"specific":spesifik,"token":token,"rewardTime":tim,"articleTime":artikeltime,"version":versi,"rewardType":tipe,"day":hari,"videoTime":tim,"activeDay":aktifday,"userid":userid})
        c = r.post(funyreward,headers=headers,data=data).text
        d = json.loads(c)
        mes = d['msg']
        if mes != 'Success':print(f'{merah}video sudah divoting')
        else:print(f'{hijau}sukses voting video')
        time.sleep(2)
except ConnectionError:exit(f'{merah}tidak ada koneksi internet , periksa koneksi internet anda !!')
except KeyboardInterrupt:exit()

print(f'{cyan}- '*25)
print(f'''{magenta}┌┬┐┌─┐┌┐┌┌─┐┌┐┌┌┬┐┌─┐┌┐┌  ┬  ┬┬┌┬┐┌─┐┌─┐
│││├┤ ││││ ││││ │ │ ││││  └┐┌┘│ ││├┤ │ │
┴ ┴└─┘┘└┘└─┘┘└┘ ┴ └─┘┘└┘   └┘ ┴─┴┘└─┘└─┘''')
print(f'{cyan}- '*25)
try:
    for dd in timerr:
        waktu = dd['time']
        rwtp = dd['rewardType']
        specifik = dd['specific']
        data = json.dumps({"specific":specifik,"token":token,"rewardTime":waktu,"articleTime":artikeltime,"version":versi,"rewardType":rwtp,"day":day,"videoTime":waktu,"activeDay":aktifday,"userid":userid})
        r9 = r.post(obtreward,headers=headers,data=data).text
        r10 = json.loads(r9)
        if r10['msg'] != "Success":print(f'{merah}video sudah ditonton')
        else:print(f'{hijau}sukses menonton video{magenta}')
        time.sleep(2)
except ConnectionError:exit(f'{merah}tidak ada koneksi internet , periksa koneksi internet anda !!')
except KeyboardInterrupt:exit('')
except Exception as e:exit(e)
print(f'{cyan}- '*25)
print(f'''{magenta}╦ ╦┌─┐┬─┐┌┬┐┌─┐  ┬┌─┌─┐┬─┐┬ ┬┌┐┌
╠═╣├─┤├┬┘ │ ├─┤  ├┴┐├─┤├┬┘│ ││││
╩ ╩┴ ┴┴└─ ┴ ┴ ┴  ┴ ┴┴ ┴┴└─└─┘┘└┘''')
print(f'{cyan}- '*25)
try:
    data = json.dumps({"token":token,"finishCashOutGuide":"false","userid":userid})
    r11 = r.post(rwlist,headers=headers,data=data).text
    r12 = json.loads(r11)
    jmlhd = r12['data']['treasureChest']
    for xx in jmlhd:
        print(f'{hijau}membuka kotak harta karun jenis',kuning+xx['type'])
        print(f'{hijau}jumlah kotak harta karun',kuning+str(xx['num']))
        if xx['num'] == 0:continue
        kotak = 1
        for xxx in range(int(xx['num'])):
            print('membuka kotak harta karun ke',kotak)
            data = json.dumps({"type":xx['type'],"token":token,"userid":userid})
            ae = r.post(oprw,data=data,headers=headers).text
            aej = json.loads(ae)
            hdd = aej['data']['rewards']
            for aep in hdd:
                print(f'{hijau}mendapatkan hadiah jenis',putih+aep['type'],f'{hijau}sebesar',putih+str(aep['quantity']))
            kotak += 1
            time.sleep(3)
except ConnectionError:exit(f'tidak ada koneksi internet , periksa koneksi internet anda !!')
except KeyboardInterrupt:exit('')
except Exception as e:exit(e)


print(f'{cyan}- '*25)
print(f'''{magenta}╔╗ ┌─┐┬─┐┌┬┐┌─┐┬┌┐┌  ╔═╗┌─┐ ┬ ┬┌─┐┬─┐┬┬ ┬┌┬┐
╠╩╗├┤ ├┬┘│││├─┤││││  ╠═╣│─┼┐│ │├─┤├┬┘││ ││││
╚═╝└─┘┴└─┴ ┴┴ ┴┴┘└┘  ╩ ╩└─┘└└─┘┴ ┴┴└─┴└─┘┴ ┴''')
print(f'{cyan}- '*25)
try:
    userlogin = 'https://game.cc.clipclaps.tv/user/login'
    data = json.dumps({"ccToken":token,"ccUserId":userid})
    headers = {
        "Host": "game.cc.clipclaps.tv",
        "charset": "UTF-8",
        "token": "",
        "cache-control": "no-cache",
        "content-type": "application/json; charset=UTF-8",
        "user-agent": "okhttp/4.2.1"
    }
    r15 = r.post(userlogin,headers=headers,data=data).text
    r16 = json.loads(r15)
    token = r16['data']['token']
    makan = 'https://game.cc.clipclaps.tv/aquarium/v1/fish/feed'
    headers = {
        "Host": "game.cc.clipclaps.tv",
        "charset": "UTF-8",
        "token": token,
        "cache-control": "no-cache",
        "content-type": "application/json; charset=UTF-8",
        "user-agent": "okhttp/4.2.1"
        }
    gameindex = 'https://game.cc.clipclaps.tv/game/index'
    data = json.dumps({})
    r17 = r.post(gameindex,headers=headers,data=data).text
    r18 = json.loads(r17)
    idakuarium = r18['data']['special'][3]['id']
    reqid = 0
    headers = {
        "Host": "game.cc.clipclaps.tv",
        "origin": "https://h5.cc.lerjin.com",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.75 Mobile Safari/537.36",
        "token": token,
        "content-type": "application/json",
        "accept": "*/*",
        "referer": "https://h5.cc.lerjin.com/aquarium/1.2.0/",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "x-requested-with": "com.sanhe.clipclaps"
    }
    while True:
        print('Memberi makan ikan ...           ',flush=True,end='\r')
        time.sleep(2)
        data = json.dumps({"gameId":idakuarium,"_reqidx":reqid})
        r19 = r.post(makan,headers=headers,data=data)
        reqid += 1
        r20 = json.loads(r19.text)
        if r20['code'] == 'ALL_FISH_FULL':tunggu(300);continue
        if r20['code'] == 'FEED_COUNT_LIMIT':exit(f'{biru}sudah mencapai limit harian !!\nsilahkan ulangi lagi besok !!')
        if r20['code'] == 'LACK_OF_BALANCE':exit(f'{merah}makanan ikan sudah habis, silahkan ulangi lagi nanti')
        namaikan = r20['data']['fish']['name']
        levelikan = r20['data']['fish']['level']
        print(f'{hijau}Nama ikan {merah}: {putih}{namaikan} | {hijau}level ikan {merah}: {putih}{levelikan}')
        buble = r20['data']['bubbles']
        pikbuble = 'https://game.cc.clipclaps.tv/aquarium/v1/bubbles/pick'
        if buble:
            for bb in buble:
                data = json.dumps({"id":bb['id'],"gameId":idakuarium,"_reqidx":reqid})
                r21 = r.post(pikbuble,headers=headers,data=data)
                r22 = json.loads(r21.text)
                hdb = r22['data']['count']
                print(f'{hijau}Mendapatkan {putih}{hdb} {hijau}bubble     ')
                reqid += 1
        reqid += 1
        tunggu(10)
except ConnectionError:exit(f'{merah}tidak ada koneksi internet , periksa koneksi internet anda !!')
except KeyboardInterrupt:exit('')
