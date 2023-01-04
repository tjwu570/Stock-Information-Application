CREATE TABLE list (
    _type VARCHAR(20) not null,
    _code VARCHAR(10) not null,
    _name VARCHAR(100),
    _ISIN VARCHAR(50),
    _start DATE,
    _market VARCHAR(50),
    _group VARCHAR(50),
    _cfi VARCHAR(50),
    primary key(_code)
);


insert into list values('股票', 1110, '台泥', 'TW0001101004', '1962/02/09', '上市', '水泥工業', 'ESVUFR');
