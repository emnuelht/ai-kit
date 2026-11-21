# Escopo de teste de segurança (regras de engajamento)
# O pentester só testa o que está aqui. O guard bloqueia qualquer alvo fora desta lista,
# e mesmo dentro dela cada ferramenta de pentest pede sua aprovação antes de rodar.

autorizado_por: <seu nome — confirmo que sou dono/autorizado a testar estes alvos>
data: <AAAA-MM-DD>
validade: <AAAA-MM-DD>

alvos:
  - localhost
  - 127.0.0.1

limites:
  - sem DoS / flood; máx. 10 req/s
  - sem força bruta em contas reais; usar apenas contas de teste
  - rotas proibidas: <ex.: /admin/delete-all, webhooks de pagamento>
  - serviços de terceiros (pagamento, e-mail, OAuth) fora do escopo

contas_de_teste:
  - <usuario_comum_teste>
  - <usuario_admin_teste>
