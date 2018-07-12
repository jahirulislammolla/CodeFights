#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
    x=[]
    y=[]
    if t==None:
        return True
    m=[]
    n=[]
    if t.left:
        m=[t.left]
        x+=[t.left.value]
    if t.right:
        n=[t.right]
        y+=[t.right.value]
    if x!=y:
        return 0
    t1=[]
    t2=[]
    x=[]
    y=[]
    while len(m)==len(n) and len(m)>0:
        d=m.pop()
        e=n.pop()
        if d.left and e.left:
            x+=[d.left.value]
            y+=[e.left.value]
            t1.append(d.left)
            t2.append(e.left)
        elif d.left:
            x+=[d.left.value]
            t1.append(d.left)
        elif e.left:
            y+=[e.left.value]
            t2.append(e.left)
        else:
            x+=[-1001]
            y+=[-1001]
        if d.right and e.right:
            x+=[d.right.value]
            y+=[e.right.value]
            t1.append(d.right)
            t2.append(e.right)
        elif d.right:
            x+=[d.right.value]
            t1.append(d.right)
        elif e.right:
            y+=[e.right.value]
            t2.append(e.right)
        else:
            x+=[-1001]
            y+=[-1001]
        if len(n)==len(m)==0:
            if x!=y[::-1]:
                return 0
            m=t1
            n=t2
            t1=[]
            t2=[]
            x=[]
            y=[]
    return m==n
