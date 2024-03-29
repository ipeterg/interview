# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PutApiV4AdminClustersClusterIdRequest(BaseModel):
    """
    PutApiV4AdminClustersClusterIdRequest
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Cluster name")
    enabled: Optional[StrictBool] = Field(default=None, description="Enable or disable Gitlab's connection to your Kubernetes cluster")
    environment_scope: Optional[StrictStr] = Field(default=None, description="The associated environment to the cluster")
    namespace_per_environment: Optional[StrictBool] = Field(default=True, description="Deploy each environment to a separate Kubernetes namespace")
    domain: Optional[StrictStr] = Field(default=None, description="Cluster base domain")
    management_project_id: Optional[StrictInt] = Field(default=None, description="The ID of the management project")
    managed: Optional[StrictBool] = Field(default=None, description="Determines if GitLab will manage namespaces and service accounts for this cluster")
    platform_kubernetes_attributes_api_url: Optional[StrictStr] = Field(default=None, description="URL to access the Kubernetes API", alias="platform_kubernetes_attributes[api_url]")
    platform_kubernetes_attributes_token: Optional[StrictStr] = Field(default=None, description="Token to authenticate against Kubernetes", alias="platform_kubernetes_attributes[token]")
    platform_kubernetes_attributes_ca_cert: Optional[StrictStr] = Field(default=None, description="TLS certificate (needed if API is using a self-signed TLS certificate)", alias="platform_kubernetes_attributes[ca_cert]")
    platform_kubernetes_attributes_namespace: Optional[StrictStr] = Field(default=None, description="Unique namespace related to Project", alias="platform_kubernetes_attributes[namespace]")
    __properties: ClassVar[List[str]] = ["name", "enabled", "environment_scope", "namespace_per_environment", "domain", "management_project_id", "managed", "platform_kubernetes_attributes[api_url]", "platform_kubernetes_attributes[token]", "platform_kubernetes_attributes[ca_cert]", "platform_kubernetes_attributes[namespace]"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PutApiV4AdminClustersClusterIdRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PutApiV4AdminClustersClusterIdRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "enabled": obj.get("enabled"),
            "environment_scope": obj.get("environment_scope"),
            "namespace_per_environment": obj.get("namespace_per_environment") if obj.get("namespace_per_environment") is not None else True,
            "domain": obj.get("domain"),
            "management_project_id": obj.get("management_project_id"),
            "managed": obj.get("managed"),
            "platform_kubernetes_attributes[api_url]": obj.get("platform_kubernetes_attributes[api_url]"),
            "platform_kubernetes_attributes[token]": obj.get("platform_kubernetes_attributes[token]"),
            "platform_kubernetes_attributes[ca_cert]": obj.get("platform_kubernetes_attributes[ca_cert]"),
            "platform_kubernetes_attributes[namespace]": obj.get("platform_kubernetes_attributes[namespace]")
        })
        return _obj


