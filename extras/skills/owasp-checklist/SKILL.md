---
name: owasp-checklist
description: Checklist OWASP Top 10 / ASVS e modelos de relatório de auditoria e pentest. Use ao revisar segurança de código, ao testar a aplicação ou ao escrever relatórios em .ai/security/.
---
# Checklist OWASP (resumido para revisão de código)

| Categoria | O que procurar no código | Correção típica |
|---|---|---|
| A01 Controle de acesso | endpoint sem checagem de dono/papel; ID vindo do cliente usado direto (IDOR); rotas admin expostas | checar autorização no servidor por recurso; deny by default |
| A02 Criptografia | senha sem bcrypt/argon2; MD5/SHA1; segredos no código; HTTP sem TLS | argon2id/bcrypt; segredos em env/secret manager; HSTS |
| A03 Injeção | concatenação em SQL/JPQL/NoSQL; `Runtime.exec`/`child_process` com entrada; `dangerouslySetInnerHTML`; templates sem escape | queries parametrizadas; allowlist; escape/sanitização (DOMPurify) |
| A04 Design inseguro | sem rate limit em login/reset; fluxos sem limite de tentativa; lógica de negócio confiando no cliente | rate limit, validação no servidor, threat model |
| A05 Configuração | CORS `*` com credenciais; stack trace em produção; debug ligado; headers ausentes (CSP, X-Frame-Options) | config por ambiente; headers de segurança |
| A06 Componentes vulneráveis | libs desatualizadas com CVE | atualizar; `npm audit`/`pip-audit`/dependency-check/trivy |
| A07 Autenticação | JWT sem expiração, `alg: none`, segredo fraco; sessão sem rotação; cookies sem HttpOnly/Secure/SameSite | expiração curta + refresh; validar alg; flags de cookie |
| A08 Integridade | desserialização de dados não confiáveis; CI baixando scripts sem verificação | formatos seguros (JSON); pin de versões e checksums |
| A09 Logs | sem log de eventos de segurança; logs com senha/token/PII | log de auth/acesso negado; mascarar dados |
| A10 SSRF | servidor busca URL vinda do usuário | allowlist de hosts; bloquear IPs internos/metadata |
| Extra | upload sem validar tipo/tamanho; path traversal (`../`); mass assignment; CSRF em form com cookie | validar MIME/tamanho e salvar fora do webroot; normalizar caminho; DTOs explícitos; token CSRF/SameSite |

Spring Boot: conferir `SecurityFilterChain`, `@PreAuthorize`, `permitAll()` amplo demais, Actuator exposto, `spring.jpa.show-sql` em prod.
React: tokens em localStorage (prefira cookie HttpOnly), `dangerouslySetInnerHTML`, URLs `javascript:` em href, chaves de API no bundle.

## Modelo de relatório (AUDIT / PENTEST)

```
# <AUDIT|PENTEST> — <projeto> — <data>
Escopo: ... | Ferramentas: ... | Commit: <hash>
## Resumo: CRÍTICA n · ALTA n · MÉDIA n · BAIXA n
## Achados
### [ALTA] <título> — <categoria OWASP>
- Onde: arquivo:linha (ou endpoint)
- Impacto: ...
- Evidência/PoC: (1 requisição ou trecho; segredos mascarados)
- Correção: ...
- Teste de regressão: ...
## Fora do escopo / não testado
```
