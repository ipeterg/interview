# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.migrations_api import MigrationsApi


class TestMigrationsApi(unittest.TestCase):
    """MigrationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MigrationsApi()

    def tearDown(self) -> None:
        pass

    def test_post_api_v4_admin_migrations_timestamp_mark(self) -> None:
        """Test case for post_api_v4_admin_migrations_timestamp_mark

        """
        pass


if __name__ == '__main__':
    unittest.main()
