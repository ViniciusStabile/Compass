CREATE TABLE Combustivel   (
    idCombustivel INT PRIMARY KEY NOT NULL,
    tipoCombustivel  VARCHAR(20) NOT NULL
);

CREATE TABLE Carro(
    idCarro INT PRIMARY KEY NOT NULL,
    kmCarro INT  NOT  NULL,
    classiCarro VARCHAR(50) NOT NULL,
    marcaCarro  VARCHAR(80) NOT NULL,
    modeloCarro VARCHAR(80) NOT NULL ,
    anoCarro INT NOT NULL,
    idCombustivel INT NOT NULL,
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel) 
);

CREATE TABLE Cliente (
    idCliente INT PRIMARY KEY NOT  NULL,
    nomeCliente VARCHAR(100) NOT NULL  ,
    cidadeCliente VARCHAR(40) NOT NULL,
    estadoCliente VARCHAR(40) NOT NULL ,
    paisCliente VARCHAR(40) NOT NULL
);

CREATE TABLE Vendedor (
    idVendedor  INT PRIMARY  KEY NOT NULL ,
    nomeVendedor VARCHAR(15) NOT NULL,
    sexoVendedor SMALLINT NOT NULL , 
    estadoVendedor  VARCHAR(40) NOT NULL
);

CREATE TABLE Locacao (
    idLocacao INT PRIMARY KEY NOT NULL,
    dataLocacao  DATE  NOT NULL,
    horaLocacao TIME NOT NULL,
    qtdDiaria INT NOT NULL,
    vlrDiaria   DECIMAL(18,2)  NOT NULL ,
    dataEntrega  DATE  NOT NULL,
    horaEntrega TIME  NOT NULL,
    idCarro INT  NOT NULL,
    idVendedor   INT NOT NULL,
    idCliente INT NOT NULL,
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idVendedor)  REFERENCES Vendedor(idVendedor) ,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente) 
);