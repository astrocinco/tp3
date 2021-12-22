import random



class Grafo:
    def __init__(self):
        self.dic = {}

    def __str__(self): # Revisar si esto es así
        for key in self.dic.keys():
            print(key)

    def agregar_vertice(self, vertice):
        if self._pertenece(vertice):
            return False
        self.dic[vertice] = {}
        return True

    def borrar_vertice(self, vertice):
        if vertice not in self.dic:
            return False
        self.dic.pop(vertice)

            # Del no da error cuando intentás sacar y el elemento no está en el diccionario

            #no conviene fijarnos si esta y usar una que si de error cuando esta en lugares equivocados?

        return True

    def agregar_arista(self, vertice_1, vertice_2, peso = 1):
        if not self._pertenece(vertice_1) or not self._pertenece(vertice_2):
            return False
        # if vertice_1 == vertice_2:
        #     return False
        self.dic[vertice_1][vertice_2] = peso
        return True

    def borrar_arista(self, vertice_1, vertice_2):
        if not self.estan_unidos(vertice_1, vertice_2):
            return False
        self.dic[vertice_1].pop(vertice_2)
        return True

    def estan_unidos(self, vertice_1, vertice_2):
        if not self._pertenece(vertice_1) or not self._pertenece(vertice_2):
            return False # Tal vez esto debería ser Raise Error
        return vertice_2 in self.dic[vertice_1]

    def peso_arista(self, vertice_1, vertice_2):
        if not self.estan_unidos(vertice_1, vertice_2):
            return 0
        return self.dic[vertice_1][vertice_2]

    def obtener_vertices(self):
        elementos = self.dic.keys()
        return elementos

    def vertice_aleatorio(self):
        lista = self.obtener_vertices()
        vertice = random.choice(list(lista))
        return vertice

    def adyacentes(self, vertice):
        return list(self.dic[vertice])

    def _pertenece(self, vertice):
        return vertice in self.dic
