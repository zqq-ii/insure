# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Pay_voucher:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Pay_voucher(self):
        url = "/issuingmc/channelapi/certificate/file/upload"
        request_url = self.host + url
        body = {
            "Data": {
                "AgencyPolicyRef": "GeIZe9e9UIC6c4Va",  # 对应大订单号
                "ApplyPolicyRef": "ET202300000160945045",  # 对应大投保单号
                "AccountName": "游点叼",  # 银行账户名称(非必填)
                "BankAccountNo": "5154555659656565",  # 银行账号(非必填)
                "BankName": "中国建设银行",  # 开户银行(非必填)
                "BranchBankName": "中国建设银行南山支行",  # 开户支行(非必填)
                "BranchBankNo": "5215656165656565",  # 支行银行卡号(非必填)
                "Certificate":
                    {
                        "FileName": "支付凭证.jpg",  # 带后缀名称的文件名
                        "FileType": "FILE_URL",  # 文件类型，FILE_URL 文件url；BASE64，base64编码格式
                        "Data": "https://ts1.cn.mm.bing.net/th/id/R-C.69570f49f6f2567035b26ee26ab327d0?rik=%2fuDc6mLtfp7i4w&riu=http%3a%2f%2fwww.siwuprint.com%2fupsmb%2f201512%2f2015122321562514666.JPG&ehk=U%2bYrhAth%2fD8G08fLR%2fmC7doRr8zsNlXlWIPMRvAXIb4%3d&risl=&pid=ImgRaw&r=0"
                        # 文件地址
                    }
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0050",
            "Version": "1.0.0"
        }
        print(f'[{co.Execution_Time()}]-Request:\n{co.JsonFormatting(body)}')
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Pay_voucher().Pay_voucher()
    print(f'[{co.Execution_Time()}]-Response:\n{Res}')
