import requests

def enable_test(agent):
    enable_body = {"enabled": 'true'}
    headers = {"Authorization": "Bearer 05dd35b2-863a-469c-86da-99e74ba499d8"}
    enable_response = requests.put("https://api.thousandeyes.com/v7/tests/http-server/4519688?aid=1129196", json=enable_body, headers=headers)
    print("test enabled")
    return