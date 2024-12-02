class UnionFind():
    def __init__(self,n):
        self.root = [i for i in range(n)]

    def findRoot(self,a):
        return self.root[a]

    def isConnected(self, a, b):
        return self.findRoot(a) == self.findRoot(b)
    
    def union(self, a,b):
        rootA = self.findRoot(a)
        rootB = self.findRoot(b)
        
        if rootA != rootB :
            self.root[b] = rootA
            for index in [index for index,value in enumerate(self.root) if value == rootB]:
                self.root[index] = rootA
        

