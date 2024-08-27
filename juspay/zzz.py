import math
class Node:
    def __init__(self, val):
        self.val = val
        self.uid = None
        self.parent = None
        self.children = []
        self.isLocked = False
        self.isDescendantLocked = 0
class Tree:
    def __init__(self,n,m,node_lst,queries):
        self.node_lst=[]
        self.node_map={}

        for node in node_lst:
            conv=Node(node)
            self.node_lst.append(conv)
            self.node_map[node]=conv
        for i in range((n/m)):
            start=i*m+1
            end=i*m+m
            if end> n-1:
                end-=end%(n-1)
            if end<n:
                self.node_lst[i].children= self.node_lst[start:end+1]
        for i in range(1,n):
            self.node_lst[i].parent= self.node_lst[math.ceil(i/m)-1]
        
        self.root=self.node_lst[0]
        self.processed_queries=[query.split() for query in queries]
    

    def lock(self,node,uid):
        if node.isDescendantLocked>0 or node.isLocked or self.isAncestorLocked(node.parent):
            return False
        node.uid=uid
        node.isLocked=True
        parent_node=node.parent

        while parent_node:
            parent_node.isDescendantLocked+=1
            parent_node=parent_node.parent
        return True
    
    def unlock(self,node,uid):
        if node.uid!=uid or not node.isLocked:
            return False
        node.isLocked=False
        node.uid=None
        parent_node=node.parent
        while parent_node:
            parent_node.isDescendantLocked-=1
            parent_node=parent_node.parent
        return True
    
    def upgrade(self,node,uid):
        if node.isDescendantLocked==0 or self.isAncestorLocked(node.parent):
            return False
        self.unlockChildren(node,uid)
        self.lock(node,uid)
    

    def isAncestorLocked(self,node):
        while node:
            if node.islocked:
                return True
            node=node.parent
        return False
    def unlockChildren(self,node,uid):
        for child in node.children:
            self.unlock(child,uid)
            self.unlockChildren(child,uid)










n = 7 # no of nodes
m = 2 # To create m-ary tree
nodes = ["World", "Asia", "Africa", "China", "India", "SouthAfrica", "Egypt"]
queries = ["1 China 9", "1 India 9", "3 Asia 9", "2 India 9", "2 Asia 9"]
obj = Tree(n, m, nodes, queries)

res = []
for query in obj.processed_queries:
    if query[0]=='1':
        res.append(lock(obj.node_map[query[1]],query[2]))