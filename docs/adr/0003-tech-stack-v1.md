# 0003 — Stack técnica para a V1

## Status
Aceito

## Contexto
Era necessário fixar uma stack técnica para a V1 do ACE, equilibrando
produtividade de desenvolvimento, maturidade das ferramentas e adequação
ao domínio (conteúdo de afiliados multi-marketplace, com geração de vídeo
prevista para o futuro).

## Decisão
| Camada                    | Escolha                                   |
|---------------------------|--------------------------------------------|
| Frontend                  | Next.js + React + TypeScript               |
| UI                        | Tailwind CSS + shadcn/ui                   |
| Data fetching (frontend)  | TanStack Query                             |
| Validação (frontend)      | Zod                                        |
| Backend                   | Python 3.12+ + FastAPI + Pydantic v2       |
| ORM                       | SQLAlchemy 2                               |
| Migrations                | Alembic                                    |
| Database / Auth / Storage | Supabase (PostgreSQL)                      |
| HTTP client (backend)     | httpx                                      |
| Processamento de vídeo    | Python + FFmpeg (futuro, fora da V1)       |
| Testes backend            | pytest                                     |
| Testes frontend           | Vitest + React Testing Library             |
| E2E                       | Playwright (futuro)                        |
| Qualidade Python          | Ruff + mypy                                |
| Qualidade JS/TS           | ESLint + Prettier + TypeScript strict      |
| CI                        | GitHub Actions                             |
| Deploy frontend           | Vercel (futuro)                            |
| Deploy backend/worker     | Railway (futuro)                           |

## Consequências
- Stack full-typed nas duas pontas (TypeScript estrito + Pydantic v2 +
  mypy), reduzindo classes inteiras de bugs de integração.
- Supabase cobre banco, autenticação e storage com um único provider
  gerenciado, reduzindo esforço operacional na V1 (single-user).
- FFmpeg e o pipeline de vídeo ficam isolados como capacidade futura — não
  há dependência instalada nem código relativo a isso na Etapa 1A.
- Qualquer desvio desta stack (ex.: trocar Supabase por outro provider,
  ou adicionar uma fila de mensageria) deve ser registrado em um novo ADR
  antes de ser implementado.
