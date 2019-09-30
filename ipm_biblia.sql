BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "ipm_biblia" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"testamento"	varchar(255) NOT NULL,
	"version"	varchar(255) NOT NULL,
	"chapter"	integer unsigned NOT NULL CHECK("chapter">=0),
	"verse"	integer unsigned NOT NULL CHECK("verse">=0),
	"text"	text NOT NULL,
	"livro"	varchar(255) NOT NULL
);
INSERT INTO "ipm_biblia" ("id","testamento","version","chapter","verse","text","livro") VALUES (1,'Velho Testamento','nvi',1,1,'gafdga','Gênesis');
INSERT INTO "ipm_biblia" ("id","testamento","version","chapter","verse","text","livro") VALUES (2,'Novo Testamento','nvi',12,12,'dsagdfhdhdhhdfadfadgdfgfdgad','Êxodo');
COMMIT;
