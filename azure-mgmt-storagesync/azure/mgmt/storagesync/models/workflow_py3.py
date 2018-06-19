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

from .resource_py3 import Resource


class Workflow(Resource):
    """Workflow resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The id of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource
    :vartype type: str
    :param last_step_name: last step name
    :type last_step_name: str
    :param status: workflow status. Possible values include: 'active',
     'expired', 'succeeded', 'aborted', 'failed'
    :type status: str or ~azure.mgmt.storagesync.models.enum
    :param operation: operation direction. Possible values include: 'do',
     'undo', 'cancel'
    :type operation: str or ~azure.mgmt.storagesync.models.enum
    :param steps: workflow steps
    :type steps: str
    :param last_operation_id: workflow last operation identifier.
    :type last_operation_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'last_step_name': {'key': 'properties.lastStepName', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'operation': {'key': 'properties.operation', 'type': 'str'},
        'steps': {'key': 'properties.steps', 'type': 'str'},
        'last_operation_id': {'key': 'properties.lastOperationId', 'type': 'str'},
    }

    def __init__(self, *, last_step_name: str=None, status=None, operation=None, steps: str=None, last_operation_id: str=None, **kwargs) -> None:
        super(Workflow, self).__init__(**kwargs)
        self.last_step_name = last_step_name
        self.status = status
        self.operation = operation
        self.steps = steps
        self.last_operation_id = last_operation_id