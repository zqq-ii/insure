# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time,Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")
"""
团险,执行定时任务异步退保团体中保单数量不得低于3个否则不可退保
退保批减流程:请求退保接口-泰康团险主动异步退保定时任务-保单状态变更更新数据库-保单状态变更推送销售方
"""


class Synchronous_surrender:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Synchronous_surrender(self):
        url = "/issuingmc/channelapi/policy/cancelConfirm"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "6H2405DA5Y1K0C6",  # 保单号
                "CancelDate": Time(),  # 退保申请时间
                "RefundPremium": "0.00",  # 退保金额（不一定等于实际退费金额）
                "Currency": "CNY",  # 币种
                "Type": "NORMAL",  # 退保类型： 正常退保 - NORMAL ，协商退保 - NEGOTIATE
                "ReasonRemark": "测试单,退保",  # 退保原因
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0027",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Synchronous_surrender().Synchronous_surrender()
    print(f'[Execution_Time:{Execution_Time()}]\n{Res}')
