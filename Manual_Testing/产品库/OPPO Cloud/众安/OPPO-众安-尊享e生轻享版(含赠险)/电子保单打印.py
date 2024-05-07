# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.communal import RandomStr, Time, Execution_Time, Logger
from Manual_Testing.Environment import Environment

config = Config("config.ini")


class Policy_printing:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Policy_printing(self):
        url = "/issuingmc/channelapi/policy/print"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "IH1100512150001372",  # 保单号
                "CertificateType": "100"  # 保单打印类型100-主保单,200-其它
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0012",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Policy_printing().Policy_printing()
    print(f'[{Execution_Time()}]\n{Res}')
