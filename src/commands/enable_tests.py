import requests, re

test_relation = {
    'AK' : '1129196'
}

re_pattern = re.compile(r'\b([A-Z]{2})\d{3}\b')

def enable_test(agents):
    states = re.findall(re_pattern, agents)
    for codigo_estado in states:
        test = test_relation.get(codigo_estado, '4520164')
        enable_body = {"enabled": 'true'}
        headers = {"Authorization": "Bearer 05dd35b2-863a-469c-86da-99e74ba499d8"}
        enable_response = requests.put("https://api.thousandeyes.com/v7/tests/http-server/"+ test + "?aid=1129196", json=enable_body, headers=headers)
        print("test enabled")
    return