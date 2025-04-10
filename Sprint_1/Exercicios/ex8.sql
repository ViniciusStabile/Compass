/*
E08
Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem),
e que estas vendas estejam com o status concluída.  
As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.
*/

SELECT vendedor.cdvdd, vendedor.nmvdd
FROM tbvendedor vendedor
LEFT JOIN tbvendas vendas
ON vendedor.cdvdd = vendas.cdvdd
WHERE vendas.status = 'Concluído'
GROUP BY vendas.cdvdd
ORDER by count(*) DESC
LIMIT 1