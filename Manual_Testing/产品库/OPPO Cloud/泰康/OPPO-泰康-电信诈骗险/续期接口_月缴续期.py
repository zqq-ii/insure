# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Renewal:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Renewal(self):
        url = "/issuingmc/channelapi/insure/renewal"
        request_url = self.host + url
        body = {
            "Data": {
                "AgencyPolicyRef": "w3hOa2mNPvUdGvyC",  # 第三方订单号
                "PlanCode": "TK2023100902",  # 保险计划代码
                "PaymentDate": co.Time(),  # 支付完成时间
                "Currency": "CNY",  # 币别
                "PaymentMethod": "2",  # 支付方式：1-支付宝；2-微信支付；3-通联支付；4-快钱支付
                "PaymentFlowNum": co.RandomStr().create(),  # 支付流水号（第三方支付流水号）
                "InstallmentNo": "2",  # 分期数整数(第几期)
                "InstallmentPremium": "8.30",  # 分期产品，期次保费
                "OriginalPolicyRef": "H231226443265840109785"  # 需要续期的保单号码
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0026",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Renewal().Renewal()
    print(f'[{co.Execution_Time()}]\n{Res}')
