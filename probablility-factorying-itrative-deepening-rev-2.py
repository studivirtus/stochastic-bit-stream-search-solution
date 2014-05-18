#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Michael
#
# Created:     17/05/2014
# Copyright:   (c) Michael 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import bisect
import operator
import functools

def main():
    pass

if __name__ == '__main__':
    main()

def factors(n):
    return set(functools.reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
print(factors(71874))

class tree():
    operation = str
    operationType = str
    result0 = 0
    result1 = 0
    leaf = False

    def __init__(self,operation,operationType,result0,result1):
        self.operation = operation
        self.operationType = operationType
        self.result0 = result0
        self.result1 = result1
        self.isLeaf()

    def isLeaf():
        if ((self.result0 == 0.5 or self.result0 == 0.4) and
            (self.result1 == 0.5 or self.result0 == 0.4)):
                self.leaf = True




class node:
    nValue = 0
    pNode = 0
    nCost = 0
    nDepth = 0
    maxDepth = 0
    def __init__(self, nodeValue,parentNode,nodeCost,nodeDepth,maxDepth):
        self.nValue = nodeValue
        self.pNode = parentNode
        self.nCost = nodeCost
        self.nDepth = nodeDepth
        self.maxDepth = maxDepth

    def __lt__(self,other):
        return self.nCost < other.nCost
    def __gt__(self,other):
        return self.nCost > other.nCost

    def hasChildren(self):
        """verify that the node has children"""
        """NOTE if maxDepth set to '0' maxDepth is infinite"""
        if (self.nDepth < self.maxDepth or self.maxDepth == 0):
            return True
        return False

    def factors(n):
        """function to help generate factors"""
        factors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                factors.append((i, int(n / i)))
        return factors

    def getFactors(number):
        """getting factors to generate child nodes"""
        #first convert the decimal to a whole number
        power10 = (len(str(n-int(number))[1:])-1) #remeber what power of 10 you used
        number10 = int (number * 10 ** power10) #here is the decimal as a whole number
        fact = factors(number10)#get factors
        del(fact[0]) #remove (1,number)
        return(fact)
        def getChildren(self,pNode):
            """get children of a node"""
            rNode = pNode.nValue*2
            lNode = pNode.nValue*2+1
            rNodeCost = pNode.nCost+1
            lNodeCost = pNode.nCost+1
            return[node(rNode,pNode,rNodeCost,(pNode.nDepth + 1),pNode.maxDepth),
                   node(lNode,pNode,lNodeCost,(pNode.nDepth + 1),pNode.maxDepth)]



class depthFirstSearch():
    goalFound = False

    """ Completes a depth first search"""
    """NOTE providing '0' as a 'maxDepth' value allows an infinit search depth"""
    frontier = list() #sorted list
    nodesVisited = list()
    goal = 0
    depthLimit = 0


    def __init__(self,firstNode,goalValue,depthLimit):
        self.frontier.append(firstNode)
        self.goal = goalValue
        self.depthLimit = depthLimit

    def explore(self):
        """Explore for a solution"""
        curNode = node(0,0,0,0,0)
        solutionNode = (0,0,0,0,0)
        found = False

        #test child nodes
        while((not self.frontierIsEmpty()) and (not found)):
            reverseChildren = list()
            """print('-----------------new-----------------')#DEBUG
            print('current frontier:')#DEBUG
            self.printlist(self.frontier)#DEBUG
            print('current visited nodes:')#DEBUG
            self.printlist(self.nodesVisited)#DEBUG"""
            curNode = self.frontier.pop(0)
            #print("current node: %i" %curNode.nValue) #DEBUG
            if self.goalReached(curNode.nValue):
                found = True
                self.goalFound = True
                solutionNode = curNode
                self.addNodesVisited(curNode)
                break
            #self.addNodesVisited(curNode)
            if (curNode.nDepth < self.depthLimit or  self.depthLimit == 0):
                if curNode.hasChildren():
                    children = curNode.getChildren(curNode)
                    for x in range(len(children)):
                        reverseChildren.insert(0,children.pop(0))
                    for child in reverseChildren:
                        self.addToFrontier(child)

        if(found):
            print("Depth first search FOUND A SOLUTION %i" % solutionNode.nValue)
            print("here are the nodes visited:")
            #Sself.printlist(self.nodesVisited)
        #selif not found and self.frontierIsEmpty():
            #print("FAILURE, Depth first search did not find a solution")
            #print("here are the nodes visited:")
            #self.printlist(self.nodesVisited)

    def atMaxDepth(self,curNode):
        if curNode.nDepth == self.depthLimit:
            return True
        return False


    def addNodesVisited(self,curNode):
        self.nodesVisited.append(curNode)

    def frontierIsEmpty(self):
        """check if frontier is empty"""
        if (len(self.frontier) > 0):
            return False
        return True

    def addToFrontier(self,curNode):
        """add node to frontier"""
        self.frontier.insert(0,curNode)


    def goalReached(self,nValue):
        """YAY GOAL IS REACHED WE"RE DONE"""
        if nValue == self.goal:
            return True
        return False

    def printlist(self,list):
        """Utility for printing lists"""
        for item in list:
            print(item.nValue,end=', ')
        print('')

def main():
    pass


if __name__ == '__main__':
    main()
    goalNode = 2000
    maxNodeDepth = 2000 #Nodes beyond this level don't have children
    depthLimit = 1 #Set maximun level for DFS to search 0 = INFINITY
    done = False


    startingNode = node(1,0,0,0,maxNodeDepth)
    while not done:
        DFS = depthFirstSearch(startingNode,goalNode,depthLimit)
        DFS.explore()
        if DFS.goalFound == True:
            done = True
            node = DFS.nodesVisited[0]
            while node.nDepth != 0:
                print (node.nValue)
                node = node.pNode
            print (node.nValue)
        else:
            print("No solution found at depth:")
            print(depthLimit)
        depthLimit += 1

print("DONE")