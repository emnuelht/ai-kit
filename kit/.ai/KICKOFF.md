# Kickoff — perguntas antes de qualquer código

**Passo 0 (sem perguntar):** `.ai/state/ENV.md` ausente ou `guard: inativo` → `/setup` básico. `CLAUDE.md` do usuário sem o bloco `<!-- ai-kit:start -->` → acrescente o bloco do kit e `@.ai/project.md`. `.claude/settings.json` pré-existente → mescle as regras de `.ai/settings.kit.json` (só adicionar). Projeto com código → olhe só a estrutura (2 níveis) e o `package.json`/`pom.xml`.

**Perguntas (1 bloco, múltipla escolha se houver; "decide você" = ★):**
1. O que vamos construir e o que a v1 precisa fazer (até 3 itens)?
2. Você é ★ dev (programa junto) · leigo (explique simples)
3. Stack (sugira se não souber) · roda ★ local · online · celular
4. Referências visuais? (só se tiver interface)

**Depois:** preencha `.ai/project.md` (curto), resuma em ≤ 6 linhas e peça um "ok" (inclui instalar o que a stack pedir via `/setup`). Próximo passo:
- Com interface → planeje o design e desenhe as telas no canvas (`.ai/DESIGN.md`); `status: DESIGN`.
- Sem interface → planeje a v1, gere o `TASKS.md` (1 linha por tarefa); `status: BUILD`.
