import base64
import hashlib
import hmac
import time
import datetime
from util.QrcodeData import QrcodeData
class GoogleKey:

    def byte_secret(self,secret):
        missing_padding = len(secret) % 8
        if missing_padding != 0:
           secret += '=' * (8 - missing_padding)
        return base64.b32decode(secret, casefold=True)


    def int_to_bytestring(self,i, padding=8):
        result = bytearray()
        while i != 0:
            result.append(i & 0xFF)
            i >>= 8
        return bytes(bytearray(reversed(result)).rjust(padding, b'\0'))


    # 根据约定的密钥计算当前动态密码
    def generate_otp(self,secret):

        for_time = datetime.datetime.now()
        i = time.mktime(for_time.timetuple())
        input = int(i / 30)
        digest = hashlib.sha1
        digits = 6
        if input < 0:
            raise ValueError('input must be positive integer')
        hasher = hmac.new(GoogleKey.byte_secret(self,secret), GoogleKey.int_to_bytestring(self,input), digest)
        hmac_hash = bytearray(hasher.digest())
        offset = hmac_hash[-1] & 0xf
        code = ((hmac_hash[offset] & 0x7f) << 24 |
                (hmac_hash[offset + 1] & 0xff) << 16 |
                (hmac_hash[offset + 2] & 0xff) << 8 |
                (hmac_hash[offset + 3] & 0xff))
        str_code = str(code % 10 ** digits)
        while len(str_code) < digits:
            str_code = '0' + str_code
        return str_code

# if __name__ == '__main__':
#     gk = GoogleKey()
#     data = QrcodeData.qr_code_secret(filename2)
#     key = gk.generate_otp(data)
#     print(key)