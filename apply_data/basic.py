# encoding='utf8'
import py2neo
from py2neo import Graph, Node, Relationship, PropertyDict

print(py2neo.__version__)

#graph = Graph("http://127.0.0.1:7474", username="neo4j", password=",5d0_74f")
#graph = Graph("http://neo4j:,5d0_74f@localhost:7474/db/data")
graph = Graph("http:127.0.0.1:7474")

data1 = graph.data('MATCH (transaction {timestamp: "0x57582e1c", label: "transaction"})-[belong]->(block {label: "block"}) return block')
print("data1 = ", data1, type(data1))
