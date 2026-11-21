---
name: threat-model
description: Modelagem de ameaças STRIDE leve para uma funcionalidade ou sistema. Use no planejamento de features sensíveis (login, pagamentos, uploads, dados pessoais, integrações) ou quando pedirem threat model.
---
# Threat model leve (STRIDE) — 15 minutos, não um tratado

1. **Desenhe o fluxo** em texto: atores → componentes → armazenamentos → fronteiras de confiança.
2. **Ativos**: o que um atacante quer (dados, contas, dinheiro, disponibilidade).
3. **STRIDE por fronteira de confiança**:
   - Spoofing (se passar por outro) · Tampering (alterar dados) · Repudiation (negar ação)
   - Information disclosure (vazar) · Denial of service · Elevation of privilege
4. Para cada ameaça relevante: probabilidade (B/M/A) × impacto (B/M/A) → mitigação concreta → vira tarefa no TASKS.md.
5. Salve em `.ai/security/THREAT-MODEL.md` (máx. 1 página). Atualize quando a arquitetura mudar.
