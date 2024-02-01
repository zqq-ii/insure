# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")


class Refund_sales:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "callback_host")

    def Refund_sales(self):
        url = "/issuingmc/channelopenapi/query/statusNotice"
        request_url = self.host + url
        body = {
            "apply_content": {
                "end_policy_type": "16",
                "endorTypeTips": "EPC0011",
                "endor_no": "E231113000083010138620",
                "id_no": "522624199801072257",
                "id_type": "01",
                "installments_detail": [{
                    "num": "1",
                    "refund_amount": "830"
                },
                    {
                        "num": "2",
                        "refund_amount": "0"
                    },
                    {
                        "num": "3",
                        "refund_amount": "0"
                    },
                    {
                        "num": "4",
                        "refund_amount": "0"
                    },
                    {
                        "num": "5",
                        "refund_amount": "0"
                    },
                    {
                        "num": "6",
                        "refund_amount": "0"
                    },
                    {
                        "num": "7",
                        "refund_amount": "0"
                    },
                    {
                        "num": "8",
                        "refund_amount": "0"
                    },
                    {
                        "num": "9",
                        "refund_amount": "0"
                    },
                    {
                        "num": "10",
                        "refund_amount": "0"
                    },
                    {
                        "num": "11",
                        "refund_amount": "0"
                    },
                    {
                        "num": "12",
                        "refund_amount": "0"
                    }
                ],
                "installments_num": "1",
                "installments_total": "12",
                "policy_no": "H231113004063920138620",
                "premium": "0",
                "ret_endtime": "2023-11-13 14:46:39",
                "ret_money": "830",
                "ret_time": "2023-11-13 14:46:37"
            },
            "endorInfo": "4KV0PhxzpVZLsjrHJp2K3mkNIHHUxzD8Ik4NagUQISj3Ht+9JUMS56qMN5RG5FeX+hiaWvSzjcBRv8U470/8OcYy9lsDYaZURsMZlklLhzHQsp15f2OuJplzhWYBYYWOWvs22nGhpbyZJdBiJPnP2S0NIkFAhyhW6N+dZ68GWGSm4w5vbLBiDYoY0wC4Lny/nueIBGCfeDHjmAjQfVx7SoiL3dEDKwg9XwBIMA8G7W+mLmcJRd8Ve4Qak23UCNSnaH6A9xR9yTzUzZQm8uyVoDIHp0SpbA9MUSlxoe4dDo5gAehSsRhBkWz+3Lowm2LLBgfce1FL5aIR/v1Qwf05GmTcDqIuG4dbREjEbpM5nszGg3YyQZQ61ftzDJ4qwF+6Jvd1T46z+e9eeoYQfxgP/m84owqA3rZl9jldQysxXofLEbhEMNUBj1bjRUfJEwzxDJ6DKR6aoHfOuKM96CdoZ5rgzHf0EZZ3Pr1VzEbf1z+onVPVjTPO2IWXMRzF8af6kEXz9zO+VuLXH/mkQRwLH/clPDBzsv3ppSSY6U6RotfzI/hftpvi59A1RVlf6QNtRfB20xlBIlcwWi+b7Pb9A6JJ7gsr+yWX9f+XBtJSCQ+KaEAbcZWrpxJtqI9bjxjVT9vQxS4I0ED9k6EGrPwVkR43YVRC52CqrYFJxDw3jr5P29DFLgjQQP2ToQas/BWRuL74e1jKhO7Q6ZmcXjbf3U/b0MUuCNBA/ZOhBqz8FZFXaDSG40GYoGvNGpShJorYT9vQxS4I0ED9k6EGrPwVkRX4qGqS+G6HA4IknnCqhsF+4/rgdFMxw5I6fs8PSljXPDn77ZJmTlx44z2lAIDuHxvLSRZlg9Sa4ECxymqA3nSVTOrn919nDebW0K2uj8p+iWRvkU3PnPwKdjveyz8AOEHM5X08NDrksTaIQL8tqWBHNKOBt3tuc1tLVy6acAg6ybMeaay4F9EegIIQbgBUSNztSlACbxIiAZRaBCC1BXQU8SbtzFlVXUyBMBqNoMh5ZXWt4b649L+471L6cw+U2QQjmD67NFqUJHE6VHTyfWcPbCC4K1SkX8v4kDfXqrNVOcTTMyU4ZcfATF1Oiu36iEFSisZsFrnOQk8I4mwIFO6Q9eCrxTt1CWScpTGbZt8khnYwsqnl2GCl/rdM8hcRQQcRk5stekYVbX0/t+CZDFjsICljk/lPZdtbaJqbs627j0NdHXLCMW3qno5tPHunp2al+tO7x4NZGEjPubqY7DcQh43ocnvQmbzsS1fiGY9s",
            "payway": "5",
            "serial_no": "54846210161939931",
            "service_id": "01",
            "sign": "6c1fa630777cd441e33a683403a980d9"
        }

        return SendMethod.post_json(url=request_url, json=body)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Refund_sales().Refund_sales()
    print(f'[{Execution_Time()}]\n{Res}')
