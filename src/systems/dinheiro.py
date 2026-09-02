"""Sistema de economia básica da cafeteria."""


class SistemaDinheiro:
    def __init__(self, saldo_inicial: int = 20) -> None:
        self.saldo = saldo_inicial
        self.receita_do_dia = 0

    def receber(self, valor: int) -> None:
        self.saldo += valor
        self.receita_do_dia += valor

    def iniciar_dia(self) -> None:
        self.receita_do_dia = 0
