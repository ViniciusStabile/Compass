CREATE VIEW vw_dimCarro AS
SELECT DISTINCT 
    ca.idCarro, 
    ca.kmCarro, 
    ca.classiCarro, 
    ca.marcaCarro, 
    ca.modeloCarro, 
    ca.anoCarro, 
    co.tipoCombustivel
FROM Carro ca
INNER JOIN Combustivel co ON ca.idCombustivel = co.idCombustivel;

CREATE VIEW dimCliente AS
SELECT DISTINCT 
    idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM Cliente;

CREATE VIEW dimVendedor AS
SELECT DISTINCT 
    idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM Vendedor;


CREATE VIEW dimTempo AS
SELECT DISTINCT
    datalocacao,
    horaLocacao,
    horaEntrega,
    
    CAST(substr(dataLocacao, 7, 2) AS INT) AS diaLocacao,
    CAST(substr(dataEntrega, 7, 2) AS INT) AS diaEntrega,
    
    CAST(substr(dataLocacao, 5, 2) AS INT) AS mesLocacao,
    CAST(substr(dataEntrega, 5, 2) AS INT) AS mesEntrega,
    
    CAST(substr(dataLocacao, 1, 4) AS INT) AS anoLocacao,
    CAST(substr(dataEntrega, 1, 4) AS INT) AS anoEntrega,
    
    (CAST(substr(dataLocacao, 5, 2) AS INT) + 2) / 3 AS trimestreLocacao,
    (CAST(substr(dataEntrega, 5, 2) AS INT) + 2) / 3 AS trimestreEntrega,
    
    strftime('%w', date(substr(dataLocacao, 1, 4) || '-' || substr(dataLocacao, 5, 2) || '-' || substr(dataLocacao, 7, 2))) AS diaSemanaLocacao,
    strftime('%w', date(substr(dataEntrega, 1, 4) || '-' || substr(dataEntrega, 5, 2) || '-' || substr(dataEntrega, 7, 2))) AS diaSemanaEntrega,
    CASE WHEN strftime('%w', date(substr(dataLocacao, 1, 4) || '-' || substr(dataLocacao, 5, 2) || '-' || substr(dataLocacao, 7, 2))) IN ('0', '6') THEN 1 ELSE 0 
    END AS fimDeSemanaLocacao,
    CASE WHEN strftime('%w', date(substr(dataEntrega, 1, 4) || '-' || substr(dataEntrega, 5, 2) || '-' || substr(dataEntrega, 7, 2))) IN ('0', '6') THEN 1 ELSE 0 
    END AS fimDeSemanaEntrega
    
FROM locacao;

CREATE VIEW vw_fatoLocacao AS
SELECT
    idLocacao,
    dataLocacao,
    dataEntrega,
    horaLocacao,
    horaEntrega,
    qtdDiaria,
    vlrDiaria,
    qtdDiaria * l.vlrDiaria AS vlrTotal,
    idCarro,
    idVendedor,
    idCliente
FROM locacao l;