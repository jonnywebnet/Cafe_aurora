# Documento de Assets

Este documento lista todos os recursos gráficos e sonoros utilizados no jogo.

---

# Estrutura de Assets
assets/
sprites/ clientes/ itens/ cenarios/
sons/ musicas/ efeitos/
Copiar código

---

# Sprites de Clientes

| Nome | Descrição |
|-----|-----|
cliente_estudante.png | cliente jovem
cliente_artista.png | cliente alternativo
cliente_empresario.png | cliente formal
cliente_idoso.png | cliente tradicional

---

# Sprites de Itens

| Nome | Descrição |
|-----|-----|
cafe.png | café simples
espresso.png | espresso
cappuccino.png | cappuccino
croissant.png | croissant
bolo.png | fatia de bolo

---

# Cenários

| Nome | Descrição |
|-----|-----|
cafeteria_interior.png | interior do café
balcao.png | balcão de atendimento

---

# Sons

| Nome | Descrição |
|-----|-----|
porta.wav | cliente entrando
moeda.wav | pagamento
pedido.wav | pedido feito

---

# Música

| Nome | Descrição |
|-----|-----|
tema_cafe.mp3 | música ambiente


## Assets disponíveis na versão atual

O primeiro asset visual integrado ao protótipo é:

| Caminho | Uso | Estado |
|---|---|---|
| `assets/generated/cafe_aurora_interior.png` | Fundo panorâmico do interior da cafeteria | Integrado em `src/game.py` |

Os demais sprites, sons e músicas continuam planejados para as próximas iterações. O jogo utiliza um fallback de cores caso o cenário não seja encontrado, portanto a execução continua possível sem o arquivo visual.
