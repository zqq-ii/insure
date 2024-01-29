# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Mobilephone, Time, TomorrowPresently, Mailbox,Execution_Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")
"""
产品码：RB20231111
计划码：RB2023111105
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
                    "AgencyPolicyRef": RandomStr().create(),  # 第三方订单号
                    "PlanCode": "RB2023111105",  # 计划代码
                    "IssueDate": Time(),  # 出单时间      (注:不可倒签)
                    "EffectiveDate": Time(),  # 生效时间
                    "ExpireDate": TomorrowPresently(90),  # 失效时间
                    "GroupSize": "1",  # 被保人个数
                    "TotalPremium": "0.44",  # 总保费
                    "Currency": "CNY",  # 币别
                    "PaymentType": "3",  # 缴费方式：1-年缴2-月缴3-趸缴4-免缴
                    "FaceAmount": "100.00",  # 保额,注：1、保额可批增为初始保额2、医疗险多种条款为保额之和
                    "ResponsibilityList": None  # 组合责任列表(部分产品必传) 示例： [“010231”,”010232”]
                },
                "PolicyHolder": {
                    "PolicyHolderType": "2",  # 投保人类型1-个人2-企业或者机构
                    "PolicyHolderName": "欧珀广东移动通信有限公司",  # 用户姓名（企业、公司名称）
                    "PolicyHolderSex": None,  # 性别（0女，1男，2其它）
                    "PHIdType": "09",
                    # 证件类型01身份证,02户口簿,03护照,04军官证,05驾驶执照,06港澳返乡证,07台胞证,08出生证,09统一社会信用代码,10纳税人识别号,11其他)
                    "PHIdNumber": "914419007480321175",  # 证件号
                    "PHTelephone": Mobilephone(),  # 手机号（投保人类型为2-企业时非必填）
                    "PHBirthDate": None,  # 出生日期 （投保人类型为2-企业时非必填）
                    "PHEmail": Mailbox(),  # 邮箱
                    "PHAddress": "深圳市",  # 详细地址
                    "PHAreaCode": None  # 市级区域编码（例如：泰康人寿飞铁保需要传第三级区域编码“421381”对应“广水市”，全称为“湖北省随州市广水市”，区域编码由经济公司提供）
                },
                "InsuredList": [
                    {
                        "InsuredId": "6",  # 被保险人唯一Id，用来确认该保单下被保险人的唯一性
                        "InsuredName": "欧珀广东移动通信有限公司",  # 用户姓名
                        "Gender": None,  # 性别（0女，1男，2其它）
                        "Type": "2",  # 被保人类型1-个人2-企业或者机构
                        "InsuredType": None,  # 被保险人类型(证件类型)
                        "IdType": "09",
                        # 证件类型01身份证,02户口簿,03护照,04军官证,05驾驶执照,06港澳返乡证,07台胞证,08出生证,09统一社会信用代码,10纳税人识别号,11其他)
                        "IdNumber": "914419007480321175",  # 证件号
                        "Mobile": None,  # 手机号
                        "BirthDate": None,  # 出生日期
                        "Email": Mailbox(),  # 邮箱
                        "ResideAddress": "深圳市",  # 详细地址
                        "PolicyholderInsuredRelation": "22",  # 被保人与投保人关系(01本人,02配偶,07儿女,08父母,22其他) 投保类型为2时不传
                        "SocialSecurityFlag": None,  # 有无社保,健康险必传，意外险非必传 投保类型为2时不传   (0无1有)
                        "UnderwritingType": None,  # 智能核保问卷告知 支持智能核保产品必传0-全无 1-部分是
                        "UnderwritingQuestionList": None,  # 智能核保问卷(智能核保问卷部分是时必填 )
                        "AreaCode": None,  # 市级区域编码（例如：泰康人寿飞铁保需要传第三级区域编码“421381”对应“广水市”，全称为“湖北省随州市广水市”，区域编码由经济公司提供）
                        "ProfessionHighRisk": None  # 是否高危职业：0-否，1-是
                    }
                ],
                "Extension": {  # 拓展信息
                    "DeliveryInfo": {  # 货运信息(非必填),退运险必传
                        "Ssoid": "666666",  # 用户唯一ID(OPPO用户唯一标识)
                        "SigningTime": Time(),  # 签收时间 yyyyMMddHHmmss
                        "OrderNO": RandomStr().create(),  # 大订单号，存在多个订单时的的父订单号
                        "SubOrderNo": [RandomStr().create(), RandomStr().create()],  # 小订单号
                    }
                }
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0005",
            "Version": "1.0.0",
        }
        # print(json.dumps(body, ensure_ascii=False))
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = (One_order().One_order())
    print(f'[Execution_Time:{Execution_Time()}]\n{Res}')
