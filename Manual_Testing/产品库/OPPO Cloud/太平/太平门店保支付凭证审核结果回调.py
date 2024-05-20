# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Callback:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")

    def Callback(self):
        url = "/core/backend/certificate/check"
        request_url = self.host + url
        body = {
            "id": 40,  # 支付凭证审核id
            "auditStatus": "REJECT"  # 审核状态:PASSED-通过,REJECT-驳回
        }
        return SendMethod.post_json(url=request_url, json=body)


if __name__ == "__main__":
    Res = Callback().Callback()
    print(f'[{co.Execution_Time()}]\n{Res}')
