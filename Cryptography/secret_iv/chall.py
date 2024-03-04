from Crypto.Cipher import AES
import os

FLAG = open("flag.txt", "r").read().strip()

key = os.urandom(16)
iv = os.urandom(16)

def encrypt(msg, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
    enc = cipher.encrypt(msg)
    return enc

enc1 = key + encrypt(b'I\'m the author. I will hint you...', key, iv)
print(f'> {enc1.hex()} \n...\nConnection closed.')

'''
I made a huge mistake! Establishing new connection...
'''
key = iv    # This one is still secret, let's reuse it.
iv = os.urandom(16)

enc2 = iv + encrypt(b'flag='+FLAG[:11], key, iv)
print(f'> {enc2.hex()}')

      
iv = os.urandom(16)

enc_flag = iv + encrypt(FLAG, key, iv)
print(f'enc_flag = \'{enc_flag.hex()}\'')




print(f'enc1 = \'{enc1.hex()}\'')
print(f'enc2 = \'{enc2.hex()}\'')
print(key)


