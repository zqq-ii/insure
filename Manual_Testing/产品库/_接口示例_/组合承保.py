# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Time,Execution_Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")


class Zh_Underwriting:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Zh_Underwriting(self):
        url = "/issuingmc/channelapi/insure/permutation/accept"
        request_url = self.host + url
        body = {
            "Data":
                {
                    "ApplyPolicyRef": "ET202300000009118660",  # 大投保单号
                    "TotalPremium": "860.00",  # 保费
                    "Currency": "CNY",  # 币别
                    "PaymentMethod": "7",  # 支付方式
                    "FaceAmount": "2500000",  # 总保额，单位元
                    "PaymentDate": Time(),  # 支付时间
                    "PaymentFlowNum": RandomStr().create()  # 支付流水号,对公转账可为空
                },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0048",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Zh_Underwriting().Zh_Underwriting()
    print(f'[{Execution_Time()}]\n{Res}')
