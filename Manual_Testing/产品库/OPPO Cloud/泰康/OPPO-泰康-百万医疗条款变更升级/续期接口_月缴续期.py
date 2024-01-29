# This Python file uses the following encoding: utf-8
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr,Time, Execution_Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

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
                "AgencyPolicyRef": "bNKBxg2JOndDuMzD",  # 第三方订单号
                "PlanCode": "PlanCode",  # 保险计划代码
                "PaymentDate": Time(),  # 支付完成时间
                "Currency": "CNY",  # 币别
                "PaymentMethod": "2",  # 支付方式：1-支付宝；2-微信支付；3-通联支付；4-快钱支付
                "PaymentFlowNum": RandomStr().create(),  # 支付流水号（第三方支付流水号）
                "InstallmentNo": "3",  # 分期数整数(第几期)
                "InstallmentPremium": "53.40",  # 分期产品，期次保费
                "OriginalPolicyRef": "H240124000377210129758"  # 需要续期的保单号码
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0026",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Renewal().Renewal()
    print(f'[Execution_Time:{Execution_Time()}]\n{Res}')
