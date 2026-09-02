"""Sistema de reputação da cafeteria."""


class SistemaReputacao:
    def __init__(self, valor_inicial: int = 3) -> None:
        self.valor = max(1, min(5, valor_inicial))

    def aumentar(self) -> None:
        self.valor = min(5, self.valor + 1)

    def diminuir(self) -> None:
        self.valor = max(1, self.valor - 1)

    def __str__(self) -> str:
        return f"{self.valor}/5"
