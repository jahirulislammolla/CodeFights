class Prizes(object):
    def __init__(self,p,n,d):
        self.p=p
        self.n=n-1
        self.b=n
        self.d=d
    def __iter__(self):
        return self
    def __next__(self):
        while self.n<len(self.p):
            self.n+=self.b
            if self.p[self.n-self.b]%self.d==0:
                return self.n-self.b+1
        else:
            raise StopIteration

def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))
