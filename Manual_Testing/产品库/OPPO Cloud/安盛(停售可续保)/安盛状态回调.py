# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as co

config = Config("config.ini")


class Status_callback:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "callback_host")

    def Status_callback(self):
        url = "/issuingmc/channelopenapi/as/status/notice"
        request_url = self.host + url
        body = ("bIC/xcN8VjrOz26/8X1CNhiscWuqHVIePPphDqlvoivGw9liZOnW4ZTavZJk9RbrCPJ9p1pxFM7CbQHS4hlCzYUwGOiJktq"
                "nEz7gM4V1v8T+ZD9PrvUc52PJkjIU7oyavilS0kw1invIuasloXnQ3Rk/aary3uny5XArBpPQ/M/APa0bhZM53EyJA7NxLf"
                "74mWzxREeVVTTYRusD2F6RtlQJk5UzQgL7VOEd/SmQt/9Ia4AUsbFFxJBkYt3Y49wt1FyjEFuLTHgybN+VO1M8ep/r+JvDK"
                "7JTQqyivfvaiazw7aEr3+26D7Q/1XizzOVF6ummO9FbeXr7h4afOGShoxTlVEJG6MjHfi1Jk53PbaPdFUoSCFdjQQQOKr4J+"
                "kLKk/xiwb8NVSfwLrbbOG0ydNtR9tMv2hL/XxPpuZtvoSG3gMGGbarbxCMEnCHtfQGUsP4elDLjW18oUA0wplLHZ3KYjwwAa3"
                "R48cUhPkk33V7LXVNuqcl+WhzuIqMEC5jUeAWxrhVCOPklRSCRu9bj3mk2sn9ufDa762HjJiquxKnCgrxRed/CFbPEiGDlBu+"
                "fMVPg1HkjsBTG6zLznuPNNGXzZkcFN/v/uRukMvVHcR/yaAMDtgovsJj3WJK0WKM4wsQhEzsoAB1D2J5czylHT1F2VW6BJQWi"
                "/k81U+7YUJ52OqmkBklPZukYoht6ia1yMmMmBakC+HQAHUzASWFoDcB9zh6aDbe+ur2+i4WSgUelyEymXGzpE7Xx2Rmw37uqXg"
                "AfppqXlcpj4UcRH7HwmFGlaNRc2tZX1jHOScgLi6oDwflm8xOQCkxXQqd+yffnPu1c+LQSyBx5H0ZDOPjkgDk5OEfs8npfqyou"
                "7M/LQRL3SnIy/ODP0E4Yzso3wVzrU1Y+FsYt9IZW5nC4S8rn3q5VJoknH3coJspzk9M5oxMdqkA01utdI5akxGz4cBFWXJnI2v"
                "hQy57LuP49JZNcrwuwuZaLYGrFJnabK+/Q6wKGxmoDmTKxcvFasWxLKDtODxo04olDPZlaWQwE8L3CJOCmrNQxC7AMUE6dNv8j"
                "QFcr4s/xtGyufKHJGbR6JDq/x7tkE+rQQ6qDoSEGYjNRvKNF5hWEeFwF4uR+7Kb9BBE6A0zlD2m9KQrqg5VMcSfN6g4ABHE+Ol"
                "urQ1GwjRj8zJINi9JxVs64GQUH5uT7/AhbvoKrCDuyU4rN/UFzzYFQJNhBBsAQDVQp57GnRLPj8XfrBf1IiKHD9neJigltRioK"
                "gzMD/yNuHAkj4sVNEZnX8t0IYWTe5O2aSvLBHtPU4y1oq55p3PZZ1dbR/BBF89zV9sGoAo5JyPUweuOuL2W8dR91FndiggMkxB"
                "F7ZAg+1A== ")
        return SendMethod.post_data(url=request_url, data=body)


if __name__ == "__main__":
    Res = Status_callback().Status_callback()
    print(f'[{co.Execution_Time()}]\n{Res}')
