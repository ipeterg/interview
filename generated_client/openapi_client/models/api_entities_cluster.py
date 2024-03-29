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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.api_entities_platform_kubernetes import APIEntitiesPlatformKubernetes
from openapi_client.models.api_entities_project_identity import APIEntitiesProjectIdentity
from openapi_client.models.api_entities_provider_gcp import APIEntitiesProviderGcp
from openapi_client.models.api_entities_user_basic import APIEntitiesUserBasic
from typing import Optional, Set
from typing_extensions import Self

class APIEntitiesCluster(BaseModel):
    """
    API_Entities_Cluster model
    """ # noqa: E501
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    domain: Optional[StrictStr] = None
    enabled: Optional[StrictStr] = None
    managed: Optional[StrictStr] = None
    provider_type: Optional[StrictStr] = None
    platform_type: Optional[StrictStr] = None
    environment_scope: Optional[StrictStr] = None
    cluster_type: Optional[StrictStr] = None
    namespace_per_environment: Optional[StrictStr] = None
    user: Optional[APIEntitiesUserBasic] = None
    platform_kubernetes: Optional[APIEntitiesPlatformKubernetes] = None
    provider_gcp: Optional[APIEntitiesProviderGcp] = None
    management_project: Optional[APIEntitiesProjectIdentity] = None
    __properties: ClassVar[List[str]] = ["id", "name", "created_at", "domain", "enabled", "managed", "provider_type", "platform_type", "environment_scope", "cluster_type", "namespace_per_environment", "user", "platform_kubernetes", "provider_gcp", "management_project"]

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
        """Create an instance of APIEntitiesCluster from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of platform_kubernetes
        if self.platform_kubernetes:
            _dict['platform_kubernetes'] = self.platform_kubernetes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of provider_gcp
        if self.provider_gcp:
            _dict['provider_gcp'] = self.provider_gcp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of management_project
        if self.management_project:
            _dict['management_project'] = self.management_project.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of APIEntitiesCluster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "created_at": obj.get("created_at"),
            "domain": obj.get("domain"),
            "enabled": obj.get("enabled"),
            "managed": obj.get("managed"),
            "provider_type": obj.get("provider_type"),
            "platform_type": obj.get("platform_type"),
            "environment_scope": obj.get("environment_scope"),
            "cluster_type": obj.get("cluster_type"),
            "namespace_per_environment": obj.get("namespace_per_environment"),
            "user": APIEntitiesUserBasic.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "platform_kubernetes": APIEntitiesPlatformKubernetes.from_dict(obj["platform_kubernetes"]) if obj.get("platform_kubernetes") is not None else None,
            "provider_gcp": APIEntitiesProviderGcp.from_dict(obj["provider_gcp"]) if obj.get("provider_gcp") is not None else None,
            "management_project": APIEntitiesProjectIdentity.from_dict(obj["management_project"]) if obj.get("management_project") is not None else None
        })
        return _obj


