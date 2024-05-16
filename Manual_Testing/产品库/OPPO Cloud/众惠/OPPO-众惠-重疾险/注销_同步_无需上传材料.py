# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Synchronize_logout:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Synchronize_logout(self):
        url = "/issuingmc/channelapi/policy/cancel"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "P10E120230101X1169793",  # 保单号
                "CancelDate": co.Time(),  # 注销申请时间
                "RefundPremium": None,  # 注销金额（不一定等于实际退费金额）
                "Currency": None,  # 币种
                "Type": None,  # 注销类型： 正常注销 - NORMAL ，协商注销 - NEGOTIATE
                "ReasonRemark": "测试,注销",  # 注销原因
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0015",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_ae(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Synchronize_logout().Synchronize_logout()
    print(f'[{co.Execution_Time()}]\n{Res}')
