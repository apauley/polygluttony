-- SQL solution by Dawie Strauss

CREATE TABLE notfib ( item INT );
INSERT INTO notfib VALUES (1);
INSERT INTO notfib VALUES (2);
INSERT INTO notfib VALUES (3);
INSERT INTO notfib VALUES (4);
INSERT INTO notfib VALUES (5);
SELECT nf1.item + nf2.item AS total
FROM notfib AS nf1, notfib AS nf2
WHERE nf1.item = (nf2.item - 1)
ORDER BY nf1.item;
DROP TABLE notfib;
