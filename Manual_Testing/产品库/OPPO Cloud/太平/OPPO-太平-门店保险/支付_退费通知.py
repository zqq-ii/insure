# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Payment_refund:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Payment_refund(self):
        url = "/issuingmc/channelapi/pay/resultNotice"
        request_url = self.host + url
        body = {
            "Data": {
                "AgencyPolicyRef": "TENSERXU0NI685YOQIO1GJQD16R35VSH",  # 第三方渠道公司保单号码或者第三方渠道公司订单号码;[太平门店险传大订单号]
                # "PolicyRef": "ET202400029540000181",  # 保单号;[太平门店险传大投保单号,可不传]
                "InstallmentNo": "1",  # 分期号(兼容资金安全险非必填),非分期产品默认为第一期
                "TotalPremium": "860.00",  # 保费，分期产品为对应期数保费
                "Currency": "CNY",  # 币别
                "PaymentMethod": "2",  # 支付方式：1-支付宝2-微信支付3-通联支付4-快钱支付
                "MerchantOrderNum": co.RandomStr().create(),  # 商户订单号（钱包侧给到微信/支付宝的订单号）
                "PaymentFlowNum": co.RandomStr().create(),
                # 说明：1、“支付流水号”为微信支付宝自动生成的（微信支付单号/支付宝交易号）2、“商户退款订单号”为钱包侧给到微信支付宝的（商户退款单号/退款请求号）
                "BusinessType": "1",  # 业务类型：1-支付，2-退保退费 , 3-批改退费
                "PayTime": co.Time(),  # 支付退费时间
                "PayStatus": "0",  # 支付/退费状态：0-成功1-失败
                "IsTest": "1"  # 是否测试单，只要是请求了钱包发生支付和退款时必传0-非测试单1-测试单(兼容资金安全险非必填)
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0024",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_ae(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Payment_refund().Payment_refund()
    print(f'[{co.Execution_Time()}]\n{Res}')
