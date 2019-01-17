#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'


from neomodel import config, db
from dayu_database.nodes import *
config.DATABASE_URL = 'bolt://neo4j:123456@localhost:7687'


print globals()
p = Project.nodes.all()[0]
print p.sequences.all()
# s = Sequence(name='pl')
#
# with db.transaction:
#     s.save()
#     s.project.connect(p)
#     s.save()
