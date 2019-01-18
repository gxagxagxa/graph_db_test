#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

from neomodel import RelationshipTo, RelationshipFrom, ZeroOrOne
from dayu_database.nodes.base import BaseSavableNode


class Workfile(BaseSavableNode):
    project = RelationshipFrom('dayu_database.nodes.project.Project', 'HAVE', cardinality=ZeroOrOne)

    shot_or_asset = RelationshipFrom('dayu_database.nodes.base.BaseProductionUnitNode', 'HAVE',
                                     cardinality=ZeroOrOne)
    vendor = RelationshipFrom('dayu_database.nodes.vendor.Vendor', 'SEND_BACK', cardinality=ZeroOrOne)
    task = RelationshipTo('dayu_database.nodes.task.Task', 'BELONG_TO', cardinality=ZeroOrOne)
    file = RelationshipTo('dayu_database.nodes.task.Task', 'HAVE', cardinality=ZeroOrOne)

    prev_workfile = RelationshipFrom('dayu_database.nodes.workfile.Workfile', 'SAVE_TO', cardinality=ZeroOrOne)
    next_workfile = RelationshipTo('dayu_database.nodes.workfile.Workfile', 'SAVE_TO')

    published_workfiles = RelationshipFrom('dayu_database.nodes.workfile.Workfile', 'NEED')
    published_dailies = RelationshipFrom('dayu_database.nodes.dailies.Dailies', 'NEED')
    published_elements = RelationshipFrom('dayu_database.nodes.element.Element', 'NEED')
    published_caches = RelationshipFrom('dayu_database.nodes.cache.Cache', 'NEED')
    needed_by_nodes = RelationshipFrom('dayu_database.nodes.base.BaseSavableNode', 'NEED')

    need_nodes = RelationshipTo('dayu_database.nodes.base.BaseSavableNode', 'NEED')
    need_workfiles = RelationshipTo('dayu_database.nodes.workfile.Workfile', 'NEED')
    need_elements = RelationshipTo('dayu_database.nodes.element.Element', 'NEED')
    need_caches = RelationshipTo('dayu_database.nodes.cache.Cache', 'NEED')
    need_dailies = RelationshipTo('dayu_database.nodes.dailies.Dailies', 'NEED')
