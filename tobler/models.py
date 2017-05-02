from py2neo import Graph, Relationship, Node


#add to a config file
graph = Graph('http://localhost:7474/db/data', user='neo4j', password='test1234')

class Nodes:
    def __init__(self, name, label):
        self.__name = name
        self.__label = label

    def getNames(self):
        return self.__name

    def setNames(self, name):
        self.__name = name

    def getLabels(self):
        return self.__label

    def setLabels(self, label):
        self.__label = label

    def createNode(self, name, label):
        node = Node(label, name=name)
        graph.create(node)

class Relationships:
    def __init__(self, relationship):
        self.__relationship = relationship

    def get(self):
        return self.__relationship

    def set(self,relationship):
        self.__relationship = relationship