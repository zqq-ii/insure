# -*- coding: utf-8 -*-
import base64, rsa
from Crypto.Cipher import AES
from Manual_Testing.common.operation_config import Config
from Manual_Testing.Environment import Environment

config = Config("config.ini")


class EncryptDate:
    """
    加密初始化:封装AES+base64,ECB模式加解密
    """

    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.length = AES.block_size
        self.aes = AES.new(self.key, AES.MODE_ECB)
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):
        res = self.aes.encrypt(self.pad(encrData).encode("utf-8"))
        msg = str(base64.b64encode(res), encoding="utf-8")
        return msg

    def decrypt(self, decrData):
        res = base64.decodebytes(decrData.encode("utf-8"))
        msg = self.aes.decrypt(res).decode()
        return self.unpad(msg)


class AES_DES:
    """
    二次封装AES+base64,ECB模式加解密,方便手动加解密
    """

    def __init__(self):
        self.environment = Environment
        self.key = config.get_value(self.environment, "key")

    def AES_DES(self, task=None, text=None):
        try:
            if task == 0 or task == "0":
                eg = EncryptDate(self.key)
                res = eg.decrypt(text)
                return "解密res:" + res
            elif task == 1 or task == "1":
                eg = EncryptDate(self.key)
                res = eg.encrypt(text)
                return "加密res:" + res
            else:
                return f"注意task:0-解密,1-加密!"
        except:
            return f"秘钥错误! 或 传入的text数据非文本!"


class Rsa:
    """
    加密初始化:封装ras加解密
    """

    def __init__(self, pubkey, privkey):
        self.pubkey = pubkey
        self.privkey = privkey

    def encrypt(self, message):  # 加密
        message_bytes = message.encode('utf-8')
        ciphertext = rsa.encrypt(message_bytes, self.pubkey)
        return base64.b64encode(ciphertext).decode()

    def decrypt(self, ciphertext):  # 解密
        ciphertext = base64.b64decode(ciphertext)
        plaintext = rsa.decrypt(ciphertext, self.privkey)
        return plaintext.decode()


if __name__ == '__main__':
    """"""
    print(AES_DES().AES_DES(
        task=0,
        text='Je0ffRcDnT6GSPNbAOqcipXdec5M/MLuuE/jydKaWZ18loGvOstyW3Sj+vYiKmGH2iUXdNDbv53zO6sw/BODa/6pPlW0SPVeLJn4OLoXVEOefWXuBJLOo0bF25ywVTyjA3feA0dhfEJjNrotupLnZRcDw4K9EM7wd/VXQllhXCuuaiHVbkxxAKwymEB8R7oRH9s3UBMHwZrPIG94j6iJPKsBwE0FQFOhgY/OObVOnhOzdi/Sp6S6VYevIHBZq45gsfoLLdPqAgEPA++Fl0POlBADKQ9VaellXzEBgsNzrTqkerdo9MZgtRK0p9NemiiEBq55/OcWNEn4quc3Kdfo/YyF7qlb//h79+ClP4j/djYdOZhbdZRMFSl6ew+mol4pL15MKYdtvDacDUc+pfw1BtrAJ5ER0rEnWiutiF8FOeU='))
    ####################################################
    # """Rsa"""
    # # 生成公钥和私钥
    # (pubkey, privkey) = rsa.newkeys(2048)
    # # 创建加密对象
    # rsa_ = Rsa(pubkey, privkey)
    # # 加密和解密中文消息
    # message = "你好，世界！"
    # encrypted_message = rsa_.encrypt(message)
    # print("加密后的消息：", encrypted_message)
    # decrypted_message = rsa_.decrypt(encrypted_message)
    # print("解密后的消息：", decrypted_message)
