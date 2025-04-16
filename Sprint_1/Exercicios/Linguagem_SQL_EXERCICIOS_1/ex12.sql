/*
E12
Apresente a query para listar código, nome e data de nascimento 
dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). 
As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.

Observação: Apenas vendas com status concluído.
*/

SELECT dep.cddep,dep.nmdep,dep.dtnasc, sum(ven.qtd * ven.vrunt) as valor_total_vendas
FROM tbdependente dep
INNER JOIN tbvendedor vdd
ON dep.cdvdd = vdd.cdvdd
INNER JOIN tbvendas ven
ON vdd.cdvdd = ven.cdvdd
WHERE ven.status = 'Concluído'
GROUP BY nmdep
ORDER BY valor_total_vendas
LIMIT 1
