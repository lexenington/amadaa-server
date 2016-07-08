import sys
import psycopg2

def connection():
	# TODO: grab connection information from configuration file 
	return psycopg2.connect("dbname=lorenzo user=lorenzo")

def table_exists(table, schema='public'):
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
