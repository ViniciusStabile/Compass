WITH nomes_com_decada AS (
  SELECT 
    nome,
    sexo,
    FLOOR(ano / 10) * 10 AS decada,
    SUM(total) AS total_decada
  FROM meubanco.nomes_csv
  WHERE ano >= 1950
  GROUP BY nome, sexo, FLOOR(ano / 10) * 10
),
ranking_por_decada AS (
  SELECT 
    nome,
    sexo,
    decada,
    total_decada,
    ROW_NUMBER() OVER (
      PARTITION BY decada
      ORDER BY total_decada DESC
    ) AS posicao
  FROM nomes_com_decada
)

SELECT 
  decada,
  nome,
  sexo,
  total_decada
FROM ranking_por_decada
WHERE posicao <= 3
ORDER BY decada, posicao;