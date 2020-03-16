# AnimalFinder

Site testado tanto em Ubuntu 18LTS quanto no windows 10

Você precisará ter instalado em sua máquina:
- python3 (testado com python 3.5 e 3.7)
- django (testado com django 2.2 e 3.0)

Instalação em Linux:

como administrador, instale as dependências:

- (para instalar o python 3): **sudo apt-get install python3**
- (para intalar o django): **pip install django** ou **pip3 install django** dependendo da instalação do seu python3

Execução:

- Clone o repositório para o seu computador, descompacte se necessário
- Vá para a pasta que contém o arquivo manage.py
- Execute o comando: **python manage.py runserver** ou **python3 manage.py runserver** dependendo da instalação do seu python3
- aba um navegador e acesse **127.0.0.1:8000**

Banco de dados:

O site vem com alguns animais e dono pré-cadastrados com o objetivo de verificar as validades exigidas.

Usuários cadastrados:
- Email= a@gmail.com   senha: a
- Email= b@gmail.com   senha: b
- Email= c@gmail.com   senha: c

Usuário administrador: para acessar o banco de dados como administrador (apenas para critérios de análise): vá em
**127.0.0.1:8000/admin** e faça login com os seguintes dados:

email: **guilherme.chiqueti@gmail.com**
senha: **admin**