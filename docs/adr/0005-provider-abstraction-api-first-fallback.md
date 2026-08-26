# 0005 — Providers desacoplados, API-first com fallback manual

## Status
Aceito

## Contexto
O ACE é multi-marketplace e multi-brand por design. Cada marketplace (e,
futuramente, cada provider de IA) tem sua própria API, limites, formatos e
disponibilidade. Nenhuma integração externa pode se tornar um ponto único
de falha que impeça o sistema de operar — e scraping não deve ser uma
dependência da V1.

## Decisão
- Cada integração externa (marketplace, IA, etc.) é implementada como um
  **provider desacoplado**, atrás de uma interface interna estável do
  backend. O domínio nunca depende diretamente do SDK/cliente de um
  provider específico.
- A estratégia de obtenção de dados é **API-first**: sempre que o
  marketplace/serviço oferecer uma API oficial, ela é o caminho primário.
- Quando a API não estiver disponível, autorizada ou cobrir o caso de uso,
  o sistema deve permitir **fallback manual** (entrada de dados por um
  humano), em vez de depender de scraping.
- Scraping explicitamente **não é dependência da V1** e não deve ser
  necessário para o sistema operar.
- Nenhuma integração externa individual pode impedir o funcionamento geral
  do sistema: falhas de um provider devem ser isoladas (o restante do
  sistema continua operável).

## Consequências
- A estrutura de providers (interfaces, implementações concretas por
  marketplace/IA) será definida quando o backend for inicializado — fora
  do escopo da Etapa 1A.
- Testar um novo marketplace não deve exigir mudanças em código de
  domínio, apenas a adição de um novo provider que implemente a interface
  esperada.
- O fallback manual implica que o modelo de dados deve acomodar entrada
  humana como fonte de dados legítima, não apenas dados vindos de APIs.
