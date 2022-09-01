import api_call_service
import csv_service
import call_parameters_creator

data = csv_service.create_string_list_from_csv("../Data/test_users.csv")
apis = csv_service.create_string_list_from_csv("../Data/api_under_test.csv")
#api = "https://localhost:51928/clientlist/get-clients"
for api in apis:
    for user_name in data:
        print("---------")
        print("User name: ", user_name)
        params = call_parameters_creator.create_params_for_client_list_api(user_name)
        api_call_service.get_with_params(api, params)
        print("---------")

