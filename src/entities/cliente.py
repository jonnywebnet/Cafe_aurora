"""Entidade que representa um cliente da cafeteria."""

from dataclasses import dataclass
import random

from entities.pedido import CARDAPIO, Pedido


@dataclass
class Cliente:
    nome: str
    pedido: Pedido
    paciencia: int

    @classmethod
    def aleatorio(cls, nomes: list[str] | None = None) -> "Cliente":
        nomes = nomes or ["Lia", "Rafael", "Dona Amélia", "Caio", "Bia"]
        return cls(
            nome=random.choice(nomes),
            pedido=Pedido(random.choice(CARDAPIO)),
            paciencia=random.randint(1, 3),
        )

    def perdeu_paciencia(self) -> None:
        self.paciencia = max(0, self.paciencia - 1)
