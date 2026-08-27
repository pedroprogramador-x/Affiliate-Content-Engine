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
preferidas a partir deste ADR. ADRs anteriores a esta atualização podem
não ter essas seções preenchidas quando a informação real (data exata da
decisão, alternativas de fato avaliadas no momento) não foi registrada —
nesse caso a seção é omitida em vez de preenchida com conteúdo inventado
retroativamente. Esses ADRs continuam válidos; a lacuna é aceitável e não
precisa ser corrigida artificialmente, mas ADRs novos ou revisados devem
incluir as seções quando a informação existir.

## Consequências
- Decisões ficam versionadas junto com o código, no mesmo repositório.
- Onboarding de novas sessões (humanas ou de IA) fica mais rápido: basta
  ler `docs/adr/`.
- Exige disciplina de escrever o ADR no momento da decisão, não depois.
- Registrar alternativas consideradas dá visibilidade ao "porquê não"
  de uma decisão, não apenas ao "porquê sim".
