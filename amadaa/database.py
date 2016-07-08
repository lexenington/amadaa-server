import sys
import psycopg2

def connection():
	# TODO: grab connection information from configuration file 
	return psycopg2.connect("dbname=lorenzo user=lorenzo")
