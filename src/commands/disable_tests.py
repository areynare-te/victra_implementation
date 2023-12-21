import requests, re

test_relation = {
    "Shops AK" : "4529007",
    "Shops AL" : "4529008",
    "Shops AZ" : "4529011",
    "Shops CA" : "4529015",
    "Shops CO" : "4529018",
    "Shops DE" : "4529025",
    "Shops FL" : "4529027",
    "Shops GA" : "4529029",
    "Shops HI" : "4529031",
    "Shops IA" : "4529050",
    "Shops ID" : "4529032",
    "Shops IL" : "4529046",
    "Shops IN" : "4529048",
    "Shops KS" : "4529053",
    "Shops KY" : "4529054",
    "Shops LA" : "4529055",
    "Shops MA" : "4529060",
    "Shops MD" : "4529059",
    "Shops ME" : "4529057",
    "Shops MI" : "4529062",
    "Shops MN" : "4529063",
    "Shops MO" : "4529085",
    "Shops MS" : "4529083",
    "Shops MT" : "4529086",
    "Shops NC" : "4529093",
    "Shops ND" : "4529094",
    "Shops NE" : "4529087",
    "Shops NH" : "4529089",
    "Shops NJ" : "4529090",
    "Shops NM" : "4529092",
    "Shops NV" : "4529088",
    "Shops NY" : "4529091",
    "Shops OH" : "4529102",
    "Shops OK" : "4529103",
    "Shops OR" : "4529105",
    "Shops PA" : "4529106",
    "Shops RI" : "4529107",
    "Shops SC" : "4529108",
    "Shops SD" : "4529109",
    "Shops TN" : "4529111",
    "Shops TX" : "4529112",
    "Shops UT" : "4529113",
    "Shops VA" : "4529121",
    "Shops VT" : "4529120",
    "Shops WA" : "4529123",
    "Shops WI" : "4529125",
    "Shops WV" : "4529124",
    "Shops WY" : "4529126"
}

re_pattern = re.compile(r'Shops\s(.*?)(?=\s*-)')

def enable_test(alerted_test):
    region = re.search(re_pattern, alerted_test)
    test = test_relation.get(region.group(0), '4519688')
    enable_body = {"enabled": 'false'}
    headers = {"Authorization": "Bearer 05dd35b2-863a-469c-86da-99e74ba499d8"}
    enable_response = requests.put("https://api.thousandeyes.com/v7/tests/http-server/"+ test + "?aid=1129196", json=enable_body, headers=headers)
    return