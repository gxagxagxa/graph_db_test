#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

from neomodel import RelationshipTo, RelationshipFrom, ZeroOrOne
from dayu_database.nodes.base import BaseProductionUnitNode


class Shot(BaseProductionUnitNode):
    project = RelationshipFrom('dayu_database.nodes.project.Project', 'HAVE', cardinality=ZeroOrOne)
    episode = RelationshipFrom('dayu_database.nodes.project.Project', 'HAVE', cardinality=ZeroOrOne)

    workfiles = RelationshipTo('dayu_database.nodes.workfile.Workfile', 'HAVE')
    elements = RelationshipTo('dayu_database.nodes.element.Element', 'HAVE')
    cache = RelationshipTo('dayu_database.nodes.cache.Cache', 'HAVE')
    dailies = RelationshipTo('dayu_database.nodes.dailies.Dailies', 'HAVE')

    production_status = RelationshipTo('dayu_database.nodes.status.Status', 'PRODUCTION_STATUS', cardinality=ZeroOrOne)
    tasks = RelationshipTo('dayu_database.nodes.task.Task', 'BREAKDOWN_TO')

    used_by_shots = RelationshipFrom('dayu_database.nodes.shot.Shot', 'USING')
    used_by_assets = RelationshipFrom('dayu_database.nodes.asset.Asset', 'USING')
    using_assets = RelationshipTo('dayu_database.nodes.asset.Asset', 'USING')
    using_metadatas = RelationshipTo('dayu_database.nodes.metadata.Metadata', 'USING')

    vendors = RelationshipTo('dayu_database.nodes.vendor.Vendor', 'SEND_TO')