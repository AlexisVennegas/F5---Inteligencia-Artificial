-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para airline
CREATE DATABASE IF NOT EXISTS `airline` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `airline`;

-- Volcando estructura para tabla airline.data_client
CREATE TABLE IF NOT EXISTS `data_client` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `id_passenger` int(11) NOT NULL DEFAULT 0,
  `Gender` varchar(50) DEFAULT NULL,
  `Customer_Type` varchar(50) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Type_of_Travel` varchar(50) DEFAULT NULL,
  `Class` varchar(50) DEFAULT NULL,
  `Flight_distance` varchar(50) DEFAULT NULL,
  `Inflight_wifi_service` varchar(50) DEFAULT NULL,
  `datc` varchar(50) DEFAULT NULL,
  `Ease_of_Online_booking` varchar(50) DEFAULT NULL,
  `Gate_location` varchar(50) DEFAULT NULL,
  `Food_and_drink` varchar(50) DEFAULT NULL,
  `Online_boarding` varchar(50) DEFAULT NULL,
  `Departure_delay_minutes` varchar(50) DEFAULT NULL,
  `Columna 16` varchar(50) DEFAULT NULL,
  `Seat_comfort` varchar(50) DEFAULT NULL,
  `Inflight_entertainment` varchar(50) DEFAULT NULL,
  `Onboard_service` varchar(50) DEFAULT NULL,
  `Leg_room_service` varchar(50) DEFAULT NULL,
  `Baggage_handling` varchar(50) DEFAULT NULL,
  `Checkin_service` varchar(50) DEFAULT NULL,
  `Inflight_service` varchar(50) DEFAULT NULL,
  `Cleanliness` varchar(50) DEFAULT NULL,
  `Arrival_delay_minutes` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla airline.predictions
CREATE TABLE IF NOT EXISTS `predictions` (
  `ID` int(11) NOT NULL,
  `prediction` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `ID` (`ID`),
  CONSTRAINT `FK_predictions_data_client` FOREIGN KEY (`ID`) REFERENCES `data_client` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
