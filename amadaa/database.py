""" Collection of database functions. Not much here at the moment (and perhaps
it will stay that way. """

import sys
import psycopg2

def connection():
	""" Get a database connection. """
	# TODO: grab connection information from configuration file
	return psycopg2.connect("dbname=lorenzo user=lorenzo")

def table_exists(table, schema='public'):
	""" Check if a table exists, optionally within a particular schema. Return
	True or False. """
	conn = connection()
	with conn:
		with conn.cursor() as cur:
			sql = """select exists(
				select 1 from information_schema.tables
				where table_schema = %s and table_name = %s)"""
			cur.execute(sql, (schema, table,))
			ret = cur.fetchone()[0]
	conn.close()
	return ret
