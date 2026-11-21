<!-- ai-kit:start -->
# AI Kit — regras (uma sessão, um agente)

**Início:** `.ai/project.md` com `status: NOVO` → siga `.ai/KICKOFF.md` antes de qualquer código. Senão leia só `.ai/state/HANDOFF.md`. Não explore o repositório para "se situar".

**Sem subagentes.** Todo o trabalho acontece nesta sessão. Não delegue.

**Planejar vs executar (troca de modelo):**
- Difícil → planeje primeiro, em plan mode (no Claude Code com `opusplan` isso usa Opus): arquitetura, modelo de dados, funcionalidade com vários arquivos, bug sem causa clara, decisão difícil de desfazer, design de telas. Se não estiver em plan mode, peça ao usuário: "isso precisa de planejamento — ative o plan mode (Shift+Tab ou /plan)".
- Óbvio → execute direto (Sonnet): ler, buscar, editar, renomear, ajustar estilo, testes simples, seguir um plano aprovado.
- Planeje no **começo** da funcionalidade, com o contexto ainda pequeno (trocar de modelo no meio de uma conversa longa reprocessa tudo).

**Economia:**
- Busque antes de ler (`grep`/`glob`) e leia só o trecho. Nunca `node_modules`, `dist`, `build`, `target`, lockfiles, binários.
- Saídas filtradas (`| tail -30`). Respostas curtas; mostre diffs, não arquivos inteiros.
- `TASKS.md`: 1 linha por tarefa; concluídas → `.ai/state/archive/`. `HANDOFF.md` ≤ 15 linhas.
- Funcionalidade concluída → atualize o HANDOFF e sugira `/clear` + `/resume`.

**Interface:** antes do código, desenhe no canvas único do projeto (regras em `.ai/DESIGN.md`; um só, toda tela nova entra nele). Backend/CLI: texto basta.

**Git:** branch pela situação; **pergunte antes de cada commit**; versão MAJOR.MINOR.PATCH; push só se pedirem (skill `git-workflow`).

**Segurança:** nunca ler/commitar segredos; nada destrutivo sem confirmação; `.claude/settings*`, `.claude/hooks/`, `.mcp.json` e scripts só mudam com confirmação.

**Ambiente:** falta algo instalado → `/setup` (o usuário não precisa saber instalar). Atualizar o kit → `/kit-update`.
<!-- ai-kit:end -->

@.ai/project.md
