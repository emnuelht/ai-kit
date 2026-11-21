---
name: api-design
description: Padrões de API REST (recursos, status, paginação, erros, versionamento, OpenAPI). Use ao criar ou alterar endpoints ou contratos entre frontend e backend.
---
- Contrato primeiro: atualize `docs/openapi.yaml` (ou equivalente) antes do código; frontend e backend leem o mesmo contrato.
- Recursos no plural (`/users/{id}/orders`); verbos HTTP corretos; 201 + Location no create; 204 sem corpo.
- Erros no formato ProblemDetail: `type, title, status, detail, instance` + `errors[]` de validação.
- Paginação: `?page=&size=&sort=` com `totalElements`; ou cursor para listas grandes.
- Versionamento: `/api/v1`; nunca quebrar contrato sem nova versão.
- Idempotência em POST sensível (header `Idempotency-Key`); rate limit em auth.
