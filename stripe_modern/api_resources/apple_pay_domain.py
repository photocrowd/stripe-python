from __future__ import absolute_import, division, print_function

from stripe_modern.api_resources.abstract import CreateableAPIResource
from stripe_modern.api_resources.abstract import DeletableAPIResource
from stripe_modern.api_resources.abstract import ListableAPIResource


class ApplePayDomain(
    CreateableAPIResource, DeletableAPIResource, ListableAPIResource
):
    OBJECT_NAME = "apple_pay_domain"

    @classmethod
    def class_url(cls):
        return "/v1/apple_pay/domains"
