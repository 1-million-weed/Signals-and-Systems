import math

def get_input_data():
    input_1, input_2, input_3 = map(int, input().split())
    return input_1, input_2, input_3

def print_output_data(output_data):
    print("{:.2f}".format(output_data))
    pass

def print_output_list(output_list):
    for output_data in output_list:
        print(output_data)
    pass