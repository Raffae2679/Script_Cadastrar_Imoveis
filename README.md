# Script para cadastrar imóveis 

Script desenvolvido para realizar integração entre um sistema de imobiliaria (Ingaia) e o site desenvolvido pela empresa júnior da escola de ciência e tecnologia (EJECT).

## Problemática:

Os clientes não queriam recadastrar os imoveis no site que a EJECT havia desenvolvido, então pediram para realizar a integração com o ingaia. Quando fomos pesquisar, descobrimos que o ingaia disponibilizava um arquivo xml onde ficava todos os imoveis cadastrados pelo usuário, servindo como um db, que era atualizado toda vez que algo novo era cadastrado.

## Solução:

Sabendo disso, tive orientação de um pós-junior que me indicou usar PANDAS para estar "manuseando e tratando as informações" e junto com o meu diretor, fizemos um planejamento do que precisava ser feito para conseguir fazer esse script.

  **Planejamento**
- Leitura do XML
  - Encontrar biblioteca para importar
  - Entender como funciona o Xtree e Xroot
  - Desenvolver o código para leitura
- Colocar as informações do XML em um data frame
  - Definir as colunas do banco de dados 
  - Atribuir valores as colunas
- Criar as tabelas no banco de dados
  - Importar bibliotecas para acessar postgree
  - Fazer login 
  - Desenvolver uma função para criar objetos no banco e armazenar os valores do data frame
- Verificação dos valores do banco 
  - Desenvolver função que percorra os valores no banco de dados e retorne se o imovel do xml já está cadastrado lá. Caso não, cadastre ele.
- Configuração do Kronos para chamar o arquivo
  - Importar bibliotecas 
  - Definir um horário para executar o script 

Depois desse planejamento, ficou mais claro para onde tinha que seguir e o que deveria ser feito para chegar no resultado final. Então, tive que fazer um curso de pandas para me orientar e entender como funcionava essa lib e no que ela poderia me ajudar. Após isso, tive que quebrar um pouco a cabeça com a leitura do XML, acabou que ele foi um pouquinho complicado, pois não entendia tão bem o funcionamento de algumas funções, entretanto, acabei conseguindo ajuda num grupo de programação, onde um cara me ajudou mandando umas documentações que clarearam bastante.

Cerca de 2 meses depois, eu ainda tava desenvolvendo isso, tentando acertar uns últimos detalhe... Tive um problema com o tipo dos numeros que vinham do data frame para o que era aceito no banco de dados, ai para resolver esse problema, achei em uns foruns uma função do Numpy para resolver esse meu problema e acabou que deu certo.

Após 3 meses, eu consegui finalmente finalizar o script e aplica-lô no site que meu squad havia desenvolvido, foi tudo incrível, ver o script cadastrando mais de mil imoveis em apenas 15 minutos, o que se fosse a gente iria demorar uma semana ou até mais. A melhor parte disso tudo é que o códgio funciona de forma totalmente autonoma, basta executar e ele fará todo o trabalho. Para deixar ele com essa autonomia, fora toda a construção dele, usei um "cronjob" que funciona igual ao kronos, porém tinha suporte no heroku. Bastou  eu criar um arquvio e definir nas minhas informações do deploy e pronto, o script seria executado automaticamente.



