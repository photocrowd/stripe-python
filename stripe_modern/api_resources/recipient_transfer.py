from __future__ import absolute_import, division, print_function

from stripe_modern.stripe_object import StripeObject


# This resource can only be instantiated when expanded on a BalanceTransaction
class RecipientTransfer(StripeObject):
    OBJECT_NAME = "recipient_transfer"
