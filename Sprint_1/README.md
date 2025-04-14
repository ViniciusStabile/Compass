# Resumo do Curso: SQL para Análise de Dados — Do basico ao avançado

## Seção 3: Comandos basicos

- `SELECT`: Seleciona colunas de uma tabela
- `DISTINCT`: Remove duplicatas nos resultados.
- `WHERE`: Filtra linhas com base em condições
- `ORDER BY`: Ordena os resultados por uma ou mais colunas (ascendente ou descendente).
- `LIMIT`: Restringe o número de linhas retornadas

## Seção 4: Operadores

###  Aritméticos:
- `+`, `-`, `*`, `/`, `%`, `|`

###  De comparação:
- `=`, `!=`, `>`, `<`, `>=`, `<=`, `BETWEEN`, `IN`, `LIKE`

### Logicos:
- `AND`, `OR`, `NOT`

##   Seção 5: Funções agregadas e agrupamentos

- `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
- `GROUP BY`: Agrupa dados para aplicar funções agregadas .
- `HAVING`: Filtra os resultados agregados .

##  Seção 6: Joins

- `INNER JOIN`: Retorna registros com correspondencia nas duas tabelas.
- `LEFT JOIN`: Retorna todos os registros da tabela da esquerda e os correspondentes da direita
- `RIGHT JOIN`: O oposto do `LEFT JOIN`.
- `FULL JOIN`: Retorna todos os registros quando há correspondência em uma das tabelas

##  Seção 7: unions

- `UNION`: Combina os resultados de duas ou mais `SELECT`, removendo duplicatas
- `UNION ALL`: Semelhante ao `UNION`, mas mantem duplicatas

##  Seção 8: Subqueries

- Subconsultas dentro de `SELECT`, `WHERE` ou  `FROM`
- Permite realizar operações mais complexas e encadeadas

##  Seção 9: Tratamento de Dados

###  Conversão de unidades

- `::numeric`, `::date`, `::text`: Operadores para conversão direta de tipos.
- `CAST(valor AS tipo)`: Conversão explícita de dados.


###  tratamento geral

- `CASE WHEN`: Estrutura condicional para retornar valores diferentes conforme critérios.
- `COALESCE()`: Retorna o primeiro valor não nulo entre os parâmetros.



###  Tratamento de Texto

- `LOWER()`: Converte texto para letras minúsculas.
- `UPPER()`: Converte texto para letras maiúsculas.
- `TRIM()`: Remove espaços em branco no início e fim de strings.
- `REPLACE()`: Substitui parte de uma string por outra.

---

###  Funções de datas

- `INTERVAL`: Representa períodos de tempo (ex: `'7 days'::interval`).
- `DATE_TRUNC()`: Trunca uma data para uma unidade específica (mês, dia, ano...).
- `EXTRACT()`: Extrai partes de uma data (ano, mês, dia...).
- `DATEDIFF()`: Calcula a diferença entre duas datas.

##  Seção 10: Manipulação de tabelas

### Tabelas - Criação e deleção

- **Criação de tabela a partir de uma query**  
- **Criação de tabela a partir do zero**  
- **Deleção de tabelas**  

###  Linhas - Inserção, atualização e deleção

- **Inserção de linhas**  
- **Atualização de linhas**  
- **Deleção de linhas**  


# Resumo do Curso: Data & Analytics I

## 1. Big Data
- Volume massivo de dados gerado diariamente.
- Definido pelos 3Vs (Volume, Velocidade, Variedade), depois ampliado com Variabilidade e Complexidade.
- Tecnologias como Hadoop e Spark facilitaram o crescimento do Big Data.
- Big Data permite insights que ajudam na redução de custos , otimizaçao e prevenção de fraudes.

## 2. Ciência de Dados
- Area interdisciplinar que une estatística, computaçao e negócios.
- Foco em extrair insights de dados .
- Envolve Big Data , machine learning, bancos de dados e visualizaçao .

## 3. Papéis em Projetos de Dados
- **Cientista de Dados:** analisa e modela os dados.
- **Engenheiro de Dados:** constroi pipelines e estrutura o armazenamento.
- **Arquiteto de soluções:** define a arquitetura de dados.
- **Desenvolvedor:** implementa soluçoes com foco técnico.

**Modelagem relacional e dimensional:** Pude entender como funciona isso e aquilo.

## 4. Tipos de Dados
- **Estruturados:** organizados (ex: bancos de dados).
- **Semiestruturados:** com marcações flexíveis (ex: XML, JSON).
- **Não estruturados:** livres e variados (ex: videos, audios, redes sociais).

## 5. Bancos de Dados
- **Relacionais (RDBMS):** estruturados, com SQL e propriedades ACID.
- **OLAP:** otimizado para realização de seleção/extração de dados ou de grande volume de dados
- **OLTP:**  otimizado para registrar transações.
- **NoSQL:** flexíveis, com tipos como chave-valor, grafos e documentos.

## 6. Formatos de Armazenamento
- **Texto:** TXT, CSV
- **Semiestruturados:** XML, JSON
- **Binários e eficientes:** AVRO, PARQUET, ORC

## 7. Data Lake e Arquitetura Lambda
- Armazena dados em estado bruto com flexibilidade.
- **Lambda Architecture:** combina três camadas:
  - **Batch Layer:** dados históricos.
  - **Speed Layer:** dados em tempo real.
  - **Serving Layer:** entrega de dados processados


# Resumo: Conceitos de Data & Analytics II

## 1. Tecnicas de Processamento de Dados

- **Batch Processing:** processa dados em blocos armazenados (ex: ETL).
- **Stream Processing:** processa dados em tempo real conforme chegam.

## 2. Business Intelligence (BI)

- Conjunto de praticas e ferramentas para analise e tomada de decisão.
- Engloba relatorios, dashboards, análises preditivas e prescritivas.

## 3. Data Warehouse (DW)

- Repositório centralizado para analise de dados.
- Utiliza **modelagem dimensional** (Tabelas Fato e Dimensão).
- Inclui **Data Marts** (subconjuntos focados por área).
- **SCD (Slowly Changing Dimension):**
  - Tipo 1: sobrescreve
  - Tipo 2: cria novo registro (histórico)
  - Tipo 3: novo campo
  - Tipo 6: híbrido

## 4. Mineração de Dados

- Técnica para descobrir padrões e correlações em grandes volumes de dados.
- Usa estatística, machine learning e IA.

## 5. Machine Learning

- Área da IA que permite que algoritmos aprendam com dados.
- Tipos:
  - **Supervisionado:** aprende com dados rotulados (ex: classificação).
  - **Não-supervisionado:** encontra padrões em dados não rotulados (ex: clusterização).
  - **Semi-supervisionado:** mistura os dois anteriores.
  - **Reforço:** aprende por tentativa e erro (ex: jogos, robótica).

## 6. Deep Learning

- Subárea do ML baseada em redes neurais profundas.
- Usado para: reconhecimento de voz, imagem, texto e previsões.

## 7. Relatórios

- Documentos organizados para comunicar dados e insights.
- Não são apenas gráficos, mas análises direcionadas a um público específico.

## 8. Dashboards

- Painéis interativos com KPIs, métricas e gráficos.
- Conectam-se a APIs, arquivos e bancos para visualização em tempo real.

## 9. Internet das Coisas (IoT)

- Dispositivos físicos conectados que coletam e transmitem dados em tempo real.
- Ex: sensores, câmeras, eletrodomésticos.



