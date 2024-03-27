# This Python file uses the following encoding: utf-8
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time, Tomorrow
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")
"""
(1)初始保额:10元
(2)批增保额规则:1、每次批增保额是10的倍数；2、每日可批增2次，每次批增保额上限是1000元；
   3、最高批增保额至20000元;4、团险采购模式下的两个计划，16周岁-50周岁总保额累计不超过30000元
(3)费率:	0.01元/10元保额，根据保额整数倍计算
"""


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
                        "OriginalAmount": "1000.00",  # 原有保额
                        "CorrectAmount": "10",  # 批增保额
                        "CorrectNo": RandomStr().create(),  # 批单申请号,保证唯一
                        "CorrectEffectiveDate": Tomorrow()  # 批单生效时间，T+1零点生效
                    },
                    "PlanCode": "TKG20240324F04",  # 计划代码
                    "PolicyRef": "H231228446736240117481"  # 保单号
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
