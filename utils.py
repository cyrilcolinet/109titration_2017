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
	print("USAGE:\n\t./109titration <file>\n")
	print("DESCRIPTION:\n\tfile\tCa csv file containing \"vol;ph\" lines")
	print("\t-h\tDisplay this help file")
	sys.exit(0)

def check_arguments():
	length = len(sys.argv)
	if length != 2:
		print("Wrong arguments number.\nUsage: ./109titration <file>", file=sys.stderr)
		sys.exit(84)
	elif length == 2 and sys.argv[1] == "-h":
		my_help()
	elif length == 2 and ".csv" not in sys.argv[1]:
		print("Invalid CSV file.\nUsage: ./109titration <file>", file=sys.stderr)
		sys.exit(84)
	elif not path.isfile(sys.argv[1]):
		print("Non existant file.", file=sys.stderr)
		sys.exit(84)

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
				print("Invalid line : %s" % csv_data[i], file=sys.stderr)
				sys.exit(84)
	except (PermissionError, FileNotFoundError) as err:
		print(err, file=sys.stderr)
		sys.exit(84)
	if len(csv_data) <= 4:
		print("Not enough data in file", file=sys.stderr)
		sys.exit(84)
	return data
