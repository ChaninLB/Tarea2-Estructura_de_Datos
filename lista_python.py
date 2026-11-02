from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Las mismas operaciones usando los métodos del list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):                      # ✅ resuelto
        self.pasajeros.append(pasajero)
        return True

    def listar(self):                                 # ✅ resuelto
        if not self.pasajeros:
            print("  (lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    # ---------------- ✍ IMPLEMENTA (tabla 3.2 de la guía) ----------------
    def insertar(self, posicion, pasajero):
        if 0 < posicion < len(self.pasajeros):
            print("posicion no validad")
            return
        self.pasajeros.insert(posicion, pasajero)

    def buscar(self, numero):
        resultado = [i for i, p in enumerate(self.pasajeros) if p.numero == numero]
        if resultado:
            return resultado[0]
        else:
            return -1

    def buscar_binaria(self, numero):
        numeros = [p.numero for p in self.pasajeros]
        num = bisect_left(numeros, numero)
        if num < len(numeros) and numeros[num] == numero:
            return num
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            print(numero, "no existe")
            return
        self.pasajeros[pos].destino = nuevo_destino
        self.pasajeros[pos].asiento = nuevo_asiento

    def eliminar_por_posicion(self, posicion):
        if 0 < posicion < len(self.pasajeros):
            self.pasajeros.pop(posicion)
        else:
            print(posicion, "posicion no validad")

    def eliminar_por_valor(self, numero):
        self.pasajeros = [p for p in self.pasajeros if p.numero != numero]

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p : p.numero)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p : p.numero, reverse = True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        return self.pasajeros.copy()

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):           # solo Lista 2
        return [p for p in self.pasajeros if p.destino == destino]

    def mayores_de_edad(self):                        # solo Lista 2
        return [p for p in self.pasajeros if p.es_mayor_de_edad()]