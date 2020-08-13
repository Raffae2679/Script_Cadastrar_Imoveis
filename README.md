# Script para cadastrar imóveis 

Script desenvolvido para realizar integração entre um sistema de imobiliaria (Ingaia) e o site desenvolvido pela empresa júnior da escola de ciência e tecnologia (EJECT).

## Problematica:

Os clientes não queriam recadastrar os imoveis no site que a EJECT havia desenvolvido, então pediram para realizar a integração com o ingaia. Quando fomos pesquisar, descobrimos que o ingaia disponibilizava um arquivo xml onde ficava todos os imoveis cadastrados pelo usuário, servindo como um db, que era atualizado toda vez que algo novo era cadastrado.

## Solução:

Sabendo disso, tive orientação de um pós-junior que me indicou usar PANDAS para estar "manuseando e tratando as informações" e junto com o meu diretor, fizemos um planejamento do que precisava ser feito para conseguir fazer esse script.

### Planejamento
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


