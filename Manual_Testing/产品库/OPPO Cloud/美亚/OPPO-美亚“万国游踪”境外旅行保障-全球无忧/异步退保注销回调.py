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
        self.host = config.get_value(self.environment, "callback_host")

    def Callback(self):
        url = "/issuingmc/channelopenapi/aig/cancel/callback"
        request_url = self.host + url
        body = ('ignature=3ED6BBA72B2BE71B4B6FDD48383C2A0848F8C122&MessageText={'
                '"header":{'
                '"transactionType":"policyNotify",'   # 退保：policyNotify；注销
                '"messageId":"63603f09-4be6-4545-a6d0-71e08051b2ed",'
                '"transactionId":"TYBJTEST-insure-I9061967681279541335",'
                '"agencyPcc":"TYBJTEST"},'
                '"segment":[{'
                '"applicationId":"1",'
                '"premium":272.94,'    #应收保费
                '"policyNumber":"LBJUE51554",'   # 保单号
                '"policyStatus":"Cancelled",'
                '"surrenderEffDate":"2024-10-10"'
                '}]}'
                '&AgencyUserId=10710&')
        print(f'[{co.Execution_Time()}]-Request:\n{co.JsonFormatting(body)}')
        return SendMethod.post_datax(url=request_url, data=body)


"""请求成功后,查看日志是否有回调推送给OPPO"""
if __name__ == "__main__":
    Res = Callback().Callback()
    print(f'[{co.Execution_Time()}]-Response:\n{Res}')
