CREATE TABLE dimCarro  (
    idCarro INT PRIMARY KEY,
    kmCarro  INT,
    classiCarro  VARCHAR(50),
    marcaCarro VARCHAR(80) ,
    modeloCarro VARCHAR(80),
    anoCarro INT,
    tipoCombustivel VARCHAR(20)
);


CREATE TABLE dimCliente(
    idCliente INT PRIMARY  KEY ,
    nomeCliente VARCHAR(100),
    cidadeCliente  VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);


CREATE TABLE dimVendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor  SMALLINT,
    estadoVendedor VARCHAR(40)
);

CREATE TABLE dimTempo   (
    datalocacao DATE PRIMARY KEY ,
    horaLocacao TIME,
    horaEntrega TIME,
    diaLocacao INT ,
    diaEntrega INT,
    diaSemanaLocacao  INT,
    diaSemanaEntrega INT,
    mesLocacao INT,
    mesEntrega INT ,
    anoLocacao  INT,
    anoEntrega INT,
    trimestreLocacao INT,
    trimestreEntrega INT,
    fimDeSemanaLocacao  TINYINT ,
    fimDeSemanaEntrega TINYINT
);


CREATE TABLE fatoLocacao   (
    idLocacao INT PRIMARY KEY,
    dataLocacao  DATE,
    dataEntrega DATE ,
    horaLocacao TIME,
    horaEntrega TIME ,
    qtdDiaria INT,
    vlrDiaria DECIMAL (18,2),
    vlrTotal DECIMAL(18,2),
    idCarro INT ,
    idVendedor  INT,
    idCliente INT,

    FOREIGN KEY (datalocacao) REFERENCES  dimTempo(datalocacao),
    FOREIGN KEY (idCarro)  REFERENCES dimCarro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES dimVendedor(idVendedor),
    FOREIGN KEY (idCliente) REFERENCES dimCliente(idCliente)
);