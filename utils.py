##
## EPITECH PROJECT, 2018
## 109titration_2017
## File description:
## utilfs functions
##

import csv
import sys

def my_help():
	print("USAGE:\n\t./109titration <file.csv>\n")
	print("DESCRIPTION:\n\t<file.csv>\tCSV file for valies list")
	exit(0)

def check_arguments():
	length = len(sys.argv)
	if length != 2:
		print("Wrong arguments number.\nUsage: ./109titration <file.csv>", file=sys.stderr)
		exit(84)
	elif length == 2 and sys.argv[1] == "-h":
		my_help()
