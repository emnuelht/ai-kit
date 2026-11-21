---
name: react-ts-conventions
description: Convenções para React + TypeScript (componentes, estado, dados, formulários, testes). Use ao escrever ou revisar frontend React/TS.
---
- `strict: true`; sem `any` (use `unknown` + narrowing). Tipos de API gerados/centralizados em `src/api/types.ts`.
- Componentes pequenos e funcionais; pastas por funcionalidade (`features/<x>/`).
- Dados do servidor com TanStack Query (cache, loading, erro); estado local com `useState`; global só se necessário (Zustand/Context).
- Formulários: React Hook Form + Zod (o mesmo schema valida e tipa).
- Todo componente de dados trata: carregando, vazio, erro.
- Estilo segue `.ai/design/tokens.md` (CSS vars ou tema Tailwind).
- Acessibilidade: elementos semânticos, label em todo input, foco visível.
- Testes: Vitest + Testing Library (comportamento, não implementação); Playwright para fluxos críticos.
- Segurança: nada de token em localStorage, nada de segredo no bundle, evitar `dangerouslySetInnerHTML`.
