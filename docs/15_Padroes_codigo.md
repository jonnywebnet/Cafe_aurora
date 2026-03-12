Padrões de Código

Este documento define padrões de programação para manter o projeto organizado.

---

# Convenções de Nome

## Classes

Utilizar **PascalCase**

Exemplo:
Cliente Pedido Cardapio Game
Copiar código

---

## Variáveis

Utilizar **snake_case**

Exemplo:
dinheiro_jogador fila_clientes pedido_atual
Copiar código

---

## Funções

Utilizar **snake_case**

Exemplo:
criar_cliente() gerar_pedido() verificar_pedido() finalizar_dia()
Copiar código

---

# Organização de Arquivos

Cada sistema deve ficar em um arquivo separado.

Exemplo:
cliente.py pedido.py cardapio.py game.py
Copiar código

---

# Comentários

Sempre explicar partes importantes do código.

Exemplo:
gera um cliente aleatório
def criar_cliente():
Copiar código

---

# Boas Práticas

- evitar funções muito grandes
- dividir lógica em módulos
- reutilizar código sempre que possível
- manter nomes claros e descritivos
