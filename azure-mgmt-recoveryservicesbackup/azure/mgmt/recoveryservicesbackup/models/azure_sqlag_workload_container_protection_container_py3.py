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

from .azure_workload_container_py3 import AzureWorkloadContainer


class AzureSQLAGWorkloadContainerProtectionContainer(AzureWorkloadContainer):
    """Container for SQL workloads under SQL Availability Group.

    All required parameters must be populated in order to send to Azure.

    :param friendly_name: Friendly name of the container.
    :type friendly_name: str
    :param backup_management_type: Type of backup managemenent for the
     container. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB',
     'DPM', 'AzureBackupServer', 'AzureSql', 'AzureStorage', 'AzureWorkload',
     'DefaultBackup'
    :type backup_management_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.BackupManagementType
    :param registration_status: Status of registration of the container with
     the Recovery Services Vault.
    :type registration_status: str
    :param health_status: Status of health of the container.
    :type health_status: str
    :param container_type: Required. Constant filled by server.
    :type container_type: str
    :param source_resource_id: ARM ID of the virtual machine represented by
     this Azure Workload Container
    :type source_resource_id: str
    :param last_updated_time: Time stamp when this container was updated.
    :type last_updated_time: datetime
    :param extended_info: Additional details of a workload container.
    :type extended_info:
     ~azure.mgmt.recoveryservicesbackup.models.AzureWorkloadContainerExtendedInfo
    :param workload_type: Workload type for which registration was sent.
     Possible values include: 'Invalid', 'VM', 'FileFolder', 'AzureSqlDb',
     'SQLDB', 'Exchange', 'Sharepoint', 'VMwareVM', 'SystemState', 'Client',
     'GenericDataSource', 'SQLDataBase', 'AzureFileShare', 'SAPHanaDatabase',
     'SAPAseDatabase'
    :type workload_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.WorkloadType
    :param operation_type: Re-Do Operation. Possible values include:
     'Invalid', 'Register', 'Reregister'
    :type operation_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.OperationType
    """

    _validation = {
        'container_type': {'required': True},
    }

    _attribute_map = {
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'registration_status': {'key': 'registrationStatus', 'type': 'str'},
        'health_status': {'key': 'healthStatus', 'type': 'str'},
        'container_type': {'key': 'containerType', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'last_updated_time': {'key': 'lastUpdatedTime', 'type': 'iso-8601'},
        'extended_info': {'key': 'extendedInfo', 'type': 'AzureWorkloadContainerExtendedInfo'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'str'},
    }

    def __init__(self, *, friendly_name: str=None, backup_management_type=None, registration_status: str=None, health_status: str=None, source_resource_id: str=None, last_updated_time=None, extended_info=None, workload_type=None, operation_type=None, **kwargs) -> None:
        super(AzureSQLAGWorkloadContainerProtectionContainer, self).__init__(friendly_name=friendly_name, backup_management_type=backup_management_type, registration_status=registration_status, health_status=health_status, source_resource_id=source_resource_id, last_updated_time=last_updated_time, extended_info=extended_info, workload_type=workload_type, operation_type=operation_type, **kwargs)
        self.container_type = 'SQLAGWorkLoadContainer'
