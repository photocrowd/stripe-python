from __future__ import absolute_import, division, print_function

from stripe_modern.api_resources.abstract import CreateableAPIResource


class Session(CreateableAPIResource):
    OBJECT_NAME = "billing_portal.session"
