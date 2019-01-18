#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

from neomodel import RelationshipTo, RelationshipFrom, ZeroOrOne, EmailProperty, StringProperty
from dayu_database.nodes.base import BaseNode
from dayu_database.relationships.user_create import UserCreateOtUpdateRelationship


class User(BaseNode):
    email = EmailProperty()
    phone = StringProperty()

    projects = RelationshipTo('dayu_database.nodes.project.Project', 'ATTEND')
    creates = RelationshipTo('dayu_database.nodes.base.BaseNode', 'CREATE', model=UserCreateOtUpdateRelationship)
    updates = RelationshipTo('dayu_database.nodes.base.BaseNode', 'UPDATE', model=UserCreateOtUpdateRelationship)

    departments = RelationshipTo('dayu_database.nodes.department.Department', 'AFFILIATED_TO')
    permissions = RelationshipFrom('dayu_database.nodes.permission.Permission', 'PERMIT')

    tasks = RelationshipFrom('dayu_database.nodes.task.Task', 'ASSIGN_TO')
    workfiles = RelationshipTo('dayu_database.nodes.workfile.Workfile', 'CREATE')
    elements = RelationshipTo('dayu_database.nodes.element.Element', 'CREATE')
    caches = RelationshipTo('dayu_database.nodes.cache.Cache', 'CREATE')
    dailies = RelationshipTo('dayu_database.nodes.dailies.Dailies', 'CREATE')
