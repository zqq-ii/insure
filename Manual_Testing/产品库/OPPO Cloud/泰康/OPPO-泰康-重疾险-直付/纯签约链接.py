# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Pure_contract_link:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Pure_contract_link(self):
        url = "/issuingmc/channelapi/insure/notChannelCharge/applyContractUrl"
        request_url = self.host + url
        body = {
            "Data": {
                "ApplyPolicyRef": "P00420320240104360819064929718",  # 投保单号
                "PlatformType": "WAP",  # 支付平台类型：WAP — WAP端支付(浏览器打开，拉起微信或支付签约)
                "SuccessUrl": "https://www.taikang.com/product.html",  # 签约成功跳转链接
                "DeductConfig": {  # 扣费配置（当支付平台类型为WAP端支付时必传）
                    "StartTime": "20240104000000",  # 扣费开始时间
                    "EndTime": "20240203000000",  # 扣费结束时间
                    "Type": "0",  # 扣费类型：0 - 连续扣，在扣费时间段内每天按照固定频率尝试扣费，直到扣费成功（泰康：每天10.00和14.00）
                    "PayMethod": "WECHAT"  # 支付方式：微信支付 - WECHAT，支付宝支付 - ALI
                }
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "A_0001",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_ae(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Pure_contract_link().Pure_contract_link()
    print(f'[{co.Execution_Time()}]\n{Res}')
