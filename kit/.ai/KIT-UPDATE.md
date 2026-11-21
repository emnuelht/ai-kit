<!-- ai-kit 1.0.0 -->
# Atualizar (ou instalar) o AI Kit neste projeto

Procedimento do comando `/kit-update`. Funciona com qualquer IA que tenha terminal e git.
Uso: `/kit-update` (última versão) · `/kit-update 1.0.0` (versão específica) · `/kit-update verificar` (só mostra o que mudou).

**Princípios:** nunca perder nada do usuário · mostrar antes de aplicar · um "ok" para o plano, uma pergunta por conflito · arquivos que controlam permissões só mudam com confirmação.

## 1. Versão instalada
- Versão instalada: 1ª linha do `.ai/KIT-UPDATE.md` (`<!-- ai-kit X.Y.Z -->`); em kits pré-1.0, a 1ª linha do `AGENTS.md` ou `.ai/KIT_VERSION`.
- Kit pré-1.0 (o projeto tem `.ai/` e `AGENTS.md`/`KIT_VERSION`): as tags antigas não existem no repositório, então **não há base** — todo arquivo do kit diferente do novo conta como "modificado pelo usuário" (mostre o diff e pergunte). Siga as **Notas de migração**.
- Não existe nada do kit → **modo instalação** (seção 7).
- Repositório padrão: `https://github.com/emnuelht/ai-kit`.

## 2. Baixar a fonte
- Sem `.ai/.kit-src/`: `git clone --quiet <repo> .ai/.kit-src` · com: `git -C .ai/.kit-src fetch --quiet --tags origin`.
- Versão alvo: a pedida, senão a tag `vX.Y.Z` mais alta (`git -C .ai/.kit-src tag --sort=-v:refname | head -1`).
- Alvo == instalada → "o kit já está na versão X" e pare.
- Atalhos: `OLD=v<instalada>` (base), `NEW=v<alvo>`. Conteúdo de um arquivo numa versão: `git -C .ai/.kit-src show $NEW:kit/<caminho>`.

## 3. O que mudou
- Mostre ao usuário, em até 10 linhas, as seções do `CHANGELOG.md` entre `OLD` e `NEW` (`git -C .ai/.kit-src show $NEW:CHANGELOG.md`). Itens de **Segurança** primeiro.
- `/kit-update verificar` para aqui.

## 4. Plano arquivo por arquivo
Lista de arquivos: `git -C .ai/.kit-src ls-tree -r --name-only $NEW -- kit/` (novos/atuais) e o mesmo para `$OLD` (para achar removidos). Tire o prefixo `kit/`.
Classifique pela seção **Donos dos arquivos** (no `KIT-UPDATE.md` da versão NEW; versões antigas usavam `.ai/kit-manifest.json`). Caminho exato vence padrão; depois `user` → `merge` → `kit`; não listado → `kit`.

Para cada arquivo, compare três versões: **base** (em OLD), **meu** (no projeto), **novo** (em NEW).

| Grupo | Situação | Ação |
|---|---|---|
| user | qualquer | não tocar |
| kit | não existe no projeto | adicionar |
| kit | meu == novo | nada |
| kit | meu == base | substituir pelo novo (o usuário não mexeu) |
| kit | meu ≠ base | **conflito**: mostrar diff curto e perguntar — manter o meu · pegar o novo · mesclar (`git merge-file meu base novo` em cópias temporárias) |
| kit/merge | existe na base, sumiu no novo | siga as **Notas de migração** abaixo; senão: meu == base → remover; meu ≠ base → mostrar e perguntar |
| merge | — | regra do manifesto (abaixo) |

Regras de `merge`:
- **Agentes** (`.claude/agents/*.md`): do usuário ficam `model`, `effort`, `maxTurns`, `color` e `skills` (união das do usuário com as novas do kit). `tools` e o corpo: merge de 3 vias; se o novo **remover** uma ferramenta de `tools`, aplique (é endurecimento).
- **`.claude/settings.json`**: para `permissions.allow/ask/deny` e `enabledPlugins`: remova entradas que estavam na base e sumiram no novo (o kit retirou — pode ser correção de segurança); adicione as novas do kit; mantenha as do usuário. `hooks`: troque só as entradas cujo comando é do kit (`guard.py`). Outras chaves: do usuário. Valide o JSON.
- **`CLAUDE.md`**: troque só o bloco entre `<!-- ai-kit:start -->` e `<!-- ai-kit:end -->` pelo do kit novo; o resto é do usuário.
- **`.gitignore` do kit**: união de linhas.

## 5. Mostrar o plano e aplicar
Mostre (até 15 linhas): `OLD → NEW`, quantos arquivos serão adicionados / atualizados / removidos / mantidos, os conflitos, e **em destaque** o que mexe em permissões: `.claude/settings.json`, `.claude/hooks/`, `tools:` de agentes, `.mcp.json`.
Peça **um "ok"** para o plano; resolva os conflitos um a um.

Aplicar:
- Escreva com as ferramentas de edição de arquivo (Edit/Write), **não** com `cp`/`mv`/redirecionamento para dentro de `.claude/` — assim as confirmações de segurança do Claude Code aparecem para o usuário (o guard também pergunta nesses casos).
- Remoções: só as listadas no plano aprovado.

## 6. Depois
1. A versão fica registrada na 1ª linha do `.ai/KIT-UPDATE.md` novo. Apague `.ai/KIT_VERSION` e `.ai/kit-manifest.json` antigos, se existirem.
2. Verifique: `python .claude/hooks/guard.py --selftest` (ou `python3`/`py`) termina com `SELFTEST PASS`; `.claude/settings.json` é JSON válido.
3. Registre em `.ai/state/DECISIONS.md`: `<data> | AI Kit OLD → NEW | <resumo de 1 linha>`.
4. Proponha o commit (skill `git-workflow`): `chore(kit): atualiza AI Kit OLD → NEW`.
5. Diga ao usuário: "reabra o Claude Code para hooks e permissões novos valerem".
6. `.ai/.kit-src/` fica (está no `.gitignore`) para a próxima atualização ser rápida.

## 7. Modo instalação (projeto sem o kit)
1. Passo 2 (baixar a fonte, alvo = última tag).
2. Copie tudo de `kit/` (versão NEW) para a raiz do projeto **sem sobrescrever** nada que exista.
3. Ignore a pasta `extras/` do repositório (opcional). Já existia `CLAUDE.md` → acrescente ao final o bloco `<!-- ai-kit:start -->…<!-- ai-kit:end -->` do kit e a linha `@.ai/project.md`. Já existia `.claude/settings.json` → mescle como na regra de `merge` (sem base: só adicionar).
4. Siga para o kickoff (`.ai/KICKOFF.md`).

## Donos dos arquivos
- **user** (nunca tocar): `.ai/project.md`, `.ai/state/**`, `.ai/design/CANVAS.md`, `.ai/design/tokens.md`, `.ai/design/canvas/**`, `.ai/.tools/**`, `.claude/settings.local.json`, `.mcp.json`, `.ai/design/**`
- **merge**: `.claude/settings.json` (listas allow/ask/deny: tire o que o kit tirou, acrescente o novo, mantenha o do usuário; garanta `model: opusplan` e deny `Task`/`Agent`), `CLAUDE.md` (só o bloco do kit), `.ai/.gitignore` (união de linhas)
- **kit**: `.claude/commands/**`, `.claude/skills/{design-direction,git-workflow}/**`, `.claude/hooks/guard.py`, `.ai/KICKOFF.md`, `.ai/SETUP.md`, `.ai/DESIGN.md`, `.ai/KIT-UPDATE.md`, `.ai/settings.kit.json`

## Notas de migração
- **Pré-1.0 → 1.0.0:** sessão única. Remova `.claude/agents/` (agente alterado pelo usuário → mostre e pergunte uma vez) e os comandos que não existem mais. Remova, se não modificados: `.ai/profiles/`, `.ai/sessions/`, `.ai/security/README.md`, `.ai/skills-catalog.md`, `.ai/SKILLS.md`, `.ai/README-KIT.md`, `.ai/templates/`, `.ai/extras/`, `.ai/KIT_VERSION`, `.ai/kit-manifest.json`, `.ai/design/README.md`, `.ai/design/canvas-local/` (exceto `manifest.js`, `screens/`, `feedback.json` se o usuário usou). Em `.ai/project.md` remova `mode:`/`budget:`/`autonomy:`.
