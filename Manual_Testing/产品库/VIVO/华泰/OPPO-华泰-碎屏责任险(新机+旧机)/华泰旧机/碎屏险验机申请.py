# This Python file uses the following encoding: utf-8
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")


class Machine_inspection_application:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Machine_inspection_application(self):
        url = "/issuingmc/channelapi/machine/check/apply"
        request_url = self.host + url
        body = {
            "Data": {
                "AgencyPolicyRef": "10588003900173684348",  # 渠道订单号（可与投保信息关联）
                "ProductSerialNo": "MIME24343545",  # 产品序列号
                "PlanCode": "MIME24343545",  # 计划码
                "ProductBrand": "MIME24343545",  # 产品品牌：01(oppo) 04（一加） 05（realme）
                "ProductCategory": "MIME24343545",  # 产品分类：01(手机)
                "ProductModel": "MIME24343545",  # 产品型号
                "PurchaseChannel": "MIME24343545",  # 购买渠道(预留字段)
                "NeedCheck": "true"  # true 需要验机、false 申请免验机，默认true
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0037",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Machine_inspection_application().Machine_inspection_application()
    print(f'[Execution_Time:{Execution_Time()}]\n{Res}')
