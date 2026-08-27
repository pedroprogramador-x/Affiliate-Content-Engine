# 0002 — Estrutura de monorepo com `apps/` e `docs/`

## Status
Aceito

## Contexto
O ACE terá pelo menos dois componentes de runtime desde a V1 (frontend
Next.js e backend FastAPI), e possivelmente um terceiro **ainda dentro da
V1** (worker de processamento de vídeo, na etapa de Video Factory — ver
`docs/adr/0003-tech-stack-v1.md`). Era preciso escolher entre múltiplos
repositórios (polyrepo) ou um único repositório (monorepo), e definir o
layout de diretórios mínimo para a Etapa 1A.

## Decisão
Adotar um monorepo único, com os aplicativos isolados sob `apps/`:

```
apps/
  web/   # Next.js (frontend)
  api/   # FastAPI (backend)
docs/
  adr/   # decisões arquiteturais
```

Justificativa para monorepo (em vez de polyrepo):
- Single-user na V1: não há necessidade de deploys/times independentes por
  repositório.
- Facilita manter código e documentação sincronizados (ver princípio
  "código e documentação evoluem juntos").
- Simplifica revisão de mudanças que atravessam frontend e backend (ex.:
  um novo endpoint e o client que o consome).

Diretórios como `packages/` (código compartilhado) ou `apps/worker`
(processamento de vídeo) **não são criados agora**, pois não há ainda
código para compartilhar nem funcionalidade de vídeo — serão adicionados
quando a necessidade concreta aparecer, conforme o princípio de
desenvolvimento incremental. Isso é uma questão de sequenciamento, não de
escopo: `apps/worker` pertence à V1 (processamento de vídeo é uma
capacidade da V1, não um "futuro" pós-V1) e pode ser criado ainda dentro
dela, assim que a etapa de Video Factory tornar sua necessidade concreta.

## Consequências
- Um único histórico de commits e uma única pipeline de CI a configurar.
- Cada app (`web`, `api`) será inicializado com suas próprias ferramentas
  nativas (`create-next-app`-like setup manual, `pyproject.toml`) em etapas
  futuras, não nesta.
- Se o projeto crescer para múltiplos times ou precisar de deploy
  independente por repositório, esta decisão deve ser revisitada em um
  novo ADR.
