from __future__ import absolute_import, division, print_function

from stripe_modern import util
from stripe_modern.api_resources.abstract import CreateableAPIResource
from stripe_modern.api_resources.abstract import ListableAPIResource
from stripe_modern.api_resources.abstract import UpdateableAPIResource
from stripe_modern.api_resources.abstract import custom_method


@custom_method("cancel", http_verb="post")
class Topup(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "topup"

    def cancel(self, idempotency_key=None, **params):
        url = self.instance_url() + "/cancel"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
