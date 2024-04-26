# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.common.RandomNumber import RandomStr, Execution_Time
from Manual_Testing.Environment import Environment
from Manual_Testing.common.PrintData import Logger

config = Config("config.ini")


class Payment_callback:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "callback_host")

    def Payment_callback(self):
        url = "/issuingmc/channelopenapi/directPay/activePay/callback"
        request_url = self.host + url
        body = ("e4Qez8VnpsQG83sxchd7aSHFgMO7a9wolbpCE7slS52Q9dRwD9KMH1TjOsYUO01MQFUhPmN071jSk6Jmip9EV7TeklKgHDMvAZer"
                "PzBqux8a3b7JndZ+IE0v1NVqvh8o8x7ALV0WNGiUTrJ+ugqrSslkucfJapYPVdE9aRPIVwBWUcjF50dGESoTWlBRhSXBViYON2GO"
                "84g8V8zGh8L4aNC04SHd6hp1pofyfVH3q6aJZ8mgqXRWn+5I299TANJbagSo3S1fgP5Vr8O6jn0AnRyWyMnIZTVsF8At1J1H768Xs"
                "bpGMmtuALNe/CUlX+DPw4+bqSyCWhgWXEyRF7/6GYx8TuYAMn18aep9IxlsBMNJVjiP6u25N22L7RDw37mfjWbeCkvr1+6o/16mMb"
                "Uim896B9IJQAUDe8DZ19m3fNGQb7qWatwr/qiWUuQnFK+/jmZvSfX09aNkucyg7PVu7kflSvM8nDphaHD70z3QPXIYv3d2OVF6iob"
                "RiHbJ1XUlVKm7fSLLIrv0cbrCvV3PkZ9j0AS4tBtYlWQPgC7U0sy+ECLq4g5JB1+ZGsFfHO/Y ")

        return SendMethod.post_data(url=request_url, data=body)


if __name__ == "__main__":
    sys.stdout = Logger()
    Res = Payment_callback().Payment_callback()
    print(f'[{Execution_Time()}]\n{Res}')
