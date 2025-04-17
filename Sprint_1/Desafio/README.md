#  Objetivo do Desafio

O objetivo deste desafio foi aplicar conceitos de modelagem de dados, divididos em duas etapas:

##  Etapas do Desafio

- **Etapa 1:** Aplicar as três formas normais à tabela `tb_locacao`, criar scripts `.sql` com a definição das estruturas e gerar o diagrama do modelo relacional.
- **Etapa 2:** A partir do modelo relacional, construir um modelo dimensional, adequado para análises.

---

##  Tabela Original

A tabela original `tb_locacao` foi fornecida no seguinte formato:

![Tabela Original](tb_locacao.png)

---

##  Etapa 1 – Modelo Relacional

###  Passos Realizados

1. **Identificação das entidades:** Cliente, Carro, Vendedor, Combustível e Locação.
2. **Aplicação das Formas Normais:**
   - **1FN:** Colunas atômicas e eliminação de grupos repetitivos.
   - **2FN:** Separação de atributos que não dependem da chave primária.
   - **3FN:** Eliminação de dependências transitivas.
3. **Definição de chaves primárias e estrangeiras.**
4. **Criação do modelo relacional normalizado.**

###  Modelo Relacional

![Modelo Relacional](../Evidencias/MODELO_RELACIONAL.png)

####  Exemplo de Criação de Tabela
```sql
CREATE TABLE Carro (
    idCarro INT PRIMARY KEY NOT NULL,
    kmCarro INT NOT NULL,
    classiCarro VARCHAR(50) NOT NULL,
    marcaCarro VARCHAR(80) NOT NULL,
    modeloCarro VARCHAR(80) NOT NULL,
    anoCarro INT NOT NULL,
    idCombustivel INT NOT NULL,
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);
```
*Exemplo de criação da tabela `Carro`, com chave estrangeira para garantir integridade referencial.*

####  Exemplo de Inserção
```sql
INSERT OR IGNORE INTO Carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM tb_locacao;
```
*Inserção de dados distintos a partir da tabela `tb_locacao`, evitando duplicações.*

 **Scripts completos disponíveis em:** [`etapa-1`](./etapa_1/)

---

##  Etapa 2 – Modelo Dimensional

###  Passos Realizados

1. **Criação das views para as dimensões:**
   - `dimCarro`
   - `dimCliente`
   - `dimVendedor`
   - `dimTempo`

2. **Criação da view de fato `fatoLocacao`, com as métricas:**
   - `vlrDiaria`
   - `qtdDiaria`
   - `vlrTotal` (`qtdDiaria * vlrDiaria`)
   - `horaLocacao`, `horaEntrega`

###  Modelo Dimensional

![Modelo Dimensional](../Evidencias/MODELO_DIMENSIONAL.png)

####  Exemplo de Criação de View – `dimCliente`
```sql
CREATE VIEW dimCliente AS
SELECT 
    idCliente,
    nomeCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
FROM Cliente;
```
*Exemplo da view `dimCliente`, representando informações descritivas do cliente no modelo dimensional..*


####  Exemplo de Criação de View – `dimCarro`
```sql
CREATE VIEW dimCarro AS
SELECT 
    c.idCarro,
    c.kmCarro,
    c.classiCarro,
    c.marcaCarro,
    c.modeloCarro,
    c.anoCarro,
    comb.tipoCombustivel
FROM Carro c
JOIN Combustivel comb ON c.idCombustivel = comb.idCombustivel;
```
*Esta view resolve a relação entre `Carro` e `Combustivel`, apresentando o tipo de combustível diretamente na dimensão para facilitar análises.*


 **Scripts completos disponíveis em:** [`etapa-2`](./etapa_2/)

---

##  Destaques Técnicos

###  Construção da `dimTempo`

A view `dimTempo` foi construida com base nas colunas `dataLocacao` e `dataEntrega`, extraindo atributos temporais úteis para análise.

####  Extrações com `SUBSTR` + `CAST`

As datas estavam no formato `yyyymmdd` e como `TEXT`, por isso utilizei `SUBSTR` para fatiar e `CAST` para converter em `INT`:

```sql
CAST(SUBSTR(dataLocacao, 1, 4) AS INT),  -- Ano
CAST(SUBSTR(dataLocacao, 5, 2) AS INT),  -- Mês
CAST(SUBSTR(dataLocacao, 7, 2) AS INT)   -- Dia
```

####  Cálculo do Dia da Semana com `STRFTIME`

Utilizei `STRFTIME('%w', ...)` para retornar o dia da semana:

- `0` → domingo  
- `6` → sábado  
- `1–5` → segunda a sexta

```sql
STRFTIME('%w', DATE(SUBSTR(dataLocacao, 1, 4) || '-' || SUBSTR(dataLocacao, 5, 2) || '-' || SUBSTR(dataLocacao, 7, 2)))
```
*Exemplo de uso da função `STRFTIME` em conjunto com `SUBSTR` e `DATE` para identificar o dia da semana a partir de uma data armazenada como texto no formato `yyyymmdd`. A data é reformatada para `yyyy-mm-dd` e, em seguida, o `STRFTIME('%w')` retorna um número de 0 a 6, representando de domingo a sábado, respectivamente.*


####  Identificação de Fim de Semana com `CASE WHEN`

Com base no valor retornado pelo `STRFTIME`, foi possível identificar finais de semana:

```sql
CASE
  WHEN STRFTIME('%w', DATE(SUBSTR(dataLocacao, 1, 4) || '-' || SUBSTR(dataLocacao, 5, 2) || '-' || SUBSTR(dataLocacao, 7, 2))) IN ('0', '6')
  THEN 1
  ELSE 0
END
```
*Exemplo de uso da cláusula `CASE WHEN` para identificar se a data corresponde a um fim de semana. A data é convertida para o formato `yyyy-mm-dd`, o `STRFTIME('%w')` retorna o dia da semana, e se o valor for `'0'` (domingo) ou `'6'` (sábado), o resultado será `1` indicando fim de semana; caso contrário, retorna `0`. Ideal para análises sazonais e comportamentais baseadas em dias da semana.*


###  Cálculo de Valor Total Gasto
```sql
vlrTotal = qtdDiaria * vlrDiaria
```








