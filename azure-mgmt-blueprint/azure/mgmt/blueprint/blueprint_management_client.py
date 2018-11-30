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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.blueprints_operations import BlueprintsOperations
from .operations.artifacts_operations import ArtifactsOperations
from .operations.published_blueprints_operations import PublishedBlueprintsOperations
from .operations.published_artifacts_operations import PublishedArtifactsOperations
from .operations.operations import Operations
from .operations.assignments_operations import AssignmentsOperations
from .operations.assignment_operations import AssignmentOperations
from . import models


class BlueprintManagementClientConfiguration(AzureConfiguration):
    """Configuration for BlueprintManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(BlueprintManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-blueprint/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class BlueprintManagementClient(SDKClient):
    """Blueprint Client

    :ivar config: Configuration for client.
    :vartype config: BlueprintManagementClientConfiguration

    :ivar blueprints: Blueprints operations
    :vartype blueprints: azure.mgmt.blueprint.operations.BlueprintsOperations
    :ivar artifacts: Artifacts operations
    :vartype artifacts: azure.mgmt.blueprint.operations.ArtifactsOperations
    :ivar published_blueprints: PublishedBlueprints operations
    :vartype published_blueprints: azure.mgmt.blueprint.operations.PublishedBlueprintsOperations
    :ivar published_artifacts: PublishedArtifacts operations
    :vartype published_artifacts: azure.mgmt.blueprint.operations.PublishedArtifactsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.blueprint.operations.Operations
    :ivar assignments: Assignments operations
    :vartype assignments: azure.mgmt.blueprint.operations.AssignmentsOperations
    :ivar assignment_operations: AssignmentOperations operations
    :vartype assignment_operations: azure.mgmt.blueprint.operations.AssignmentOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = BlueprintManagementClientConfiguration(credentials, base_url)
        super(BlueprintManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.blueprints = BlueprintsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.artifacts = ArtifactsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.published_blueprints = PublishedBlueprintsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.published_artifacts = PublishedArtifactsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.assignments = AssignmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.assignment_operations = AssignmentOperations(
            self._client, self.config, self._serialize, self._deserialize)