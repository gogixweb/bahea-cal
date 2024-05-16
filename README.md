# Bahea Calendar 🇺🇸

Bahea Calendar is a project that adds the standings of your favorite soccer team games to your google calendar!

## How to run

To run the Bahea Calendar, follow these steps:

**1. Make sure you have Python version 3.8+ and pdm installed on your machine.**

For more details acess:
[PDM Project](https://pdm-project.org/en/stable/)
[Python Official](https://www.python.org/)

**2. Acess the Google Calendar API.**

To acess the Google Calendar API, you must create a project. You can create a project by going to the [Developer Console](https://console.developers.google.com/)

- Enable the Google Calendar API;

- Create a client ID;

- Under _Authorized JavaScript origins_ configure this URI:

```
http://localhost:800
```

- Under _Authorized redirect URIs_ configure this URI:

```
http://localhost:8000/calendar/redirect
```

- Create a _secret.json_ file in the _webapp_ folder and insert the credentials you downloaded previously, as show in the following example:

```
{
    "dev/google/calendar": {YOUR GOOGLE CREDENTIALS}
}
```

**3. Clone this repository to your local environment.**

```
git clone https://github.com/gogixweb/bahea-cal.git
```

**4. Create a new virtual environment named `.venv` in the project folder:**

```
pdm venv create
```

**5. Activate the virtual environment:**

```
pdm use
```
Select the virtual environment located in the root folder of the project.

**6. Install the project dependencies from the file `pyproject.toml`:**

```
pdm install
```

**7. Create a .env file in the project root**

**8. Insert the environment variables into the .env file and edit them according to your needs:**

```
DJANGO_DEBUG=true
DJANGO_SECRET_KEY="anyonestring"
DJANGO_ALLOWED_HOSTS="*"
DJANGO_BASE_URL="http://localhost:8000"
DJANGO_DATABASES__default__ENGINE="django.db.backends.sqlite3"
DJANGO_DATABASES__default__NAME="/path/to/your/project/bahea-cal/db.sqlite3"
DJANGO_ENVIRONMENT="dev"
DJANGO_CALENDAR_NAME_PREFIX="(dev) "
```

**9. Apply database migrations:**

```
python manage.py migrate
```

**10. Collect static files:**

```
python manage.py collectstatic
```

**11. Execute the project:**

```
python manage.py runserver
```
## How to add new dependencies to the project:

**1. Activate the pdm virtual environment:**

```
pdm use
```

**2. Add a new dependency:**

```
pdm add -d <dependency_name>
```

**3. Install the new dependency:** 

```
pdm install
```

**4. Check that the dependency has been installed correctly:**
```
pdm show <dependency_name>
```

**5. Export the new dependency to the project:**
```
pdm export -d -o requirements-dev.txt --without-hashes
```

# Bahea Calendar 🇧🇷

O Bahea Calendar é um projeto que permite adicionar a agenda de jogos do seu time do coração ao seu calendário do Google!

## Como rodar o projeto

Para executar o Bahea Calendar, siga estas etapas:

**1. Certifique-se de ter o Python3 e o pdm instalados na sua máquina.**

Para mais detalhes acesse:
[PDM Project](https://pdm-project.org/en/stable/)
[Python Official](https://www.python.org/)


**2. Acesse a API do Google Calendar.**

É preciso criar um projeto para acessar a API do google calendar. Você pode criar acessando o [Console de Desenvolvedores](https://console.developers.google.com/)

- Ative a API do Google Calendar

- Crie uma client ID

- Em _Origens JavaScript autorizada_ configure a seguinte URI:

  ```
  http://localhost:8000
  ```

- Em _URIs de redirecionamento autorizados_ configure a seguinte URI:

  ```
  http://localhost:8000/calendar/redirect
  ```

- Navegue até a Tela de permissão OAuth e adicione um usuário de teste.

- Faça o download do arquivo JSON das suas credenciais

- Crie um arquivo _secrets.json_ na pasta _webapp_ e insira as credenciais que você baixou anteriormente, conforme o exemplo a seguir:

  ```
  {
  "dev/google/calendar": {SUAS CREDENCIAIS GOOGLE}
  }
  ```

**3. Clone este repositório para o seu ambiente local.**

```
git clone https://github.com/gogixweb/bahea-cal.git
```

**4. Crie um ambiente virtual chamado `.venv` na pasta do projeto:**

```
pdm venv create
```

**5. Ative o ambiente virtual:**

```
pdm use
```

Selecione o ambiente virtual localizado da pasta raiz do projeto.

**6. Instale as dependências do projeto do arquivo `pyproject.toml`:**

```
pdm install
```

**7. Crie um arquivo `.env` na pasta raiz do projeto.**

**8. Insira as variáveis de ambiente no arquivo `.env` e personalize conforme sua necessidade:**

```
DJANGO_DEBUG=true
DJANGO_SECRET_KEY="qualquerstring"
DJANGO_ALLOWED_HOSTS="*"
DJANGO_BASE_URL="http://localhost:8000"
DJANGO_DATABASES__default__ENGINE="django.db.backends.sqlite3"
DJANGO_DATABASES__default__NAME="/caminho/para/o/projeto/bahea-cal/db.sqlite3"
DJANGO_ENVIRONMENT="dev"
DJANGO_CALENDAR_NAME_PREFIX="(dev) "
```

**9. Aplique as migrações do banco de dados:**

```
python manage.py migrate
```

**10. Colete os arquivos estáticos:**

```
python manage.py collectstatic
```

**11. Execute o projeto:**

```
python manage.py runserver
```

## Como adicionar novas dependências ao projeto:

**1. Ative o ambiente virtual do pdm:**

```
pdm use
```

**2. Adicione a nova dependência ao pdm:**

```
pdm add -d <nome_da_dependencia>
```

**3. Instale a nova dependência:** 

```
pdm install
```
**4. Verifique se a dependência foi instalada corretamente:**
```
pdm show <nome_da_dependencia>
```
**5. Exporte a dependência para o projeto:**
```
pdm export -d -o requirements-dev.txt --without-hashes
```