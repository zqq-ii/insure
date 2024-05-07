# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.communal import RandomStr, Time, Execution_Time, Logger
from Manual_Testing.Environment import Environment

config = Config("config.ini")


class Synchronous_surrender:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Synchronous_surrender(self):
        url = "/issuingmc/channelapi/policy/syncPolicyCancel"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "PI07306230824779982661",  # 保单号
                "CancelDate": "20230222000000",  # 退保申请时间
                "CancelPremium": None,  # 退保金额（不一定等于实际退费金额）
                "Currency": None,  # 币种
                "Type": None,  # 退保类型： 正常退保 - NORMAL ，协商退保 - NEGOTIATE
                "ReasonRemark": None,  # 退保原因
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0017",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Synchronous_surrender().Synchronous_surrender()
    print(f'[{Execution_Time()}]\n{Res}')
