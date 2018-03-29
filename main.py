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
	default = 0.0
	derive = []
	tmp = 0
	sub = 1
	derive.append(0)
	print("Derivative:", file=sys.stderr)
	for i in range(1, len(data) - 1):
		calc = data[i + 1][1] - data[i - 1][1]
		calc /= (data[i + 1][0] - data[i - 1][0])
		derive.append(calc)
		print("volume: %g ml -> %.2f" %(data[i][0], derive[i]))
		if default < derive[i]:
			default = derive[i]
			sub = data[i][0]
			tmp = i
	derive.append(0)

def main():
	data = []
	check_arguments()
	data = load_csv_file()
	titration(data)
