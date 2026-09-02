"""Regras de paciência dos clientes."""


def avaliar_paciencia(valor: int) -> str:
    if valor <= 1:
        return "baixa"
    if valor == 2:
        return "média"
    return "alta"
