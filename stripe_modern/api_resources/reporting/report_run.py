from __future__ import absolute_import, division, print_function

from stripe_modern.api_resources.abstract import CreateableAPIResource
from stripe_modern.api_resources.abstract import ListableAPIResource


class ReportRun(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "reporting.report_run"
