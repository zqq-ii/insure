# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.communal import RandomStr, Time, Execution_Time, Logger
from Manual_Testing.Environment import Environment

config = Config("config.ini")


class Surrender_trial:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Surrender_trial(self):
        url = "/issuingmc/channelapi/policy/premiumCalculation"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "PLDO20244403Q000E10023",  # 保单号
                "CancelDate": Time(),  # 退保申请日期
                "CancelFlag": "0"  # 退保说明(0-主动，1-被动)
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0016",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Surrender_trial().Surrender_trial()
    print(f'[{Execution_Time()}]\n{Res}')
