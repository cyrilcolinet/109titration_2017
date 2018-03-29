##
## EPITECH PROJECT, 2018
## 109titration_2017
## File description:
## calc functions
##

import sys
import math

def calc_pns(data, derive):
	default = 0.0
	result = []
	result.append(1)
	result.append(0)
	for i in range(1, len(data) - 1):
		if default < derive[i]:
			default = derive[i]
			result[0] = data[i][0]
			result[1] = i
	return result

def calc_derivative(data):
	derive = []
	derive.append(0)
	print("Derivative:", file=sys.stderr)
	for i in range(1, len(data) - 1):
		calc = data[i + 1][1] - data[i - 1][1]
		calc /= (data[i + 1][0] - data[i - 1][0])
		derive.append(calc)
		print("volume: %g ml -> %.2f" %(data[i][0], derive[i]))
	pns = calc_pns(data, derive)
	derive.append(0)
	print("\nEquivalent point at %g ml\n" % pns[0])
	return derive

def calc_second_derivative(derive, data):
	print("Second derivative")
	for i in range(1, len(derive) - 3):
		ph = (derive[i + 2] - derive[i])
		ph /= (data[i + 2][0] - data[i][0])
		print("volume: %g ml -> %.2f" % (data[i + 1][0], ph))
	print("\nSecond derivative estimated:")

def calc_second_derivative_estimation(derive, data):
	pns = calc_pns(data, derive)
	recursive = pns[0]
	key = pns[1]
	it = data[key - 1][0]
	ph = 0
	one = 0
	if not key - 2 < 0:
		ph = (derive[key] - derive[key - 2])
		ph /= (data[key][0] - data[key - 2][0])
		one = ph
	two = (derive[key + 1] - derive[key - 1])
	two /= (data[key + 1][0] - data[key - 1][0])
	res = (two - one)
	res /= (10 * (data[key][0] - data[key - 1][0]))
	while it - 0.05 < data[key][0]:
		print("volume: %g ml -> %.2f" % (it, one))
		if math.fabs(ph) > math.fabs(two) and key + 3 < len(data):
			ph = one
			recursive = it
		one += res
		it += 0.1
