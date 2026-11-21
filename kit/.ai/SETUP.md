Objetivo: o usuário NÃO precisa instalar nada nem saber comandos. Você detecta, instala e verifica. Fale com ele em linguagem simples.
Alvo: o argumento do `/setup` (vazio = básico + o que `.ai/project.md` pedir; "completo" = tudo da tabela).

## 1. Já está pronto?
Se `.ai/state/ENV.md` existe, tem `guard: ativo` e o alvo não pede nada novo → mostre 3 linhas de resumo e pare.

## 2. Detectar
- Sistema: `uname -s` → Linux | Darwin (macOS) | MINGW*/MSYS*/CYGWIN* (Windows).
- Para cada ferramenta: `command -v <nome>` e `--version`. No Windows, Python pode ser `py` ou `python`; ignore o atalho falso da Microsoft Store (se `python --version` falhar, trate como ausente).

## 3. O que instalar
- **Básico (sempre):** git, python (o guard depende dele).
- **Pelo projeto:** stack Node/React → node · Java/Spring → JDK 21 + maven · nível de segurança padrão/alto → semgrep, pip-audit, gitleaks, trivy · pentest → docker.
- Liste em 1 bloco curto o que vai instalar e por quê, e peça **um único "ok"**. Avise: "o Windows pode abrir uma janela pedindo permissão — clique em Sim" / "o Mac pode abrir uma janela de instalação — clique em Instalar".

## 4. Comandos de instalação (use EXATAMENTE estes — são os que o guard libera sem perguntar)

| ferramenta | Windows (winget) | macOS (brew, se existir) | Linux |
|---|---|---|---|
| python | `winget install -e --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements` | `brew install python@3.12` · sem brew: `xcode-select --install` (abre janela) | quase sempre já vem; se faltar, ver §6 |
| git | `winget install -e --id Git.Git --accept-package-agreements --accept-source-agreements` | `brew install git` · sem brew: `xcode-select --install` | ver §6 |
| node | `winget install -e --id OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements` | `brew install node` | ver §6 |
| JDK 21 / maven | `winget install -e --id EclipseAdoptium.Temurin.21.JDK ...` / `Apache.Maven` | `brew install openjdk@21` / `brew install maven` | prefira `./mvnw` do projeto |
| gitleaks / trivy | `winget install -e --id Gitleaks.Gitleaks ...` / `AquaSecurity.Trivy` | `brew install gitleaks` / `brew install trivy` | `docker pull zricethezav/gitleaks` / `docker pull aquasec/trivy` |
| semgrep, pip-audit | **todos os sistemas, sem admin:** `python -m venv .ai/.tools` e depois `.ai/.tools/bin/pip install -U pip semgrep pip-audit` (Windows: `.ai/.tools/Scripts/pip.exe ...`). Use depois como `.ai/.tools/bin/semgrep` / `.ai/.tools/Scripts/semgrep.exe`. |
| zap (pentest) | `docker pull ghcr.io/zaproxy/zaproxy:stable` | idem | idem |

Docker Desktop é pesado e pede reinício: só sugira se o usuário quiser pentest/gitleaks/trivy no Linux; nesse caso explique e deixe ele decidir.

## 5. Depois de instalar
- **Windows/macOS:** programas recém-instalados só entram no PATH numa sessão nova. Se `command -v` ainda não achar, diga: "feche e abra o Claude Code (ou o terminal) e mande `/setup` de novo" — e registre isso em Pendências.
- Rode `python .claude/hooks/guard.py --selftest` (ou `python3`/`py`) → precisa terminar com `SELFTEST PASS`.
- **Teste do guard real:** rode `echo AI_KIT_GUARD_CANARY`.
  - Se foi **bloqueado** com "CANÁRIO OK" → `guard: ativo`.
  - Se **imprimiu** o texto → `guard: inativo` (geralmente Python fora do PATH do Claude Code → peça para reabrir). Enquanto isso, as regras do settings.json continuam protegendo o básico.

## 6. Quando precisar de senha de administrador (Linux sem o pacote, Mac sem brew)
Você não consegue digitar senha. Explique em 1 frase e dê **um único comando** para o usuário colar no terminal dentro do Claude Code com `!` na frente (ex.: `! sudo apt install -y python3 python3-venv git`). Depois continue sozinho.

## 6b. Plugins (mínimo)
Cada plugin ocupa contexto em toda sessão. Projeto com interface → só `frontend-design`: `claude plugin install frontend-design@claude-plugins-official --scope project` (o guard libera). Nada mais por padrão; `context7`, `playwright` etc. só se o usuário pedir, e desligue depois. Registre em `ENV.md` e peça `/reload-plugins`.

## 7. Registrar
Grave `.ai/state/ENV.md` curto: `verificado_em`, `sistema`, `guard: ativo|inativo`, uma linha por ferramenta (`nome: ok versão` / `falta`), plugins e pendências. Resumo final ao usuário: até 5 linhas, sem jargão.
