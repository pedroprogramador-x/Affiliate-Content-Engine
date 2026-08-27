# 0009 — Hatchling como build backend do pacote `apps/api`

## Status
Aceito

## Data
2026-08-27

## Contexto
O `apps/api` é instalado em desenvolvimento com `pip install -e ".[dev]"`
dentro de um virtualenv padrão (`python -m venv`). Uma instalação
editável por `pip` exige que o projeto declare um **build backend PEP 517**
na seção `[build-system]` do `pyproject.toml`; sem isso, `pip install -e`
não funciona de forma padronizada.

O bootstrap da Etapa 1B já vinha usando Hatchling como build backend, mas
com `requires = ["hatchling"]` sem limite de versão. A auditoria pediu
para formalizar essa escolha em um ADR e delimitar a faixa de versão.

Restrições e princípios que moldam a decisão:

- O fluxo de ambiente/dependências do projeto continua sendo `pip` +
  `venv` padrão. Não está em discussão adotar um gerenciador de
  ambientes/dependências (Poetry, uv, Pipenv) — ver
  `docs/adr/0003-tech-stack-v1.md`.
- A escolha é **local ao empacotamento Python do backend**: afeta apenas
  como o pacote `ace_api` é construído/empacotado, não o runtime da
  aplicação nem o restante do monorepo.
- O `apps/api` precisa de versão derivada de uma única fonte de verdade
  (`ace_api.__version__`) e de um layout `src/`.

A versão de Hatchling efetivamente exercitada ao rodar
`pip install -e ".[dev]"` neste ambiente foi observada (log verboso do
`pip`, ambiente de build isolado do PEP 517) como **1.32.0**.

## Decisão
- Manter **Hatchling** como build backend do `apps/api`, declarado em
  `apps/api/pyproject.toml`:

  ```toml
  [build-system]
  requires = ["hatchling>=1.32,<2"]
  build-backend = "hatchling.build"
  ```

- A faixa `>=1.32,<2` tem como piso a versão realmente testada (1.32.0) e
  como teto o próximo major de Hatchling, ainda inexistente. Hatchling
  mantém uma linha 1.x estável e sem quebras conhecidas para este uso
  (leitura de versão via `[tool.hatch.version]`, target de wheel via
  `[tool.hatch.build.targets.wheel]`); um eventual 2.0 poderia introduzir
  mudanças incompatíveis e fica deliberadamente fora da faixa até ser
  avaliado.
- Hatchling é usado **apenas para empacotamento/build** do pacote. Isto
  **não** adota Hatch como gerenciador de ambientes ou de dependências.
- `pip` + `venv` padrão continuam sendo o fluxo de ambiente e instalação.
- **Não** estão sendo adotados Poetry, uv nem Pipenv.
- Esta decisão é **local ao empacotamento Python do backend** e não se
  estende a outros apps do monorepo (ex.: `apps/web`, que tem toolchain
  própria).

## Alternativas consideradas
- **Hatchling (escolhida).** Build backend PEP 517 pequeno e sem estado,
  já usado no bootstrap. Suporte nativo a layout `src/`, a versão dinâmica
  a partir de um atributo do pacote (`[tool.hatch.version]`) e a seleção
  explícita de pacotes na wheel. Não arrasta um gerenciador de ambientes
  junto. Configuração mínima no `pyproject.toml`.
- **setuptools.** Também é build backend PEP 517 e é onipresente. Rejeitada
  para este caso por exigir mais configuração/boilerplate para o mesmo
  resultado (descoberta de pacotes em `src/`, versão dinâmica via
  `[tool.setuptools.dynamic]` + `attr:`), com histórico de mais superfície
  de configuração legada. Não há ganho concreto que justifique trocar o
  que já funciona.
- **Não instalar o pacote e depender de `PYTHONPATH`.** Manteria
  `[build-system]` ausente e os testes/execução achariam `ace_api` via
  `pythonpath`/`PYTHONPATH` apontando para `src/`. Rejeitada: `pip install
  -e ".[dev]"` deixaria de funcionar como método padrão de setup; o
  ambiente passaria a depender de configuração implícita de path (frágil e
  específica por ferramenta), e a resolução de imports em execução real da
  API divergiria da de testes.

## Consequências
- `apps/api/pyproject.toml` declara `requires = ["hatchling>=1.32,<2"]`;
  o `pip` resolve Hatchling em um ambiente de build isolado (PEP 517), e
  Hatchling **não** aparece como dependência instalada no virtualenv de
  runtime/desenvolvimento.
- Atualizações de Hatchling dentro de `>=1.32,<2` são absorvidas sem
  mudança no projeto. Passar do teto (`2.x`) exige revisar este ADR e
  revalidar o build.
- Trocar o build backend no futuro (ex.: para setuptools ou outro) é uma
  mudança localizada em `[build-system]`, a ser registrada com um novo
  ADR que substitua este.
- Nenhum efeito sobre runtime da aplicação, sobre o fluxo `pip` + `venv`
  ou sobre a decisão de stack do `docs/adr/0003-tech-stack-v1.md`.
