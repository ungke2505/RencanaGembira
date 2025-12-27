# Copyright (c) 2025, IT Gembira and contributors
# For license information, please see license.txt

# # import frappe
# from frappe.model.document import Document

# class CompanyPlanTask(Document):
# 	pass


import frappe
from frappe.model.document import Document

class CompanyPlanTask(Document):
    def validate(self):
        self.update_progress()

    def before_save(self):
        self.update_progress()

    def update_progress(self):
        # hitung checklist
        total = len(self.checklist)
        if total == 0:
            self.percent = 0
            self.status = "Not Started"
            return

        completed = len([c for c in self.checklist if c.is_completed])
        self.percent = round((completed / total) * 100, 2)

        # update status otomatis
        if self.percent == 0:
            self.status = "Not Started"
        elif self.percent == 100:
            self.status = "Completed"
        else:
            self.status = "In Progress"
