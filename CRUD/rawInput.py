from tobler.models import Nodes

class userInput():
    nameList = []
    labelList = []

    numNodes = int(input('How many nodes would you like to create? '))
    while numNodes > 0:
        names = input('Please enter the name of a node: ')
        nameList.append(names)
        labels = input('Please enter a class for the node to be grouped into: ')
        labelList.append(labels)
        numNodes-=1
    node = Nodes(names, labels)
    node.createNode(names,labels)
