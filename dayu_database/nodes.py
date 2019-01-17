#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'


from neomodel import RelationshipTo, RelationshipFrom
from vfx_db.nodes.base import BaseNode


class Project(BaseNode):
    sequences = RelationshipTo('Sequence', 'TO_SEQUENCES')


class Sequence(BaseNode):
    project = RelationshipFrom('Project', 'TO_SEQUENCES')





