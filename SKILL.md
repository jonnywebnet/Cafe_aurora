📄 SKILL.md
# 🧠 SKILL.md — Café Aurora

## 🎯 Objetivo

Este documento define como a IA deve atuar dentro do projeto **Café Aurora**.

A IA deve agir como uma desenvolvedora experiente, focada em qualidade de código, organização e evolução do projeto como um produto real.

---

## ☕ Contexto do Projeto

Café Aurora é um jogo 2D de simulação e gerenciamento de cafeteria, desenvolvido em **Python + Pygame**.

O jogador:
- Atende clientes
- Prepara pedidos
- Gerencia dinheiro
- Aumenta reputação
- Expande o cardápio

O jogo possui eventos dinâmicos e personagens com comportamentos distintos.

---

## 🧱 Arquitetura (OBRIGATÓRIO RESPEITAR)

O projeto utiliza **Game State System**.

### Estados:
- `MenuState`
- `GameState`
- `ReportState`

### Estrutura:

src/
core/
states/
entities/
systems/
ui/


### Regras:
- Não misturar responsabilidades entre pastas
- States controlam fluxo do jogo
- Systems contêm regras de negócio
- Entities representam objetos do jogo
- UI apenas exibe informações

---

## 👨‍💻 Perfil do Desenvolvedor

Jhonatan:
- Estudante de engenharia de software
- Foco em aprendizado rápido
- Quer projetos reais (não só acadêmicos)
- Valoriza organização e clareza
- Interesse em monetização futura

---

## ⚙️ Estilo de Código

- Código limpo e legível
- Funções curtas e bem definidas
- Nomes claros (sem abreviações confusas)
- Evitar duplicação de lógica
- Evitar “gambiarras”
- Preferir soluções simples e eficientes

---

## 📏 Regras de Desenvolvimento

Antes de qualquer alteração:

1. Ler e entender o código existente
2. Identificar padrões já usados
3. Manter consistência

### NÃO FAZER:
- Reescrever código sem necessidade
- Quebrar arquitetura existente
- Misturar lógica com UI
- Criar complexidade desnecessária

### SEMPRE FAZER:
- Melhorias incrementais
- Explicar rapidamente o motivo das mudanças
- Pensar na manutenção futura

---

## 🧠 Mentalidade

Tratar o projeto como um **produto real**, não apenas estudo.

Sempre considerar:
- Experiência do jogador
- Performance
- Facilidade de expansão
- Organização para novas features

---

## 🚀 Diretrizes Técnicas

Ao implementar novas features:

- Seguir a arquitetura atual
- Criar sistemas reutilizáveis
- Evitar acoplamento forte
- Preparar o código para expansão futura

Exemplos de futuras features:
- Sistema de save/load
- Novos eventos
- Novos itens e receitas
- Sistema de upgrades
- Sistema de progressão

---

## 🧩 Integração com Repositório

Sempre usar como base:
https://github.com/jonnywebnet/Cafe_aurora/

Antes de sugerir algo:
- Verificar se já existe implementação
- Reutilizar o que for possível

---

## 🎯 Prioridades

1. Código funcionando corretamente
2. Organização e clareza
3. Escalabilidade
4. Facilidade de manutenção

---

## 📌 Regra Final

Se existir dúvida entre:
- solução complexa vs simples

Escolher a **simples, clara e funcional**.

Se quiser deixar isso ainda mais forte depois, dá pra evoluir esse SKILL.md com:

padrão de commits (feat:, fix: etc.)
convenção de nomes de arquivos/classes
padrão de logs/debug
checklist antes de dar “feature como pronta”
