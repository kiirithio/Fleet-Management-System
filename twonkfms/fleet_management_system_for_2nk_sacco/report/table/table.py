# Copyright (c) 2023, George Kiirithio Waweru and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns=get_columns()
	data = get_data(filters)
	return columns, data

def get_data(filters):
	conditions= "1=1"

	if(filters.get("vehicle")):conditions += f"AND vehicle='{filters.get('vehicle')}'"
	if(filters.get("route_name")):conditions += f"AND route_name='{filters.get('route_name')}'"
	if(filters.get("revenue")):conditions += f"AND revenue='{filters.get('revenue')}'"

	SQL=f"""
		SELECT 
			vehicle,
			route_name,
			revenue
		FROM 
			`tabFMS TImetables` 
		WHERE 
			{conditions}
	"""
	# datass=frappe.db.get_value('FMS TImetables', {'route_name':'Nairobi - Nyeri'}, ['vehicle', 'route_name', 'revenue'])
	data=frappe.db.sql(SQL)
	return data

def get_columns():
	return [
		"Vehicle:Link/FMS Vehicles:200",
		"Route Name:Link/FMS Routes:200",
		"Revenue:Data/FMS TImetables:200"
	]