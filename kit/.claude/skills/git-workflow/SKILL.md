---
name: git-workflow
description: Branch, pedido de commit, mensagem e versão MAJOR.MINOR.PATCH. Use antes de mexer em código num repositório git e ao concluir cada mudança.
---
**Sem git:** pergunte uma vez se pode `git init` (+ `.gitignore` com `.env*`, `node_modules/`, `dist/`, `target/`, `.ai/.tools/`, `.ai/.kit-src/`).

**Branch (pela situação):** funcionalidade → `feat/<curto>` · correção → `fix/<curto>` · experimento → `exp/<curto>` · ajuste pequeno em projeto pessoal sem remoto → direto na principal · com remoto/colaboradores → sempre branch. Diga em 1 linha por quê.

**Commit (padrão: perguntar):** ao concluir cada mudança, com testes ok, mostre:
```
Posso commitar?  branch: feat/x · arquivos: 3 · mensagem: feat(x): ... · versão: 1.4.2 → 1.5.0
```
Só com "sim". `git add` só dos arquivos da mudança. Nunca `--amend` em commit enviado, `--no-verify` ou push sem pedido.
Mensagem: `tipo(escopo): resumo` — feat, fix, refactor, perf, test, docs, chore, build, ci, security; `tipo!:` quando quebra compatibilidade.

**Versão (se o projeto tem: package.json, pom.xml, build.gradle, pyproject.toml, VERSION...):**
- quebra compatibilidade → MAJOR · `feat` → MINOR · `fix`/`perf`/`security` → PATCH · docs/test/chore → não muda. Zera à direita.
- Fase 0.x: quebra → MINOR; o resto → PATCH. 1.0.0 só quando o usuário disser.
- Quando: ao juntar a branch na principal (ou a cada commit, se `.ai/project.md` disser). Atualize o arquivo, `CHANGELOG.md` (Adicionado/Corrigido/Alterado) e proponha a tag `vX.Y.Z`.

**Fim da branch:** pergunte se pode juntar (`git merge --no-ff`) e apagar a branch.
