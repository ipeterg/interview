# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.put_api_v4_application_plan_limits_request import PutApiV4ApplicationPlanLimitsRequest

class TestPutApiV4ApplicationPlanLimitsRequest(unittest.TestCase):
    """PutApiV4ApplicationPlanLimitsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PutApiV4ApplicationPlanLimitsRequest:
        """Test PutApiV4ApplicationPlanLimitsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PutApiV4ApplicationPlanLimitsRequest`
        """
        model = PutApiV4ApplicationPlanLimitsRequest()
        if include_optional:
            return PutApiV4ApplicationPlanLimitsRequest(
                plan_name = 'default',
                ci_pipeline_size = 56,
                ci_active_jobs = 56,
                ci_project_subscriptions = 56,
                ci_pipeline_schedules = 56,
                ci_needs_size_limit = 56,
                ci_registered_group_runners = 56,
                ci_registered_project_runners = 56,
                conan_max_file_size = 56,
                enforcement_limit = 56,
                generic_packages_max_file_size = 56,
                helm_max_file_size = 56,
                maven_max_file_size = 56,
                notification_limit = 56,
                npm_max_file_size = 56,
                nuget_max_file_size = 56,
                pypi_max_file_size = 56,
                terraform_module_max_file_size = 56,
                storage_size_limit = 56,
                pipeline_hierarchy_size = 56
            )
        else:
            return PutApiV4ApplicationPlanLimitsRequest(
                plan_name = 'default',
        )
        """

    def testPutApiV4ApplicationPlanLimitsRequest(self):
        """Test PutApiV4ApplicationPlanLimitsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
