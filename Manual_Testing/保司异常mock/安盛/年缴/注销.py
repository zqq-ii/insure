# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")


class Mock_logout:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "mock_host")

    def Mock_logout(self):
        url = "/hlcpTest/webservice/as/mock/cancel/year"
        request_url = self.host + url
        body = {}
        return SendMethod.post_jsonx(url=request_url, json=body)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Mock_logout().Mock_logout()
    print(f'time:{Time()}丨{Res}')
