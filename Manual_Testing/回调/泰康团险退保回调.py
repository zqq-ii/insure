# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")


class Status_callback:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "callback_host")

    def Status_callback(self):
        url = "/issuingmc/channelopenapi/tk/group/insure/del/callback"
        request_url = self.host + url
        body = {"requestTime": "20240125161103", "requestId": "5c85524dc4fa467cb5215567fe26a7a7",
                "requestData": {"groupPolicyNo": "8H2405DA1A10N28", "validDate": "20240126000000",
                                "groupEpolicyUrl": "http://ecuat.taikang.com/sp-greedy/api/v2/?api_s=document.property&api_m=policy.download&applicantName=E56A70AF25C90BF102CF101BF96DE41AF120A49B97C73D9AE78A50A61&policyNo=F106C29D86B37D76DF53BF113AE117CE108CF23B53AE86DF110D92D40C94",
                                "groupEndorNo": "3A2400000009K68", "comboCode": "10N01503", "paymentType": "5",
                                "endorType": 2, "endorStatus": "1", "groupAppEndorNo": "2H2405DA1AC6KN8",
                                "productCode": "10N01500", "groupActuallyRefundPremium": 0, "personalPolicyList": [
                        {"personalPolicyNo": "6H2405DA5Y1CN86", "credentialType": "01",
                         "credentialNo": "610727199801070854", "actuallyRefundPremium": 0,
                         "effectiveTime": "20240126000000", "refundPremium": -190, "name": "强夏山",
                         "channelPolicyNo": "I8331982876302763115", "personalTxtJSONString": "",
                         "expiredTime": "20240125235959"}], "channelContractNo": "G8329363873968398604",
                                "groupRefundPremium": -190, "channelCode": "086000001042",
                                "endorAppNo": "2H2405DA1AC6KN8"}}

        return SendMethod.post_json(url=request_url, json=body)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Status_callback().Status_callback()
    print(f'time:{Time()}丨{Res}')
