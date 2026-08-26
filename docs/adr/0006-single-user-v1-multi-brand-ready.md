# 0006 — V1 single-user, modelo preparado para multi-brand

## Status
Aceito

## Contexto
O produto final visado é multi-marketplace e multi-brand, mas a V1 será
usada por um único usuário/operador. Implementar multi-tenancy completo
(múltiplos usuários, permissões, isolamento de dados entre contas) desde o
início contradiria o princípio de desenvolvimento incremental e adicionaria
complexidade sem valor imediato.

## Decisão
- A V1 opera com um único usuário (autenticação simples via Supabase Auth,
  sem gestão de múltiplos usuários/papéis).
- Ainda assim, o **modelo de dados** trata "marca" (brand) como uma
  entidade de primeira classe desde o início (mesmo que a V1 só crie/opere
  uma única marca), para que a evolução para multi-brand no futuro seja
  uma extensão do modelo existente, não uma reescrita.
- Entidades de domínio (a serem modeladas em etapas futuras, não na 1A)
  devem ser escopadas por marca desde a primeira migration que as criar.

## Consequências
- Não há tabelas/lógica de multi-tenancy (organizações, papéis, convites)
  na V1 — isso fica para quando houver necessidade real de múltiplos
  usuários.
- Toda modelagem futura de domínio (produtos, conteúdo, publicações) deve
  incluir uma referência à marca, mesmo operando com uma única marca
  ativa.
- Avaliar multi-usuário por marca (equipes) é uma decisão futura, a ser
  registrada em novo ADR quando houver demanda concreta.
