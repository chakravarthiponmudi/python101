from collections import defaultdict
def sort(graph):
    
    indegree = defaultdict(int)
    nodes = set()
    queue = []
    depList = []
    for key in graph:
        nodes.add(key)
        for value in graph[key]:
            nodes.add(value)
            indegree[value] +=1
    
    for node in nodes:
        if indegree[node] == 0:
           queue.append(node) 
           
    while(len(queue) > 0) :
        n = queue.pop()
        depList.append(n)
        if n in graph:
            for node in graph[n]:
                    indegree[node] -=1
                    if indegree[node] == 0:
                        queue.append(node)
                    
    return depList

g = {
    'A' : ['C','D'],
    'B' : ['A','D'],
    'C': ['D'],
    'E': ['B','A','C','D'],
    'D':['E']

}

print(sort(g))
    
    
    
            