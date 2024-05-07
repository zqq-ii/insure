# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.communal import RandomStr, Execution_Time
from Manual_Testing.Environment import Environment

config = Config("config.ini")


class Order_callback:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "callback_host")

    def Order_callback(self):
        url = "/issuingmc/channelopenapi/tk/group/insure/callback"
        request_url = self.host + url
        body = {
            "requestTime": "20240109110503",
            "requestId": "8283940780878766087",
            "requestData": {
                "utmSource": "",
                "groupPolicyNo": "8H2405DA1A091S8",
                "productCode": "10N01500",
                "groupEpolicyUrl": "http://ecuat.taikang.com/sp-greedy/api/v2/?api_s=document.property&api_m=policy.download&applicantName=41DE52B87D28DF71DF96CE76DE6AE98BE23AF107A17CE5AE60B92DE87&policyNo=92C85A38A125DF124CE60BE23CE117C113B87D60C1DF120DE34B81C31",
                "personalPolicyList": [{
                    "personalPolicyNo": "6H2405DA1A3K1T6",
                    "effectiveTime": "20240110000000",
                    "openid": "",
                    "channelPolicyNo": "I8281611053178454097",
                    "Premium": 190,
                    "personalTxtJSONString": "{\"nationality\":\"CN\"}",
                    "Openid": "",
                    "expiredTime": "20250109235959",
                    "credentialType": "01",
                    "credentialNo": "530500199801072947",
                    "premium": 190,
                    "ExpiredTime": "20250109235959",
                    "name": "纳吉丹烟",
                    "epolicyUrl": "http://ecuat.taikang.com/sp-greedy/api/v2/?api_s=document.property&api_m=policy.download&applicantName=41AF52D87C28CE71BF96CF76AE6AE98CF23BE107B17AF5AF60C92CF87&policyNo=E60A27AF122AF125B119A41A7AF6DE3DF89A53CF115AE55AE90DF85AF27",
                    "status": 1
                }, {
                    "personalPolicyNo": "6H2405DA1A3K1N6",
                    "effectiveTime": "20240110000000",
                    "openid": "",
                    "channelPolicyNo": "I8281611053178454095",
                    "Premium": 190,
                    "personalTxtJSONString": "{\"nationality\":\"CN\"}",
                    "Openid": "",
                    "expiredTime": "20250109235959",
                    "credentialType": "01",
                    "credentialNo": "230400199801077813",
                    "premium": 190,
                    "ExpiredTime": "20250109235959",
                    "name": "钳耳静曼",
                    "epolicyUrl": "http://ecuat.taikang.com/sp-greedy/api/v2/?api_s=document.property&api_m=policy.download&applicantName=41BE52A87B28BE71CF96BF76DE6DF98BF23BF107A17AE5CF60A92CE87&policyNo=F37B38C45A77BE96A95DE101AF109D7B18C40C101A6DE73D127D119",
                    "status": 1
                }, {
                    "personalPolicyNo": "6H2405DA1A3K1Y6",
                    "effectiveTime": "20240110000000",
                    "openid": "",
                    "channelPolicyNo": "I8283940780878766084",
                    "Premium": 190,
                    "personalTxtJSONString": "{\"nationality\":\"CN\"}",
                    "Openid": "",
                    "expiredTime": "20250109235959",
                    "credentialType": "01",
                    "credentialNo": "360921199801072244",
                    "premium": 190,
                    "ExpiredTime": "20250109235959",
                    "name": "毛又蓝",
                    "epolicyUrl": "http://ecuat.taikang.com/sp-greedy/api/v2/?api_s=document.property&api_m=policy.download&applicantName=41DF52C87C28CE71BF96BE76DF6CF98AF23AF107C17CE5CE60D92DF87&policyNo=E68DE41CF49A113CE28B104BF107DE91A95A112A79D37A122BF80BF66B73",
                    "status": 1
                }, {
                    "personalPolicyNo": "6H2405DA1A3K206",
                    "effectiveTime": "20240110000000",
                    "openid": "",
                    "channelPolicyNo": "I8283940780878766085",
                    "Premium": 190,
                    "personalTxtJSONString": "{\"nationality\":\"CN\"}",
                    "Openid": "",
                    "expiredTime": "20250109235959",
                    "credentialType": "01",
                    "credentialNo": "542129199801072466",
                    "premium": 190,
                    "ExpiredTime": "20250109235959",
                    "name": "责夜白",
                    "epolicyUrl": "http://ecuat.taikang.com/sp-greedy/api/v2/?api_s=document.property&api_m=policy.download&applicantName=41BE52C87B28DE71CE96AF76DE6CE98DE23AE107C17AF5DF60D92AE87&policyNo=E54C23B115CE96BF86BE31B69BF109CF83B0DE51BE22C49B98A51D113",
                    "status": 1
                }, {
                    "personalPolicyNo": "6H2405DA1A3K1S6",
                    "effectiveTime": "20240110000000",
                    "openid": "",
                    "channelPolicyNo": "I8281611053178454096",
                    "Premium": 190,
                    "personalTxtJSONString": "{\"nationality\":\"CN\"}",
                    "Openid": "",
                    "expiredTime": "20250109235959",
                    "credentialType": "01",
                    "credentialNo": "659000199801070851",
                    "premium": 190,
                    "ExpiredTime": "20250109235959",
                    "name": "长元从梦",
                    "epolicyUrl": "http://ecuat.taikang.com/sp-greedy/api/v2/?api_s=document.property&api_m=policy.download&applicantName=41CF52D87D28AE71CE96AF76AE6CF98BF23BE107B17BF5AE60C92CF87&policyNo=8DE46D81A37C85C127AF44CF1CE124C61BE77DF124BE10DE26CF123DF19",
                    "status": 1
                }],
                "requestFlag": "1",
                "channelContractNo": "G8283940609083121695",
                "channelCode": "086000001042"
            }
        }
        return SendMethod.post_json(url=request_url, json=body)


if __name__ == "__main__":
    Res = Order_callback().Order_callback()
    print(f'[{Execution_Time()}]\n{Res}')
