-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-02-2026 a las 16:45:24
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
  `total` float NOT NULL,
  `fecha` date NOT NULL
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
(189, 3, 1, 4),
(190, 1, 2, 4),
(209, 1, 6, 3.5);

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
  `imagen_principal` varchar(2000) NOT NULL,
  `tags` char(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `juego`
--

INSERT INTO `juego` (`id`, `titulo`, `precio`, `stock`, `descripcion`, `portada`, `imagen_principal`, `tags`) VALUES
(1, 'Hollow Knight', 12.45, 8, 'Bajo la deteriorada ciudad de Petrópolis yace un antiguo reino en ruinas. A muchos les atrae la vida bajo la superficie y van en busca de riquezas, gloria o respuestas a viejos enigmas.  Hollow Knight es una aventura de acción clásica en 2D ambientada en un vasto mundo interconectado. Explora cavernas tortuosas, ciudades antiguas y páramos mortales. Combate contra criaturas corrompidas, haz amistad con extraños insectos y resuelve los antiguos misterios que yacen en el corazón de reino.', 'f888b933-bdc7-4e69-aade-e4354608aeaa.png', 'a63659b6-1519-4b21-8def-b4a3085364cf.jpg', 'RPG,FPS,3D'),
(2, 'SUPERHOT', 1, 3, 'En SUPERHOT se desdibujan los límites entre estrategia precavida y caos desatado, creando un shooter en primera persona donde el tiempo solo se mueve si tú lo haces. Sin barras de salud que se regeneren. Ni alijos de municiones convenientemente situados. Solo estás tú, superado en número y armamento, aunque podrás recoger las armas de los enemigos abatidos, disparando, dando tajos y maniobrando en medio de un aluvión de balas a cámara lenta.', 'f686b5bb-f15d-4724-84b6-b540213a50c4.png', 'c0740dab-e208-4a38-8779-358df5f8282a.jpg', 'FPS,Indie,Acción'),
(3, 'Garry\'s Mod', 1, 32, 'Garry\'s Mod es un entorno que te permite jugar libremente con el motor físico. Al contrario que en la mayoría de juegos, no hay metas u objetivos predeterminados. Te proporcionamos las herramientas y te damos libertad para jugar. Tú generas los objetos y los unes para crear tus propios artefactos: ya sea un coche, un cohete, una catapulta o algo aún por inventar. Tú decides. Si no eres un experto en construcción, no te desanimes. Puedes colocar una gran variedad de objetos en posiciones absurdas', '5cc2076f-fb4b-4873-a182-4b2d98434cdf.jpeg', 'b860e3c3-b8a0-4509-ae6a-acc8f0decebb.jpg', '3D,Sandbox,FPS'),
(4, 'Celeste', 15.5, 33, 'Ayuda a Madeline a sobrevivir a los demonios de su interior en su viaje hasta la cima de la montaña Celeste, en este ajustadísimo plataforma, obra de los creadores de TowerFall. Enfréntate a cientos de desafíos diseñados a mano, devela retorcidos secretos y, y reconstruye el misterio de la montaña.', '9de28c58-166b-4c72-a4ed-2cf09c802051.png', '08b282e2-1f31-4994-8b31-339c7295c8f0.jpg', 'Indie'),
(5, 'Cuphead', 20, 43, 'Cuphead es un juego de acción clásico estilo \"dispara y corre\" que se centra en combates contra el jefe. Inspirado en los dibujos animados de los años 30, los aspectos visual y sonoro están diseñados con esmero empleando las mismas técnicas de la época, es decir, animación tradicional a mano, fondos de acuarela y grabaciones originales de jazz.  Juega como Cuphead o Mugman (en modo de un jugador o cooperativo) y cruza mundos extraños, adquiere nuevas armas, aprende poderosos supermovimientos y d', 'ae959bcb-bb16-460d-b35e-98591c9509ef.jpg', '37da338a-55da-421b-8379-a4bc5ced22f1.jpg', ''),
(6, 'UFO 50', 11.2, 31, 'UFO 50 es una colección de 50 juegos individuales y multijugador, que nos llega de los creadores de Spelunky, Downwell y Catacomb Kids. Explora una gran cantidad de géneros, desde plataformas hasta disparos, pasando por rompecabezas, roguelites y RPG. Nuestro objetivo es combinar una estética familiar de 8 bits con nuevas ideas y un diseño moderno.', '572b9db3-2a4e-486a-ac1c-eba46e0bbf9c.jpeg', '97e629cc-34e6-485f-8446-4992dcc16e35.jpeg', ''),
(7, 'Among Us', 8.8, 38, 'Un juego de socialización local o en línea de trabajo en equipo y traición para 4 a 15 jugadores... ¡ambientado en el espacio!', '372c407e-c5a2-4430-8e12-6fe5438d3ea3.jpg', 'a9b97d52-919c-4961-9d1c-0deb45d08bcf.jpg', ''),
(8, 'Slime Rancher', 5.35, 14, 'Slime Rancher es la historia de Beatrix LeBeau, una intrépida y joven ranchera que se prepara para una vida a mil años luz de la Tierra en la ‘Lejana, Lejana Pradera’ donde prueba su suerte para ganarse la vida lidiando con slimes.', 'a2a37d2d-1b93-44d0-868a-e04c5f74ec3a.png', '319fb680-6115-4027-8f92-fa47174282d8.jpg', ''),
(9, 'God of War', 20, 4, 'Kratos ha dejado atrás su venganza contra los dioses del Olimpo y vive ahora como un hombre en los dominios de los dioses y monstruos nórdicos. En este mundo cruel e implacable debe luchar para sobrevivir… y enseñar a su hijo a hacerlo también.', '7f812730-767d-4506-80d3-127add71a43e.jpg', 'e662da59-ad23-4ffd-b500-fd46d3fe4c40.jpg', ''),
(10, 'Portal', 17.15, 13, 'Portal™ es la nueva aventura para un solo jugador de Valve. Ambientado en los misteriosos laboratorios de Aperture Science, Portal ha sido calificado como uno de los juegos más innovadores de los últimos tiempos y ofrece incontables horas de rompecabezas nunca vistos.', '98e18a30-a2de-40aa-824b-10dc8cfce9b4.jpg', '854a2487-0436-4414-a1ed-bf373e31da62.jpg', ''),
(12, 'Assassin\'s Creed Syndicate', 18.55, 45, 'Londres, 1868. Dirige tu organización clandestina en plena Revolución Industrial para acabar con la corrupción de la ciudad en una aventura visceral llena acción, intriga y combates brutales.', 'e1ad78cd-830f-44f7-9705-555dc4bda2c4.jpg', '755b09a4-0721-426a-9bf8-1d32ad075d1e.jpg', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pago`
--

CREATE TABLE `pago` (
  `id` int(11) NOT NULL,
  `id_compra_detalle` int(11) NOT NULL,
  `comprobante` varchar(100) NOT NULL,
  `localidad` tinytext NOT NULL,
  `domicilio` tinytext NOT NULL,
  `piso` tinytext NOT NULL
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
(1, 'aaa', 'uuujad@aol.com', 'Nanitogo8!', 'admin'),
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
(26, 'Woob', 'woob999@hotmail.com', 'Wooo888\"', 'buyer'),
(29, 'adnjkanf', 'jjj@gmail.com', 'Nanitogo8!', 'buyer'),
(33, 'akldjafaa', 'aaaagg@aol.com', 'Nanitogo8!', 'buyer'),
(39, 'dsjkahbdla', 'alñfkjlanfsoa@k', 'añlfkanfofñjan', 'buyer'),
(41, 'adsnkajd', 'adma@gmail.com', 'Nanitogo8!', 'buyer'),
(42, 'yaya', 'a@hotmail.com', 'Nanitogo8!', 'buyer'),
(46, 'alkjhgiauhikdj', 'kkkd@gmail.com', 'Nanitogo8!', 'buyer'),
(47, 'adknlajkd', 'ajjj@aol.com', 'Nanitogo8!', 'buyer'),
(50, 'vvvvvvvvvv', 'v@aol.com', 'Nanitogo8!', 'buyer'),
(51, 'jjjjj', 'jdsadi@aol.com', 'Nanitogo8!', 'buyer'),
(52, 'sam,a d', 'adad2@aol.com', 'Nanitogo8!', 'buyer'),
(53, 'aaldnjaajd', 'ada111d@aol.com', 'Nanitogo8!', 'buyer'),
(54, 'kkkk', 'ada@hotmail.com', 'Nanitogo8!', 'buyer');

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
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `un_juego_titulo` (`titulo`);

--
-- Indices de la tabla `pago`
--
ALTER TABLE `pago`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_compra_detalle` (`id_compra_detalle`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=599;

--
-- AUTO_INCREMENT de la tabla `compra_detalle`
--
ALTER TABLE `compra_detalle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- AUTO_INCREMENT de la tabla `estrella`
--
ALTER TABLE `estrella`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=285;

--
-- AUTO_INCREMENT de la tabla `juego`
--
ALTER TABLE `juego`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `pago`
--
ALTER TABLE `pago`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=118;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

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
  ADD CONSTRAINT `id_compra_detalle` FOREIGN KEY (`id_compra_detalle`) REFERENCES `compra_detalle` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
