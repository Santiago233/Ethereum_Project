# -*- coding:utf-8 -*-
import os
from py2neo import Graph, Node, Relationship, NodeSelector 
graph = Graph("http://localhost:7474", username="neo4j", password=',5d0_74f')

data1 = graph.data('MATCH (transaction {timestamp: "0x57582e1c", label: "transaction"})-[belong]->(block {label: "block"}) return block')
print("data1 = ", data1, type(data1))