# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Renewal_payment_link:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Renewal_payment_link(self):
        url = "/issuingmc/channelapi/insure/notChannelCharge/applyPayUrl"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "H231218427185080166377",  # 保单号
                "PayMethod": "WECHAT",  # 支付方式：微信支付 - WECHAT，支付宝支付 - ALI
                "Amount": "36.20",  # 支付金额，分期保费之和
                "PayPlatformType": "WAP",  # 支付平台类型：PC - PC端支付（返回一个二维码页面，只能在pc端打开，用户扫码支付） WAP—WAP端支付(浏览器打开，拉起微信或支付宝支付)
                "SuccessUrl": "https://www.baidu.com/",  # 签约成功跳转链接
                "FailUrl": "https://www.taikang.com/",  # 支付失败跳转链接（泰康重疾险直付产品必传）
                "PremiumPlanList": [
                    {
                        "InstallmentNo": "2",  # 分期号
                        "InstallmentPremium": "36.20"  # 分期保费
                    }
                ]
            },

            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "A_0002",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_aes(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Renewal_payment_link().Renewal_payment_link()
    print(f'[{co.Execution_Time()}]\n{Res}')
