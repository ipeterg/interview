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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.api_entities_bulk_imports_entity_failure import APIEntitiesBulkImportsEntityFailure
from typing import Optional, Set
from typing_extensions import Self

class APIEntitiesBulkImports(BaseModel):
    """
    API_Entities_BulkImports model
    """ # noqa: E501
    id: Optional[StrictInt] = None
    bulk_import_id: Optional[StrictInt] = None
    status: Optional[StrictStr] = None
    entity_type: Optional[StrictStr] = None
    source_full_path: Optional[StrictStr] = None
    destination_full_path: Optional[StrictStr] = None
    destination_name: Optional[StrictStr] = None
    destination_slug: Optional[StrictStr] = None
    destination_namespace: Optional[StrictStr] = None
    parent_id: Optional[StrictInt] = None
    namespace_id: Optional[StrictInt] = None
    project_id: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    failures: Optional[List[APIEntitiesBulkImportsEntityFailure]] = None
    migrate_projects: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "bulk_import_id", "status", "entity_type", "source_full_path", "destination_full_path", "destination_name", "destination_slug", "destination_namespace", "parent_id", "namespace_id", "project_id", "created_at", "updated_at", "failures", "migrate_projects"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['created', 'started', 'finished', 'timeout', 'failed']):
            raise ValueError("must be one of enum values ('created', 'started', 'finished', 'timeout', 'failed')")
        return value

    @field_validator('entity_type')
    def entity_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['group', 'project']):
            raise ValueError("must be one of enum values ('group', 'project')")
        return value

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
        """Create an instance of APIEntitiesBulkImports from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in failures (list)
        _items = []
        if self.failures:
            for _item in self.failures:
                if _item:
                    _items.append(_item.to_dict())
            _dict['failures'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of APIEntitiesBulkImports from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "bulk_import_id": obj.get("bulk_import_id"),
            "status": obj.get("status"),
            "entity_type": obj.get("entity_type"),
            "source_full_path": obj.get("source_full_path"),
            "destination_full_path": obj.get("destination_full_path"),
            "destination_name": obj.get("destination_name"),
            "destination_slug": obj.get("destination_slug"),
            "destination_namespace": obj.get("destination_namespace"),
            "parent_id": obj.get("parent_id"),
            "namespace_id": obj.get("namespace_id"),
            "project_id": obj.get("project_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "failures": [APIEntitiesBulkImportsEntityFailure.from_dict(_item) for _item in obj["failures"]] if obj.get("failures") is not None else None,
            "migrate_projects": obj.get("migrate_projects")
        })
        return _obj


