# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Paid_up:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Paid_up(self):
        url = "/issuingmc/channelapi/insure/renewalAll"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "PI07306230824779981301",  # 需要缴费的保单号码
                "Type": "0",  # 0-月缴一次性缴清，仍是月缴保单；1- 月缴缴清转年缴
                "PaymentDate": "20230221000000",  # 支付完成时间
                "Currency": "CNY",  # 币别
                "PaymentMethod": "2",  # 支付方式：1-支付宝；2-微信支付；3-通联支付；4-快钱支付
                "PaymentFlowNum": co.RandomStr().create(),  # 支付流水号/商户订单号（第三方支付流水号）
                "StartInstallmentNo": "4",  # 开始缴费分期号
                "PaymentPremium": "54.90",  # 实际支付总保费
                "DiscountPremium": "0",  # 优惠总金额(无优惠为0)
                "MerchantOrderNum": None  # 备注无
            },
            "RequestID": co.RandomStr().create(),
            "Version": "1.0.0",
            "ChannelCode": self.ChannelCode,
            "RequestType": "0035"
        }
        return SendMethod.PostData_aes(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Paid_up().Paid_up()
    print(f'[{co.Execution_Time()}]\n{Res}')
