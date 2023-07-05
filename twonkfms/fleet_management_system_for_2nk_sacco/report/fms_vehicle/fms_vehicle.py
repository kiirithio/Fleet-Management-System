# Copyright (c) 2023, George Kiirithio Waweru and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns=get_columns()
	data = get_data(filters)

	return columns, data

def get_data(filters):

	conditions= "1=1"

	if(filters.get("vehicle")):conditions += f" AND vehicle='{filters.get('vehicle')}'"
	if(filters.get("revenue")):conditions += f" AND revenue='{filters.get('revenue')}'"

	SQL = f"""
		SELECT vehicle, SUM(revenue) FROM `tabFMS TImetables` GROUP BY vehicle
		WHERE 'vehicle' = 'kdk200m'
	"""
	
	data=frappe.db.sql(SQL)
	return data

def get_columns():
	return [
		"Vehicle:Link/FMS Vehicles:200",
		"Revenue:Data/FMS TImetables:200"
	]
