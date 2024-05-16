# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")
"""
注:测试环境出单成功后需保司手动汇总后才可进行理赔申请
"""


class Freight_claims:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Freight_claims(self):
        url = "/issuingmc/channelapi/claims"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyNo": "PLE220244403QX00A00178",  # 保单号
                "ReportTime": co.Time(),  # 报案时间 yyyyMMddHHmmss
                "ReporterName": "OPPO商城",  # 报案人姓名
                "ReporterPhone": "13410506136",  # 报案人联系电话
                "ReportProvinceName": "广东省",  # 报案地-省
                "ReportCityName": "东莞市",  # 报案地-市
                "ReportAreaName": "长安镇",  # 报案地-区
                "ReportAddrDetail": "广东省东莞市长安镇乌沙海滨路18号OPPO工业园F2二楼售后业务中心",  # 报案地-具体地址
                "DamageTime": co.Time(),  # 出险时间
                "DamageReasonName": "7天无理由退货",  # 出险详细原因
                "ExtraVo": {  # 拓展信息
                    "LogisticsInfo": {  # 物流信息(非必填)，退运险必传
                        "ReturnLogisticsTrackingNo": co.RandomStr().create(),  # 发货物流单号HarvestDate
                        "BuyerDeliveryTime": co.Time(),  # 买方退换货发货时间yyyyMMddHHmmss
                        "BuyerId": "666666",  # 买方唯一标识ID ssoid(OPPO用户唯一标识)
                        "DeliveryTime": co.Time(),  # 发货时间yyyyMMddHHmmss
                        "GoodsType": "手机周边",  # 货物类型，值例:手机周边,耳机,表带,生活周边,平板电脑配件,平板电脑,无线耳机,手机,日用品,通信设备、计算机及其他电子设备,手表
                        "OrderNo": "TenSer41QNgY0o8A",  # 需要理赔的订单编号
                        "ReceivingTime": co.Tomorrow(0),  # 买方签收时间,收货时间yyyyMMddHHmmss;(注:退原险,该时间必须早于出险时间)
                        "ReturnCost": "4.99",  # 退货费用，保留两位小数
                        "ReturnDestinationAddress": "东莞市长安镇乌沙海滨路18号OPPO工业园F2二楼售后业务中心",  # 退货目的地地址
                        "ReturnLogisticsCompany": "专业物流公司",  # 退货物流公司名称
                        "ReturnReceivingTime": co.Time(),  # 卖方收到退货时间yyyyMMddHHmmss
                        "ReturnTime": co.Time(),  # 发起退换货时间yyyyMMddHHmmss
                        "ShippingLogisticsNo": co.RandomStr().create(),  # 发货物流单号
                        "ReceiptAddress": "广东深圳"  # 发货目的地 可简写到省市
                    }
                }
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0052",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_aes(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = (Freight_claims().Freight_claims())
    print(f'[{co.Execution_Time()}]\n{Res}')
