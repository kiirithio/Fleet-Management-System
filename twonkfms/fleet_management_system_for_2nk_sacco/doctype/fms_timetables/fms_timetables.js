// Copyright (c) 2023, George Kiirithio Waweru and contributors
// For license information, please see license.txt

frappe.ui.form.on('FMS TImetables', {
	route_name: function(frm) {
		frappe.call({
			method: 'twonkfms.fleet_management_system_for_2nk_sacco.doctype.fms_timetables.fms_timetables.get_routes',
			args: {
				'route_name': frm.doc.route_name
			},
			callback: function(r) {
				let ra_values=r.message
				frm.set_value('fuel', ra_values[0])
                frm.set_value('fare', ra_values[1])
				frm.set_value('distance', ra_values[2])
			}
		});
	},
	vehicle: function(frm) {
		frappe.call({
			method: 'twonkfms.fleet_management_system_for_2nk_sacco.doctype.fms_timetables.fms_timetables.get_vehicle',
			args: {
				'vehicle': frm.doc.vehicle
			},
			callback: function(r) {
				let ve_value=r.message
				frm.set_value('id_number', ve_value[0])
				frm.set_value('driver', ve_value[1])
			}
		});
	},
	completed: function(frm) {
		frappe.call({
			method: 'twonkfms.fleet_management_system_for_2nk_sacco.doctype.fms_timetables.fms_timetables.get_revenue',
			args: {
				'vehicle': frm.doc.vehicle,
				'fare': frm.doc.fare,
				'fuel': frm.doc.fuel,
				'route_name':frm.doc.route_name
			},
			callback: function(r) {
				let reve_value=r.message
				frm.set_value('revenue', reve_value)
			}
		});
	},
	on_location: function(frm) {
		frappe.call({
			method: 'twonkfms.fleet_management_system_for_2nk_sacco.doctype.fms_timetables.fms_timetables.get_location',
			args: {
				'route_name': frm.doc.route_name
			},
			callback: function(r) {
				let location = r.message
				// for (let i = 0; i < vehicles.length; i++) {
				// 	console.log(vehicles[i]);
				// 	frm.set_value('vehicle', vehicles[i]);
				// }
				frm.set_query("vehicle", function() {
					return {
						"filters": {
							"current_location": location
						}
					};
				});
			}
		});
	}
});
