# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Status_callback:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "callback_host")

    def Status_callback(self):
        url = "/issuingmc/channelopenapi/tp/store/invoice/callback"
        request_url = self.host + url
        body = """<?xml version="1.0" encoding="UTF-8"?>
                    <document>
                        <request>
                            <head>
                                <productCode>0201797</productCode>
                                <businessType>invoice</businessType>
                                <transTime>2024-05-12 16:34:00</transTime>
                                <agencyCode>BBK</agencyCode>
                                <orderNo>O162220240512163325972</orderNo>
                            </head>
                            <body>
                                <policyno>EP202403202280000123</policyno>
                                <invoiceurl>http://dzdz.cbit.com.cn/#/S?d=950497fb585dbb3d</invoiceurl>
                            </body>
                        </request>
                    </document>
               """
        return SendMethod.post_datax(url=request_url, data=body)


if __name__ == "__main__":
    Res = Status_callback().Status_callback()
    print(f'[{co.Execution_Time()}]\n{Res}')
