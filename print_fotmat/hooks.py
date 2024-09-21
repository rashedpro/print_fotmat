app_name = "print_fotmat"
app_title = "Print Fotmat"
app_publisher = "pro"
app_description = "this for print fromat"
app_email = "pro@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------


jinja = {
    "methods": [
	"print_fotmat.fatoora.getqrcode",
	# "print_fotmat.test.test",
	"print_fotmat.data.money_in_words",
	"print_fotmat.utils.print_format.encrypt"

    ]
}

# include js, css files in header of desk.html
# app_include_css = "/assets/print_fotmat/css/print_fotmat.css"
# app_include_js = "/assets/print_fotmat/js/print_fotmat.js"

# include js, css files in header of web template
# web_include_css = "/assets/print_fotmat/css/print_fotmat.css"
# web_include_js = "/assets/print_fotmat/js/print_fotmat.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "print_fotmat/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "print_fotmat.utils.jinja_methods",
# 	"filters": "print_fotmat.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "print_fotmat.install.before_install"
# after_install = "print_fotmat.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "print_fotmat.uninstall.before_uninstall"
# after_uninstall = "print_fotmat.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "print_fotmat.utils.before_app_install"
# after_app_install = "print_fotmat.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "print_fotmat.utils.before_app_uninstall"
# after_app_uninstall = "print_fotmat.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "print_fotmat.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"print_fotmat.tasks.all"
# 	],
# 	"daily": [
# 		"print_fotmat.tasks.daily"
# 	],
# 	"hourly": [
# 		"print_fotmat.tasks.hourly"
# 	],
# 	"weekly": [
# 		"print_fotmat.tasks.weekly"
# 	],
# 	"monthly": [
# 		"print_fotmat.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "print_fotmat.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "print_fotmat.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "print_fotmat.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["print_fotmat.utils.before_request"]
# after_request = ["print_fotmat.utils.after_request"]

# Job Events
# ----------
# before_job = ["print_fotmat.utils.before_job"]
# after_job = ["print_fotmat.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"print_fotmat.auth.validate"
# ]
