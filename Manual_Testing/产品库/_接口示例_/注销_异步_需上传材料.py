# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Synchronize_logout:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Synchronize_logout(self):
        url = "/issuingmc/channelapi/policy/asyncCancel"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "H231122004152070112535",  # 保单号
                "CancelDate": co.Time(),  # 注销申请时间
                "RefundPremium": "0",  # 注销金额（不一定等于实际退费金额）
                "Currency": "CNY",  # 币种
                "Type": "NORMAL",  # 注销类型： 正常注销 - NORMAL ，协商注销 - NEGOTIATE
                "ReasonRemark": "测试单,注销",  # 注销原因
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
            "RequestType": "0031",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Synchronize_logout().Synchronize_logout()
    print(f'[{co.Execution_Time()}]-Response:\n{Res}')
