# Copyright (c) 2025, IT Gembira and contributors
# For license information, please see license.txt

# # import frappe
# from frappe.model.document import Document

# class CompanyPlan(Document):
# 	pass

import frappe
from frappe.model.document import Document

class CompanyPlan(Document):
    def validate(self):
        self.update_progress()
    
    def before_save(self):
        self.update_progress()

    def update_progress(self):
        if not self.task:
            self.progress = 0
            return

        total = len(self.task)
        progress_sum = sum([t.progress or 0 for t in self.task])
        self.progress = progress_sum / total if total else 0
