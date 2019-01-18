#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

from neomodel import (StructuredNode,
                      BooleanProperty, DateTimeProperty, UniqueIdProperty, StringProperty,
                      JSONProperty,
                      RelationshipFrom, RelationshipTo, Relationship, ZeroOrOne)
from dayu_database.relationships.user_create import UserCreateOtUpdateRelationship


class BaseNode(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    label = StringProperty()
    active = BooleanProperty(default=True)
    comment = StringProperty()
    created_time = DateTimeProperty(default_now=True)
    extra_data = JSONProperty(default=dict())
    debug_data = JSONProperty(default=dict())

    created_by = RelationshipFrom('dayu_database.nodes.user.User', 'CREATE',
                                  cardinality=ZeroOrOne, model=UserCreateOtUpdateRelationship)
    updated_by = RelationshipFrom('dayu_database.nodes.user.User', 'UPDATE',
                                  model=UserCreateOtUpdateRelationship)
    tags = Relationship('dayu_database.nodes.tag.Tag', 'TAG_WITH')
    histories = RelationshipTo('dayu_database.nodes.history.History', 'MODIFIED_HISTORIES')
    packages = RelationshipFrom('dayu_database.nodes.package.Package', 'CONTAIN')


class BaseProductionUnitNode(BaseNode):
    pass


class BaseSavableNode(BaseNode):
    pass