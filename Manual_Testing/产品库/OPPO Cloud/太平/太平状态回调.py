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
        url = "/issuingmc/channelopenapi/tp20221025/policy/callback"
        request_url = self.host + url
        body = {
            "content": "1CB6C4B3F2D5C52ED399200529B1D6C235C6E9AF2E09475AA8EE60D83B7CFFF55B82F3A9325EDB7AC4E98010FCBDE1C2115965984DBDCD77838DBE48A9C6E41D65A536D034163FF76F39E0BA0C101E0A12FF1A1E1C11E40E990FB411B049265F6C775F0539DD92CC9412D33489E4327BC847AFE8F3B7ABA1569BE70CB6FCB0CFAE08CD4C3E47DD891BAF8CA28AEF5E405879F1DA873C1F89CF50A006CF6E8C5B13FE9AE9825C7A4898C65F5604BE67F19CE4437CDEC223FA",
            "sign": "f920af3a72dad5a05a803344b34678a5"}
        print(f'[{co.Execution_Time()}]-Request:\n{co.JsonFormatting(body)}')
        return SendMethod.post_json(url=request_url, json=body)


"""请求成功后,查看日志是否有回调推送给OPPO"""
if __name__ == "__main__":
    Res = Callback().Callback()
    print(f'[{co.Execution_Time()}]-Response:\n{Res}')
