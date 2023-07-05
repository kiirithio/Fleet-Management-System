// Copyright (c) 2023, George Kiirithio Waweru and contributors
// For license information, please see license.txt

frappe.ui.form.on('FMS Routes', {
	refresh: function(frm) {
		console.log("hello bthere")
	},
	get_details: function(frm) {
		frappe.call({
			method: 'twonkfms.fleet_management_system_for_2nk_sacco.doctype.fms_routes.fms_routes.get_both',
			args: {
				'start': frm.doc.start,
				'destination':frm.doc.destination
			},
			callback: function(r) {
				let na=r.message
				frm.set_value('route_name', na)
			}
		});
	}
});
