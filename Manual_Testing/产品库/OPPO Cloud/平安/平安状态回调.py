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
        url = "/issuingmc/channelopenapi/pingan/20210808/policyNotice"
        request_url = self.host + url
        body = {
            "retMoney": "5325",
            "partnerCode": "P_ZCAX_PE",
            "installmentsDetail": [
                {
                    "num": 1,
                    "refundAmount": "5325"
                },
                {
                    "num": 2,
                    "refundAmount": "0"
                },
                {
                    "num": 3,
                    "refundAmount": "0"
                },
                {
                    "num": 4,
                    "refundAmount": "0"
                },
                {
                    "num": 5,
                    "refundAmount": "0"
                },
                {
                    "num": 6,
                    "refundAmount": "0"
                },
                {
                    "num": 7,
                    "refundAmount": "0"
                },
                {
                    "num": 8,
                    "refundAmount": "0"
                },
                {
                    "num": 9,
                    "refundAmount": "0"
                },
                {
                    "num": 10,
                    "refundAmount": "0"
                },
                {
                    "num": 11,
                    "refundAmount": "0"
                },
                {
                    "num": 12,
                    "refundAmount": "0"
                }],
            "endorseNo": "30560001900157824290",
            "departmentCode": "20560",
            "installmentsNum": "1",
            "transactionNo": "P_ZCAX_PEO8224827290557694202",
            "policyNo": "10560006600504723214",
            "policyStatus": "04",
            "installmentsTotal": "12",
            "applyPolicyNo": "50560006600553533360",
            "productCode": "MP03051526",
            "premium": "0",
            "policyType": "1",
            "endorseAcceptDate": "2023-12-21 16:29:21",
            "signMsg": "f65b8a664fce2e4f8ac6415de3580ba9",
            "applyDate": "2023-12-21 16:24:19",
            "dataSource": "openApi",
            "effectiveDate": "2023-12-22 00:00:00"
        }
        return SendMethod.post_json(url=request_url, json=body)


"""请求成功后,查看日志是否有回调推送给OPPO"""
if __name__ == "__main__":
    Res = Callback().Callback()
    print(f'[{co.Execution_Time()}]\n{Res}')
