# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")
"""
产品码:ZAN20220108
计划代码:ZAN2022010804
"""


class One_order:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def One_order(self):
        url = "/issuingmc/channelapi/insure/commit"
        request_url = self.host + url
        body = {
            "Data": {
                "Policy": {
                    "AgencyPolicyRef": co.RandomStr().create(),  # 第三方订单号
                    "PlanCode": "ZAN2022010804",  # 计划代码
                    "IssueDate": co.Time(),  # 出单时间
                    "EffectiveDate": co.Tomorrow(),  # 生效时间
                    "ExpireDate": co.SeveralDays(30),  # 失效时间
                    "GroupSize": "1",  # 被保人个数
                    "TotalPremium": "0",  # 总保费
                    "Currency": "CNY",  # 币别
                    "PaymentType": "4",  # 缴费方式：1-年缴2-月缴3-趸缴4-免缴
                    "FaceAmount": "6000000.00",  # 保额,注：1、保额可批增为初始保额2、医疗险多种条款为保额之和
                    "ResponsibilityList": None  # 组合责任列表(部分产品必传) 示例： [“010231”,”010232”]
                },
                "PolicyHolder": {
                    "PolicyHolderType": "1",  # 投保人类型1-个人2-企业或者机构
                    "PolicyHolderName": "张学帅",  # 用户姓名（企业、公司名称）
                    "PolicyHolderSex": None,  # 性别（0女，1男，2其它）
                    "PHIdType": "01",
                    # 证件类型01身份证,02户口簿,03护照,04军官证,05驾驶执照,06港澳返乡证,07台胞证,08出生证,09统一社会信用代码,10纳税人识别号,11其他)
                    "PHIdNumber": "21060219990416440X",  # 证件号
                    "PHTelephone": co.Mobilephone(),  # 手机号（投保人类型为2-企业时非必填）
                    "PHBirthDate": "19990416000000",  # 出生日期 （投保人类型为2-企业时非必填）
                    "PHEmail": co.Mailbox(),  # 邮箱
                    "PHAddress": "深圳市",  # 详细地址
                    "PHAreaCode": None  # 市级区域编码（例如：泰康人寿飞铁保需要传第三级区域编码“421381”对应“广水市”，全称为“湖北省随州市广水市”，区域编码由经济公司提供）
                },
                "InsuredList": [
                    {
                        "InsuredId": "1",  # 被保险人唯一Id，用来确认该保单下被保险人的唯一性
                        "InsuredName": "张学帅",  # 用户姓名
                        "Gender": None,  # 性别（0女，1男，2其它）
                        "Type": "1",  # 被保人类型1-个人2-企业或者机构
                        "InsuredType": None,  # 被保险人类型(证件类型)
                        "IdType": "01",
                        # 证件类型01身份证,02户口簿,03护照,04军官证,05驾驶执照,06港澳返乡证,07台胞证,08出生证,09统一社会信用代码,10纳税人识别号,11其他)
                        "IdNumber": "21060219990416440X",  # 证件号
                        "Mobile": None,  # 手机号
                        "BirthDate": "19990416000000",  # 出生日期
                        "Email": co.Mailbox(),  # 邮箱
                        "ResideAddress": "深圳市",  # 详细地址
                        "PolicyholderInsuredRelation": "01",  # 被保人与投保人关系(01本人,02配偶,07儿女,08父母,22其他) 投保类型为2时不传
                        "SocialSecurityFlag": "0",  # 有无社保,健康险必传，意外险非必传 投保类型为2时不传   (0无1有)
                        "UnderwritingType": None,  # 智能核保问卷告知 支持智能核保产品必传0-全无 1-部分是
                        "UnderwritingQuestionList": None,  # 智能核保问卷(智能核保问卷部分是时必填 )
                        "AreaCode": None,  # 市级区域编码（例如：泰康人寿飞铁保需要传第三级区域编码“421381”对应“广水市”，全称为“湖北省随州市广水市”，区域编码由经济公司提供）
                        "ProfessionHighRisk": None  # 是否高危职业：0-否，1-是
                    }
                ]
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0005",
            "Version": "1.0.0",
        }
        # print(json.dumps(body, ensure_ascii=False))
        print(f'[{co.Execution_Time()}]-Request:\n{co.JsonFormatting(body)}')
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = (One_order().One_order())
    print(f'[{co.Execution_Time()}]-Response:\n{Res}')
