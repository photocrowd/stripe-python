from __future__ import absolute_import, division, print_function

from stripe_modern.stripe_object import StripeObject


class InvoiceLineItem(StripeObject):
    OBJECT_NAME = "line_item"
