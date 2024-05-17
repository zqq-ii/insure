# -*- coding: utf-8 -*-
import json, sys
from Manual_Testing.common.operation_config import Config
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

"""
太平门店一切险: TP2023051101
太平门店公责险: TP2023051102
"""
config = Config("config.ini")
RandomZ = co.RandomStr().create()


class Joint_Investment:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Joint_Investment(self):
        url = "/issuingmc/channelapi/insure/permutation/check"
        request_url = self.host + url
        body = {
            "Data": {
                "IsPermutation": True,  # 是否组合投保;默认为true,可不传,
                "PoliciesCommon":
                    {
                        "AgencyPolicyRef": RandomZ,  # 第三方订单号
                        "TotalPremium": "860.00",  # 总保费
                        "Currency": "CNY",  # 币别
                        "PaymentType": "1",  # 缴费方式：1-年缴2-月缴3-趸缴4-免缴
                        "TotalFaceAmount": "2500000.00",  # 总保额
                        "PlanCodeList": ["TP2023051101", "TP2023051102"]  # 组合投保的计划码列表，可以是一个或者多个 如 [10001,10002]
                    },
                "PolicyInfoList":
                    [
                        {
                            "Policy": {
                                "AgencyPolicyRef": co.RandomStr().create(),  # 小保单第三方订单号
                                "PlanCode": "TP2023051101",  # 计划代码
                                "GroupSize": "1",  # 被保人个数
                                "IssueDate": co.Time(),  # 出单时间
                                "EffectiveDate": co.Tomorrow(),  # 生效时间
                                "ExpireDate": co.SeveralYears(),  # 失效时间
                                "PaymentType": "1",  # 缴费方式
                                "Currency": "CNY",  # 币别
                                "TotalPremium": "470.00",  # 保费
                                "FaceAmount": "500000.00"  # 保额
                            },
                            "PolicyHolder":
                                {
                                    "PolicyHolderType": "1",  # 投保人类型：1-个人，2-企业或者机构
                                    "PolicyHolderName": "游点叼",  # 投保人名称（个人-姓名；企业/机构-公司/机构名称）
                                    "PHIdType": "01",  # 证件类型;01居民身份证,09统一社会信用代码;投保类型为2不传
                                    "PHIdNumber": "431123199801075873",  # 证件号
                                    "PHContactName": "游点叼",  # 联系人姓名
                                    "PHTelephone": "13410506136",  # 联系人手机号
                                    "PHEmail": "45454546@qq.com",  # 电子邮箱
                                    "PHAddress": "深圳市前海卓越T1",  # 联系地址
                                    "PHPostCode": "518000",  # 邮政编码
                                    "PHBirthDate": "19980107000000"  # 出生日期;个人投保必传，格式YYYYMMDDHHMMSS
                                },
                            "InsuredList":
                                [
                                    {
                                        "InsuredId": "1",  # 被保险人唯一Id（一个被保人默认传“1”，多个被保人按顺序排序 ）
                                        "InsuredName": "欧珀官方旗舰店前海分店",  # 被保人名称（个人-姓名；企业/机构-公司/机构名称）
                                        "Email": "889776565@qq.com",  # 电子邮箱
                                        "IdType": "09",  # 证件类型;01居民身份证,09统一社会信用代码;投保类型为2不传
                                        "IdNumber": "91441900MA545CQH4R",  # 证件号
                                        "Type": "2",  # 被保人类型：1个人，2-企业或者机构
                                        "InsuredContactName": "游点叼",  # 联系人姓名
                                        "InsuredContactTelephone": "18289782730",  # 联系人手机号
                                        "InsuredAddress": "深圳市前海卓越T1-L02"  # 联系地址
                                    }
                                ],
                            "SubjectMatterInsured":
                                {
                                    "SubjectMatterInsuredName": "欧珀官方旗舰店前海分店",  # 门店名称
                                    "SubjectMatterInsuredAddress": "广东省深圳市南山区前海卓越T1-L02",  # 门店地址
                                    "FaceAmount": None,  # 标的保额 ，单位 元
                                    "StoreArea": None,  # 门店面积 1：0-150平米，2：150-300平米
                                    "Province": "广东省",  # 省份
                                    "City": "深圳市",  # 市
                                    "District": "南山区"  # 区
                                }
                        },
                        {
                            "Policy":
                                {
                                    "AgencyPolicyRef": co.RandomStr().create(),
                                    "PlanCode": "TP2023051102",
                                    "GroupSize": "1",
                                    "IssueDate": co.Time(),  # 出单时间
                                    "EffectiveDate": co.Tomorrow(),  # 生效时间
                                    "ExpireDate": co.SeveralYears(),  # 失效时间
                                    "PaymentType": "1",
                                    "Currency": "CNY",
                                    "TotalPremium": "390.00",
                                    "FaceAmount": "2000000.00"
                                },
                            "PolicyHolder":
                                {
                                    "PolicyHolderType": "1",  # 投保人类型：1-个人，2-企业或者机构
                                    "PolicyHolderName": "游点叼",  # 投保人名称（个人-姓名；企业/机构-公司/机构名称）
                                    "PHIdType": "01",  # 证件类型;01居民身份证,09统一社会信用代码;投保类型为2不传
                                    "PHIdNumber": "431123199801075873",  # 证件号
                                    "PHContactName": "游点叼",  # 联系人姓名
                                    "PHTelephone": "13410506136",  # 联系人手机号
                                    "PHEmail": "45454546@qq.com",  # 电子邮箱
                                    "PHAddress": "深圳市前海卓越T1",  # 联系地址
                                    "PHPostCode": "518000",  # 邮政编码
                                    "PHBirthDate": "19980107000000"  # 出生日期;个人投保必传，格式YYYYMMDDHHMMSS
                                },
                            "InsuredList":
                                [
                                    {
                                        "InsuredId": "1",  # 被保险人唯一Id（一个被保人默认传“1”，多个被保人按顺序排序 ）
                                        "InsuredName": "欧珀官方旗舰店前海分店",  # 被保人名称（个人-姓名；企业/机构-公司/机构名称）
                                        "Email": "889776565@qq.com",  # 电子邮箱
                                        "IdType": "09",  # 证件类型;01居民身份证,09统一社会信用代码;投保类型为2不传
                                        "IdNumber": "91441900MA545CQH4R",  # 证件号
                                        "Type": "2",  # 被保人类型：1个人，2-企业或者机构
                                        "InsuredContactName": "游点叼",  # 联系人姓名
                                        "InsuredContactTelephone": "18289782730",  # 联系人手机号
                                        "InsuredAddress": "深圳市前海卓越T1-L02"  # 联系地址
                                    }
                                ],
                            "SubjectMatterInsured":
                                {
                                    "SubjectMatterInsuredName": "欧珀官方旗舰店前海分店",  # 门店名称
                                    "SubjectMatterInsuredAddress": "广东省深圳市南山区前海卓越T1-L02",  # 门店地址
                                    "FaceAmount": 390,  # 标的保额 ，单位 元
                                    "StoreArea": 1,  # 门店面积 1：0-150平米，2：150-300平米
                                    "Province": "广东省",  # 省份
                                    "City": "深圳市",  # 市
                                    "District": "南山区"  # 区
                                }
                        }
                    ]
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomZ,
            "RequestType": "0047",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Joint_Investment().Joint_Investment()
    print(f'[{co.Execution_Time()}]\n{Res}')
