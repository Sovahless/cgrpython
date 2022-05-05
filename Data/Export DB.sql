-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           5.7.33 - MySQL Community Server (GPL)
-- SE du serveur:                Win64
-- HeidiSQL Version:             11.3.0.6441
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour cgr
CREATE DATABASE IF NOT EXISTS `cgr` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `cgr`;

-- Listage de la structure de table cgr. film
CREATE TABLE IF NOT EXISTS `film` (
  `idFilm` int(11) NOT NULL,
  `nomFilm` varchar(400) NOT NULL,
  PRIMARY KEY (`idFilm`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Listage des données de la table cgr.film : ~12 rows (environ)
INSERT INTO `film` (`idFilm`, `nomFilm`) VALUES
	(1, 'Avengers Endgame'),
	(2, 'Voyage de Chihiro'),
	(3, 'Spiderman No Way Home'),
	(4, 'The Batman'),
	(5, 'L\'Affaire Collini'),
	(6, 'Morbius'),
	(7, 'Ogre'),
	(8, 'Abuela'),
	(9, 'Sonic'),
	(10, 'Le secret de la cité perdu'),
	(11, 'Jujutsu Kaisen 0'),
	(12, 'Les Barbapapa');

-- Listage de la structure de table cgr. salle
CREATE TABLE IF NOT EXISTS `salle` (
  `idSalle` int(11) NOT NULL,
  `place_Prise` int(11) NOT NULL,
  `idFilm` int(11) DEFAULT NULL,
  PRIMARY KEY (`idSalle`),
  KEY `Film_idx` (`idFilm`),
  CONSTRAINT `Film` FOREIGN KEY (`idFilm`) REFERENCES `film` (`idFilm`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Listage des données de la table cgr.salle : ~12 rows (environ)
INSERT INTO `salle` (`idSalle`, `place_Prise`, `idFilm`) VALUES
	(1, 128, 1),
	(2, 148, 2),
	(3, 300, 3),
	(4, 234, 4),
	(5, 86, 5),
	(6, 189, 6),
	(7, 28, 7),
	(8, 122, 8),
	(9, 249, 9),
	(10, 296, 10),
	(11, 300, 11),
	(12, 300, 12);

-- Listage de la structure de table cgr. tickets
CREATE TABLE IF NOT EXISTS `tickets` (
  `idTickets` int(11) NOT NULL AUTO_INCREMENT,
  `Prix` float NOT NULL,
  `idSalle` int(11) NOT NULL,
  `idFilm` int(11) NOT NULL,
  `Nom` varchar(50) NOT NULL,
  PRIMARY KEY (`idTickets`),
  KEY `Film_idx` (`idFilm`),
  KEY `Salle_idx` (`idSalle`),
  CONSTRAINT `Salle` FOREIGN KEY (`idSalle`) REFERENCES `salle` (`idSalle`),
  CONSTRAINT `nomFilm` FOREIGN KEY (`idFilm`) REFERENCES `film` (`idFilm`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

-- Listage des données de la table cgr.tickets : ~10 rows (environ)
INSERT INTO `tickets` (`idTickets`, `Prix`, `idSalle`, `idFilm`, `Nom`) VALUES
	(1, 8.5, 1, 1, 'Mr John Doe'),
	(2, 8.5, 7, 7, 'Mme Jane Doe'),
	(3, 8.5, 11, 11, 'Mr Anderson'),
	(4, 8.5, 9, 9, 'Mr Kevin Bardou'),
	(5, 8.5, 12, 12, 'Mr Obama Care'),
	(6, 8.5, 11, 11, 'Mr Lucas Messio'),
	(7, 8.5, 8, 8, 'Mr Gerad Beurre'),
	(8, 8.5, 5, 5, 'Mr Alain Moya'),
	(11, 8.5, 2, 2, 'Mr Paul Mirabel'),
	(12, 8.5, 4, 4, 'Mr Bruce Wayne');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
