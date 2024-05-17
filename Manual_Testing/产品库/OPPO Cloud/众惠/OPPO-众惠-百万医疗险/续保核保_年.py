# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

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
                    "OriginalPolicyRef": "P10E120240101V0014490",  # 原保单号
                    "AgencyPolicyRef": co.RandomStr().create(),  # 第三方订单号
                    "PlanCode": "ZH2023110901",  # 续保计划码
                    "IssueDate": co.Time(),  # 出单时间      (注:不可倒签)
                    "EffectiveDate": co.Tomorrow(),  # 生效时间
                    "ExpireDate": co.SeveralYears(),  # 失效时间
                    "GroupSize": "1",  # 被保人个数
                    "Currency": "CNY",  # 币种
                    "PaymentType": "1",  # 缴费方式：1-年缴2-月缴3-趸缴4-免缴
                    "TotalPremium": "806.40",  # 总保费
                    "FaceAmount": "6000000.00",  # 保额
                    "InstallmentNumber": None,  # 分期期数
                    "ResponsibilityList": None  # 责任列表(无特殊说明必传)目前用于续保责任免除场景示例： [“010231”,”010232”]
                },
                "PolicyHolder": {
                    "PolicyHolderType": "1",  # 投保人类型1-个人2-企业或者机构
                    "PolicyHolderName": "斜刘海",  # 用户姓名
                    "PHIdType": "01",
                    # 证件类型01居民身份证,02户口簿,03护照,04军官证,05驾驶执照,06港澳返乡证,07台胞证,08出生证,09统一社会信用代码,10纳税人识别号,11其他) 特殊说明下必传
                    "PHIdNumber": "513333199801079028",  # 证件号
                    "PHBirthDate": "19980107000000",  # 出生日期
                    "PHTelephone": "13410506136",  # 手机号
                    "SocialSecurityFlag": "0"  # 有无社保 (0无1有)
                },
                "InsuredList": [
                    {
                        "InsuredId": "7",  # 被保险人唯一Id
                        "InsuredName": "斜刘海",  # 用户姓名
                        "InsuredType": None,  # 被保险人类型(参考附录 证件类型（个人）) 特殊说明下必传
                        "Type": "1",  # 被保人类型1-个人2-企业或者机构（默认个人）
                        "IdType": "01",
                        # 证件类型证件类型01居民身份证,02户口簿,03护照,04军官证,05驾驶执照,06港澳返乡证,07台胞证,08出生证,09统一社会信用代码,10纳税人识别号,11其他) 特殊说明下必传
                        "IdNumber": "513333199801079028",  # 证件号
                        "BirthDate": "19980107000000",  # 出生日期
                        "Mobile": "13410506135",  # 手机号投保类型为2非必传
                        "PolicyholderInsuredRelation": "01",
                        # 被保人与投保人关系(01本人,02配偶,03丈夫,04妻子,05儿子,06女儿,07儿女,08父母,09父亲,10母亲) 投保类型为2时不传
                        "UnderwritingType": "0",  # 智能核保问卷告知 支持智能核保产品必传0-全无 1-部分是
                        "SocialSecurityFlag": "0"  # 有无社保 (0无1有)
                    }
                ],
                # "InstallmentList": [
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
            "RequestType": "0032",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Renew_insurance().Renew_insurance()
    print(f'[{co.Execution_Time()}]\n{Res}')
