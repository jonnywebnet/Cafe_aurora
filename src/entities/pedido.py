"""Entidades relacionadas ao cardápio e aos pedidos."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ItemCardapio:
    nome: str
    preco: int
    cor: tuple[int, int, int]


CARDAPIO = (
    ItemCardapio("Café", 3, (145, 94, 58)),
    ItemCardapio("Espresso", 4, (103, 63, 43)),
    ItemCardapio("Cappuccino", 6, (190, 139, 92)),
    ItemCardapio("Croissant", 5, (221, 169, 75)),
    ItemCardapio("Bolo", 7, (181, 103, 112)),
)


@dataclass(frozen=True)
class Pedido:
    item: ItemCardapio

    def confere(self, item: ItemCardapio) -> bool:
        return self.item.nome == item.nome
