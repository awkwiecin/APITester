import csv

def create_list_from_csv(file_name):
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def create_string_list_from_csv(file_name):
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        data_joined_into_one_list = [''.join(ele) for ele in data]
    return data_joined_into_one_list