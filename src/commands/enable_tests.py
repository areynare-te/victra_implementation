import requests, re

test_relation = {
    "Alaska" : "4519688",
    "Bay Area" : "4520897",
    "California" : "4520906",
    "Carolina": "4520919",
    "Florida" : "4520920",
    "Georgia" : "4520921",
    "Hawaii" : "4520922",
    "Iowa" : "4520923",
    "Kansas" : "4520924",
    "Michigan" : "4520925",
    "MidWest" : "4520945",
    "Midwest Central" : "4520953",
    "Minnesota" : "4520954",
    "NorthEast" : "4520955",
    "NorthWest" : "4520956",
    "Ohio" : "4520957",
    "Pennsylvania" : "4520958",
    "Southeast Central" : "4520959",
    "SouthWest" : "4520960",
    "Tenesse" : "4520968",
    "Virginia" : "4520969",
    "Wisconsin" : "4520970"
}

re_pattern = re.compile(r'Shops\s(.*?)(?=\s*-)')

def enable_test(alerted_test):
    region = re.search(re_pattern, alerted_test)
    print(region)
    test = test_relation.get(region, '4519688')
    enable_body = {"enabled": 'true'}
    headers = {"Authorization": "Bearer 05dd35b2-863a-469c-86da-99e74ba499d8"}
    enable_response = requests.put("https://api.thousandeyes.com/v7/tests/http-server/"+ test + "?aid=1129196", json=enable_body, headers=headers)
    return