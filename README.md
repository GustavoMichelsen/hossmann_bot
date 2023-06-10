## Projeto Rossmann
O objetivo desse projeto foi fazer a previsão de vendas das lojas para as seis semanas seguintes.

Esse projeto visa ajudar os gestores da empresa a terem uma previsão do faturamento com alta confiabilidade e com isso poderem tomar decisões mais acertadas e com certa antecedência. Com base nessa informação seria possível acionar o time de marketing para melhorar as campanhas ou então diminuir o budget de marketing sem prejuízo para as vendas, por exemplo.

A entrega dessas previsões é feita através do Telegram. O vídeo mais abaixo demonstra o uso, mas você mesmo pode testar adicionando o contato abaixo:

[Telegram](https://t.me/rossmann_predict_bot)

PS: Quando fizer a primeira consulta é possível que demore a responder devido a inicialização do serviço.

[YouTube](https://www.youtube.com/embed/cJpMNjYFM24)

Outros serviços poderiam ser acoplados ao chat do Telegram, como por exemplo previsão de tipo de itens vendidos por loja, previsão geral, gráficos, etc.

A seguir você poderá entender mais a respeito do desenvolvimento desse projeto.

### Detalhes do Projeto

#### Premissas de Negócio – O que se procurou resolver?
O problema fictício abordado foi a necessidade do CEO (Chief Executive Officer) de separar um budget para a reforma das lojas, para isso ele precisaria de uma previsão de vendas por loja das próximas semanas.

### Planejamento da Solução

##### Qual o plano utilizado para resolver o problema?

<ul>
  <li>Coleta dos dados - Fiz no https://www.kaggle.com/;</li>
  <li>Limpeza dos dados – Retirei as linhas com dados faltantes e alterado os tipos onde necessário;</li>
  <li>Criação de novas Features – Criei novas features baseadas nas originais;</li>
  <li>Seleção de colunas – Excluí colunas que eu não iria mais precisar ou de dados que eu não utilizaria;</li>
  <li>Exploração dos dados – Explorei os dados buscando entender o fenômeno e gerar Insigths;</li>
  <li>Preparação dos dados – Preparei os dados para o treinamento dos algoritmos de Machine Learning;</li>
  <li>Seleção das Features mais relevantes – Para isso utilizei o algoritmo Boruta;</li>
  <li>Treinamento dos algoritmos de Machine Learning – Treinei 5 tipos de algoritmos de Machine Learning para poder comprar o desempenho de cada um deles, escolhendo por fim o melhor;</li>
  <li>Ajuste dos hiperparâmetros do modelo – Testei o modelo escolhido com diferentes hiperparâmetros e comparei os resultados;</li>
  <li>Treinamento do modelo de Machine Learning – Treinei o modelo com os hiperparâmetros que apresentaram o melhor desempenho;</li>
  <li>Análise dos resultados – Fiz a previsão do faturamento e comparei os resultados obtidos com os dados originais para descobrir a confiabilidade do modelo;</li>
  <li>Criação do bot no Telegram – Criei e testei o bot para Telegram.</li>
</ul>

### Principais Insights de dados
<ul>
  <li>Lojas com competidores próximos vendem mais;</li>
  <li>Lojas com promoções mais curtas vendem mais. Lojas com promoções muito longas acabam vendendo menos;</li>
  <li>As lojas vendem menos durante feriados.</li>
</ul>

### Resultados financeiros para o negócio

Com a implementação do algoritmo de Machine Learning na previsão de faturamento, O CEO poderá separar o valor que será gasto nas reformas de acordo com a capacidade de cada loja. Além disso, os gestores da empresa poderiam utilizar o algoritmo para tomar medidas preventivas para alavancar as vendas, trazendo assim os resultados esperados para empresa e atingindo as metas de crescimento.

### Lições aprendidas
Uma das principais lições que aprendi durante a confecção deste projeto está ligada ao entendimento da necessidade do negócio e como o projeto de Machine Learning pode realmente trazer resultados financeiros.

O entendimento do negócio é importante para que a solução final realmente atenda a expectativa de quem demandou aquele projeto, já a decisão de fazer o projeto é importante para que ele traga retorno financeiro para empresa, não sendo feito somente por capricho, ou seja, que o projeto traga resultados que não possam acionar decisões na empresa.

### Próximos passos
Entre os próximos passos para a evolução do projeto está a possibilidade de melhorar o chatbot do Telegram, adicionado informações relevantes sobre cada loja.

Outros projetos ligados a este primeiro também poderiam ser desenvolvidos, como a previsão de vendas por produto e por loja para o setor de compra, fazendo com que as lojas tenham estoque realizar as vendas previstas.

### Contatos
<p> Email: gtv.michelsen@gmail.com
<br> Linkedin: <a href="https://www.linkedin.com/in/gustavo-michelsen-30946a223/"> Clique aqui!!! </a> </p>
