##
## EPITECH PROJECT, 2018
## 109titration_2017
## File description:
## utilfs functions
##

from os import path
import csv
import sys

def my_help():
	print("USAGE:\n\t./109titration <file>\n")
	print("DESCRIPTION:\n\t<file.csv>\tCSV file for valies list")
	exit(0)

def check_arguments():
	length = len(sys.argv)
	if length != 2:
		print("Wrong arguments number.\nUsage: ./109titration <file>", file=sys.stderr)
		exit(84)
	elif length == 2 and sys.argv[1] == "-h":
		my_help()
	elif length == 2 and ".csv" not in sys.argv[1]:
		print("Invalid CSV file.\nUsage: ./109titration <file>", file=sys.stderr)
		exit(84)
	else:
		if not path.isfile(sys.argv[1]):
			print("Non existant file.\nUsage: ./109titration <file>", file=sys.stderr)
			exit(84)
