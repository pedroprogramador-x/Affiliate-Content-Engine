# 0008 — Uvicorn como servidor ASGI de desenvolvimento local

## Status
Aceito

## Data
2026-08-27

## Contexto
A Etapa 1B inicializa o backend FastAPI (`apps/api`) e exige que seja
possível "subir a API localmente" e consultar `GET /health` por HTTP
real. FastAPI é um framework ASGI e não embute um servidor: para atender
uma requisição HTTP de verdade é necessário um servidor ASGI.

A stack fixada no `docs/adr/0003-tech-stack-v1.md` lista FastAPI,
Pydantic v2 e httpx no backend, mas não nomeia um servidor ASGI. O extra
`fastapi[standard]` traz uvicorn junto de várias dependências adicionais
(python-multipart, jinja2, email-validator, websockets, etc.) que a
Etapa 1B não utiliza.

## Decisão
Adotar **uvicorn** como servidor ASGI para **execução local e smoke
tests HTTP** de `apps/api`, adicionado **apenas ao grupo de dependências
de desenvolvimento** (`[project.optional-dependencies].dev`) em
`apps/api/pyproject.toml`.

- Uvicorn é usado para rodar a aplicação em desenvolvimento
  (`uvicorn ace_api.main:app --reload`) e para o smoke test HTTP da
  Etapa 1B.
- Isto **não** define o servidor nem o modelo de processo de produção.
- A decisão de runtime/deploy de produção (servidor ASGI de produção,
  número de workers, gerenciador de processo, plataforma) permanece
  adiada para a etapa de deploy, como já previsto no ADR 0003.
- **Não** adotar `fastapi[standard]` nesta etapa, para não trazer
  dependências transitivas desnecessárias.

## Alternativas consideradas
- **`fastapi[standard]`**: traz uvicorn mais extras não usados na
  Etapa 1B; descartada por peso desnecessário.
- **Nenhum servidor (smoke test só via `httpx.ASGITransport` em
  memória)**: mantém a stack literal, mas não cumpre "subir a API
  localmente" com um servidor HTTP real; descartada.
- **Outros servidores ASGI (hypercorn, granian)**: sem vantagem concreta
  para o caso de uso atual; uvicorn é a opção mais comum e documentada no
  ecossistema FastAPI.

## Consequências
- `apps/api` passa a ter uvicorn como dependência de desenvolvimento;
  ambientes de produção não recebem uvicorn automaticamente por este ADR.
- Na etapa de deploy, a escolha do servidor ASGI de produção
  (possivelmente uvicorn sob um gerenciador de processo, possivelmente
  outro) será registrada — atualizando este ADR ou em um novo.
- Se uvicorn passar a ser necessário em runtime de produção, isso exige
  decisão explícita registrada; não é consequência automática desta.
