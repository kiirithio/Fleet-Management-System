# Copyright (c) 2023, George Kiirithio Waweru and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FMSTImetables(Document):
	pass
@frappe.whitelist()
def get_routes(route_name):
	route_values = frappe.db.get_value('FMS Routes', route_name, ['fuel', 'fare', 'distance'])
	return route_values

@frappe.whitelist()
def get_vehicle(vehicle):
	vehicle_val = frappe.db.get_value('FMS Vehicles', vehicle, 'assign_driver')
	vehicle_vals = frappe.db.get_value('FMS Driver', vehicle_val, ['name','first_name'])
	return vehicle_vals

@frappe.whitelist()
def get_revenue(vehicle, fare, fuel, route_name):
	veh_capacity = frappe.db.get_value('FMS Vehicles', vehicle, 'passenger_capacity')
	dest = frappe.db.get_value('FMS Routes', route_name, 'destination')
	SQL=f"""
		Update `tabFMS Vehicles` SET current_location='{dest}' WHERE name='{vehicle}'
	"""
	frappe.db.sql(SQL)
	if (veh_capacity == 14):
		final_revenue = (float(fare) * float(veh_capacity)) - float(fuel)
	else :
		fare_eleven = float(fare) * 1.3
		final_revenue = (float(fare_eleven) * float(veh_capacity)) - float(fuel)
	return final_revenue

@frappe.whitelist()
def get_location(route_name):
	location = frappe.db.get_value('FMS Routes', route_name, 'start')
	on_location = frappe.db.get_values('FMS Vehicles', {'current_location' : location}, 'number_plate')
	print(f"\n\n {on_location} \n\n\n")
	return location

