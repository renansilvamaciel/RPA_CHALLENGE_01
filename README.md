## RPA Challenge Automation with Python and Singleton Pattern

Este repositório contém um script Python para automatizar o desafio RPA disponível no site [RPA Challenge][RPA Challenge]. O projeto utiliza o framework  da [Botcity][Botcity] para interagir com o site e implementa o padrão de projeto Singleton para garantir a existência de apenas uma instância do navegador durante a execução.

#### 🚀 Sobre o Projeto

O script automatiza o seguinte processo no site RPA Challenge:

1. Acessa o site RPA Challenge.
2. Faz o download do arquivo CSV contendo os dados.
3. Preenche o formulário com os dados do CSV.
4. Submete o formulário.
5. Extrai e exibe o tempo total de execução e o número de registros inseridos. ( Aguardando implementação)

####  🏛️ Padrão de Projeto Singleton

O padrão Singleton garante que apenas uma instância do navegador seja criada durante toda a execução do script. Isso é crucial para otimizar o desempenho e evitar conflitos de recursos, especialmente ao lidar com automações web.

A classe Input_forms implementa o padrão Singleton, permitindo que o script acesse a mesma instância do navegador em diferentes pontos da execução.

####  ⚙️ Pré-requisitos

- Python 3.x
- botcity-framework-web>=0.8.0,<1.0
- pandas
- Webdriver do Chrome (certifique-se de que o webdriver seja compatível com a sua 		versão do Chrome)

#### 💻 Instalação

1. Clone este repositório:
`git clone https://github.com/seu-usuario/rpa-challenge-automation.git`

2. Instale as dependências:
`pip install -r requirements.txt`

3. Baixe o Webdriver do Chrome compatível com sua versão do Chrome em https://chromedriver.chromium.org/downloads e coloque o executável na pasta do projeto ou em um local no seu PATH.

####  ▶️ Execução

Para executar o script, navegue até o diretório do projeto e execute:

`python bot.py`

📁 Estrutura do Projeto
└── main.py                  # Script principal que executa a automação
└── input_forms.py       # Implementação do padrão Singleton para o navegador
└──pastas_arquivos      # Implementaação funções que interagem com aquivos.
└── requirements.txt    # Arquivo com as dependências do projeto

####  🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request para:

- Implementar melhorias no código.
- Adicionar funcionalidades.
- Corrigir bugs.
- Melhorar a documentação.

####  📝 Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para obter mais detalhes.

[RPA Challenge]: http://https://www.rpachallenge.com/ "RPA Challenge"
[BotCity]: https://github.com/botcity-dev "Botcity"
