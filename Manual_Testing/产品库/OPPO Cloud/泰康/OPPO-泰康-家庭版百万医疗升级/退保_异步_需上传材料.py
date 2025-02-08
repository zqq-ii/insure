# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


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
                "PolicyRef": "H240409001422800173953",  # 保单号
                "CancelDate": co.Time(),  # 退保申请时间
                "RefundPremium": "235.91",  # 退保金额（不一定等于实际退费金额）
                "Currency": "CNY",  # 币种
                "Type": "NEGOTIATE",  # 退保类型： 正常退保 - NORMAL ，协商退保 - NEGOTIATE
                "ReasonRemark": "测试单,退保",  # 退保原因
                "MaterialList": [
                    {
                        "MaterialName": "身份证正面.jpg",  # 材料名，示例：xxx.png
                        "MaterialType": "1",  # 材料类型：1 - 证件照正面 2、证件照反面
                        "MaterialFileType": "BASE64",
                        # 材料文件类型：FILE_URL - 文件地址、BASE64 - base64数据流(目前只支持BASE64数据流)
                        "Data": "/9j/4AAQSkZJRgABAQAAAQABAAD/"
                    },
                    {
                        "MaterialName": "身份证反面.jpg",  # 材料名，示例：xxx.png
                        "MaterialType": "2",  # 材料类型：1 - 证件照正面 2、证件照反面
                        "MaterialFileType": "BASE64",
                        # 材料文件类型：FILE_URL - 文件地址、BASE64 - base64数据流(目前只支持BASE64数据流)
                        "Data": "/9j/4AAQSkZJRgABAQAAAQABAAD/"
                    }
                ]
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0027",
            "Version": "1.0.0"
        }
        print(f'[{co.Execution_Time()}]-Request:\n{co.JsonFormatting(body)}')
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Synchronous_surrender().Synchronous_surrender()
    print(f'[{co.Execution_Time()}]-Response:\n{Res}')
