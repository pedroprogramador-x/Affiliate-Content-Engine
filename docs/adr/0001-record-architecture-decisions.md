# 0001 — Registrar decisões arquiteturais com ADRs

## Status
Aceito

## Contexto
O ACE será desenvolvido de forma incremental, por múltiplas sessões de
trabalho (humanas e de agentes de IA) ao longo do tempo. Decisões técnicas
tomadas cedo (stack, modelagem, padrões de integração) precisam ser
rastreáveis, para que sessões futuras entendam o "porquê" e não apenas o
"o quê", evitando retrabalho ou reversões acidentais de decisões
deliberadas.

## Decisão
Toda decisão arquitetural relevante será registrada como um Architecture
Decision Record (ADR) em `docs/adr/`, seguindo o formato:

```
# NNNN — Título curto no imperativo

## Status
Proposto | Aceito | Substituído por NNNN | Obsoleto

## Data
AAAA-MM-DD

## Contexto
## Decisão
## Alternativas consideradas
## Consequências
```

Os arquivos são numerados sequencialmente (`0001`, `0002`, ...) e nunca
renumerados. Uma decisão revista gera um novo ADR que referencia e
substitui o anterior, em vez de editar o histórico.

`Data` e `Alternativas consideradas` são as seções que passam a ser
exigidas a partir deste ADR, com o seguinte alcance:

- **ADRs novos** (criados a partir deste padrão) devem incluir `Data`; e
  devem incluir `Alternativas consideradas` quando alternativas tiverem
  sido efetivamente avaliadas no momento da decisão (se nenhuma
  alternativa real foi avaliada, a seção é omitida, não preenchida com
  conteúdo genérico).
- **ADRs legados (0001–0007)**, escritos antes deste padrão, continuam
  válidos mesmo sem `Data` ou `Alternativas consideradas`. A ausência
  desses campos não invalida a decisão nem exige correção.
- **Revisar um ADR legado** (correção editorial, esclarecimento, ajuste de
  redação) não obriga, por si só, a reconstruir retroativamente uma data
  exata ou alternativas que não foram registradas no momento da decisão
  original. Informação histórica não registrada não deve ser inventada
  para preencher um campo — a seção fica ausente.

## Consequências
- Decisões ficam versionadas junto com o código, no mesmo repositório.
- Onboarding de novas sessões (humanas ou de IA) fica mais rápido: basta
  ler `docs/adr/`.
- Exige disciplina de escrever o ADR no momento da decisão, não depois.
- Registrar alternativas consideradas dá visibilidade ao "porquê não"
  de uma decisão, não apenas ao "porquê sim".
