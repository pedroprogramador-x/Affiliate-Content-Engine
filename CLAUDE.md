# CLAUDE.md

Este arquivo é a referência específica para sessões do Claude Code neste
repositório. As regras de projeto, princípios arquiteturais e stack estão
em [`AGENTS.md`](./AGENTS.md) — leia-o primeiro; ele é a fonte de verdade
compartilhada entre qualquer agente de IA. Este arquivo só existe para
notas específicas do Claude Code que não fazem sentido em `AGENTS.md`.

## Notas específicas para Claude Code

- Trate cada "Etapa" mencionada nas instruções da tarefa como um limite
  rígido de escopo. Ao final da etapa pedida, pare, resuma o que foi
  feito e aguarde revisão explícita antes de iniciar a próxima etapa —
  mesmo em modo autônomo.
- Antes de qualquer comando que possa descartar trabalho (`git reset
  --hard`, `git clean -f`, `git checkout -- .`, etc.), rode `git status`
  e confirme que não há mudanças não relacionadas em risco.
- Ao criar ou alterar arquivos de configuração sensível (`.env.example`,
  workflows de CI, scripts de deploy), nunca inclua segredos reais —
  apenas placeholders vazios ou de exemplo.
- Sempre que uma tarefa envolver decisão arquitetural nova (nova
  dependência relevante, novo padrão, mudança na stack definida em
  `docs/adr/0003-tech-stack-v1.md`), registre um ADR em `docs/adr/` como
  parte da própria tarefa, não como follow-up.
- Ao terminar uma tarefa que altera arquivos, rode as validações
  disponíveis no momento (ex.: `git diff --check` para whitespace/conflitos,
  linters e testes assim que os apps existirem) e reporte os resultados
  explicitamente, mesmo que "não há validação aplicável ainda".
- A política de push está em `AGENTS.md` (push normalmente exige
  autorização; exceção apenas para persistir trabalho na própria branch
  da tarefa, em ambiente remoto efêmero, nunca em `main`). Quando essa
  exceção for usada, informe branch e SHA no relatório final.
- Mensagens de commit não devem conter URLs privadas ou identificadores de
  sessão (Claude Code, Codex ou qualquer outra ferramenta) — apenas
  informação relevante ao código/projeto.
