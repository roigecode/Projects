
"""
      Mergesort Python Implementation:
      
            [7,5,1,3,8,2,4,6]
        [7,5,1,3]       [8,2,4,6]
      [7,5]   [1,3]   [8,2]   [4,6]
     [7] [5] [1] [3] [8] [2] [4] [6]
      [5,7]   [1,3]   [2,8]   [4,6]
        [1,3,5,7]       [2,4,6,8]
            [1,2,3,4,5,6,7,8]

"""

def mergesort(llista):
    if len(llista) < 2:
        return llista
    else:
        mitg = len(llista)//2
        esquerra = mergesort(llista[:mitg])
        dreta = mergesort(llista[mitg:])
        return merge(esquerra,dreta)

def merge(x,y):
    if len(x)<1:
        return y
    if len(y)<1:
        return x
    if x[0]<=y[0]:
        return [x[0]]+merge(x[1:],y)
    else:
        return [y[0]]+merge(x, y[1:])
    
assert mergesort([7,5,1,3,8,2,4,6]) == [1, 2, 3, 4, 5, 6, 7, 8]
