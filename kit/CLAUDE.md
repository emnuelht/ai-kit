<!-- ai-kit:start -->
# AI Kit — regras (uma sessão, um agente)

**Início:** `.ai/project.md` com `status: NOVO` → siga `.ai/KICKOFF.md` antes de qualquer código. Senão leia só `.ai/state/HANDOFF.md`. Não explore o repositório para "se situar".

**Sem subagentes.** Todo o trabalho acontece nesta sessão. Não delegue.

**Modelo:** quem escolhe é o usuário (`/model`). Nunca troque, sugira trocar nem peça plan mode por conta própria; trabalhe com o modelo da sessão.

**Planejar vs executar:** coisa difícil (arquitetura, modelo de dados, funcionalidade com vários arquivos, bug sem causa clara, decisão difícil de desfazer, design de telas) → antes do código, escreva um plano curto e espere o "ok". Coisa óbvia (ler, buscar, editar, ajustar estilo, seguir plano aprovado) → faça direto.

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
