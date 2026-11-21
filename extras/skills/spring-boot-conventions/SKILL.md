---
name: spring-boot-conventions
description: Convenções para código Java/Spring Boot (camadas, DTOs, validação, exceções, testes). Use ao escrever ou revisar código Java/Spring.
---
- Pacotes por funcionalidade (`feature/controller|service|repository|dto`), não por camada global.
- Controller fino: valida (`@Valid`), chama service, retorna DTO. Nunca expor entidade JPA.
- DTOs como `record`; mapeamento explícito (MapStruct ou método estático).
- Erros: exceções de domínio + `@RestControllerAdvice` retornando `ProblemDetail` (RFC 9457).
- Transação no service (`@Transactional` só onde precisa; `readOnly = true` em leitura).
- Injeção por construtor (`final` + `@RequiredArgsConstructor` ou construtor explícito).
- Config por `@ConfigurationProperties`; segredos só por env.
- Testes: unitário de service com Mockito; `@WebMvcTest` p/ controller; `@DataJpaTest` ou Testcontainers p/ repositório.
- Evitar N+1: `@EntityGraph`/fetch join; paginação com `Pageable`.
