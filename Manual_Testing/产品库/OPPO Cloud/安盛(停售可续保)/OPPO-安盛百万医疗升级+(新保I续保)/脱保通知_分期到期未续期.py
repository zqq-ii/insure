# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Release_Notice:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Release_Notice(self):
        url = "/issuingmc/channelapi/insure/endorNotice"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "21010000H27230001560",  # 保单号
                "EndorDate": "20230602235959",  # 脱保日期
                "EndorReason": None  # 脱保原因 (阳光百万医疗(计划码YG2021010701，YG2021010702)非必填,其余产品必填)
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0030",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_ae(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Release_Notice().Release_Notice()
    print(f'时间:{co.Time()};安盛百万医疗升级:脱保>{Res}')
