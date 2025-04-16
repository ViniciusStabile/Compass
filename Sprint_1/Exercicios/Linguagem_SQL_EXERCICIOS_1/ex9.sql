/*
E09
Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02,
e que estas vendas estejam com o status concluída. 
As colunas presentes no resultado devem ser cdpro e nmpro.
*/

SELECT es.cdpro,ven.nmpro
FROM tbestoqueproduto es  
INNER JOIN tbvendas ven  
ON es.cdpro = ven.cdpro
WHERE ven.status = 'Concluído' and ven.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY ven.nmpro
ORDER BY count(ven.nmpro) DESC
LIMIT 1