# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "aristo"
app_title = "Aristo"
app_publisher = "sujay"
app_description = "Aristo"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sujay.j@promantia.com"
app_license = "MIT"

fixtures = ["Workflow","Workflow State","Print Format","Notification","Workflow Action Master","Report",
	{"dt": "Custom Field",
		"filters": [
         [
             "name", "in", ["Purchase Order-registration_type",
"Purchase Order-mode_of_transport",
"Purchase Order-supplier_gstin",
"Purchase Order-place_of_supply",
"Purchase Order-company_gstin",
"Purchase Order-remarks",
"Purchase Order-authorised_signatory",
"Sales Order-remarks",
"Sales Invoice-authorised_signatory",
"Sales Invoice-remarks",
"Address-cin_no",
"Purchase Receipt-authorised_signatory",
"Purchase Receipt-mode_of_transport",
"Delivery Note-authorised_signatory",
  		]
	]
]},
{"dt": "Notification", 
		"filters": [
			"is_standard != 1"
]}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/aristo/css/aristo.css"
# app_include_js = "/assets/aristo/js/aristo.js"

# include js, css files in header of web template
# web_include_css = "/assets/aristo/css/aristo.css"
# web_include_js = "/assets/aristo/js/aristo.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "aristo.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "aristo.install.before_install"
# after_install = "aristo.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "aristo.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"aristo.tasks.all"
# 	],
# 	"daily": [
# 		"aristo.tasks.daily"
# 	],
# 	"hourly": [
# 		"aristo.tasks.hourly"
# 	],
# 	"weekly": [
# 		"aristo.tasks.weekly"
# 	]
# 	"monthly": [
# 		"aristo.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "aristo.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "aristo.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "aristo.task.get_dashboard_data"
# }
