# Daily-Task (BACKEND)
## O que é o projeto?

O projeto foi concebido com o propósito de aprimorar a organização de um time de desenvolvimento de software, especificamente o grupo de desenvolvedores do laboratório LASIC, no IFCE. Parcialmente inspirado no framework SCRUM, uma das principais funcionalidades do projeto é a Daily. Embora tradicionalmente a Daily seja uma reunião rápida realizada no início do expediente, no LASIC optamos por um formato de dailies escritas. Essa alternativa dispensa encontros presenciais, otimiza o tempo da equipe e gera um registro detalhado das atividades do dia anterior, proporcionando maior transparência e controle sobre o progresso das tarefas.

Com o uso das dailies escritas e a gestão de tarefas (tasks), nosso projeto permite a automatização de várias etapas do trabalho, gerando dashboards e tabelas de forma automática, que refletem os resultados e o desempenho do time de maneira clara e objetiva.
## Diagrama de Entidade Relacionamento
![Blank document(2)](https://github.com/user-attachments/assets/95ac9c54-5eb9-427e-810f-3ddb5f371313)

## Instalação
### Pré-requisitos
#### Arquivos de ambiente
Para instalar o backend do Daily-Task é necessário antes ter no repositório raiz do projeto um .env com as informações necessárias (acesse .env-example para mais detalhes) e na pasta auth é necessário existir o arquivo client_secret.json para realizar a autenticação do Google.
#### Banco de dados
É necessário estar utilizando um banco de dados postgres que terá nome, porta, endereço e nome do banco definido no .env
como por exemplo DATABASE_URL=postgresql://postgres:postgres@localhost:5432/daily_db
### Passo a Passo
#### Clonando repositório
```bash
git clone https://github.com/DAILY-TASK-IFCE/daily-task-backend.git
cd daily-task-backend
```
#### Instalando ambiente
Lembre de garantir que os [pré-requisitos](README.md#Pré-requisitos) estão satisfeitos antes de executar os comandos e que você está no diretório raíz do projeto.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db upgrade
# Talvez o nome de usuário, host e nome do banco de dados varie, verifique antes o que está definido no seu .env
psql -U postgres -h localhost -d daily_db -f init_database.sql
pre-commit install
```
#### Rodando aplicação
Para rodar a aplicação é necessário estár no diretório raíz do projeto e executar o seguinte comando:
```bash
flask run
```
