# apps/web

Frontend do ACE (Affiliate Content Engine).

**Status:** ainda não iniciado. Este diretório existe apenas para reservar o
lugar do app na estrutura do monorepo (Etapa 1A — bootstrap).

Stack planejada (ver `docs/adr/0003-tech-stack-v1.md`):

- Next.js + React + TypeScript
- Tailwind CSS + shadcn/ui
- TanStack Query (data fetching)
- Zod (validação)
- Vitest + React Testing Library (testes)
- Playwright (E2E, futuro)

A inicialização do projeto Next.js (scaffolding, `package.json`,
dependências) será feita em uma etapa posterior, não na Etapa 1A.
