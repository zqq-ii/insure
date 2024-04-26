# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time
from Manual_Testing.Environment import Environment

config = Config("config.ini")


class Status_callback:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "callback_host")

    def Status_callback(self):
        url = "/issuingmc/channelopenapi/claimconclusion/taiping/callback"
        request_url = self.host + url
        body = {
            "charset": "UTF-8",
            "merchantCode": "M1660793414859",
            "bizModel": "{\"date\":\"2024-03-04 19:05:35\",\"reason\":\"单证退回\",\"applyNo\":\"TenSerRgDdEJ3k99\",\"registNo\":\"07P20212912024000105\",\"status\":\"2\"}",
            "sign": "3BA071EF6CAE29BDC525792FFB592DE0",
            "signType": "MD5",
            "nonce": "192bf9ccebc5431c8e19a1a2f9e26612",
            "version": "1.0.1",
            "timestamp": "1709550359331"
        }
        return SendMethod.post_json(url=request_url, json=body)


# 报案号:registNo
# status和reason: 1-审核通过(单证齐全),2-单证退回,3-核赔通过,4-核赔退回,5-支付成功,6-支付失败

if __name__ == "__main__":
    Res = Status_callback().Status_callback()
    print(f'[{Execution_Time()}]\n{Res}')
