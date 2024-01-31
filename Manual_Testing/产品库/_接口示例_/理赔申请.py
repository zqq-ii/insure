# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Time,Execution_Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")


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
                "PolicyNo": "PLE220234403QX00A00165",  # 保单号
                "ReportTime": "20231129173615",  # 报案时间 yyyyMMddHHmmss
                "ReporterName": Time(),  # 报案人姓名
                "ReporterPhone": "本人的电话号码",  # 报案人联系电话
                "ReportProvinceName": "广东省",  # 报案地-省
                "ReportCityName": "东莞市",  # 报案地-市
                "ReportAreaName": "长安镇",  # 报案地-区
                "ReportAddrDetail": "广东省东莞市长安镇乌沙海滨路18号OPPO工业园F2二楼售后业务中心",  # 报案地-具体地址
                "DamageTime": Time(),  # 出险时间
                "DamageReasonName": "7天无理由退货",  # 出险详细原因
                "ExtraVo": {  # 拓展信息
                    "LogisticsInfo": {  # 物流信息(非必填)，退运险必传
                        "ReturnLogisticsTrackingNo": RandomStr().create(),  # 发货物流单号
                        "BuyerDeliveryTime": Time(),  # 买方退换货发货时间yyyyMMddHHmmss
                        "BuyerId": "666666",  # 买方唯一标识ID ssoid(OPPO用户唯一标识)
                        "DeliveryTime": Time(),  # 发货时间yyyyMMddHHmmss
                        "GoodsType": "数码产品",  # 货物类型，值例，数码产品
                        "OrderNo": "3r4KD6z7EaDW8zY9",  # 需要理赔的订单编号
                        "ReceivingTime": Time(),  # 收货时间yyyyMMddHHmmss
                        "ReturnCost": "4.999",  # 退货费用，保留两位小数
                        "ReturnDestinationAddress": "东莞市长安镇乌沙海滨路18号OPPO工业园F2二楼售后业务中心",  # 退货目的地地址
                        "ReturnLogisticsCompany": "专业物流公司",  # 退货物流公司名称
                        "ReturnReceivingTime": Time(),  # 卖方收到退货时间yyyyMMddHHmmss
                        "ReturnTime": Time(),  # 发起退换货时间yyyyMMddHHmmss
                        "ShippingLogisticsNo": RandomStr().create(),  # 发货物流单号
                        "ReceiptAddress": "广东深圳"  # 发货目的地 可简写到省市
                    }
                }
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": RandomStr().create(),
            "RequestType": "0052",
            "Version": "1.0.0"
        }
        return SendMethod.AesEcb_post(key=self.key, url=request_url, body=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = (Freight_claims().Freight_claims())
    print(f'[{Execution_Time()}]\n{Res}')
