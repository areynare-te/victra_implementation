import requests, re

test_relation = {
    "Alaska" : "4519688",
    "Bay Area" : "4520897",
    "California" : "4520906",
    "Carolina": "4520919",
    ""
}

re_pattern = re.compile(r'Shops\s(.*?)(?=-)')

def enable_test(alerted_test):
    region = re.search(re_pattern, alerted_test)
    test = test_relation.get(region, '4519688')
    enable_body = {"enabled": 'true'}
    headers = {"Authorization": "Bearer 05dd35b2-863a-469c-86da-99e74ba499d8"}
    enable_response = requests.put("https://api.thousandeyes.com/v7/tests/http-server/"+ test + "?aid=1129196", json=enable_body, headers=headers)
    return