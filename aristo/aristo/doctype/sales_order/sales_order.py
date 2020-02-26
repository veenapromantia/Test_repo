# -*- coding: utf-8 -*-
# Copyright (c) 2019, sujay and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _, msgprint, throw
from frappe import _
from six import string_types
from frappe.utils import cstr, flt, getdate, cint, nowdate, add_days, get_link_to_form
from aristo.aristo.doctype.customer.customer import check_credit_limits

class SalesOrder(Document):
	pass


def hello(self,doc,handle=""):
	if not cint(frappe.db.get_value("Customer Credit Limit",
			{'parent': self.customer, 'parenttype': 'Customer', 'company': self.company},
			"bypass_credit_limit_check")):
		check_credit_limits(self.customer, self.company)

		


