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

from .resource import Resource


class ServerEndpoint(Resource):
    """Server Endpoint object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The id of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource
    :vartype type: str
    :param server_local_path: Server Local path.
    :type server_local_path: str
    :param cloud_tiering: Cloud Tiering. Possible values include: 'on', 'off'
    :type cloud_tiering: str or ~azure.mgmt.storagesync.models.enum
    :param volume_free_space_percent: Level of free space to be maintained by
     Cloud Tiering if it is enabled.
    :type volume_free_space_percent: int
    :param friendly_name: Friendly Name
    :type friendly_name: str
    :param server_resource_id: Server Resource Id.
    :type server_resource_id: str
    :param provisioning_state: ServerEndpoint Provisioning State
    :type provisioning_state: str
    :param last_workflow_id: ServerEndpoint lastWorkflowId
    :type last_workflow_id: str
    :param last_operation_name: Resource Last Operation Name
    :type last_operation_name: str
    :param sync_status: Sync Health Status
    :type sync_status: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'volume_free_space_percent': {'maximum': 100, 'minimum': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'server_local_path': {'key': 'properties.serverLocalPath', 'type': 'str'},
        'cloud_tiering': {'key': 'properties.cloudTiering', 'type': 'str'},
        'volume_free_space_percent': {'key': 'properties.volumeFreeSpacePercent', 'type': 'int'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'server_resource_id': {'key': 'properties.serverResourceId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'last_workflow_id': {'key': 'properties.lastWorkflowId', 'type': 'str'},
        'last_operation_name': {'key': 'properties.lastOperationName', 'type': 'str'},
        'sync_status': {'key': 'properties.syncStatus', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(ServerEndpoint, self).__init__(**kwargs)
        self.server_local_path = kwargs.get('server_local_path', None)
        self.cloud_tiering = kwargs.get('cloud_tiering', None)
        self.volume_free_space_percent = kwargs.get('volume_free_space_percent', None)
        self.friendly_name = kwargs.get('friendly_name', None)
        self.server_resource_id = kwargs.get('server_resource_id', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.last_workflow_id = kwargs.get('last_workflow_id', None)
        self.last_operation_name = kwargs.get('last_operation_name', None)
        self.sync_status = kwargs.get('sync_status', None)