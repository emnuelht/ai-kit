# Design (só projetos com interface)

**Um canvas por projeto.** Link em `.ai/design/CANVAS.md` (crie ao fazer o primeiro canvas: url, slug, lista de pranchetas). Toda tela, estado ou interação nova entra nele; outro canvas só se o usuário pedir (não pergunte).

**Com a ferramenta de Artefatos do Claude (tipo "Design"):**
1. Primeira vez: `describe_type` do tipo Design → siga as regras do formato. Crie o canvas (`create_from_type`, título = nome do projeto) **e publique as pranchetas na sequência** — nunca deixe vazio.
2. Arquivos de trabalho em `.ai/design/canvas/project/` (`canvas.json` + `<tela>.dc.html`); publique só os alterados no mesmo canvas.
3. Atualize `.ai/design/CANVAS.md`. Antes de mudar, leia os comentários do usuário no canvas.
4. Use a skill `frontend-design` (se o plugin existir) ou `design-direction`. Versão celular das telas-chave. Tokens em `.ai/design/tokens.md`.

**Sem Artefatos (terminal puro):** copie `extras/canvas-local/` do repositório do kit para `.ai/design/canvas-local/` (clone em `.ai/.kit-src/` se preciso) e siga o README dele.

Código de interface só depois da tela aprovada; siga a prancheta.
