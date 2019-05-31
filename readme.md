

# Objetivo

Esse projeto tem como objeto mostrar como é a implementação de um consumidor de eventos.  No projeto foi contemplado as etapas de consumo e persistência dos dados.

# Considerações de design

A interface de apresentação dos dados foi desenvolvida em angular.js, o gráfico desenvolvido deverá ser atualizado de 1 em 1 minuto. O framework escolhido para o desenvolvimento é FLASK, pois tem suporte com o python.

# Tecnologias escolhidas
Como se trata do consumo de eventos disponibilizados em JSON, foi escolhido o PYTHON para fazer a leitura dos dados, devido a de manipulação de arquivos uma vez que possui bibliotecas de análise como o NUMPY e PANDAS. A camada de  persistência dos dados foi feita no banco de dados SQL Server 2017 que possui suporte para a implementação de rotinas de Machine Learning e um grande comunidade de conhecedores dessa tecnologia.

## Prós e Contras
### PYTHON: 
Prós
	 
	 - Bibliotecas de análise de dados;
	 - Facilidade de escrita do código (normalmente é menor se comparada a outras linguagens);
	 - Suporte para desenvolvimento web;
	 - Recomendada para automação de processos.
Contras

	- Limitações quanto a execução de comandos no sql(Execução apenas de querys em texto)
	- Requer um custo computacional relativamente alto.
	- Abstração de camadas de processamento, isso pode ser um problema se o objetivo for melhorar a performance por exemplo.
### SQL Server 2017:
Prós:

	- Suporte enterprise;
	- Comunidade para compartilhamento de informação;
	- Suporte a Big Data e integração com outros bancos de dados;
	- Processamento in memory;
	- Suporte a PYTHON e R.
Contras

	-Necessita um investimento que pode ser considerado alto se comparado com outros bancos;
	-Compatibilidade com o Linux possui limitações;

## Alternativas para as tecnologias escolhidas
Para a alternativa do python temos o dot net core e o próprio R, depende para o uso, uma vez que estes tem prós e contras assimcom o Python.  Para o consumo de eventos, podemos utilizar o Java uma vez que a grande maioria de exemplos relacionado ao assunto "eventos" estão escritos na linguagem.
Quanto ao MS SQL Server, dependendo do objetivo da empresa temos alternativas como o Oracle, MariaDB ou Postgre SQL. Ai dependerá das necessidades que devem ser supridas.

# Informações complementares
Informações de metadados, estruturas do JSON e estrutura do banco de dados podem ser encontradas nos links abaixo: 

	-https://www.mediawiki.org/wiki/Manual:Recentchanges_table#Schema_summary
	-https://github.com/wikimedia/mediawiki-event-schemas/blob/master/jsonschema/mediawiki/recentchange/2.yaml
		 
