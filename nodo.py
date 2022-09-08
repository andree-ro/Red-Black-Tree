class RBN(object):
    def __init__(self, data):
        self.data = data  # Campo de datos
        self.color = 0  # 0 rojo 1 negro
        self.left = None
        self.right = None
        self.parent = None