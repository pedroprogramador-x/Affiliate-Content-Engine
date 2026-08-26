# 0004 — Supabase como plataforma de dados, autenticação e storage

## Status
Aceito

## Contexto
A V1 é single-user, mas o modelo de dados deve estar preparado para
multi-brand no futuro. Era preciso escolher uma plataforma de dados que
oferecesse banco relacional, autenticação e storage de arquivos (para
mídia de conteúdo/vídeo) sem exigir operar infraestrutura própria desde o
início.

## Decisão
Usar Supabase (PostgreSQL gerenciado) como provider único de:
- Banco de dados relacional (acessado via SQLAlchemy 2 + Alembic no
  backend FastAPI).
- Autenticação (na V1, de um único usuário; o modelo de autenticação já
  deve comportar múltiplos usuários/marcas futuramente).
- Storage de arquivos (para assets de conteúdo, mídia gerada, etc., a
  partir do momento em que essas features forem implementadas).

O acesso ao Postgres subjacente é feito via `DATABASE_URL` padrão
(compatível com SQLAlchemy), não pelo client JS/Python do Supabase para
operações de domínio — isso mantém o backend independente de SDKs
proprietários para a camada de dados. O client Supabase pode ser usado
pontualmente para Auth e Storage.

## Consequências
- Nenhuma credencial do Supabase é versionada; `.env.example` documenta as
  variáveis esperadas (`SUPABASE_URL`, `SUPABASE_ANON_KEY`,
  `SUPABASE_SERVICE_ROLE_KEY`, `DATABASE_URL`).
- Migrations continuam sendo gerenciadas via Alembic, não via ferramentas
  proprietárias do Supabase, preservando portabilidade caso o provider
  precise ser trocado no futuro.
- Trocar de provider de dados/auth/storage no futuro exigiria um novo ADR
  e migração explícita, mas o uso de SQLAlchemy/Alembic para o schema
  reduz o acoplamento a essa decisão específica.
