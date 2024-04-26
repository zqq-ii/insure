# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")


class Order_callback:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "callback_host")

    def Order_callback(self):
        url = "/issuingmc/channelopenapi/directPay/issue/callback"
        request_url = self.host + url
        body = (
            "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")

        return SendMethod.post_data(url=request_url, data=body)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Order_callback().Order_callback()
    print(f'[{Execution_Time()}]\n{Res}')
