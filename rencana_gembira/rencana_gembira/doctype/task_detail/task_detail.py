import frappe
from frappe.model.document import Document

class TaskDetail(Document):
    def validate(self):
        self.update_progress_and_status()

    def update_progress_and_status(self):
        if not self.checklist:
            self.progress = 0
            self.status = "Not Started"
            return

        total = len(self.checklist)
        done = len([c for c in self.checklist if c.is_completed])

        self.progress = (done / total) * 100 if total else 0

        if done == 0:
            self.status = "Not Started"
        elif done < total:
            self.status = "In Progress"
        else:
            self.status = "Completed"

    def on_update(self):
        # Sync ke Company Plan Task (child)
        company_tasks = frappe.get_all(
            "Company Plan Task",
            filters={"task_detail": self.name},
            fields=["name", "parent"]
        )
        for t in company_tasks:
            frappe.db.set_value("Company Plan Task", t.name, {
                "status": self.status,
                "progress": self.progress
            })
            # Update Company Plan parent progress
            frappe.get_doc("Company Plan", t.parent).update_progress()
