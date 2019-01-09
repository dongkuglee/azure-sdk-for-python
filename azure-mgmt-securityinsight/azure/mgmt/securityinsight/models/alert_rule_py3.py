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


class AlertRule(Resource):
    """Alert rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param query: The query that will create alerts for this rule.
    :type query: str
    :param period: The period that the alert will look at.
    :type period: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'query': {'key': 'properties.query', 'type': 'str'},
        'period': {'key': 'properties.period', 'type': 'str'},
    }

    def __init__(self, *, query: str=None, period: str=None, **kwargs) -> None:
        super(AlertRule, self).__init__(**kwargs)
        self.query = query
        self.period = period