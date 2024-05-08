# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.communal import RandomStr, Execution_Time, Logger
from Manual_Testing.Environment import Environment

config = Config("config.ini")


class Abnormal:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "mock_host")

    def Abnormal(self):
        url = "/hlcpTest/tk/mock/abnormal2"
        request_url = self.host + url
        body = {}
        return SendMethod.post_json(url=request_url, json=body)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Abnormal().Abnormal()
    print(f'[{Execution_Time()}]\n{Res}')
