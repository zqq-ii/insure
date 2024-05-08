# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.communal import RandomStr, Execution_Time, Logger
from Manual_Testing.Environment import Environment

config = Config("config.ini")


class Mock_renewal:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "mock_host")

    def Mock_renewal(self):
        url = "/hlcpTest/webservice/as/mock/renewal"
        request_url = self.host + url
        body = {}
        return SendMethod.post_jsonx(url=request_url, json=body)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Mock_renewal().Mock_renewal()
    print(f'[{Execution_Time()}]\n{Res}')
