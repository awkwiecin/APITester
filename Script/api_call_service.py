import requests

def simple_get(api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            print("response:")
            print(response.json())
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")

def get_with_params(api, parameters):
        response = requests.get(f"{api}", params=parameters, verify=False)
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            print("response:")
            print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

def api_test(api_uri):
    response = requests.get(api_uri)
    print(response.status_code)
