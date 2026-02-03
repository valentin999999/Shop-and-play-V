USE shopandplay;

SHOW TABLES;

DESCRIBE compra;

--1 Ver cuales usuarios son admins

SELECT * FROM usuario
WHERE tipo_usuario LIKE "%ad%"

--2 Promedio de calificación por juego

SELECT juego.id AS Id, titulo AS Juego, ROUND(AVG(estrella.cantidad),2) AS calificacion FROM juego
INNER JOIN estrella ON estrella.id_juego = juego.id 
INNER JOIN usuario ON estrella.id_usuario = usuario.id
GROUP BY juego.id;

--3 Compras completo

SELECT compra.id AS "id", compra.fecha AS "Fecha inicio", juego.titulo AS "Producto/s", usuario.email AS "Email", compra_detalle.total AS "Total", pago.comprobante AS "Comprobante", compra.estado AS "Estado" FROM compra
INNER JOIN usuario ON usuario.id = compra.id_usuario
INNER JOIN compra_detalle ON compra.id = compra_detalle.id_compra
INNER JOIN juego ON juego.id = compra_detalle.id_juego
INNER JOIN pago ON pago.id_compra = compra.id;

--4 Pagos completo

SELECT pago.id AS "id", nombre_usuario AS Usuario, juego.titulo AS Juego, pago.fechahora AS Fecha, pago.id_compra, usuario.email AS Mail, compra_detalle.total AS Total FROM pago
INNER JOIN compra ON compra.id = pago.id_compra
INNER JOIN usuario ON usuario.id = compra.id_usuario
INNER JOIN compra_detalle ON compra.id = compra_detalle.id_compra
INNER JOIN juego ON juego.id = compra_detalle.id_juego;

--5 Juegos en carrito

SELECT compra.id AS "id", juego.precio AS precio, juego.imagen AS imagen, juego.titulo AS juego, compra_detalle.cantidad AS cantidad FROM compra 
INNER JOIN compra_detalle ON compra.id = compra_detalle.id_compra
INNER JOIN juego ON compra_detalle.id_juego = juego.id
WHERE estado LIKE "%carr%";

--6 Validar login

SELECT * FROM usuario 
WHERE nombre_usuario LIKE "%roberto99%" AND password LIKE "%tututu98%";

--7 Cambio de nombre de usuario

UPDATE usuario
SET nombre_usuario = "Reemplazo"
WHERE id = 9;

--8 Cambio de contraseña de usuario

UPDATE usuario
SET password = "backup"
WHERE id = 9;

--9 Cambio de mail de usuario

UPDATE usuario
SET email = "nuevo@gmail.com"
WHERE id = 9;

--9 Nueva calificacion
INSERT estrella
VALUES (12,5,1,1.5);
--VALUES (,usuario.id,juego.id,cantidad)

--10 Modificar estado de compra

UPDATE compra
SET estado = "en carrito"
WHERE ID = 4;

--11 Añadir Foto del comprobante

UPDATE pago
SET comprobante = "newimage"
WHERE ID = 5;

--12 Crear cuenta

INSERT usuario
VALUES (12,"Trueman","stereospeaker@gmail.com","Treu1mp2","buyer");

--13 Eliminar juego del carrito

UPDATE compra 
SET compra.estado = "pagado"
WHERE id = 3;

--14 Eliminar todos los juegos del carrito

UPDATE compra 
SET compra.estado = "pagado";

--15 Agregar juego

INSERT INTO juego
VALUES (11,"Shovel Knight",9.99,50,"2d platformer","image");

--16 Mostrar todos los juegos pagados

SELECT * FROM compra
WHERE estado LIKE "%pag%";

--17 Agregar pago

INSERT INTO pago 
VALUES (12,"02/02/02 02:02:02",99,"image");

--18 Cambiar stock de un juego

UPDATE juego
SET stock = 72
WHERE id = 13

--19 Cambiar precio de un juego

UPDATE juego
SET precio = 999.99
WHERE id = 13

--20 Modificar calificacion de un usuario de un juego
UPDATE estrella
SET cantidad = 5
WHERE id = 13

SELECT * FROM usuario;
SELECT * FROM juego;
SELECT * FROM pago;
SELECT * FROM compra;
SELECT * FROM compra_detalle;
SELECT * FROM estrella;


SELECT id FROM compra
    WHERE estado LIKE "%carr%";

--21 Obtener sumatoria de productos en el carrito (total)
SELECT ROUND(SUM(juego.precio*compra.cantidad),2) AS contenido FROM compra
INNER JOIN juego ON juego.id=compra.id_juego
WHERE id_usuario = 1 AND estado = "en carrito";



--22 Obtener lista de productos en el carrito
SELECT juego.titulo FROM compra
INNER JOIN juego ON juego.id = compra.id_juego
WHERE id_usuario = 1 AND estado = "en carrito";

--23 precio
SELECT precio FROM juego
WHERE id=1;

--24 f u

DESCRIBE pago;
DELETE FROM compra;
DELETE FROM compra_detalle;
DELETE FROM pago;
DELETE FROM estrella;

UPDATE juego SET stock = 100;

SELECT ROUND(SUM(compra.cantidad*juego.precio),2) FROM compra
INNER JOIN juego ON juego.id=compra.id_juego
WHERE compra.id_usuario = 1 AND compra.estado = "en carrito";

SELECT id FROM estrella
WHERE id_juego = 2 AND id_usuario = 1;

SELECT id FROM compra_detalle
WHERE id_usuario = 1
ORDER BY id DESC
LIMIT 1;

USE shopandplay;