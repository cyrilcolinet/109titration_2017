##
## EPITECH PROJECT, 2018
## 109titration_2017
## File description:
## utilfs functions
##

from os import path
from numpy import *
import csv
import sys

def my_help():
	print("USAGE:")
	print("\t./109titration [-h, --help, -g, --graph] <file>\n")
	print("DESCRIPTION:")
	print("\t-h, --help\tDisplay this help page")
	print("\t-g, --graph\tDisplay plot graph")
	print("\tfile\t\tA csv file containing \"vol;ph\" lines")
	sys.exit(0)

def check_arguments():
	length = len(sys.argv)
	res = []
	if length < 2:
		print("Wrong arguments number.\nUsage: ./109titration [-h, --help, -g, --graph] <file>")
		sys.exit(84)
	res.append(sys.argv[1])
	if length >= 2 and (sys.argv[1] == "-g" or sys.argv[1] == "--graph"):
		if length != 3:
			print("Wrong arguments number.\nUsage: ./109titration [-h, --help, -g, --graph] <file>")
			sys.exit(84)
		res[0] = sys.argv[2]
		res.append("graph")
	elif length == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
		my_help()
	elif not path.isfile(res[0]):
		print("%s : non existant file." % res[0])
		sys.exit(84)
	return res

def load_csv_file(file):
	data = []
	try:
		with open(file) as csv_file:
			csv_data = list(csv.reader(csv_file, delimiter=';'))
			try:
				for i in range(len(csv_data)):
					data.append(csv_data[i])
					data[i][0] = float(csv_data[i][0])
					data[i][1] = float(csv_data[i][1])
					if not len(data[i]) == 2:
						raise IndexError
			except (ValueError, IndexError):
				print("Invalid line : %s" % csv_data[i])
				sys.exit(84)
	except (PermissionError, FileNotFoundError) as err:
		print(err)
		sys.exit(84)
	if len(csv_data) <= 4:
		print("Not enough data in file")
		sys.exit(84)
	return data
