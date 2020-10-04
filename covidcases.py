import requests

url = "https://corona-virus-world-and-india (From rapid API) "

headers = {
    From rapid API 
    }

response = requests.request("GET", url, headers=headers).json()


def search_by_city(cityname, status):
    for each in response['state_wise']:
        if int(response['state_wise'][each][status]) != 0:
            for city in response['state_wise'][each]['district']:
                if city == cityname and status == 'active':
                    return response['state_wise'][each]['district'][city]['active']

                if city == cityname and status == 'confirmed':
                    return response['state_wise'][each]['district'][city]['confirmed']

                if city == cityname and status == 'deaths':
                    return "No data Avilable at this moment!"
                if city == cityname and status == 'recovered':
                    return response['state_wise'][each]['district'][city]['recovered']


flag = 1
while flag != 0:
    cityname = input("Enter the city: ").title()
    status = input(
        "Must enter status: active, confirmed, recovered, deaths-: ").lower()
    if cityname == '0':
        break
    if status == '':
        print('Need to enter the status')
        break
    cases = search_by_city(cityname, status)
    print(f"Total {status} cases in {cityname}: {cases}")
    break
