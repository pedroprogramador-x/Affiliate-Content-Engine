# apps/api

Backend do ACE (Affiliate Content Engine) — aplicação FastAPI.

**Status:** Etapa 1B — fundação mínima executável. Existe apenas o
esqueleto da API e o endpoint `GET /health`. Nenhum domínio de negócio
(Product, Offer, Marketplace, AffiliateLink), banco de dados, autenticação
ou integração externa foi implementado.

## Stack desta etapa

- Python 3.12+
- FastAPI + Pydantic v2
- pytest, Ruff, mypy (qualidade)
- httpx — **apenas ferramenta de testes nesta etapa**: usado pelo
  `TestClient` do FastAPI (e disponível para o smoke test). **Não** é
  dependência de runtime do backend enquanto não houver consumo HTTP
  real; por isso está no grupo `dev`, não em `[project].dependencies`.
  httpx continua sendo o cliente HTTP planejado do backend
  (`docs/adr/0003-tech-stack-v1.md`); apenas sua instalação de runtime
  foi adiada, conforme desenvolvimento incremental.
- uvicorn — servidor ASGI **apenas para desenvolvimento local / smoke
  test** (ver `docs/adr/0008-uvicorn-dev-server.md`)

Empacotamento/build do pacote Python: **Hatchling** como build backend
PEP 517 (ver `docs/adr/0009-api-packaging-build-backend.md`). O fluxo de
ambiente e instalação continua sendo `pip` + `venv` padrão — sem Poetry,
uv ou Pipenv.

A stack completa da V1 está em `docs/adr/0003-tech-stack-v1.md`.

## Estrutura

```
apps/api/
├── pyproject.toml
├── README.md
├── .env.example
├── src/
│   └── ace_api/
│       ├── __init__.py        # __version__ (fonte única da versão)
│       ├── main.py            # create_app() + app
│       └── api/
│           ├── __init__.py
│           └── health.py      # GET /health
└── tests/
    ├── __init__.py
    └── test_health.py
```

## Setup

Todos os comandos abaixo são executados a partir de `apps/api/`.

Requisito: Python 3.12 ou superior. A instalação usa `pip` + `venv`
padrão — não há Poetry/uv/Pipenv. O `pip install -e` usa o build backend
Hatchling apenas para empacotar o pacote (ver
`docs/adr/0009-api-packaging-build-backend.md`).

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

### Linux / macOS (bash)

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

O diretório `.venv/` é ignorado pelo Git (ver `.gitignore` raiz).

## Rodar a API localmente

Com o ambiente virtual ativado, a partir de `apps/api/`:

```bash
uvicorn ace_api.main:app --reload
```

Por padrão a API sobe em `http://127.0.0.1:8000`. Para escolher host/porta
explicitamente:

```bash
uvicorn ace_api.main:app --reload --host 127.0.0.1 --port 8000
```

Documentação interativa (gerada pelo FastAPI): `http://127.0.0.1:8000/docs`.

## Endpoints

### `GET /health`

Health check do serviço. Não depende de banco, Supabase ou qualquer
provider externo.

Resposta `200 OK`:

```json
{
  "status": "ok",
  "service": "ace-api",
  "version": "0.1.0"
}
```

Verificação rápida com o servidor no ar:

```bash
curl http://127.0.0.1:8000/health
```

## Comandos de desenvolvimento

Com o ambiente virtual ativado, a partir de `apps/api/`:

| Objetivo                    | Comando                  |
|-----------------------------|--------------------------|
| Rodar os testes             | `pytest`                 |
| Lint                        | `ruff check`             |
| Checar formatação           | `ruff format --check`    |
| Aplicar formatação          | `ruff format`            |
| Type check (estrito)        | `mypy`                   |
| Checar whitespace/conflitos | `git diff --check`       |

Os testes não acessam a internet nem serviços externos.

## Aviso de depreciação nos testes

O `TestClient` atual (FastAPI/Starlette sobre `httpx`) pode emitir um
`DeprecationWarning` do Starlette relacionado à futura migração de
`httpx` para `httpx2`. Nesta etapa, deliberadamente:

- os testes continuam passando e não há incompatibilidade funcional;
- o warning **não** é suprimido/filtrado;
- **não** é feito downgrade de FastAPI/Starlette para escondê-lo;
- **não** adotamos `httpx2`.

A migração para `httpx2` será decidida de forma deliberada quando for
necessária.

## Variáveis de ambiente

A API **não exige nenhuma variável de ambiente na Etapa 1B**: não há
camada de configuração/settings e nenhuma variável é lida em código. O
`.env.example` deste diretório é apenas um marcador — novas variáveis
entram nele junto do código que efetivamente as consumir.
