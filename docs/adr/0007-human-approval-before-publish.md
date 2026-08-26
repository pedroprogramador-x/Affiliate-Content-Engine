# 0007 — Aprovação humana obrigatória antes da publicação

## Status
Aceito

## Contexto
O ACE automatiza inteligência e geração de conteúdo afiliado. Conteúdo
publicado incorretamente (preços errados, claims inadequados, mídia de
baixa qualidade) tem custo reputacional e, potencialmente, legal/comercial
junto aos programas de afiliados e marketplaces. Automação total de ponta
a ponta (geração → publicação) sem checagem humana é um risco inaceitável
para a V1.

## Decisão
Nenhum conteúdo gerado ou processado pelo ACE é publicado automaticamente
em um canal externo sem aprovação humana explícita. O fluxo de qualquer
peça de conteúdo deve incluir, no mínimo, um estado equivalente a
"aguardando aprovação" antes de um estado "publicado", e a transição para
"publicado" exige uma ação humana registrada.

Este princípio é transversal: aplica-se independentemente do marketplace,
da marca, ou de qual provider de IA gerou o conteúdo.

## Consequências
- O modelo de dados de conteúdo (a ser desenhado em etapa futura) precisa
  de um campo/estado de aprovação e de rastreabilidade de quem aprovou.
- Qualquer feature de "publicação automática" só pode ser considerada no
  futuro mediante um novo ADR que reavalie explicitamente este princípio,
  e não como consequência acidental de uma otimização de fluxo.
- Providers de IA/automação podem sugerir e preparar conteúdo, mas nunca
  publicar diretamente.
