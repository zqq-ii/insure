# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")
"""
计划代码:年缴:HT2023022801,月缴:HT2023022802
手机激活时间需20天内
"""


class SJX_Underwriting:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def SJX_Underwriting(self):
        url = "/issuingmc/channelapi/insure/check"
        request_url = self.host + url
        body = {
            "Data": {
                "Policy": {  # 保单信息
                    "AgencyPolicyRef": co.RandomStr().create(),  # 第三方订单号
                    "PlanCode": "HT2023022801",  # 计划代码
                    "IssueDate": co.Time(),  # 出单时间
                    "EffectiveDate": co.Tomorrow(8),  # 生效时间
                    "ExpireDate": co.SeveralYears(day=8),  # 失效时间
                    "GroupSize": "1",  # 被保人个数
                    "Currency": "CNY",  # 币别
                    "PaymentType": "1",  # 缴费方式：1-年缴2-月缴3-趸缴4-免缴
                    "TotalPremium": "234.00",  # 总保费
                    "FaceAmount": "3000.00",  # 保额注：1、保额可批增为初始保额2、医疗险多种条款为保额之和
                    "InstallmentNumber": None,  # 分期期数 (分期产品必传)
                    "ResponsibilityList": None,  # 组合责任列表(部分产品必传) 示例： [“010231”,”010232”]
                    "InstallmentNo": None  # 期数，分期趸交产品必传
                },
                "PolicyHolder": {  # 投保人信息
                    "PolicyHolderType": "2",  # 投保人类型1-个人2-企业或者机构
                    "PolicyHolderName": "深圳市欢太数字科技有限公司",  # 用户姓名/企业名
                    "PolicyHolderSex": None,  # 性别（0女，1男，2其它）
                    "PHIdType": "09",
                    # 证件类型01身份证,02户口簿,03护照,04军官证,05驾驶执照,06港澳返乡证,07台胞证,08出生证,09统一社会信用代码,10纳税人识别号,11其他)
                    "PHIdNumber": "91440300MA5FBC2T2F",  # 证件号/企业编号
                    "PHBirthDate": None,  # 出生日期 投保类型为2不传
                    "PHTelephone": None,  # 手机号 投保类型为2非必传
                    "PHEmail": None,  # 邮箱
                    "PHAddress": None  # 详细地址
                },
                "InsuredList": [  # 被保人信息列表
                    {
                        "InsuredId": "6",  # 被保险人唯一Id，用来确认该保单下被保险人的唯一性
                        "InsuredName": "深圳市欢太数字科技有限公司",  # 用户姓名/企业名
                        "Gender": None,  # 性别（0女，1男，2其它）
                        "InsuredType": None,  # 被保险人类型(参考附录 证件类型（个人）) 特殊说明下必传
                        "Type": "2",  # 被保人类型1-个人2-企业或者机构（默认个人）
                        "IdType": "09",  # 证件类型(参考附录 证件类型（个人）)投保类型为2不传
                        "IdNumber": "91440300MA5FBC2T2F",  # 证件号/企业编号
                        "BirthDate": None,  # 出生日期 投保类型为2非必传
                        "Mobile": None,  # 手机号投保类型为2非必传
                        "Email": None,  # 邮箱
                        "ResideAddress": None,  # 详细地址
                        "PolicyholderInsuredRelation": None,
                        # 被保人与投保人关系(01本人,02配偶,03丈夫,04妻子,05儿子,06女儿,07儿女,08父母,09父亲,10母亲) 投保类型为2时不传
                        "SocialSecurityFlag": None,  # 有无社保0无1有 健康险必传，意外险非必传 投保类型为2时不传
                        "UnderwritingType": None,  # 智能核保问卷告知 支持智能核保产品必传0-全无 1-部分是 投保类型为2时不传
                        "UnderwritingQuestionList": None,  # 智能核保问卷(智能核保问卷部分是时必填 ) 投保类型为2时不传
                        "OccupationCode": None  # 职业编码，部分产品必传，每个产品职业编码列表独立
                    }
                ],
                "PolicyObjects": [  # 手机信息列表,保险标的(手机、其它电子产品等)
                    {
                        "ProductBrand": "01",  # 产品品牌：01(OPPO) 04(OnePlus) 05(realme)
                        "ProductCategory": "01",  # 产品分类：01(手机)
                        "ProductModel": "Reno4 5G",  # 产品型号
                        "ProductSerialNo": co.RandomStr().create(),  # 产品序列号
                        "ActiveDate": "20231220000000",  # 激活日期 碎屏险必传
                        "ProductPrice": "7215.00",  # 产品价格
                        "PurchaseChannel": "6456415",  # 购买渠道(预留字段)
                        "Source": None  # 流量来源：1 - 固定入口、2 - 主动推送、3 - 其它，默认固定入口（比如钱包固定位、主动推送）
                    }
                ],
                "AutoRenewalFlag": None,
                # "InstallmentList": [  # 分期信息列表，缴费方式为月缴PaymentType=2时必填
                #     {
                #         "InstallmentNum": None,  # 分期数，如月缴12期
                #         "InstallmentNo": None,  # 分期号，按照约定传值；只有首期保费核保的产品，分期号固定值为1
                #         "InstallmentPremium": None,  # 对应分期号的保费，当前产品固定为首期保费
                #         "EachPremium": None  # 分期保费
                #     }
                # ]
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0006",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = SJX_Underwriting().SJX_Underwriting()
    print(f'[{co.Execution_Time()}]\n{Res}')
