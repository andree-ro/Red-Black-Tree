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

    # Recorrido de orden menor a mayor
    def midTraverse(self, number):
        if number is None:
            return
        self.midTraverse(number.left)
        colorStr = '1' if number.color == 1 else '0'
        print(number.data, colorStr)
        self.midTraverse(number.right)

    # Agregar un nodo
    def add(self, number):
        # Si no hay un nodo raíz como nodo raíz
        if self.root is None:
            self.root = number
            number.color = 1  # El nodo raíz es negro
            # print ('Agregado exitosamente', x.data)
            return
        # Encuentre una posición de inserción adecuada
        p = self.root
        while p is not None:
            if number.data < p.data:
                if p.left is None:
                    p.left = number
                    number.parent = p
                    # print ('Agregado exitosamente', x.data)
                    self.addFix(number)
                    break
                p = p.left
            else:
                if p.right is None:
                    p.right = number
                    number.parent = p
                    # print ('Agregado exitosamente', x.data)
                    self.addFix(number)
                    break
                p = p.right

    # Ajusta el árbol rojo-negro
    def addFix(self, number):
        while True:
            if number == self.root:  # Si se procesa el nodo raíz, el color es negro
                number.color = 1
                return
            p = number.parent  # Papi
            if p.color == 1 or number.color == 1:  # Mientras uno de mí y papá sea negro, no puede ser doblemente rojo,
                # luego regrese
                return
            # A continuación, analiza la situación de Red Dad
            g = p.parent  # El abuelo Red Dad debe tener un padre, porque el rojo nunca es el nodo raíz
            u = g.left if p == g.right else g.right  # El tío El tío puede ser un nodo vacío
            if u is not None and u.color == 0:  # Luego coloréalo y continúa ajustando del abuelo
                u.color = p.color = 1  # Tío y papá se ponen negros
                g.color = 0  # El abuelo se pone rojo
                x = g  # x apunta al abuelo y luego continúa el ciclo
                continue
            # A continuación, analiza la situación del tío Hei. Hay cuatro situaciones: izquierda, izquierda,
            # derecha, izquierda, derecha
            if p == g.left and number == p.left:  # Izquierda izquierda
                # Usa a papá como punto de apoyo
                self.rotateRight(p)
            elif p == g.left and number == p.right:  # Acerca de
                # Usa x como punto de apoyo
                self.rotateLeft(number)
                # Use x como pivote para girar al abuelo a la derecha (la rotación anterior convierte al abuelo en un
                # nuevo padre)
                self.rotateRight(number)
            elif p == g.right and number == p.right:  # Derecha derecha es en realidad la imagen especular de
                # izquierda e
                # izquierda
                # Abuelo zurdo con padre como pivote
                self.rotateLeft(p)
            elif p == g.right and number == p.left:  # Derecha izquierda es en realidad la imagen especular de
                # izquierda y
                # derecha
                # Usa x como punto de apoyo
                self.rotateRight(number)
                # Toma x como punto de apoyo para girar a la izquierda al abuelo (la rotación anterior convierte al
                # abuelo en un nuevo padre)
                self.rotateLeft(number)

    # Pivote p para diestros
    def rotateRight(self, p):
        g = p.parent  # El nodo padre del pivote es el punto de giro
        # Diestro g
        if g == self.root:  # Si g es el nodo raíz, entonces p se convierte en el nodo raíz
            self.root = p
            p.parent = None
        else:  # Si g no es el nodo raíz, entonces debe haber g. El padre p ocupa la posición de g
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
        # g y p intercambio de color
        p.color, g.color = g.color, p.color

    # Pivote p para zurdos
    def rotateLeft(self, p):
        g = p.parent  # El nodo padre del pivote es el punto de giro
        # Zurdo g
        if g == self.root:  # Si g es el nodo raíz, entonces p se convierte en el nodo raíz
            self.root = p
            p.parent = None
        else:  # Si g no es el nodo raíz, entonces debe haber g. El padre p ocupa la posición de g
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
        # g y p intercambio de color
        p.color, g.color = g.color, p.color
