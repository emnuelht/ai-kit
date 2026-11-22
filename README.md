# AI Kit

**Descompacte na pasta do projeto, abra o Claude Code e mande um "oi".** A IA prepara o computador, faz as perguntas certas, desenha as telas num canvas que você vê e edita, divide o trabalho entre agentes especializados e pede sua autorização antes de cada commit.

> 🇺🇸 *A lightweight drop-in kit for Claude Code: onboarding questions before any code, a single session where you choose the model, a visual design canvas, token-saving rules, a safety guard hook, and git/semver workflow. Docs in Portuguese.*

---

## Por que usar

| Sem o kit | Com o kit |
|---|---|
| A IA sai codando antes de entender o que você quer | Kickoff curto com perguntas primeiro |
| Contexto enchendo e tokens indo embora | ~750 tokens fixos, sem subagentes nem plugins pesados, estado em arquivo curto |
| Modelo caro fazendo tudo | Você decide o modelo (`/model`); a IA não troca por conta própria |
| Design decidido por texto | Canvas visual (Artefatos › Design do Claude) com todas as telas, antes do código |
| "Instala isso aí" — e o usuário não sabe | A própria IA instala o que falta (Python, Git, Node, ferramentas de segurança, plugins) |
| Comandos perigosos passam | Guard bloqueia `rm -rf /`, `push --force`, `curl \| sh`, leitura de `.env`, pentest fora do escopo; pede aprovação para pacote desconhecido |
| Commits aleatórios | Branch pela situação, pergunta antes de cada commit, versão MAJOR.MINOR.PATCH automática |

## Começo rápido

Escolha um jeito:

**A) Zip (mais simples)**
1. Baixe o **`ai-kit.zip`** em [Releases](../../releases/latest).
2. Descompacte **na raiz do seu projeto** (pasta vazia ou projeto existente). Já tem `CLAUDE.md` ou `.claude/settings.json`? **Não substitua** esses dois — a IA integra o kit a eles.
3. Abra o Claude Code na pasta e mande qualquer mensagem.

**B) Pedindo para a IA instalar** — abra o Claude Code na pasta do seu projeto e diga:
> instale o AI Kit de https://github.com/emnuelht/ai-kit neste projeto seguindo kit/.ai/KIT-UPDATE.md (modo instalação)

Não precisa instalar nada antes: na primeira conversa a IA roda o `/setup`, mostra o que vai instalar e pede um único "ok".

## Como fica dentro do seu projeto

O kit não mexe no seu código; ele ocupa poucos arquivos na raiz:

```
meu-site/
├── index.html, src/, assets/   ← seu projeto
├── CLAUDE.md                   ← regras do kit (bloco delimitado) + import do project.md
├── .claude/                    ← settings (permissões), guard, 5 comandos, 2 skills
└── .ai/
    ├── project.md              ← o que é o projeto (preenchido no kickoff)
    ├── state/HANDOFF.md        ← onde parou
    ├── state/TASKS.md          ← tarefas (1 linha cada)
    └── KICKOFF · SETUP · DESIGN · KIT-UPDATE .md   ← lidos só quando usados
```

Versione tudo no git, inclusive `.ai/`. Opcionais (canvas no navegador, skills de segurança e de stack, MCPs) ficam na pasta [`extras/`](extras/) deste repositório e não vão no zip.

## Atualizar

Dentro do projeto: **`/kit-update`** (ou `/kit-update verificar` para só ver o que mudou). A IA baixa a versão nova, mostra o CHANGELOG e monta um plano: seus arquivos nunca são tocados, arquivos do kit que você não alterou são atualizados, os que você alterou viram pergunta, e agentes/settings/CLAUDE.md são mesclados mantendo suas escolhas. Detalhes em [`kit/.ai/KIT-UPDATE.md`](kit/.ai/KIT-UPDATE.md).

## Como um projeto anda

```
perguntas → plano → telas no canvas → execução → /commit → /handoff
```

## Uma sessão, você escolhe o modelo

- **Sem subagentes** (bloqueados nas permissões): todo o trabalho acontece na sessão principal, sem ninguém relendo o projeto do zero.
- **Modelo é decisão sua:** o kit não define nem troca modelo. Use `/model` quando quiser (por exemplo, Opus para projetar, Sonnet para executar). Em tarefas difíceis a IA só escreve um plano curto e espera o seu "ok".
- **~750 tokens fixos** por sessão e nenhum plugin ligado por padrão.

## Comandos

`/setup` · `/commit` · `/handoff` · `/resume` · `/kit-update`

## Funciona com

- **Claude Code** — completo (comandos, hooks, skills).
- **Claude app com Artefatos** — o canvas de design abre nos seus Artefatos.

Testado em Linux e Windows (Git Bash). macOS segue os mesmos caminhos (Homebrew / Xcode CLT).

## Limitações conhecidas

- O canvas **Design** só existe em sessões com acesso aos Artefatos do Claude; no terminal puro use o canvas local de [`extras/`](extras/).
- Janelas de permissão do sistema (UAC do Windows, instalador do macOS) e senha de `sudo` no Linux precisam de você.
- Alguns plugins pedem confirmação de um comando de instalação que só pode ser aceita no seu terminal.

## Estrutura do repositório

```
kit/                 ← o que vai para dentro do seu projeto (é o conteúdo do ai-kit.zip)
extras/              ← opcionais, copiados à mão quando precisar
.github/workflows/   ← CI (testes do guard) e release (gera o zip a cada tag)
CHANGELOG.md
```



## Contribuindo

Issues e PRs são bem-vindos. Antes de abrir PR:

```bash
python kit/.claude/hooks/guard.py --selftest   # precisa terminar com SELFTEST PASS
```

Mudou uma regra de agente ou comando? Teste num projeto real e descreva no PR o que a IA fez antes e depois.

## Licença

[MIT](LICENSE)
