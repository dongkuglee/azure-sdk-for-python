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

from msrest.serialization import Model


class ConnectionSettingProperties(Model):
    """Properties for a Connection Setting Item.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param client_id: Client Id associated with the Connection Setting.
    :type client_id: str
    :ivar setting_id: Setting Id set by the service for the Connection
     Setting.
    :vartype setting_id: str
    :param client_secret: Client Secret associated with the Connection Setting
    :type client_secret: str
    :param scopes: Scopes associated with the Connection Setting
    :type scopes: str
    :param service_provider_id: Service Provider Id associated with the
     Connection Setting
    :type service_provider_id: str
    :param service_provider_display_name: Service Provider Display Name
     associated with the Connection Setting
    :type service_provider_display_name: str
    :param parameters: Service Provider Parameters associated with the
     Connection Setting
    :type parameters:
     list[~azure.mgmt.botservice.models.ConnectionSettingParameter]
    """

    _validation = {
        'setting_id': {'readonly': True},
    }

    _attribute_map = {
        'client_id': {'key': 'clientId', 'type': 'str'},
        'setting_id': {'key': 'settingId', 'type': 'str'},
        'client_secret': {'key': 'clientSecret', 'type': 'str'},
        'scopes': {'key': 'scopes', 'type': 'str'},
        'service_provider_id': {'key': 'serviceProviderId', 'type': 'str'},
        'service_provider_display_name': {'key': 'serviceProviderDisplayName', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[ConnectionSettingParameter]'},
    }

    def __init__(self, *, client_id: str=None, client_secret: str=None, scopes: str=None, service_provider_id: str=None, service_provider_display_name: str=None, parameters=None, **kwargs) -> None:
        super(ConnectionSettingProperties, self).__init__(**kwargs)
        self.client_id = client_id
        self.setting_id = None
        self.client_secret = client_secret
        self.scopes = scopes
        self.service_provider_id = service_provider_id
        self.service_provider_display_name = service_provider_display_name
        self.parameters = parameters
