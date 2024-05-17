# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")
"""出单回调关键字:太平异步门店保出单回调原始数据"""


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
                    "ApplyPolicyRef": "ET202400030809000181",  # 大投保单号
                    "TotalPremium": "860.00",  # 保费
                    "Currency": "CNY",  # 币别
                    "PaymentMethod": "7",  # 支付方式
                    "PaymentDate": co.Time(),  # 支付时间
                    "PaymentFlowNum": co.RandomStr().create()  # 支付流水号,对公转账可为空
                },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0048",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Zh_Underwriting().Zh_Underwriting()
    print(f'[{co.Execution_Time()}]\n{Res}')
