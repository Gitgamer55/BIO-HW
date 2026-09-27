class SetError(Exception):
    pass

class set_:
    def __init__(self, lst):
        self.lst = lst
    def add(self, x):
        if x not in self.lst: self.lst.append(x)
    def lowerbound(self, x):
        v = float('inf')
        for i in self.lst:
            if i >= x: v = min(v, i)
        try: return int(v)
        except OverflowError: raise SetError("No valid LowerBound found in set")
