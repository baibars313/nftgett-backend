from Crypto.Cipher import AES
import binascii
import json
import requests
from urllib.parse import quote,unquote_plus


class BenefitAPIPlugin():

    def __init__(self):
        self.__action = ''
        self.__currency_code = ''
        self.__card_type = ''
        self.__amount = ''
        self.__password = ''
        self.__tranportal_id = ''
        self.__resource_key = ''
        self.__track_id = ''
        self.__response_url = ''
        self.__error_url = ''
        self.__udf1 = ''
        self.__udf2 = ''
        self.__udf3 = ''
        self.__udf4 = ''
        self.__udf5 = ''
        self.__url = ''
        self.bs = AES.block_size


    @property
    def action(self):
        return self.__url
    @action.setter
    def url(self,val):
        self.__url = val
        
    @property
    def action(self):
        return self.__action
    @action.setter
    def action(self,val):
        self.__action = val


    @property
    def currency_code(self):
        return self.__currency_code
    @currency_code.setter
    def currency_code(self,val):
        self.__currency_code = val

    
    @property
    def card_type(self):
        return self.__card_type
    @card_type.setter
    def card_type(self,val):
        self.__card_type = val

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self,val):
        self.__amount = val

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,val):
        self.__password = val

    @property
    def tranportal_id(self):
        return self.__tranportal_id
    @tranportal_id.setter
    def tranportal_id(self,val):
        self.__tranportal_id = val

    @property
    def resource_key(self):
        return self.__resource_key
    @resource_key.setter
    def resource_key(self,val):
        self.__resource_key = val

    @property
    def track_id(self):
        return self.__track_id
    @track_id.setter
    def track_id(self,val):
        self.__track_id = val

    @property
    def response_url(self):
        return self.__response_url
    @response_url.setter
    def response_url(self,val):
        self.__response_url = val

    @property
    def error_url(self):
        return self.__error_url
    @error_url.setter
    def error_url(self,val):
        self.__error_url = val
    
    @property
    def udf1(self):
        return self.__udf1
    @udf1.setter
    def udf1(self,val):
        self.__udf1 = val

    @property
    def udf2(self):
        return self.__udf2
    @udf2.setter
    def udf2(self,val):
        self.__udf2 = val

    @property
    def udf3(self):
        return self.__udf3
    @udf3.setter
    def udf3(self,val):
        self.__udf3 = val

    @property
    def udf4(self):
        return self.__udf4
    @udf4.setter
    def udf4(self,val):
        self.__udf4 = val

    @property
    def udf5(self):
        return self.__udf5
    @udf5.setter
    def udf5(self,val):
        self.__udf5 = val

    def request_data(self):
        
        plain_data = json.dumps([{
            'action':str(self.action),
            'currencycode':str(self.currency_code),
            'cardType':str(self.card_type),
            'amt': str(self.amount),
            'password':str(self.password),
            'id':str(self.tranportal_id),
            'resourceKey':str(self.resource_key),
            'trackId':str(self.track_id),
            'responseURL':str(self.response_url),
            'errorURL':str(self.error_url),
            'udf1':str(self.udf1),
            'udf2':str(self.udf2),
            'udf3':str(self.udf3),
            'udf4':str(self.udf4),
            'udf5':str(self.udf5)
        }])
        
        encrypted_data = self.encryptAES(plain_data)
        
        return json.dumps([{
            'id':str(self.tranportal_id),
            'trandata':encrypted_data
        }])

    def encryptAES(self,plain_data):
            date = quote(plain_data)
            raw = (self._pad(date))
            iv = 'PGKEYENCDECIVSPC'.encode('utf8')
            cipher = AES.new(self.resource_key.encode('utf8'), AES.MODE_CBC, iv)
            encrypted_text = cipher.encrypt(raw.encode('utf8'))
            return binascii.hexlify(bytearray(encrypted_text)).upper().decode('utf8')

    def decrypt(self, enc):
        iv = 'PGKEYENCDECIVSPC'.encode('utf8')
        encryptedData = binascii.unhexlify(enc)
        cipher = AES.new(self.resource_key.encode('utf8'), AES.MODE_CBC, iv)
        return unquote_plus(self._unpad(cipher.decrypt(encryptedData).decode('utf8')))

    def _pad(self, s):
            return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def initiate_payment(self):
        payload = self.request_data()
        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'charset': 'utf8',
        }
        url = str(self.url)
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()[0]




    
        