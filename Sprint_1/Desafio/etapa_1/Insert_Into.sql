INSERT INTO Combustivel  ( idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel,tipoCombustivel
FROM tb_locacao;

INSERT OR IGNORE  INTO Carro(idCarro,kmCarro, classiCarro, marcaCarro,modeloCarro, anoCarro,idCombustivel)
SELECT DISTINCT  idCarro,kmCarro,classiCarro, marcaCarro,modeloCarro, anoCarro, idCombustivel
FROM tb_locacao;

INSERT INTO Cliente(idCliente, nomeCliente, cidadeCliente,estadoCliente, paisCliente)
SELECT DISTINCT idCliente,nomeCliente, cidadeCliente,estadoCliente,paisCliente
FROM tb_locacao;

INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor,estadoVendedor)
SELECT DISTINCT idVendedor ,nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao ;


INSERT OR IGNORE INTO Locacao  (
    idLocacao, dataLocacao, horaLocacao, qtdDiaria,vlrDiaria,
    dataEntrega, horaEntrega,idCarro, idVendedor, idCliente
)
SELECT 
    idLocacao,dataLocacao,horaLocacao, qtdDiaria,vlrDiaria ,
    dataEntrega,horaEntrega, idCarro, idVendedor, idCliente
FROM tb_locacao;