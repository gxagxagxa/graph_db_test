#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

from neomodel import RelationshipTo, RelationshipFrom
from dayu_database.nodes.base import BaseNode


class Project(BaseNode):
    episodes = RelationshipTo('dayu_database.nodes.episode.Episode', 'HAVE')
    sequences = RelationshipTo('dayu_database.nodes.sequence.Sequence', 'HAVE')
    shots = RelationshipTo('dayu_database.nodes.shot.Shot', 'HAVE')
    assets = RelationshipTo('dayu_database.nodes.asset.Asset', 'HAVE')
    locations = RelationshipTo('dayu_database.nodes.location.Location', 'HAVE')
    workfiles = RelationshipTo('dayu_database.nodes.workfile.Workfile', 'HAVE')
    elements = RelationshipTo('dayu_database.nodes.element.Element', 'HAVE')
    dailies = RelationshipTo('dayu_database.nodes.dailies.Dailies', 'HAVE')
    metadatas = RelationshipTo('dayu_database.nodes.metadata.Metadata', 'HAVE')

    users = RelationshipFrom('dayu_database.nodes.user.User', 'ATTEND')
    vendors = RelationshipFrom('dayu_database.nodes.vendor.Vendor', 'ATTEND')
