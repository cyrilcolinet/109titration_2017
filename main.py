##
## EPITECH PROJECT, 2018
## 109titration_2017
## File description:
## main function
##

import sys
from utils import *
from calc import *

def titration(data):
	derive = calc_derivative(data)
	calc_second_derivative(derive, data)
	calc_second_derivative_estimation(derive, data)

def main():
	data = []
	check_arguments()
	data = load_csv_file()
	titration(data)
