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

## Relação com a regra de "nenhum ponto único de falha"

O princípio geral do ACE de que "nenhuma integração externa deve impedir o
sistema de funcionar" (ver `docs/adr/0005-provider-abstraction-api-first-fallback.md`)
foi pensado para **integrações externas de negócio** desacopladas
(marketplaces, IA, voz, vídeo, assets) — não para a infraestrutura central
da aplicação. O Supabase é uma **dependência operacional aceita e central**
da V1: banco de dados, autenticação e storage não têm um fallback
funcional equivalente, e não faria sentido tratá-lo como um provider
substituível em tempo de execução nesta fase do projeto.

Para manter o risco dessa centralidade proporcional (sem implementar
redundância que a V1 não precisa), os mitigadores adotados são:

- **Portabilidade de dados via PostgreSQL puro:** o schema é definido e
  acessado via SQLAlchemy 2 + Alembic contra um `DATABASE_URL` padrão, não
  via SDK proprietário do Supabase — o mesmo schema roda em qualquer
  Postgres compatível, reduzindo o custo de uma eventual migração de
  provider.
- **Migrations versionadas:** todo o histórico de schema fica no Alembic,
  versionado no repositório, não apenas na infraestrutura do provider.
- **Backups:** os backups gerenciados do Supabase são a linha de defesa
  primária contra perda de dados na V1.
- **Restore documentado (futuro):** um runbook de restore/recuperação
  será documentado quando o projeto tiver dados reais em produção — não é
  necessário na Etapa 1A.
- **Degradação controlada quando possível:** partes do sistema que não
  dependem diretamente do Supabase (ex.: lógica que não requer leitura/
  escrita imediata) devem, na medida do razoável, degradar de forma
  controlada em vez de falhar de forma opaca.

Esta decisão **não** implica multi-cloud, replicação entre providers ou
redundância de banco de dados na V1 — isso ficaria reservado para uma
necessidade concreta futura, com ADR próprio.
