import sys
def l2tup(l):
    a=list(map(lambda x,y:x*y, [i[2] for i in l],[i[3] for i in l]))
    return [(l[i][0],a[i]+10) if a[i]<100 else (l[i][0],a[i]) for i in range(len(a))]

print(l2tup([["34587", "Learning Python, Mark Lutz", 4, 40.95],
          ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]]))    
def l2tups(l):
    
    a=[[i[0],sum(list(map(lambda x,y:x*y, [x[1] for x in i[1:]],[x[2] for x in i[1:]])))] for i in l]
    return a
print(l2tups([ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
           [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
           [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]))    