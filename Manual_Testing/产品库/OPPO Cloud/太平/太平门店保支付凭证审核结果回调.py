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
            "id": 2,  # 支付凭证审核id;(注:该条数据在支付凭证表pay_certificate中的id)
            "auditStatus": "PASSED"  # 审核状态:PASSED-通过,REJECT-驳回
        }
        return SendMethod.post_json(url=request_url, json=body)


"""请求成功后,查看日志是否有回调推送给OPPO"""
if __name__ == "__main__":
    Res = Callback().Callback()
    print(f'[{co.Execution_Time()}]-Response:\n{Res}')
