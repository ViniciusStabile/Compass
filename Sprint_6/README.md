# Resumo da Sprint 6 – Continuação de Analytics na AWS e Glue Getting Started

Nesta etapa da formação, avancei no domínio de soluções analíticas serverless da AWS com foco em **governança de dados, arquitetura Lake House** e **pipelines ETL com AWS Glue**. Os cursos realizados nesta sprint fortaleceram minha capacidade de criar fluxos de dados escaláveis e bem estruturados na nuvem.

---

## AWS Skill Builder: Fundamentals of Analytics on AWS – Part 2 (Português)

- Fundamentos de **data lakes** e **data warehouses**, seus benefícios e arquiteturas.
- Criação de data lakes com **AWS Lake Formation**, com foco em governança e segurança.
- Vantagens do **Amazon Redshift** para data warehousing moderno (serverless, ETL zero, ML).
- Pilares da arquitetura de dados moderna: escalabilidade, acesso unificado, governança e custo-benefício.
- Conceitos de **data mesh**, **dados como produto** e uso do **Amazon DataZone**.
- Casos de uso reais de analytics por setor e arquiteturas de referência com serviços da AWS.

---

## AWS Glue Getting Started (Português)

- Introdução ao **AWS Glue**, sua arquitetura e casos de uso.
- Criação de bucket no **Amazon S3** e carregamento de dados de amostra.
- Uso do **Glue Studio** para criar crawlers, catalogar dados e executar jobs ETL com PySpark.
- Uso do **Glue DataBrew** para carregar dados, criar perfis, projetos e fórmulas de transformação.
- Demonstração prática de exclusão de recursos e boas práticas operacionais.

---

#  Desafio

- O arquivo desenvolvido e utilizado para a realização do desafio desta sprint está disponível na pasta Desafio, e a documentação completa pode ser consultada em seu respectivo `README.md`:
  - 📂 [Pasta Desafio](./Desafio/)
  - 📄 [README.md do Desafio](./Desafio/README.md)

# Exercícios

Nesta Sprint, realizei os exercícios **Geração e massa de dados**

Tambem realizei um  **Lab AWS GLUE**

##  Etapas Realizadas exercicio 1 - parte 1 

1. Fiz um script python, onde declarei e inicializei uma lista contendo 250 numeros interios obtidos de forma aleatoria.
2. Fiz um script python, onde declarei uma lista com nomes de 20 animais. Ordenei essa lista em ordem crescente e depois salvei a lista em um arquivo de texto
3. Elaborei um codigo python, para gerar um dataset de nomes de pessoas.

### Código Desenvolvido

O código responsável por realizar o exercicio **Geração e massa de dados** esta em:

 [`codigo`](./Exercicios/exercicio_1/parte_1.ipynb)
 [`Resultado_animais`](./Exercicios/exercicio_1/animais.txt)
 [`Resultado_nomes`](./Exercicios/exercicio_1/nomes_aleatorios.txt)

## Etapas Realizadas Exercicio 1 - parte 2 

1. Fiz a leitura do arquivo `nomes_aleatorios.txt` e fiz um print das 5 primeiras linhas.
2. Fiz o print do schema do arquivo e renomeei a coluna para `nomes`.
3. Adicionei uma coluna chamada `Escolaridade` e atribui 3 valores de forma aleatoria.
4. Adicionei uma nova coluna chamada `Pais` e atribui o nome de um dos 13 paises da América do Sul, de forma aleatória.
5. Adicione uma nova coluna chamda `AnoNascimento` e atribui para cada linha um valor aleatório entre 1945 e 2010.
6. Usando o método SELECT, selecionei as pessoas que nasceram neste século e mostrei 10 nomes.
7. Fiz o mesmo processo da etapa 6 mas usando `Spark SQL`
8. Utilizei o método filter para ver o número total de pessoas que são da geração Millennials(1980 ate 1994)
9. Fiz o mesmo processo da etapa 8 mas com `Spark SQL`
10. Usando `Spark SQL` obtive a quantidade de pessoas de cada pais para cada uma das seguintes gerações(`Baby Boomers`,`Geração X`,`Millennials`,`Geração Z`)

O código completo esta em 
[`notebook`](./Exercicios/exercicio_2/)
---
##  Evidências exercicio 1

###  Container Spark em execução
![Container em execução](./Exercicios/Imagens_Execucao/container_running.png)

---

###  Download do arquivo README.md com autenticação
![Comando WGET com token](./Exercicios/Imagens_Execucao/WGET.png)

---

###  Inicialização do PySpark no container
![Inicialização do PySpark](./Exercicios/Imagens_Execucao/spark_iniciando.png)

---

###  Comandos PySpark para contagem de palavras
![Comandos PySpark](./Exercicios/Imagens_Execucao/comandos.png)

---

###  Resultado da contagem de palavras no README.md
![Resultado da contagem](./Exercicios/Imagens_Execucao/resultado.png)

---
##  Evidência exercicio 2

### Retorno da api
![Retorno da ape](./Exercicios/Imagens_Execucao/retorno_api.png)

---

### [Link para pasta de Imagens Execucao](./Exercicios/Imagens_Execucao)

##  Caminhos para as pastas da Sprint

- [ Certificados](./Certificados/)
- [ Desafio](./Desafio/)
- [ Evidências](./Evidencias/)
- [ Exercícios](./Exercicios/)


