# This Python file uses the following encoding: utf-8
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time,Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

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
                "PolicyRef": "H240123000357200108292",  # 保单号
                "CancelDate": Time(),  # 退保申请时间
                "RefundPremium": "1051.20",  # 退保金额（不一定等于实际退费金额）
                "Currency": "CNY",  # 币种
                "Type": "NORMAL",  # 退保类型： 正常退保 - NORMAL ，协商退保 - NEGOTIATE
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
            "RequestID": RandomStr().create(),
            "RequestType": "0027",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Synchronous_surrender().Synchronous_surrender()
    print(f'[{Execution_Time()}]\n{Res}')
