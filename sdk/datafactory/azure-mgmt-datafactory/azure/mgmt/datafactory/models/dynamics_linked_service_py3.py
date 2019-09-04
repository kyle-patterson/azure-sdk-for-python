# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .linked_service_py3 import LinkedService


class DynamicsLinkedService(LinkedService):
    """Dynamics linked service.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     linked service.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param deployment_type: Required. The deployment type of the Dynamics
     instance. 'Online' for Dynamics Online and 'OnPremisesWithIfd' for
     Dynamics on-premises with Ifd. Type: string (or Expression with resultType
     string).
    :type deployment_type: object
    :param host_name: The host name of the on-premises Dynamics server. The
     property is required for on-prem and not allowed for online. Type: string
     (or Expression with resultType string).
    :type host_name: object
    :param port: The port of on-premises Dynamics server. The property is
     required for on-prem and not allowed for online. Default is 443. Type:
     integer (or Expression with resultType integer), minimum: 0.
    :type port: object
    :param service_uri: The URL to the Microsoft Dynamics server. The property
     is required for on-line and not allowed for on-prem. Type: string (or
     Expression with resultType string).
    :type service_uri: object
    :param organization_name: The organization name of the Dynamics instance.
     The property is required for on-prem and required for online when there
     are more than one Dynamics instances associated with the user. Type:
     string (or Expression with resultType string).
    :type organization_name: object
    :param authentication_type: Required. The authentication type to connect
     to Dynamics server. 'Office365' for online scenario, 'Ifd' for on-premises
     with Ifd scenario. Type: string (or Expression with resultType string).
    :type authentication_type: object
    :param username: Required. User name to access the Dynamics instance.
     Type: string (or Expression with resultType string).
    :type username: object
    :param password: Password to access the Dynamics instance.
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'deployment_type': {'required': True},
        'authentication_type': {'required': True},
        'username': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'deployment_type': {'key': 'typeProperties.deploymentType', 'type': 'object'},
        'host_name': {'key': 'typeProperties.hostName', 'type': 'object'},
        'port': {'key': 'typeProperties.port', 'type': 'object'},
        'service_uri': {'key': 'typeProperties.serviceUri', 'type': 'object'},
        'organization_name': {'key': 'typeProperties.organizationName', 'type': 'object'},
        'authentication_type': {'key': 'typeProperties.authenticationType', 'type': 'object'},
        'username': {'key': 'typeProperties.username', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecretBase'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, *, deployment_type, authentication_type, username, additional_properties=None, connect_via=None, description: str=None, parameters=None, annotations=None, host_name=None, port=None, service_uri=None, organization_name=None, password=None, encrypted_credential=None, **kwargs) -> None:
        super(DynamicsLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description, parameters=parameters, annotations=annotations, **kwargs)
        self.deployment_type = deployment_type
        self.host_name = host_name
        self.port = port
        self.service_uri = service_uri
        self.organization_name = organization_name
        self.authentication_type = authentication_type
        self.username = username
        self.password = password
        self.encrypted_credential = encrypted_credential
        self.type = 'Dynamics'
