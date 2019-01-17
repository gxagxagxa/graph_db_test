#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

from neomodel import RelationshipTo, RelationshipFrom
from dayu_database.nodes.base import BaseNode


class Sequence(BaseNode):
    project = RelationshipFrom('dayu_database.nodes.project.Project', 'TO_SEQUENCES')
