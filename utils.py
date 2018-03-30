##
## EPITECH PROJECT, 2018
## 109titration_2017
## File description:
## utilfs functions
##

from numpy import *
import csv
import sys

def my_help():
	print("USAGE:")
	print("\t./109titration [-h, --help] <file>\n")
	print("DESCRIPTION:")
	print("\t-h, --help\tDisplay this help page")
	print("\tfile\t\tA csv file containing \"vol;ph\" lines")
	sys.exit(0)

def check_arguments():
	length = len(sys.argv)
	if length != 2:
		print("Wrong arguments number.")
		print("Usage: ./109titration [-h, --help] <file>")
		sys.exit(84)
	elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
		my_help()

def load_csv_file():
	data = []
	try:
		with open(sys.argv[1]) as csv_file:
			csv_data = list(csv.reader(csv_file, delimiter=';'))
			try:
				for i in range(len(csv_data)):
					data.append(csv_data[i])
					data[i][0] = float(csv_data[i][0])
					data[i][1] = float(csv_data[i][1])
					if not len(data[i]) == 2:
						raise IndexError
			except (ValueError, IndexError):
				print("%s : invalid file" % sys.argv[1])
				sys.exit(84)
	except (FileNotFoundError) as err:
		print(err)
		sys.exit(84)
	if len(data) <= 4:
		print("Not enough data in file")
		sys.exit(84)
	return data
