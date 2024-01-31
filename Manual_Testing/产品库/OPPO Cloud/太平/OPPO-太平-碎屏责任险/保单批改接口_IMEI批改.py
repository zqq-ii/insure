# This Python file uses the following encoding: utf-8
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")


class IMEI_correction:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def IMEI_correction(self):
        url = "/issuingmc/channelapi/modify/machine/imei"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyNo": "EP202403640000007509",  # 保单号
                "ModifyNo": RandomStr().create(),  # 批改单号 (接口幂等字段)
                "OldProductSerialNo": "65656589665777",  # 原序列号
                "NewProductSerialNo": "65656589665778"  # 新序列号
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0045",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = IMEI_correction().IMEI_correction()
    print(f'[{Execution_Time()}]\n{Res}')
