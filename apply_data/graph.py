# encoding='utf8'
import py2neo
from py2neo import Graph, Node, Relationship, PropertyDict

#graph = Graph("http://127.0.0.1:7474", username="neo4j", password=",5d0_74f")
#graph = Graph(host = "http:127.0.0.1:7474", auth = ("neo4j", ",5d0_74f"))
graph = Graph("http:127.0.0.1:7474")
#graph.data的获取格式是list