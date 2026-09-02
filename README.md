# Café Aurora

Protótipo jogável de um jogo 2D de gerenciamento de cafeteria desenvolvido em Python com Pygame.

## Estado atual

O protótipo já contém um fluxo completo de jogo:

1. Menu principal.
2. Início de um dia de atendimento.
3. Geração de clientes e pedidos aleatórios.
4. Escolha de itens do cardápio.
5. Validação dos pedidos.
6. Atualização de dinheiro e reputação.
7. Relatório ao final do dia.
8. Progressão para o próximo dia.

## Instalação

Recomenda-se utilizar Python 3.10 ou superior em um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

No Windows, ative o ambiente com:

```powershell
.venv\Scripts\activate
pip install -r requirements.txt
```

## Execução

A partir da raiz do projeto:

```bash
PYTHONPATH=src python3 src/main.py
```

No Windows PowerShell:

```powershell
$env:PYTHONPATH = "src"
python src/main.py
```

## Controles

| Ação | Controle |
|---|---|
| Iniciar pelo menu | Clique em “Abrir a cafeteria” ou pressione `Enter` |
| Escolher item | Clique no botão ou pressione `1` a `5` |
| Sair | `Esc` ou fechar a janela |

## Estrutura

```text
src/
├── core/       # Configurações compartilhadas
├── entities/   # Entidades de domínio
├── states/     # Estados planejados da aplicação
├── systems/    # Sistemas planejados do jogo
├── ui/         # Componentes de interface planejados
├── game.py     # Loop, telas e regras do protótipo atual
└── main.py     # Ponto de entrada
```

A primeira versão funcional mantém o fluxo principal em `src/game.py` para facilitar a validação. A próxima etapa é separar gradualmente as entidades, estados, sistemas e componentes de UI nos módulos correspondentes.

## Documentação

O planejamento detalhado está em `docs/`, incluindo GDD, mecânicas, arquitetura, eventos, interface, UML e roadmap de desenvolvimento.
