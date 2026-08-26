# apps/api

Backend do ACE (Affiliate Content Engine).

**Status:** ainda não iniciado. Este diretório existe apenas para reservar o
lugar do app na estrutura do monorepo (Etapa 1A — bootstrap).

Stack planejada (ver `docs/adr/0003-tech-stack-v1.md`):

- Python 3.12+ / FastAPI / Pydantic v2
- SQLAlchemy 2 (ORM)
- Alembic (migrations)
- httpx (cliente HTTP para integrações com providers)
- pytest (testes)
- Ruff + mypy (qualidade de código)

A inicialização do projeto FastAPI (scaffolding, `pyproject.toml`,
dependências) será feita em uma etapa posterior, não na Etapa 1A.
