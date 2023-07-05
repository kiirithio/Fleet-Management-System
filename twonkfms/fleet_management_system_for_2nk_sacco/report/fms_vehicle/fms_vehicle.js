// Copyright (c) 2023, George Kiirithio Waweru and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["FMS Vehicle"] = {
	"filters": [
		{
			"fieldname": "vehicle",
			"label":__("Vehicle"),
			"fieldtype":"Link",
			"options":"FMS Vehicles",
			"width":100,
			"reqd":0

		},
		{
			"fieldname": "route_name",
			"label":__("Route Name"),
			"fieldtype":"Link",
			"options":"FMS Routes",
			"width":100,
			"reqd":0

		},
		{
			"fieldname": "departure_date",
			"label":__("Departure Date"),
			"fieldtype":"Date",
			"options":"FMS TImetables",
			"width":100,
			"reqd":0

		}
	]
};
