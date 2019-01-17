#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

from neomodel import (StructuredNode,
                      BooleanProperty, DateTimeProperty, UniqueIdProperty, StringProperty,
                      JSONProperty)


class BaseNode(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    label = StringProperty()
    active = BooleanProperty(default=True)
    comment = StringProperty()
    created_time = DateTimeProperty(default_now=True)
    extra_data = JSONProperty(default=dict())
    debug_data = JSONProperty(default=dict())
