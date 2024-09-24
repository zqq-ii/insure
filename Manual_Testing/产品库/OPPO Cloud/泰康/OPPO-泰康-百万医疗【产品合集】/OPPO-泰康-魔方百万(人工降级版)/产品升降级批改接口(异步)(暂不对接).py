# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Grading_upgrading:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Grading_upgrading(self):
        url = "/issuingmc/channelapi/insure/policy/amend"
        request_url = self.host + url
        body = {
            "Data": {
                "BatchNo": "202012291053378889998",  # 唯一批单号，支持幂等操作
                "PolicyNo": "H220710014442180173758",  # 保单号
                "OriginalPlanCode": "TK202206230102",  # 原计划码
                "NewPlanCode": "TK202206230202",  # 批改后计划码
                "InstallmentNum": "1",  # 批改影响计划开始期数（比如从第一期计划开始批改）
                "PlanPremium": "53.4",  # 批改后当期计划保费
                "ActualPremium": "53.4",  # 批改后当期应收保费
                "Currency": "CNY",  # 币别
                "Reason": "价格太贵",  # 批改原因
                "AmendEffectiveDate": "20220702000000",  # 批改发起时间
                "AmendDate": "20220710000000"  # 批改生效时间
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0040",
            "Version": "1.0.0",
        }
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Grading_upgrading().Grading_upgrading()
    print(f'[{co.Execution_Time()}]-Response:\n{Res}')
