class SetError(Exception):
    pass

class Node:
    def __init__(self, v):
        self.v = v
        self.Left = None
        self.Right = None
        self.depth = 1

class BalancedBST:
    def __init__(self):
        self.root = None

    def _get_depth(self, node):
        return node.depth if node else 0

    def _get_balance(self, node):
        if not node: return 0
        return self._get_depth(node.Left) - self._get_depth(node.Right)

    def _rotate_right(self, z):
        y = z.Left
        T3 = y.Right

        y.Right = z
        z.Left = T3

        z.depth = 1 + max(self._get_depth(z.Left), self._get_depth(z.Right))
        y.depth = 1 + max(self._get_depth(y.Left), self._get_depth(y.Right))

        return y


    def _rotate_left(self, z):
        y = z.Right
        T2 = y.Left

        y.Left = z
        z.Right = T2

        z.depth = 1 + max(self._get_depth(z.Left), self._get_depth(z.Right))
        y.depth = 1 + max(self._get_depth(y.Left), self._get_depth(y.Right))

        return y


    def insert(self, root, x):
        if not root:
            return Node(x)
        if x < root.v:
            root.Left = self.insert(root.Left, x)
        elif x > root.v:
            root.Right = self.insert(root.Right, x)
        else:
            return root
        
        root.depth = 1 + max(self._get_depth(root.Left), self._get_depth(root.Right))
        balance = self._get_balance(root)

        if balance > 1 and x < root.Left.v: return self._rotate_right(root)
        if balance < -1 and x > root.Right.v: return self._rotate_left(root)
        if balance > 1 and x > root.Left.v:
            root.Left = self._rotate_left(root.Left)
            return self._rotate_right(root)
        if balance < -1 and x < root.Right.v:
            root.Right = self._rotate_right(root.Right)
            return self._rotate_left(root)

        return root

    def find(self, root, x):
        best = float('inf')
        cur = root
        
        while cur is not None:
            if cur.v >= x:
                best = min(best, cur.v)
                cur = cur.Left
            else:
                cur = cur.Right
        return best



class set_:
    def __init__(self, lst):
        self.tree = BalancedBST()
        for item in lst:
            self.add(item)
    def add(self, x):
        self.tree.root = self.tree.insert(self.tree.root, x)
    def lowerbound(self, x):
        result = self.tree.find(self.tree.root, x)
        try: return int(result)
        except OverflowError: raise SetError("No valid LowerBound found in set")
