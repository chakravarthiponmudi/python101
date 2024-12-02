from collections import Counter
def findWinner(ballots):
    counter = Counter()
    for ballot in ballots:
        counter.update(ballot[:3])
    
    print(counter)
    

ballots = [
    ['n1','n2','n3'],
    ['n2','n4'],
    ['n1','n4','n2']
]

findWinner(ballots)
    