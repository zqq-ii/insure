# This Python file uses the following encoding: utf-8
import requests, json
from Manual_Testing.common.encryption_decryption import EncryptDate


class SendMethod:
    @staticmethod
    def get(url, params=None, headers=None):
        try:
            response = requests.get(url=url, params=params, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            result["ResponseBody"] = response.json()
            return result
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
            return result
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
            return result
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
            return result
        except:
            result = None
            return result

    @staticmethod
    def AesEcb_post(key, url, body, headers):
        try:
            aes = EncryptDate(key)
            Body = aes.encrypt(json.dumps(body, ensure_ascii=False))
            response = requests.post(url=url, json=Body, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            if response.status_code == 200:
                result["ResponseBody"] = json.loads(aes.decrypt(response.text))
                return json.dumps(result, indent=4, ensure_ascii=False, separators=(',', ': '))
            else:
                try:
                    result["ResponseBody"] = json.loads(response.text)
                    return json.dumps(result, indent=4, ensure_ascii=False, separators=(',', ': '))
                except:
                    result["ResponseBody"] = response.text
                    return json.dumps(result, indent=4, ensure_ascii=False, separators=(',', ': '))
        except:
            return None


if __name__ == '__main__':
    """
    """
