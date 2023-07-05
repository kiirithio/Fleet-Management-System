# Copyright (c) 2023, George Kiirithio Waweru and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FMSRoutes(Document):
	pass
@frappe.whitelist()
def get_both(start,destination):
	both=start+' - '+destination
	print(f"\n\n\n {both} \n\n\n")
	return both