# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Claim_application:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Claim_application(self):
        url = "/issuingmc/channelapi/claim/machine/report"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyNo": "EP202303640158729486",  # 保单号
                "ReportOrderNo": co.RandomStr().create(),  # 报案订单号 (接口幂等字段)
                "ReporterName": "彦祖",  # 报案人姓名
                "ReporterPhone": "13410506136",  # 报案人联系电话
                "ReportDate": "20231108000000",  # 报案时间
                "ReportProvinceName": "广东省",  # 报案地 - 省
                "ReportCityName": "深圳市",  # 报案地 - 市
                "ReportAreaName": "南山区",  # 报案地 - 区
                "ReportAddrDetail": "梦海大道",  # 报案地 - 具体地址，比如门店地址等
                "ReportSource": "1",  # 报案来源渠道：1 - OPPO
                "ReportRepairCharge": "111.11",  # 报案维修费用
                "ReportServiceCharge": "50",  # 报案服务费
                "DamageDate": "20231108000000",  # 出险时间
                "DamageDetail": "测试单,反正就是坏了!",  # 出险详细经历（包括故障原因）
                "MaterialList": ["232320231030114019025"],  # 理赔材料Id列表 [“543534534”,”4324234234”]
                "RepairCompleteDate": "20231109000000",  # 维修完成时间
                "Reserve1": "CN097013"  # 保留字段1（网点编码）
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": co.RandomStr().create(),
            "RequestType": "0044",
            "Version": "1.0.0"
        }
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = co.Logger()
    Res = Claim_application().Claim_application()
    print(f'[{co.Execution_Time()}]-Response:\n{Res}')
