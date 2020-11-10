from __future__ import absolute_import, division, print_function

from stripe_modern.api_resources.abstract import APIResource


class Mandate(APIResource):
    OBJECT_NAME = "mandate"
