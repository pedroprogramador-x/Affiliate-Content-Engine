# 0003 — Stack técnica para a V1

## Status
Aceito

## Contexto
Era necessário fixar uma stack técnica para a V1 do ACE, equilibrando
produtividade de desenvolvimento, maturidade das ferramentas e adequação
ao domínio (conteúdo de afiliados multi-marketplace, com geração de vídeo
prevista dentro do escopo da própria V1, a ser implementada em uma etapa
futura de Video Factory).

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
| Processamento de vídeo    | Python + FFmpeg                            |
| Testes backend            | pytest                                     |
| Testes frontend           | Vitest + React Testing Library             |
| E2E                       | Playwright (futuro)                        |
| Qualidade Python          | Ruff + mypy                                |
| Qualidade JS/TS           | ESLint + Prettier + TypeScript strict      |
| CI                        | GitHub Actions                             |
| Deploy frontend           | Vercel (candidata; confirmação no futuro)  |
| Deploy backend/worker     | Railway (candidata; confirmação no futuro) |

## Consequências
- Stack full-typed nas duas pontas (TypeScript estrito + Pydantic v2 +
  mypy), reduzindo classes inteiras de bugs de integração.
- Supabase cobre banco, autenticação e storage com um único provider
  gerenciado, reduzindo esforço operacional na V1 (single-user).
- Python + FFmpeg fazem parte do escopo da V1 (não são um "futuro" fora
  dela): o processamento de vídeo é uma capacidade prevista do produto,
  introduzida quando o projeto chegar à etapa de Video Factory. Nenhuma
  dependência de FFmpeg é instalada e nenhum código relativo a vídeo existe
  na Etapa 1A.
- `apps/worker` e uma fila de processamento (ex.: para jobs de vídeo) só
  devem ser criados quando houver necessidade concreta — mas essa
  necessidade pode surgir ainda dentro da V1, na etapa de Video Factory, e
  não representa um desvio de stack quando acontecer.
- Vercel e Railway são as **candidatas principais** para deploy de
  frontend e de backend/worker, respectivamente, mas não são decisões
  irreversíveis: ainda não há requisitos de deploy conhecidos (tráfego,
  orçamento, restrições operacionais). A confirmação final ocorre quando o
  projeto chegar à etapa de deploy. Trocar de candidata nessa etapa, à luz
  de requisitos concretos, não é tratado como quebra de arquitetura —
  ainda assim, a escolha final deve ser justificada e registrada (atualização
  deste ADR ou um novo ADR).
- Qualquer desvio desta stack (ex.: trocar Supabase por outro provider,
  ou adicionar uma fila de mensageria) deve ser registrado em um novo ADR
  antes de ser implementado.
