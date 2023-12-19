import requests, re

test_relation = {
    "Shops Alaska" : "4519688",
    "Shops Bay Area" : "4520897",
    "Shops California" : "4520906",
    "Shops Carolina": "4520919",
    "Shops Florida" : "4520920",
    "Shops Georgia" : "4520921",
    "Shops Hawaii" : "4520922",
    "Shops Iowa" : "4520923",
    "Shops Kansas" : "4520924",
    "Shops Michigan" : "4520925",
    "Shops MidWest" : "4520945",
    "Shops Midwest Central" : "4520953",
    "Shops Minnesota" : "4520954",
    "Shops NorthEast" : "4520955",
    "Shops NorthWest" : "4520956",
    "Shops Ohio" : "4520957",
    "Shops Pennsylvania" : "4520958",
    "Shops Southeast Central" : "4520959",
    "Shops SouthWest" : "4520960",
    "Shops Tenesse" : "4520968",
    "Shops Virginia" : "4520969",
    "Shops Wisconsin" : "4520970"
}

re_pattern = re.compile(r'Shops\s(.*?)(?=\s*-)')

def enable_test(alerted_test):
    region = re.search(re_pattern, alerted_test)
    print(region.group(0))
    test = test_relation.get(region.group(0), '4519688')
    print(test)
    enable_body = {"enabled": 'true'}
    headers = {"Authorization": "Bearer 05dd35b2-863a-469c-86da-99e74ba499d8"}
    enable_response = requests.put("https://api.thousandeyes.com/v7/tests/http-server/"+ test + "?aid=1129196", json=enable_body, headers=headers)
    return