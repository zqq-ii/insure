# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")


class Insure:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Insure(self):
        url = "/issuingmc/channelapi/insure/accept"
        request_url = self.host + url
        body = {
            "Data": {
                "ApplyPolicyRef": "B8575020403979272241:7088:0",  # 投保单号
                "PaymentFlowNum": RandomStr().create(),  # 支付流水唯一
                "PaymentMethod": "2",  # 支付方式(1 支付宝,2 微信,3 通联支付,4 快钱支付,5 银行卡,6 优惠券,7 其它：线下结算)
                "Currency": "CNY",  # 币种
                "TotalPremium": "234.00",  # 保费（买保险付的钱,分期的就填写一期的钱）不是保额
                "PaymentDate": "20240115120252"  # 支付时间
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0007",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Insure().Insure()
    print(f'[{Execution_Time()}]\n{Res}')
