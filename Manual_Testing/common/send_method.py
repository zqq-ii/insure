# -*- coding: utf-8 -*-
import requests, json
from Manual_Testing.common.encryption_decryption import EncryptDate
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
    def PostData_ae(key, url, body, headers):
        try:
            aes = EncryptDate(key)
            Body = aes.encrypt(JsonFormatting(body))
            response = requests.post(url=url, data=Body, headers=headers)
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
