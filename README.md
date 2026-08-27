# Affiliate Content Engine (ACE)

Plataforma de inteligência e automação de conteúdo afiliado,
**multi-marketplace** e **multi-brand**.

> **Status atual: Etapa 1B — Fundação do backend.**
> Além da fundação do monorepo (Etapa 1A), o backend `apps/api` já tem
> uma aplicação FastAPI mínima e executável, com o endpoint `GET /health`.
> Nenhuma funcionalidade de produto (Product, Marketplace, IA, geração de
> vídeo), banco de dados ou autenticação foi implementada ainda.

## O que é o ACE

O ACE ajuda a operar conteúdo de afiliados através de múltiplos
marketplaces e múltiplas marcas, combinando dados vindos de APIs oficiais
dos marketplaces com automação assistida por IA — sempre com aprovação
humana antes de qualquer publicação. O design prioriza módulos
desacoplados por provider, para que a indisponibilidade de uma integração
específica nunca derrube o sistema como um todo.

Para os princípios que orientam todas as decisões técnicas do projeto
(incremental, modular, API-first com fallback manual, aprovação humana
obrigatória, etc.), veja [`AGENTS.md`](./AGENTS.md).

## Stack (V1)

| Camada          | Tecnologia                                  |
|-----------------|----------------------------------------------|
| Frontend        | Next.js + React + TypeScript                 |
| UI              | Tailwind CSS + shadcn/ui                     |
| Backend         | Python 3.12+ + FastAPI + Pydantic v2         |
| ORM / Migrations| SQLAlchemy 2 + Alembic                       |
| Dados/Auth/Storage | Supabase (PostgreSQL)                     |
| CI              | GitHub Actions                               |

Lista completa, com justificativas, em
[`docs/adr/0003-tech-stack-v1.md`](./docs/adr/0003-tech-stack-v1.md).

## Estrutura do repositório

```
.
├── apps/
│   ├── web/          # Frontend Next.js (ainda não inicializado)
│   └── api/           # Backend FastAPI (fundação + GET /health)
├── docs/
│   ├── README.md      # Índice da documentação técnica
│   └── adr/            # Architecture Decision Records
├── AGENTS.md           # Regras e princípios para agentes de IA
├── CLAUDE.md           # Notas específicas para Claude Code
├── .env.example        # Variáveis de ambiente esperadas (sem segredos)
├── .editorconfig
└── .gitignore
```

## Como este projeto é desenvolvido

O ACE é construído em etapas incrementais, cada uma com escopo explícito.
Decisões arquiteturais relevantes são registradas como ADRs em
[`docs/adr/`](./docs/adr) — comece por ali para entender o "porquê" por
trás da estrutura atual.

O backend `apps/api` já é executável: instruções de setup, execução e
comandos de teste/lint estão em [`apps/api/README.md`](./apps/api/README.md).
O frontend `apps/web` ainda não foi inicializado — sua seção de comandos
será preenchida quando isso acontecer, em etapa futura.

## Contribuindo

Este projeto segue os princípios descritos em [`AGENTS.md`](./AGENTS.md),
que se aplicam tanto a contribuidores humanos quanto a agentes de IA:
desenvolvimento incremental, sem segredos no Git, sem publicação
automática sem aprovação humana, e documentação atualizada junto com o
código.
