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
- Providers de IA/automação podem sugerir e preparar conteúdo, mas nunca
  publicar diretamente.

## Alcance de mudanças futuras

Esta é uma salvaguarda permanente do ACE, não um placeholder temporário de
uma etapa inicial. O escopo do que pode e do que não pode mudar por ADR
futuro é explícito:

- **Pode mudar por ADR futuro:** a UX da aprovação, os estados do fluxo de
  conteúdo, o mecanismo de auditoria/rastreabilidade, e os detalhes de
  implementação de como a aprovação é capturada e registrada.
- **Não pode mudar por ADR futuro comum:** a exigência em si de que toda
  publicação depende de uma ação humana explícita de aprovação. Remover
  essa exigência (ex.: autopublicação totalmente autônoma) não é uma
  evolução incremental do fluxo — é a alteração de um princípio
  fundamental do projeto, e só pode ocorrer mediante decisão explícita e
  deliberada do mantenedor, tratando-a como tal (não como consequência
  acidental de uma otimização, de uma automação de conveniência, ou de uma
  feature que "por engano" passa a publicar sem esse passo).

Nenhuma leitura deste ADR deve ser interpretada como previsão implícita de
autopublicação autônoma na V1 ou em qualquer etapa futura.
