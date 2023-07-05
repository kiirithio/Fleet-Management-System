# Copyright (c) 2023, George Kiirithio Waweru and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns=get_columns()
	data = get_data(filters)

	return columns, data

def get_data(filters):

	conditions= "1=1"

	if(filters.get("vehicle")):conditions += f" AND i.vehicle='{filters.get('vehicle')}'"
	if(filters.get("route_name")):conditions += f" AND i.route_name='{filters.get('route_name')}'"
	if(filters.get("revenue")):conditions += f" AND i.revenue='{filters.get('revenue')}'"
	if(filters.get("departure_date")):conditions += f" AND i.departure_date='{filters.get('departure_date')}'"

	SQL = f"""
		SELECT 
			i.vehicle,
			i.route_name,
			i.revenue,
			i.departure_date
		FROM 
			`tabFMS TImetables` as i
		WHERE 
			{conditions}
	"""
	
	data=frappe.db.sql(SQL)
	return data

def get_columns():
	return [
		"Vehicle:Link/FMS Vehicles:200",
		"Route Name:Link/FMS Routes:200",
		"Revenue:Data/FMS TImetables:100",
		"Departure Date:Date/FMS TImetables:200"
	]


