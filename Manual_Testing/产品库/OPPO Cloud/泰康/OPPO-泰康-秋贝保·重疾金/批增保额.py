# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time,Tomorrow
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")


class Increase_coverage:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Increase_coverage(self):
        url = "/issuingmc/channelapi/insure/addInsuranceCoverage"
        request_url = self.host + url
        body = {
            "Data": {
                "Policy": {
                    "CorrectInfo": {
                        "Currency": "CNY",  # 币种
                        "CorrectPremium": "0",  # 批增保费,赠险传0
                        "OriginalAmount": "20000.00",  # 原有保额
                        "CorrectAmount": "1",  # 批增保额
                        "CorrectNo": RandomStr().create(),  # 批单申请号,保证唯一
                        "CorrectEffectiveDate": Tomorrow()  # 批单生效时间，T+1零点生效
                    },
                    "PlanCode": "1029A06U01",  # 计划代码
                    "PolicyRef": "H231226004392770176381"  # 保单号
                }
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0028",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Increase_coverage().Increase_coverage()
    print(f'[{Execution_Time()}]\n{Res}')
