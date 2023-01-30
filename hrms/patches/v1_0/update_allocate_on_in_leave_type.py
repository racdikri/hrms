import frappe


def execute():
	if frappe.db.has_column("Leave Type", "based_on_date_of_joining"):
		LeaveType = frappe.qb.DocType("Leave Type")
		frappe.qb.update(LeaveType).set(LeaveType.allocate_on, "Last Day").where(
			(LeaveType.based_on_date_of_joining == 0) & (LeaveType.is_earned_leave == 1)
		).run()

		frappe.qb.update(LeaveType).set(LeaveType.allocate_on, "Date of Joining").where(
			LeaveType.based_on_date_of_joining == 1
		).run()

		frappe.db.sql_ddl("alter table `tabLeave Type` drop column `based_on_date_of_joining`")
