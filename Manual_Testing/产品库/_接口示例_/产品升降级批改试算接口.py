# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.communal import RandomStr, Time, Execution_Time, Logger
from Manual_Testing.Environment import Environment

config = Config("config.ini")


class Grading_upgrading_Trial:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Grading_upgrading_Trial(self):
        url = "/issuingmc/channelapi/insure/policy/amendtrial"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyNo": "H220729015162980164023",  # 保单号
                "OriginalPlanCode": "TK2022052002",  # 原计划码
                "NewPlanCode": "TK202205200302",  # 批改后计划码
                "AmendDate": "20220729000000"  # 批改发起时间
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0042",
            "Version": "1.0.0",
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Grading_upgrading_Trial().Grading_upgrading_Trial()
    print(f'[{Execution_Time()}]\n{Res}')
