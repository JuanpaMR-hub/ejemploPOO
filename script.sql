CREATE TABLE BANDA(
ID_BANDA NUMBER,
NOMBRE_BANDA VARCHAR(100),
primary key(id_banda)
);

CREATE TABLE MUSICO(
id_musico number,
nombre_musico VARCHAR(100),
instrumento VARCHAR(50),
id_banda number NULL,
PRIMARY KEY(id_musico),
FOREIGN KEY (id_banda) REFERENCES BANDA(id_banda)
);

INSERT INTO MUSICO VALUES(1,'James','Voz',NULL);
commit;