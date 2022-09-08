from nodo import RBN
from tree_BR import RBT

rbt = RBT()

# datas = [10, 20, 30, 15]
datas = [11, 5, 9, 10, 3, 4, 1, 20]
for x in datas:
    rbt.add(RBN(x))

rbt.midTraverse(rbt.root)