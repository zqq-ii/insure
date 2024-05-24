# -*- coding: utf-8 -*-
import requests, json
from Manual_Testing.common.AesDensity import AesDensity
from Manual_Testing.common.communal import JsonFormatting


class SendMethod:
    @staticmethod
    def get(url, params=None, headers=None):
        try:
            response = requests.get(url=url, params=params, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            result["ResponseBody"] = response.json()
            return JsonFormatting(result)
        except:
            result = None
            return result

    @staticmethod
    def post_data(url, data=None, headers=None):
        try:
            response = requests.post(url=url, data=data, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            result["ResponseBody"] = response.json()
            return JsonFormatting(result)
        except:
            result = None
            return result

    @staticmethod
    def post_datax(url, data=None, headers=None):
        try:
            response = requests.post(url=url, data=data, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            result["ResponseBody"] = response.text
            return JsonFormatting(result)
        except:
            result = None
            return result

    @staticmethod
    def post_json(url, json=None, headers=None):
        try:
            response = requests.post(url=url, json=json, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            result["ResponseBody"] = response.json()
            return JsonFormatting(result)
        except:
            result = None
            return result

    @staticmethod
    def post_jsonx(url, json=None, headers=None):
        try:
            response = requests.post(url=url, json=json, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            result["ResponseBody"] = response.text
            return JsonFormatting(result)
        except:
            result = None
            return result

    @staticmethod
    def PostData_aes(key, url, data=None, headers=None):
        try:
            aes = AesDensity(key)
            Data = aes.encrypt(json.dumps(data, ensure_ascii=False))
            response = requests.post(url=url, data=Data, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            if response.status_code == 200:
                result["ResponseBody"] = json.loads(aes.decrypt(response.text))
                return JsonFormatting(result)
            else:
                try:
                    result["ResponseBody"] = json.loads(response.text)
                    return JsonFormatting(result)
                except:
                    result["ResponseBody"] = response.text
                    return JsonFormatting(result)
        except:
            result = None
            return result


if __name__ == '__main__':
    """
    """
