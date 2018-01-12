'''
Created on 2018年1月9日

@author: Administrator
'''

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Hash import SHA512
from Crypto.Hash import MD5

if __name__ == '__main__':
    md5 = MD5.new()
    md5.update('2131312313123123'.encode('utf-8'))
#     print('md5: ', md5.digest())
    print('md5: ', md5.hexdigest())
    
    hash = SHA256.new()
    hash.update('2131312313123123'.encode('utf-8'))
#     print('sha256: ', hash.digest())
    print('sha256: ', hash.hexdigest())
    
    hash = SHA512.new() 
    hash.update('2131312313123123'.encode('utf-8'))
#     print('sha512: ', hash.digest())
    print('sha512: ', hash.hexdigest())
    
#     obj = AES.new('111111111', AES.MODE_CBC, 22)
#     message = 'this is message'
#     ciphertext = obj.encrypt(message)
#     print(ciphertext)
#     
#     obj2 = AES.new('111111111', AES.MODE_CBC, 22)
#     ciphertext = obj2.decrypt(ciphertext)
#     print(ciphertext)
