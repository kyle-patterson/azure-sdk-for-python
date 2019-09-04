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

from .linked_service import LinkedService


class SapBWLinkedService(LinkedService):
    """SAP Business Warehouse Linked Service.

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
    :param server: Required. Host name of the SAP BW instance. Type: string
     (or Expression with resultType string).
    :type server: object
    :param system_number: Required. System number of the BW system. (Usually a
     two-digit decimal number represented as a string.) Type: string (or
     Expression with resultType string).
    :type system_number: object
    :param client_id: Required. Client ID of the client on the BW system.
     (Usually a three-digit decimal number represented as a string) Type:
     string (or Expression with resultType string).
    :type client_id: object
    :param user_name: Username to access the SAP BW server. Type: string (or
     Expression with resultType string).
    :type user_name: object
    :param password: Password to access the SAP BW server.
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'server': {'required': True},
        'system_number': {'required': True},
        'client_id': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'server': {'key': 'typeProperties.server', 'type': 'object'},
        'system_number': {'key': 'typeProperties.systemNumber', 'type': 'object'},
        'client_id': {'key': 'typeProperties.clientId', 'type': 'object'},
        'user_name': {'key': 'typeProperties.userName', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecretBase'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(SapBWLinkedService, self).__init__(**kwargs)
        self.server = kwargs.get('server', None)
        self.system_number = kwargs.get('system_number', None)
        self.client_id = kwargs.get('client_id', None)
        self.user_name = kwargs.get('user_name', None)
        self.password = kwargs.get('password', None)
        self.encrypted_credential = kwargs.get('encrypted_credential', None)
        self.type = 'SapBW'
