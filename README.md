# EscolaApp-Web
O objetivo geral da aplicação é fornecer um ambiente que auxilie a diretora da escola no monitoramento dos alunos e repasse de informações aos pais, mantendo atualizados o calendário de eventos, frequências de faltas, notas e mensagens aos pais. O site consiste em uma estrutura MVC, onde temos as classes do dashboard, as telas que são a interface do usuário e os controladores, que interpretam as entradas do usuário e realizam as interações com o banco de dados.   


### Estrutura do Projeto
Django trabalha com App's, sua documentação os define como: “Uma app é uma aplicação web que faz alguma coisa — i.e., um weblog ou uma simples enquete.”. A primeira coisa que precisamos atentar é que App's Django não são exatamente Aplicações Web. No contexto do Django, uma Aplicação WEB está muito mais para um Django Project. É claro que é possível ter um projeto inteiro com apenas uma app, porém a utilização de multiplos app's com funcionalidades específicas torna o projeto muito mais fácil de dar manutenção e muito mais customizavel. Logo nosso projeto é estruturado em dois apps principais:
- Escolappweb: App principal que contem as configurações de todo o projeto
- Accounts: App criado para gerenciamento de login e criação de usuários
- Escolappweb_dashboard: App criado para gerar a interface do usuário, que são os templates na pasta ``Templates/``, controladores que gerenciam a interação do usuário com o banco de dados (``views.py``, ``forms_views.py`` e ``forms.py`` gerenciam a interação nas páginas e formulários respectivamente) e models.py que definem os modelos que estao salvos em nosso banco de dados. As API's para cada objeto no banco de dados são definidas no arquivo ``get_api.py`` onde cada função, quando chamada a partir de sua URL, retorna um objeto JSON para o usuário contendo os dados do modelo solicitado.

Todos os apps também contem um arquivo chamado ``urls.py``, que controlam quais serão as URL's para cada página do aplicativo.

### Instalação em um ambiente Linux

1. Clone o repositório em sua máquina.
2. Crie um ambiente virtual python: ``virtualenv venv venv``
3. Ative seu ambiente virutal: `` source venv/bin/activate``
4. Instale as dependências com o comando: ``pip install -r requirements.txt``
5. Execute o servidor com o comando: ``python manage.py runserver``


## Tecnologias

* [Bootstrap](http://www.dropwizard.io/1.0.2/docs/) - Ferramenta gratuita para desenvolvimento HTML, CSS e JS.
* [Nunjucks](https://mozilla.github.io/nunjucks/) - Linguagem de templates para Javascript
* [Django](https://rometools.github.io/rome/) - Framework para Backend em Python


## Authors

* **Cassiano Maia** - [cassianomaia](https://github.com/cassianomaia)

* **Joao Barbirato** - [joaobarbirato](https://github.com/joaobarbirato)

* **Julia Milani** - [juumilani](https://github.com/juumilani)

