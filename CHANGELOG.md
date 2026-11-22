# Changelog

Formato: [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) · Versão: [SemVer](https://semver.org/lang/pt-BR/).

## [1.1.0] - 2026-11-22
### Alterado
- **O usuário escolhe o modelo.** O kit não define mais `model: opusplan` e a IA não troca de modelo, não sugere trocar nem pede plan mode. Em tarefa difícil ela escreve um plano curto e espera o "ok".
- `/kit-update` com nota de migração 1.0.x → 1.1.0.

## [1.0.0] - 2026-11-21
### Adicionado
- Kickoff com perguntas antes de qualquer código (`.ai/KICKOFF.md`).
- Sessão única, sem subagentes (`Task`/`Agent` bloqueados) .
- Custo fixo de ~750 tokens por sessão: `CLAUDE.md` curto com as regras (bloco `ai-kit`), 5 comandos (`/setup`, `/commit`, `/handoff`, `/resume`, `/kit-update`) e 2 skills (`git-workflow`, `design-direction`).
- Guard (hook PreToolUse): bloqueia comandos destrutivos, libera só instalações conhecidas e pede confirmação para origens alternativas e escritas em arquivos de permissão; autoteste com 49+ casos.
- `/setup`: a IA detecta o sistema e instala o que falta (Python, Git, Node, JDK…).
- Canvas de design único por projeto (Artefatos › Design do Claude); canvas local de reserva em `extras/`.
- Fluxo de Git: branch pela situação, pergunta antes de cada commit, versão MAJOR.MINOR.PATCH, CHANGELOG e tag.
- `/kit-update`: atualiza o kit sem perder arquivos do usuário (3 vias), com notas de migração de kits pré-1.0.
- `.ai/` com 9 arquivos; opcionais (canvas local, skills de stack/segurança, exemplo de MCP) em `extras/`, fora do zip.
- Só Claude Code.
