"""Gerenciador de estados da aplicação."""


class StateManager:
    def __init__(self, initial_state: str = "menu") -> None:
        self.current = initial_state

    def change(self, state_name: str) -> None:
        self.current = state_name
