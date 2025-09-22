frappe.ui.form.on("Task Checklist", {
    is_completed: function(frm, cdt, cdn) {
        // refresh progress di parent task
        frm.refresh_field("checklist");
        frm.save();
    }
});
