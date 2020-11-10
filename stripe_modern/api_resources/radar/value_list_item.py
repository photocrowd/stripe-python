from __future__ import absolute_import, division, print_function

from stripe_modern.api_resources.abstract import CreateableAPIResource
from stripe_modern.api_resources.abstract import DeletableAPIResource
from stripe_modern.api_resources.abstract import ListableAPIResource


class ValueListItem(
    CreateableAPIResource, DeletableAPIResource, ListableAPIResource
):
    OBJECT_NAME = "radar.value_list_item"
