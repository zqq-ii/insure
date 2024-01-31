# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")


class Renew_insurance:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Renew_insurance(self):
        url = "/issuingmc/channelapi/insure/renewalPolicyCheck"
        request_url = self.host + url
        body = {
            "Data": {
                "Policy": {
                    "OriginalPolicyRef": "21010000H27230001509",  # 原保单号
                    "AgencyPolicyRef": RandomStr().create(),  # 第三方订单号(不能与原订单号一致)
                    "PlanCode": "HT2023022802",  # 计划代码
                    "IssueDate": "20241117000000",  # 出单时间
                    "EffectiveDate": "20241118000000",  # 生效时间
                    "ExpireDate": "20251117235959",  # 失效时间
                    "GroupSize": "1",  # 被保人个数
                    "Currency": "CNY",  # 币种
                    "PaymentType": "1",  # 缴费方式：1-年缴2-月缴3-趸缴4-免缴
                    "TotalPremium": "460.00",  # 总保费
                    "FaceAmount": "100000.00",  # 保额
                    "InstallmentNumber": None,  # 分期期数
                    "ResponsibilityList": None  # 责任列表(无特殊说明必传)目前用于续保责任免除场景示例： [“010231”,”010232”]
                },
                "PolicyHolder": {
                    "PolicyHolderType": "1",  # 投保人类型1-个人2-企业或者机构
                    "PolicyHolderName": "童琛炜",  # 用户姓名
                    "PHIdType": "01",
                    # 证件类型01居民身份证,02户口簿,03护照,04军官证,05驾驶执照,06港澳返乡证,07台胞证,08出生证,09统一社会信用代码,10纳税人识别号,11其他) 特殊说明下必传
                    "PHIdNumber": "61030319980107246X",  # 证件号
                    "PHBirthDate": "19980107000000",  # 出生日期
                    "PHTelephone": "13410506136",  # 手机号
                    "SocialSecurityFlag": "0"  # 有无社保 (0无1有)
                },
                "InsuredList": [
                    {
                        "InsuredId": "7",  # 被保险人唯一Id
                        "InsuredName": "童琛炜",  # 用户姓名
                        "InsuredType": None,  # 被保险人类型(参考附录 证件类型（个人）) 特殊说明下必传
                        "IdType": "01",
                        # 证件类型证件类型01居民身份证,02户口簿,03护照,04军官证,05驾驶执照,06港澳返乡证,07台胞证,08出生证,09统一社会信用代码,10纳税人识别号,11其他) 特殊说明下必传
                        "IdNumber": "61030319980107246X",  # 证件号
                        "BirthDate": "19980107000000",  # 出生日期
                        "PolicyholderInsuredRelation": "01",
                        # 被保人与投保人关系(01本人,02配偶,03丈夫,04妻子,05儿子,06女儿,07儿女,08父母,09父亲,10母亲) 投保类型为2时不传
                        "UnderwritingType": "0",  # 智能核保问卷告知 支持智能核保产品必传0-全无 1-部分是
                        "SocialSecurityFlag": "0"  # 有无社保 (0无1有)
                    }
                ],
                "PolicyObjects": [  # 手机信息列表,保险标的(手机、其它电子产品等)
                    {
                        "ProductBrand": "01",  # 产品品牌：01(OPPO) 04(OnePlus) 05(realme)
                        "ProductCategory": "01",  # 产品分类：01(手机)
                        "ProductModel": "Reno4 5G",  # 产品型号
                        "ProductSerialNo": RandomStr().create(),  # 产品序列号
                        "ActiveDate": "20230407000000",  # 激活日期 碎屏险必传
                        "ProductPrice": "20000",  # 产品价格
                        "PurchaseChannel": None,  # 购买渠道(预留字段)
                        "Source": None  # 流量来源：1 - 固定入口、2 - 主动推送、3 - 其它，默认固定入口（比如钱包固定位、主动推送）
                    }
                ],
                # "InstallmentList": [    # 分期信息列表，缴费方式为月缴PaymentType=2时必填
                #     {
                #         "InstallmentNum": None,  # 分期数，如月缴12期
                #         "InstallmentNo": None,  # 分期号，按照约定传值；只有首期保费核保的产品，分期号固定值为1
                #         "InstallmentPremium": None,  # 对应分期号的保费，当前产品固定为首期保费
                #         "EachPremium": None  # 分期保费
                #     }
                # ]
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0032",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Renew_insurance().Renew_insurance()
    print(f'[{Execution_Time()}]\n{Res}')
