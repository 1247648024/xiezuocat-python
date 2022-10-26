import requests
import json
import time
import base64
import sm3_signature_util

class Xiezuocat:
    def __init__(self, secret_key):
        self._secret_key = secret_key
        self._check_url = "https://apicheck.xiezuocat.com/api/text_check"
        self._rewrite_url = "https://api.xiezuocat.com/para_api_v2"

    def set_check_url(self, check_url):
        self._check_url = check_url

    def set_rewrite_url(self, rewrite_url):
        self._rewrite_url = rewrite_url

    def check(self, data):
        headers = {
            'Content-Type': 'application/json',
            'secret-key': self._secret_key
        }

        response = requests.request("POST", self._check_url, headers=headers, data=data)

        return response.text

    def rewrite(self, data):
        headers = {
            'Content-Type': 'application/json',
            'secret-key': self._secret_key
        }

        response = requests.request("POST", self._check_url, headers=headers, data=data)

        return response.text

    def signature(self, appId, user_id):
        timestamp = time.time()
        para_map = {}
        para_map["appId"] = appId
        para_map["uid"] = user_id
        para_map["timestamp"] = timestamp
        sign = sm3_signature_util.signature_sm3(para_map, self._secret_key)
        para_map["sign"] = sign
        base64_str = str(base64.b64encode(str(para_map).encode('utf-8')), "utf-8")

        return base64_str



a = Xiezuocat("xx")
# a.set_check_url("https://checkerbeta.metasotalaw.cn/api/text_check")
# check_data = json.dumps({
#             "texts": [
#                 "哈哈哈。我天今吃了一顿饭",
#                 "我想念十分赵忠祥。嘿嘿嘿。"
#             ]
#         })
# check_result = a.check(check_data)
# print("check_result === ", check_result)
#
# a.set_check_url("https://checkerbeta.metasotalaw.cn/html/api/rewrite")
# rewrite_data = json.dumps({
#   "items": [
#     "一般"
#   ],
#   "level": "middle"
# })
# rewrite_result = a.rewrite(rewrite_data)
# print("rewrite_result === ", rewrite_result)

sign_result = a.signature("xx", "ll")
print("sign_result === ", sign_result)