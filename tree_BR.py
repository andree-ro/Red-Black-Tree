class RBT(object):
    def __init__(self):
        self.root = None

    def traverse(self):
        return f"{self.pre_order()}\n {self.color_pre_order()}"

    def pre_order(self, *args) -> str:
        node = self.root if len(args) == 0 else args[0]

        if node is not None:
            if node.is_leaf():
                return str(node.data)

            else:
                result = str(node.data) + ' ('
                result += self.pre_order(node.left) + ', '
                result += self.pre_order(node.right) + ')'

                return result

        else:
            return 'X'

    def color_pre_order(self, *args) -> str:
        node = self.root if len(args) == 0 else args[0]

        if node is not None:
            if node.is_leaf():
                return str(node.color)

            else:
                result = str(node.color) + ' ('
                result += self.color_pre_order(node.left) + ', '
                result += self.color_pre_order(node.right) + ')'

                return result

        else:
            return 'X'

    # Recorrido de orden medio
    def midTraverse(self, number):
        if number is None:
            return
        self.midTraverse(number.left)
        colorStr = '1' if number.color == 1 else '0'
        print(number.data, colorStr)
        self.midTraverse(number.right)

    def add(self, number):
        if self.root is None:
            self.root = number
            number.color = 1
            return
        p = self.root
        while p is not None:
            if number.data < p.data:
                if p.left is None:
                    p.left = number
                    number.parent = p
                    self.addFix(number)
                    break
                p = p.left
            else:
                if p.right is None:
                    p.right = number
                    number.parent = p
                    self.addFix(number)
                    break
                p = p.right

    def addFix(self, x):
        while True:
            if x == self.root:
                x.color = 1
                return
            p = x.parent
            if p.color == 1 or x.color == 1:
                return
            g = p.parent
            u = g.left if p == g.right else g.right
            if u is not None and u.color == 0:
                u.color = p.color = 1
                g.color = 0
                x = g
                continue
            if p == g.left and x == p.left:
                self.rotateRight(p)
            elif p == g.left and x == p.right:
                self.rotateLeft(x)
                self.rotateRight(x)
            elif p == g.right and x == p.right:
                self.rotateLeft(p)
            elif p == g.right and x == p.left:
                self.rotateRight(x)
                self.rotateLeft(x)

    def rotateRight(self, p):
        g = p.parent
        if g == self.root:
            self.root = p
            p.parent = None
        else:
            gp = g.parent
            p.parent = gp
            if g == gp.left:
                gp.left = p
            else:
                gp.right = p
        g.left = p.right
        if p.right is not None:
            p.right.parent = g
        p.right = g
        g.parent = p
        p.color, g.color = g.color, p.color

    def rotateLeft(self, p):
        g = p.parent
        if g == self.root:
            self.root = p
            p.parent = None
        else:
            gp = g.parent
            p.parent = gp
            if g == gp.left:
                gp.left = p
            else:
                gp.right = p
        g.right = p.left
        if p.left is not None:
            p.left.parent = g
        p.left = g
        g.parent = p
        p.color, g.color = g.color, p.color
