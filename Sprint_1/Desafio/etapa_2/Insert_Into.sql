INSERT INTO dimCarro (idCarro, kmCarro, classiCarro , marcaCarro, modeloCarro, anoCarro, tipoCombustivel)
SELECT DISTINCT idCarro, kmCarro, classiCarro,marcaCarro, modeloCarro,anoCarro, tipoCombustivel
FROM Carro ca
INNER JOIN Combustivel co 
ON ca.idCombustivel = co.idCombustivel;


INSERT INTO dimCliente (idCliente,nomeCliente, cidadeCliente, estadoCliente , paisCliente)
SELECT DISTINCT idCliente, nomeCliente,cidadeCliente, estadoCliente, paisCliente
FROM Cliente;

INSERT INTO dimVendedor (idVendedor,nomeVendedor,sexoVendedor, estadoVendedor )
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM Vendedor;

INSERT INTO dimTempo (
  	datalocacao,
    horaLocacao, horaEntrega ,
    diaLocacao, diaEntrega,
    mesLocacao, mesEntrega,
    anoLocacao, anoEntrega,
    trimestreLocacao,  trimestreEntrega,
    diaSemanaLocacao , diaSemanaEntrega,
    fimDeSemanaLocacao, fimDeSemanaEntrega
)
SELECT DISTINCT
	datalocacao,
	
    horaLocacao,
    horaEntrega,

    CAST(substr(dataLocacao, 7, 2) AS INT),
    CAST(substr(dataEntrega, 7, 2) AS INT),

    CAST(substr(dataLocacao, 5, 2) AS INT),
    CAST(substr(dataEntrega, 5, 2) AS INT),

    CAST(substr(dataLocacao, 1, 4) AS INT),
    CAST(substr(dataEntrega, 1, 4) AS INT),

    (CAST(substr(dataLocacao, 5, 2) AS INT) + 2) / 3,
    (CAST(substr(dataEntrega, 5, 2) AS INT) + 2) / 3,

    strftime('%w', date(substr(dataLocacao, 1, 4) || '-' || substr(dataLocacao, 5, 2) || '-' || substr(dataLocacao, 7, 2))),
    strftime('%w', date(substr(dataEntrega, 1, 4) || '-' || substr(dataEntrega, 5, 2) || '-' || substr(dataEntrega, 7, 2))),

    CASE WHEN strftime('%w', date(substr(dataLocacao, 1, 4) || '-' || substr(dataLocacao, 5, 2) || '-' || substr(dataLocacao, 7, 2))) IN ('0', '6') THEN 1 ELSE 0 END,
    CASE WHEN strftime('%w', date(substr(dataEntrega, 1, 4) || '-' || substr(dataEntrega, 5, 2) || '-' || substr(dataEntrega, 7, 2))) IN ('0', '6') THEN 1 ELSE 0 END
    
FROM locacao;


INSERT INTO fatoLocacao (
    idLocacao,dataLocacao, dataEntrega,
    horaLocacao, horaEntrega,
    qtdDiaria, vlrDiaria, vlrTotal,
    idCarro, idVendedor, idCliente
)
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
FROM locacao l