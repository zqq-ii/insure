# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Invoice_application:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Invoice_application(self):
        url = "/issuingmc/channelapi/invoice"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyNo": "EP202403202635000123",  # 保单号
                "InvoiceHead": "游点叼",  # 发票抬头
                "TaxPayerNo": "1341050613611111",  # 纳税人识别号
                "InvoiceAmount": "390.00",  # 开票金额
                "Email": "1833247938@163.com",  # 邮箱
                "PhoneNo": "134105061361",  # 手机号码
                "InvoiceType": "1",  # 发票类型，1：电子发票2：纸质专用发票;
                "OfflineInvoiceApply":  # 收件人，当选择纸质发票时必填该项，除发票类型外其他参数可不填
                    {
                        "PolicyNo": "EP202403202635000123",  # 保单号
                        "InsuranceType": "游点叼",  # 险种名称
                        "PolicyHolderName": "吴三桂",  # 投保人名称
                        "InsuredName": "南山前海门店",  # 被保险人名称
                        "Premium": "390.00",  # 保费
                        "CompanyName": "个体工商户",  # 公司名称
                        "TaxPayerNo": "125410236958541",  # 纳税人识别号
                        "RegisteredAddress": "招商银行前海1号",  # 注册详细地址
                        "TelephoneNo": "13410506136",  # 联系电话
                        "BankName": "招商银行前海支行",  # 开户行
                        "BankCardNo": "5956196595656645454",  # 银行账户
                        "DeliveryAddress": "世界之窗",  # 收件地址
                        "Recipient": "彦祖",  # 收件人名称
                        "RecipientPhone": "13410506136"  # 收件人电话
                    }
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0049",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Invoice_application().Invoice_application()
    print(f'[{co.Execution_Time()}]\n{Res}')
