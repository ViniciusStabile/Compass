/*
E15
Apresente a query para listar os códigos das vendas identificadas como deletadas. 
Apresente o resultado em ordem crescente.
*/

SELECT ven.cdven
FROM tbvendas ven
WHERE ven.deletado = 1
ORDER BY ven.cdven 
