#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

from neomodel import RelationshipTo, RelationshipFrom
from dayu_database.nodes.base import BaseNode


class Project(BaseNode):
    sequences = RelationshipTo('dayu_database.nodes.sequence.Sequence', 'TO_SEQUENCES')
