-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-01-2026 a las 00:36:40
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `shopandplay`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compra`
--

CREATE TABLE `compra` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_juego` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `estado` enum('en carrito','pagado','entregado') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compra_detalle`
--

CREATE TABLE `compra_detalle` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `contenido` mediumtext NOT NULL,
  `total` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estrella`
--

CREATE TABLE `estrella` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_juego` int(11) NOT NULL,
  `cantidad` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estrella`
--

INSERT INTO `estrella` (`id`, `id_usuario`, `id_juego`, `cantidad`) VALUES
(3, 6, 4, 4),
(4, 5, 7, 3.5),
(5, 8, 10, 4.5),
(6, 8, 6, 5),
(7, 9, 9, 3),
(8, 2, 10, 2.5),
(9, 9, 2, 3.5),
(10, 6, 8, 1),
(11, 5, 4, 2.5),
(12, 5, 1, 1.5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `juego`
--

CREATE TABLE `juego` (
  `id` int(11) NOT NULL,
  `titulo` varchar(30) NOT NULL,
  `precio` float NOT NULL,
  `stock` int(11) NOT NULL,
  `descripcion` varchar(1000) NOT NULL,
  `portada` varchar(100) NOT NULL,
  `imagen_principal` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `juego`
--

INSERT INTO `juego` (`id`, `titulo`, `precio`, `stock`, `descripcion`, `portada`, `imagen_principal`) VALUES
(1, 'Hollow Knight', 19.99, 20, '2d metroidvania.', 'hollow.png', 'morehollow.jpg'),
(2, 'SUPERHOT', 10.99, 10, 'FPS.', 'hot.png', 'morehot.jpg'),
(3, 'Garry\'s Mod', 29.99, 30, '3d sandbox.', 'gmod.jpeg', 'moregarry.jpg'),
(4, 'Celeste', 9.99, 27, '2d precision platformer.', 'celeste.png', 'moreceleste.jpg'),
(5, 'Cuphead', 25.99, 24, '2d run and gun', 'cup.jpg', 'morecup.jpg'),
(6, 'UFO 50', 36.99, 18, '50 retro game collection', 'ufo.jpeg', 'moreufo.jpeg'),
(7, 'Among Us', 5.99, 51, 'Traitor game.', 'among.jpg', 'moreamong.jpg'),
(8, 'Slime Rancher', 27.99, 36, 'Slime tycoon', 'slime.png', 'moreslime.jpg'),
(9, 'God of War', 11, 48, 'action-adventure game.', 'god.jpg', 'moregod.jpg'),
(10, 'Portal', 17.99, 23, 'First person puzzle platformer.', 'portal.jpg', 'moreportal.jpg'),
(12, 'Assassin\'s Creed Syndicate', 19.99, 9, 'Acción 3d', 'assassin.jpg', 'moreassassin.jpg'),
(13, 'Super Meat Boy', 13.05, 12, 'Salta mucho.', 'meat.png', 'moremeat.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pago`
--

CREATE TABLE `pago` (
  `id` int(11) NOT NULL,
  `fechahora` datetime NOT NULL,
  `comprobante` varchar(100) NOT NULL,
  `id_compra` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre_usuario` varchar(30) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(30) NOT NULL,
  `tipo_usuario` enum('admin','buyer') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre_usuario`, `email`, `password`, `tipo_usuario`) VALUES
(1, 'aa', 'robgom@gmail.com', 'tututu98', 'admin'),
(2, 'rodsalvia!', 'rodsal@gmail.com', 'cthulhu', 'admin'),
(3, 'Placioman', 'amamam@gmail.com', 'adjdj', 'buyer'),
(4, 'MinervaMalicia', 'gojosman@gmail.com', 'ueuru', 'buyer'),
(5, 'Joaco81', 'joaquinstrauss@gmail.com', 'ahdhdj2193', 'buyer'),
(6, 'VelcroFurioso', 'vell@gmail.com', '87Nnna!99', 'buyer'),
(7, 'IxtraWorld', 'tomorrownow@gmail.com', 'jamen192##', 'buyer'),
(8, 'Felapton2000', 'logicalconca@gmail.com', 'treuue72543*!', 'buyer'),
(9, 'Reemplazo', 'nuevo@gmail.com', 'backup', 'buyer'),
(10, 'QuanticSandwich', 'heisenberg@gmail.com', 'nbee948', 'buyer'),
(11, 'Gelasio', 'G102@gmail.com', 'Treu1mp2', 'buyer'),
(13, 'HADHD', 'heleut@gmail.com', 'jdadbn!1', 'buyer'),
(18, 'Trrra', '2@aol.com', 'ajdadjda', 'buyer'),
(19, 'Godzilla', 'Zenith@aol.com', '84714', 'buyer'),
(20, 'efkjn', 'akdjfha@aol.com', 'ikoe', 'buyer'),
(21, 'HIA', 'rephlex@aol.com', 'akkdakdakdk', 'buyer'),
(22, 'Pancho', 'h2o@gmail.com', 'Nanitogo8!', 'buyer'),
(25, 'Machinarium', 'amanita@gmail.com', 'Makina9!', 'buyer'),
(26, 'Woob', 'woob999@hotmail.com', 'Wooo888\"', 'buyer');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `compra`
--
ALTER TABLE `compra`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_juego2` (`id_juego`);

--
-- Indices de la tabla `compra_detalle`
--
ALTER TABLE `compra_detalle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario3` (`id_usuario`);

--
-- Indices de la tabla `estrella`
--
ALTER TABLE `estrella`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_usuario` (`id_usuario`,`id_juego`),
  ADD KEY `id_juego` (`id_juego`);

--
-- Indices de la tabla `juego`
--
ALTER TABLE `juego`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pago`
--
ALTER TABLE `pago`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_compra` (`id_compra`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `un_nombre_usuario` (`nombre_usuario`),
  ADD UNIQUE KEY `un_email_usuario` (`email`),
  ADD UNIQUE KEY `nombre_usuario` (`nombre_usuario`,`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `compra`
--
ALTER TABLE `compra`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT de la tabla `compra_detalle`
--
ALTER TABLE `compra_detalle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estrella`
--
ALTER TABLE `estrella`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `juego`
--
ALTER TABLE `juego`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `pago`
--
ALTER TABLE `pago`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `compra`
--
ALTER TABLE `compra`
  ADD CONSTRAINT `id_juego2` FOREIGN KEY (`id_juego`) REFERENCES `juego` (`id`),
  ADD CONSTRAINT `id_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `compra_detalle`
--
ALTER TABLE `compra_detalle`
  ADD CONSTRAINT `id_usuario3` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `estrella`
--
ALTER TABLE `estrella`
  ADD CONSTRAINT `id_juego` FOREIGN KEY (`id_juego`) REFERENCES `juego` (`id`),
  ADD CONSTRAINT `id_usuario2` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `pago`
--
ALTER TABLE `pago`
  ADD CONSTRAINT `id_compra` FOREIGN KEY (`id_compra`) REFERENCES `compra` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
