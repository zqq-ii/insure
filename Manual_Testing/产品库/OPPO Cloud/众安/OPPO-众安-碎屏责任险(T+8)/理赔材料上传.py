# This Python file uses the following encoding: utf-8
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")
"""
先上传材料,再申请理赔
"""


class Material_upload:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Material_upload(self):
        url = "/issuingmc/channelapi/claim/machine/file/upload"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyNo": "PI07306240124872443779",  # 保单号
                "MaterialName": "维修前照片.jpg",  # 材料名，示例：xxx.png
                "MaterialType": "2",  # 材料类型：1 - 证件照 2、维修前照片 3、维修后照片
                "MaterialFileType": "FILE_URL",  # 材料文件类型：FILE_URL - 文件地址、BASE64 - base64数据流
                "Data": "https://picnew13.photophoto.cn/20190527/ziranfengjingtupiansucaibizhishanshuifengjing-33283943_1.jpg"
                # 数据
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0043",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Material_upload().Material_upload()
    print(f'[Execution_Time:{Execution_Time()}]\n{Res}')
