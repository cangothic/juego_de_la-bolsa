from dto.Jugador import Jugador

__author__ = 'rocka'


class Usuario(Jugador):
    def tranferir_cuenta(self, cuenta, monto):
        reseptor = Jugador(cuenta)
        if (self.saldo >= monto):
            reseptor.saldo += monto
            self.saldo=self.saldo - monto
        else:
            print("saldo insuficiente")


    def comprar(self, lista_de_acciones):
        pass

    def vender(self):
        pass
