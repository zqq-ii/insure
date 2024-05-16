# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")
"""
团险,执行定时任务异步退保团体中保单数量不得低于3个否则不可退保
流程注:请求退保接口>泰康团险购药金主动异步退保(执行后等待回调成功)>保单状态变更更新数据库任务>保单状态变更推送销售方任务
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
                "PolicyRef": "6H2405DA88T3926",  # 保单号
                "CancelDate": co.Time(),  # 退保申请时间
                "RefundPremium": "0.00",  # 退保金额（不一定等于实际退费金额）
                "Currency": "CNY",  # 币种
                "Type": "NORMAL",  # 退保类型： 正常退保 - NORMAL ，协商退保 - NEGOTIATE
                "ReasonRemark": "测试单,退保",  # 退保原因
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0027",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_aes(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Synchronous_surrender().Synchronous_surrender()
    print(f'[{co.Execution_Time()}]\n{Res}')
