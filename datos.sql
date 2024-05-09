CREATE TABLE creds (
    id INTEGER PRIMARY KEY,
    rut TEXT,
    password TEXT,
    status TEXT,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE scrapping (
    id INTEGER PRIMARY KEY,
    rut TEXT,
    number_1 INTEGER,
    number_2 INTEGER,
    number_3 INTEGER,
    number_4 INTEGER,
    number_5 INTEGER,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE to_chart (
    id INTEGER PRIMARY KEY,
    rut TEXT,
    number_1 INTEGER,
    number_2 INTEGER,
    number_3 INTEGER,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE message (
    id INTEGER PRIMARY KEY,
    message TEXT,
    status TEXT,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);




