#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

from neomodel import RelationshipTo, RelationshipFrom
from dayu_database.nodes.base import BaseNode


class Episode(BaseNode):
    project = RelationshipFrom('dayu_database.nodes.project.Project', 'HAVE')
    assets = RelationshipTo('dayu_database.nodes.asset.Asset', 'HAVE')
    shots = RelationshipTo('dayu_database.nodes.shot.Shot', 'HAVE')
    metadatas = RelationshipTo('dayu_database.nodes.metadata.Metadata', 'HAVE')

