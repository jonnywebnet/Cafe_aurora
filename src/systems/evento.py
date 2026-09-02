"""Eventos narrativos simples para futuras expansões."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Evento:
    titulo: str
    descricao: str
    bonus_reputacao: int = 0
    bonus_dinheiro: int = 0


EVENTOS_INICIAIS = (
    Evento("Cheiro de casa", "Uma cliente lembra do café da avó e recomenda a Aurora.", 1, 0),
    Evento("Manhã chuvosa", "O movimento diminuiu, mas quem entrou ficou mais tempo.", 0, 2),
)
