/*
E13
Apresente a query para listar os 10 produtos menos vendidos pelos 
canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  
As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.
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
