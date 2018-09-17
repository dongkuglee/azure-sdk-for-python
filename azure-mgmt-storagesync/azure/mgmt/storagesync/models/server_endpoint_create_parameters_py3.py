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


class ServerEndpointCreateParameters(Model):
    """The parameters used when creating a storage sync service.

    :param location: Required. Gets or sets the location of the resource. This
     will be one of the supported and registered Azure Geo Regions (e.g. West
     US, East US, Southeast Asia, etc.). The geo region of a resource cannot be
     changed once it is created, but if an identical geo region is specified on
     update, the request will succeed.
    :type location: str
    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used for viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key with a length no greater than 128
     characters and a value with a length no greater than 256 characters.
    :type tags: dict[str, str]
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
    """

    _validation = {
        'volume_free_space_percent': {'maximum': 100, 'minimum': 0},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'server_local_path': {'key': 'properties.serverLocalPath', 'type': 'str'},
        'cloud_tiering': {'key': 'properties.cloudTiering', 'type': 'str'},
        'volume_free_space_percent': {'key': 'properties.volumeFreeSpacePercent', 'type': 'int'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'server_resource_id': {'key': 'properties.serverResourceId', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, tags=None, server_local_path: str=None, cloud_tiering=None, volume_free_space_percent: int=None, friendly_name: str=None, server_resource_id: str=None, **kwargs) -> None:
        super(ServerEndpointCreateParameters, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.server_local_path = server_local_path
        self.cloud_tiering = cloud_tiering
        self.volume_free_space_percent = volume_free_space_percent
        self.friendly_name = friendly_name
        self.server_resource_id = server_resource_id
