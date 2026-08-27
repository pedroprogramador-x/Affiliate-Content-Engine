# AGENTS.md

Guia para qualquer agente de IA (Claude Code, Cursor, Copilot, etc.) que for
trabalhar neste repositório. Complementa, mas não substitui, o julgamento do
mantenedor humano do projeto.

## O que é o ACE

Affiliate Content Engine (ACE): plataforma de inteligência e automação de
conteúdo afiliado, multi-marketplace e multi-brand. Ver `README.md` para
visão geral e `docs/adr/` para o histórico de decisões arquiteturais.

## Princípios não-negociáveis

Estes princípios valem para qualquer etapa do projeto, presente ou futura:

1. **Desenvolvimento incremental.** Não implemente além do que foi pedido
   na etapa atual. Se a tarefa descrever uma "Etapa N", pare ao final dela
   e aguarde revisão antes de avançar para a próxima — mesmo que o próximo
   passo pareça óbvio.
2. **Modularidade e providers desacoplados.** Integrações externas
   (marketplaces, IA, etc.) vivem atrás de interfaces internas. O domínio
   nunca depende diretamente do SDK de um provider específico.
3. **API-first + fallback manual.** Scraping não é dependência da V1.
   Quando uma API não cobrir um caso, o sistema deve permitir entrada
   manual em vez de depender de scraping.
4. **Nenhuma integração externa de negócio é ponto único de falha.** Esta
   regra vale principalmente para providers de negócio desacoplados
   (marketplaces, IA, voz, vídeo, assets): o sistema deve continuar
   funcionando mesmo se um desses providers estiver fora do ar ou não
   configurado. Ela não se aplica da mesma forma a dependências de
   infraestrutura central da V1, como o Supabase — ver
   `docs/adr/0004-supabase-as-platform.md` para os mitigadores
   proporcionais adotados nesse caso (portabilidade via Postgres puro,
   migrations versionadas, backups; o procedimento de restore será
   documentado quando existirem dados reais em produção).
5. **Single-user na V1, modelo pronto para multi-brand.** Não implemente
   multi-tenancy completo (múltiplos usuários/papéis) sem necessidade
   concreta, mas escope entidades de domínio por marca desde o início.
6. **Aprovação humana obrigatória antes de publicar.** Nenhum fluxo pode
   publicar conteúdo automaticamente sem uma ação humana explícita de
   aprovação.
7. **Nenhuma credencial ou segredo no Git.** Nunca commitar `.env`, chaves,
   tokens ou credenciais. Use `.env.example` para documentar variáveis
   esperadas, sempre com valores vazios/placeholder.
8. **Código e documentação evoluem juntos.** Mudanças relevantes de
   arquitetura ganham um ADR em `docs/adr/`. Mudanças de comportamento
   relevantes atualizam o `README.md` e/ou docs correlatas no mesmo PR/commit.

## Stack (V1)

Ver `docs/adr/0003-tech-stack-v1.md` para a lista completa e justificativa.
Resumo: Next.js/React/TypeScript + Tailwind/shadcn no frontend; Python
3.12+/FastAPI/Pydantic v2 + SQLAlchemy 2/Alembic no backend; Supabase
(Postgres/Auth/Storage); GitHub Actions para CI.

Não adicione dependências, frameworks ou serviços fora dessa lista sem
antes propor a mudança (e, se aceita, registrar um novo ADR).

## Estrutura do repositório

```
apps/
  web/    # frontend Next.js
  api/    # backend FastAPI
docs/
  adr/    # decisões arquiteturais
```

Novos diretórios de topo (ex.: `packages/`, `apps/worker`) só devem ser
criados quando houver necessidade concreta, não preventivamente. Isso é
sequenciamento, não escopo: `apps/worker` (processamento de vídeo,
Video Factory) pertence à V1 e pode surgir ainda dentro dela — não é um
item necessariamente pós-V1.

## Regras específicas para agentes de IA

- **Antes de alterar qualquer arquivo**, inspecione o estado atual do
  repositório (branch, working tree, histórico) e reporte o que
  encontrou. Nunca presuma que o repositório está vazio ou limpo.
- **Nunca descarte trabalho não commitado** sem antes investigar e, se
  necessário, perguntar. Prefira `git stash` a `git checkout --`/`reset
  --hard`/`clean -f` quando houver dúvida.
- **Não avance de etapa sozinho.** Se a tarefa é "Etapa 1A", implemente
  apenas a Etapa 1A, mesmo que o contexto sugira o que viria na 1B.
- **Não instale dependências desnecessárias.** Cada dependência nova deve
  ser justificável pela tarefa em questão.
- **Rode as validações disponíveis** (lint, type-check, testes) antes de
  considerar uma tarefa concluída, e relate os resultados — inclusive
  quando ainda não há validações aplicáveis (ex.: projeto sem código
  ainda).
- **Push normalmente exige autorização explícita.** Confirme com o usuário
  antes de enviar mudanças a um branch compartilhado, a menos que
  instruções do projeto/tarefa autorizem previamente.
  - **Exceção:** em um ambiente remoto efêmero (container descartável ao
    fim da sessão), quando for tecnicamente necessário para não perder o
    trabalho, é permitido fazer commit e push automaticamente — mas
    **somente** para a branch isolada da própria tarefa em andamento
    (nunca para `main` ou qualquer branch compartilhada/de outra tarefa).
  - Essa exceção nunca autoriza push direto para `main`, nem, sob
    nenhuma circunstância, force-push para `main`.
  - Todo commit/push feito sob essa exceção deve ser reportado de forma
    explícita no relatório final da tarefa, informando branch e SHA do
    commit.
  - Push para branches compartilhadas (ex.: `main`, branches de outras
    tarefas) sempre exige autorização explícita do usuário — a exceção
    acima não se estende a elas.
- **Ao terminar uma tarefa**, liste os arquivos criados/alterados e
  explique as decisões tomadas — especialmente qualquer desvio em relação
  ao que foi pedido ou à stack definida.
- **Mensagens de commit não devem conter URLs privadas nem identificadores
  de sessão** de nenhuma ferramenta de IA (Claude Code, Codex ou outra).
  Commits devem conter apenas informação relevante ao código/projeto. Isto
  vale para commits novos a partir de agora — não é motivo para reescrever
  histórico já existente só para remover um trailer desse tipo.
