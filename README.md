# ControleFo · Portfólio

Sistema Flask para registrar, homologar e consultar ocorrências, com perfis de acesso e exportação. O banco local é criado pelas migrações. O script de demonstração usa identidades fictícias.

1. Copie `.env.example` para `.env`. Gere uma chave com `python -c "import secrets; print(secrets.token_hex(32))"` e preencha `SECRET_KEY`.
2. Execute `docker compose up --build -d`.
3. Execute `docker compose exec app sh`, defina `DEMO_ADMIN_PASSWORD` com uma senha de pelo menos 12 caracteres e rode `python seed.py` no contêiner.
4. Abra http://localhost:5000 e entre como `9000000001`.

## Interface

O painel apresenta os indicadores disponíveis para o perfil conectado. A navegação organiza lançamento, homologação, histórico e exportação conforme as permissões da conta. Em telas menores, o menu fica recolhido e as tabelas de homologação podem ser roladas horizontalmente.
