from __future__ import absolute_import, division, print_function

from stripe_modern.api_resources.abstract import ListableAPIResource


class OrderReturn(ListableAPIResource):
    OBJECT_NAME = "order_return"
