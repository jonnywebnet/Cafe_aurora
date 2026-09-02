"""Loop e telas do protótipo jogável Café Aurora."""

from __future__ import annotations

import random
import sys
import time
from dataclasses import dataclass

import pygame

from core.settings import (
    BG, CREAM, DAY_LENGTH, FPS, GOLD, GREEN, HEIGHT, PANEL, PANEL_LIGHT,
    RED, STARTING_MONEY, STARTING_REPUTATION, TEXT_MUTED, TITLE, WIDTH, WHITE,
)


@dataclass(frozen=True)
class MenuItem:
    name: str
    price: int
    color: tuple[int, int, int]


MENU = (
    MenuItem("Café", 3, (145, 94, 58)),
    MenuItem("Espresso", 4, (103, 63, 43)),
    MenuItem("Cappuccino", 6, (190, 139, 92)),
    MenuItem("Croissant", 5, (221, 169, 75)),
    MenuItem("Bolo", 7, (181, 103, 112)),
)


@dataclass
class Customer:
    name: str
    patience: int
    order: MenuItem


class CafeGame:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.title_font = pygame.font.Font(None, 56)
        self.heading_font = pygame.font.Font(None, 36)
        self.body_font = pygame.font.Font(None, 26)
        self.small_font = pygame.font.Font(None, 21)
        self.running = True
        self.state = "menu"
        self.day = 1
        self.money = STARTING_MONEY
        self.reputation = STARTING_REPUTATION
        self.served = 0
        self.missed = 0
        self.customer: Customer | None = None
        self.customer_started_at = 0.0
        self.message = ""
        self.message_color = TEXT_MUTED
        self.buttons: list[tuple[pygame.Rect, str]] = []
        self.customer_names = ["Lia", "Rafael", "Dona Amélia", "Caio", "Bia"]
        self.day_event = "A vizinhança começa a descobrir a cafeteria."

    def text(self, value: str, position: tuple[int, int], font: pygame.font.Font | None = None, color: tuple[int, int, int] = CREAM) -> None:
        surface = (font or self.body_font).render(value, True, color)
        self.screen.blit(surface, position)

    def panel(self, rect: pygame.Rect, color: tuple[int, int, int] = PANEL, radius: int = 14) -> None:
        pygame.draw.rect(self.screen, color, rect, border_radius=radius)

    def button(self, rect: pygame.Rect, label: str, color: tuple[int, int, int] = GOLD) -> None:
        pygame.draw.rect(self.screen, color, rect, border_radius=10)
        surface = self.body_font.render(label, True, BG)
        self.screen.blit(surface, surface.get_rect(center=rect.center))
        self.buttons.append((rect, label))

    def reset_buttons(self) -> None:
        self.buttons = []

    def draw_header(self, subtitle: str) -> None:
        self.text("CAFÉ AURORA", (48, 32), self.heading_font, GOLD)
        self.text(subtitle, (50, 72), self.small_font, TEXT_MUTED)
        pygame.draw.line(self.screen, PANEL_LIGHT, (48, 110), (WIDTH - 48, 110), 2)

    def draw_menu(self) -> None:
        self.draw_header("Uma cafeteria pequena, muitos encontros.")
        self.text("Uma nova manhã começa", (80, 190), self.title_font)
        self.text("Atenda clientes, mantenha a reputação e faça a Aurora prosperar.", (84, 255), self.body_font, TEXT_MUTED)
        self.text(f"História do dia: {self.day_event}", (84, 290), self.small_font, GOLD)
        self.panel(pygame.Rect(80, 330, 410, 170), PANEL)
        self.text("PROGRESSO", (110, 360), self.small_font, GOLD)
        self.text(f"Dia atual: {self.day}", (110, 400))
        self.text(f"Caixa: $ {self.money}", (290, 400))
        self.text(f"Reputação: {self.reputation}/5", (110, 440))
        self.button(pygame.Rect(650, 360, 280, 64), "Abrir a cafeteria")
        self.text("Clique ou pressione Enter para começar", (650, 445), self.small_font, TEXT_MUTED)

    def _event_for_day(self) -> str:
        events = (
            "Uma cliente lembra do café da avó e recomenda a Aurora.",
            "A chuva trouxe novos visitantes para o bairro.",
            "Um músico local promete tocar na cafeteria esta noite.",
        )
        return events[(self.day - 1) % len(events)]

    def start_day(self) -> None:
        self.state = "game"
        self.served = 0
        self.missed = 0
        self.next_customer()

    def next_customer(self) -> None:
        name = random.choice(self.customer_names)
        order = random.choice(MENU)
        self.customer = Customer(name, random.randint(1, 3), order)
        self.customer_started_at = time.monotonic()
        self.message = f"{name} entrou e aguarda seu atendimento."
        self.message_color = TEXT_MUTED

    def draw_game(self) -> None:
        self.draw_header(f"Dia {self.day}  •  Atendimento {self.served + self.missed + 1}/{DAY_LENGTH}")
        self.panel(pygame.Rect(48, 135, 1004, 86), PANEL)
        self.text(f"Caixa  $ {self.money}", (75, 166), self.body_font, GOLD)
        self.text(f"Reputação  {self.reputation}/5", (300, 166), self.body_font, GREEN if self.reputation >= 3 else RED)
        self.text(f"Clientes atendidos  {self.served}", (590, 166), self.body_font, CREAM)
        if not self.customer:
            return
        self.panel(pygame.Rect(48, 250, 430, 330), PANEL)
        self.text(self.customer.name, (82, 290), self.heading_font)
        self.text("“Olá! Eu gostaria de…”,", (82, 350), self.body_font, TEXT_MUTED)
        self.text(self.customer.order.name, (82, 395), self.title_font, GOLD)
        elapsed = time.monotonic() - self.customer_started_at
        time_limit = 5.0 + self.customer.patience * 2.0
        remaining = max(0.0, time_limit - elapsed)
        self.text(f"Paciência: {'●' * self.customer.patience}{'○' * (3 - self.customer.patience)}", (82, 475), self.body_font, GREEN if remaining > 4 else RED)
        pygame.draw.rect(self.screen, PANEL_LIGHT, pygame.Rect(82, 505, 300, 10), border_radius=5)
        pygame.draw.rect(self.screen, GREEN if remaining > 4 else RED, pygame.Rect(82, 505, int(300 * remaining / time_limit), 10), border_radius=5)
        self.text(self.message, (82, 530), self.small_font, self.message_color)
        self.text("Escolha o item preparado:", (540, 270), self.body_font)
        self.reset_buttons()
        for index, item in enumerate(MENU):
            column, row = index % 2, index // 2
            rect = pygame.Rect(540 + column * 250, 320 + row * 88, 220, 64)
            self.button(rect, f"{item.name}   $ {item.price}", item.color)

    def serve(self, selected_name: str) -> None:
        if not self.customer:
            return
        selected = next(item for item in MENU if item.name == selected_name)
        if selected.name == self.customer.order.name:
            self.money += selected.price
            self.reputation = min(5, self.reputation + 1 if self.reputation < 5 else 5)
            self.served += 1
            self.message = f"Pedido correto! +$ {selected.price} e a cliente ficou feliz."
            self.message_color = GREEN
        else:
            self.reputation = max(1, self.reputation - 1)
            self.missed += 1
            self.message = "Esse não era o pedido. A reputação caiu um ponto."
            self.message_color = RED
        if self.served + self.missed >= DAY_LENGTH:
            self.state = "report"
        else:
            self.next_customer()

    def draw_report(self) -> None:
        self.draw_header(f"Relatório do dia {self.day}")
        self.text("A cafeteria fechou por hoje", (80, 185), self.title_font)
        self.text("Cada atendimento ajudou a construir a história da Aurora.", (84, 250), self.body_font, TEXT_MUTED)
        self.panel(pygame.Rect(80, 330, 850, 180), PANEL)
        self.text(f"Atendimentos corretos: {self.served}/{DAY_LENGTH}", (120, 370), self.body_font, GREEN)
        self.text(f"Pedidos incorretos: {self.missed}", (120, 415), self.body_font, RED if self.missed else CREAM)
        self.text(f"Caixa acumulado: $ {self.money}", (560, 370), self.body_font, GOLD)
        self.text(f"Reputação: {self.reputation}/5", (560, 415), self.body_font, CREAM)
        self.reset_buttons()
        self.button(pygame.Rect(80, 560, 250, 60), "Próximo dia")
        self.button(pygame.Rect(370, 560, 220, 60), "Menu principal", PANEL_LIGHT)

    def update(self) -> None:
        if self.state != "game" or not self.customer:
            return
        time_limit = 5.0 + self.customer.patience * 2.0
        if time.monotonic() - self.customer_started_at >= time_limit:
            self.reputation = max(1, self.reputation - 1)
            self.missed += 1
            self.message = f"{self.customer.name} perdeu a paciência e foi embora."
            self.message_color = RED
            if self.served + self.missed >= DAY_LENGTH:
                self.state = "report"
            else:
                self.next_customer()

    def draw(self) -> None:
        self.screen.fill(BG)
        self.reset_buttons()
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "game":
            self.draw_game()
        else:
            self.draw_report()
        pygame.display.flip()

    def click(self, position: tuple[int, int]) -> None:
        for rect, label in self.buttons:
            if rect.collidepoint(position):
                if self.state == "menu":
                    self.start_day()
                elif self.state == "game":
                    self.serve(label.split("   $")[0])
                elif label == "Próximo dia":
                    self.day += 1
                    self.day_event = self._event_for_day()
                    self.start_day()
                else:
                    self.state = "menu"
                break

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.click(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.key == pygame.K_RETURN and self.state == "menu":
                self.start_day()
            elif event.key == pygame.K_1 and self.state == "game":
                self.serve(MENU[0].name)
            elif event.key == pygame.K_2 and self.state == "game":
                self.serve(MENU[1].name)
            elif event.key == pygame.K_3 and self.state == "game":
                self.serve(MENU[2].name)
            elif event.key == pygame.K_4 and self.state == "game":
                self.serve(MENU[3].name)
            elif event.key == pygame.K_5 and self.state == "game":
                self.serve(MENU[4].name)

    def run(self) -> None:
        while self.running:
            self.update()
            for event in pygame.event.get():
                self.handle_event(event)
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
