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
        url = "/issuingmc/channelopenapi/ks20220420/policy/callback"
        request_url = self.host + url
        body = {
            "extId": "B8602218267201454410",  # 业务单号
            "msg": "成功",  # 返回信息
            "policyNo": "",  # 保单号
            "status": "0",  # 状态(成功：0失败：1未知：2)
            "product": "1304104136",  # 产品编码
            "inid": "15"  # 保司编码
        }
        return SendMethod.post_jsonx(url=request_url, json=body)


"""
太平任逍遥意外伤害保险（互联网专属）; (product: 1303104237, inid: 15), 保障期限: 3个月（自然月）, 推送渠道"AtcualPlanCode":"KS20240423F0401"
太平众安心住院医疗保险; (product: 1304104136, inid: 15), 保障期限: 6个月（自然月）,  推送渠道"AtcualPlanCode":"KS20240423F0402"
招商信诺海陆空意外伤害保险产品; (product: HLKYW, inid: 11, 不传输保单号), 保障期限: 90天,  推送渠道"AtcualPlanCode":"KS20240423F0403"
阳光融客-出行无忧意外保障2023款; (product: WDDE10, inid: 1, 不传输保单号), 保障期限: 1个月（自然月）,  推送渠道"AtcualPlanCode":"KS20240423F0404"
"""

if __name__ == "__main__":
    Res = Callback().Callback()
    print(f'[{co.Execution_Time()}]\n{Res}')
