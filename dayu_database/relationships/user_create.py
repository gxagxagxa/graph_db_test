#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

from neomodel import StructuredRel, DateTimeProperty

class UserCreateOtUpdateRelationship(StructuredRel):
    on_datetime = DateTimeProperty(default_now=True)