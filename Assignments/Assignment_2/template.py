import numpy as np
from PIL import Image
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

def readSignal():
    input_line = input().strip()
    length = int(input_line.split(':')[0])
    signal = list(map(int, input_line.split(':')[1].strip()[1:-1].split(',')))
    return signal, length

def printSignal(length, signal):
    print(f"{length}: {signal}")