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
        url = "/issuingmc/channelopenapi/tp20221025/policy/callback"
        request_url = self.host + url
        body = {
            "content": "1CB6C4B3F2D5C52ED399200529B1D6C2CE7E38AA9F923FB2354204EADD87B695577D4AB1F2046D29C4E98010FCBDE1C2115965984DBDCD77D18813478F45C1F665A536D034163FF76F39E0BA0C101E0A63164BED87B17964B3F346E5B10AADA76C775F0539DD92CC9412D33489E4327BC847AFE8F3B7ABA1C51523510A884242058DE10BDD2A64F31BAF8CA28AEF5E405879F1DA873C1F89CF50A006CF6E8C5B13FE9AE9825C7A4898C65F5604BE67F19CE4437CDEC223FA",
            "sign": "019e2ea7231b860920c9d757d83735b7"}

        return SendMethod.post_json(url=request_url, json=body)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Status_callback().Status_callback()
    print(f'time:{Time()}丨{Res}')
