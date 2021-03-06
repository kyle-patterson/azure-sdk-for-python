# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ErrorResponse(msrest.serialization.Model):
    """Describes the format of Error response.

    :param code: Error code.
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class LogSettings(msrest.serialization.Model):
    """Part of MultiTenantDiagnosticSettings. Specifies the settings for a particular log.

    All required parameters must be populated in order to send to Azure.

    :param category: Name of a Diagnostic Log category for a resource type this setting is applied
     to. To obtain the list of Diagnostic Log categories for a resource, first perform a GET
     diagnostic settings operation.
    :type category: str
    :param enabled: Required. a value indicating whether this log is enabled.
    :type enabled: bool
    :param retention_policy: the retention policy for this log.
    :type retention_policy: ~$(python-base-namespace).v2015_07_01.models.RetentionPolicy
    """

    _validation = {
        'enabled': {'required': True},
    }

    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(
        self,
        *,
        enabled: bool,
        category: Optional[str] = None,
        retention_policy: Optional["RetentionPolicy"] = None,
        **kwargs
    ):
        super(LogSettings, self).__init__(**kwargs)
        self.category = category
        self.enabled = enabled
        self.retention_policy = retention_policy


class MetricSettings(msrest.serialization.Model):
    """Part of MultiTenantDiagnosticSettings. Specifies the settings for a particular metric.

    All required parameters must be populated in order to send to Azure.

    :param time_grain: Required. the timegrain of the metric in ISO8601 format.
    :type time_grain: ~datetime.timedelta
    :param enabled: Required. a value indicating whether this timegrain is enabled.
    :type enabled: bool
    :param retention_policy: the retention policy for this timegrain.
    :type retention_policy: ~$(python-base-namespace).v2015_07_01.models.RetentionPolicy
    """

    _validation = {
        'time_grain': {'required': True},
        'enabled': {'required': True},
    }

    _attribute_map = {
        'time_grain': {'key': 'timeGrain', 'type': 'duration'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(
        self,
        *,
        time_grain: datetime.timedelta,
        enabled: bool,
        retention_policy: Optional["RetentionPolicy"] = None,
        **kwargs
    ):
        super(MetricSettings, self).__init__(**kwargs)
        self.time_grain = time_grain
        self.enabled = enabled
        self.retention_policy = retention_policy


class Resource(msrest.serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class RetentionPolicy(msrest.serialization.Model):
    """Specifies the retention policy for the log.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. a value indicating whether the retention policy is enabled.
    :type enabled: bool
    :param days: Required. the number of days for the retention in days. A value of 0 will retain
     the events indefinitely.
    :type days: int
    """

    _validation = {
        'enabled': {'required': True},
        'days': {'required': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'days': {'key': 'days', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        enabled: bool,
        days: int,
        **kwargs
    ):
        super(RetentionPolicy, self).__init__(**kwargs)
        self.enabled = enabled
        self.days = days


class ServiceDiagnosticSettingsResource(Resource):
    """Description of a service diagnostic setting.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param storage_account_id: The resource ID of the storage account to which you would like to
     send Diagnostic Logs.
    :type storage_account_id: str
    :param service_bus_rule_id: The service bus rule ID of the service bus namespace in which you
     would like to have Event Hubs created for streaming Diagnostic Logs. The rule ID is of the
     format: '{service bus resource ID}/authorizationrules/{key name}'.
    :type service_bus_rule_id: str
    :param metrics: the list of metric settings.
    :type metrics: list[~$(python-base-namespace).v2015_07_01.models.MetricSettings]
    :param logs: the list of logs settings.
    :type logs: list[~$(python-base-namespace).v2015_07_01.models.LogSettings]
    :param workspace_id: The workspace ID (resource ID of a Log Analytics workspace) for a Log
     Analytics workspace to which you would like to send Diagnostic Logs. Example:
     /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-
     integration/providers/Microsoft.OperationalInsights/workspaces/viruela2.
    :type workspace_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'storage_account_id': {'key': 'properties.storageAccountId', 'type': 'str'},
        'service_bus_rule_id': {'key': 'properties.serviceBusRuleId', 'type': 'str'},
        'metrics': {'key': 'properties.metrics', 'type': '[MetricSettings]'},
        'logs': {'key': 'properties.logs', 'type': '[LogSettings]'},
        'workspace_id': {'key': 'properties.workspaceId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        storage_account_id: Optional[str] = None,
        service_bus_rule_id: Optional[str] = None,
        metrics: Optional[List["MetricSettings"]] = None,
        logs: Optional[List["LogSettings"]] = None,
        workspace_id: Optional[str] = None,
        **kwargs
    ):
        super(ServiceDiagnosticSettingsResource, self).__init__(location=location, tags=tags, **kwargs)
        self.storage_account_id = storage_account_id
        self.service_bus_rule_id = service_bus_rule_id
        self.metrics = metrics
        self.logs = logs
        self.workspace_id = workspace_id
