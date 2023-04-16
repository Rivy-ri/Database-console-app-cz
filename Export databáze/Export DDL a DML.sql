/* 
Autor: Adela Kopecka
Projekt: alfa -3
email:kopecka@spsejecna.cz
*/

CREATE DATABASE  IF NOT EXISTS `alfa_3` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `alfa_3`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: alfa_3
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `hodnoceni_produktu`
--

DROP TABLE IF EXISTS `hodnoceni_produktu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hodnoceni_produktu` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `FK_produkt` int NOT NULL,
  `FK_uzivatel` int NOT NULL,
  `Pocet_hvezd` int NOT NULL,
  `Komentar` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`),
  KEY `FK_produkt` (`FK_produkt`),
  KEY `FK_uzivatel` (`FK_uzivatel`),
  CONSTRAINT `hodnoceni_produktu_ibfk_1` FOREIGN KEY (`FK_produkt`) REFERENCES `zbozi` (`ID`),
  CONSTRAINT `hodnoceni_produktu_ibfk_2` FOREIGN KEY (`FK_uzivatel`) REFERENCES `zakaznik` (`ID`),
  CONSTRAINT `hodnoceni_produktu_chk_1` CHECK (((`Pocet_hvezd` > 0) and (`Pocet_hvezd` <= 5)))
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hodnoceni_produktu`
--

LOCK TABLES `hodnoceni_produktu` WRITE;
/*!40000 ALTER TABLE `hodnoceni_produktu` DISABLE KEYS */;
INSERT INTO `hodnoceni_produktu` VALUES (48,5,1,4,'lectus pellentesque'),(49,6,2,1,'ut'),(50,2,3,3,'justo nec condimentum neque sapien'),(51,5,4,3,'vestibulum'),(52,2,5,4,'suscipit nulla elit'),(53,6,6,4,'quisque'),(54,5,7,4,'vestibulum vestibulum ante ipsum'),(55,1,8,2,'ante ipsum primis in faucibus'),(56,5,9,5,'nisi at nibh in hac'),(57,2,10,2,'purus eu magna vulputate'),(58,1,1,2,'cursus urna ut tellus nulla'),(59,2,2,2,'cursus vestibulum'),(60,6,3,3,'erat'),(61,1,4,2,'magnis'),(62,1,5,3,'convallis duis consequat dui nec'),(63,5,6,2,'amet'),(64,5,7,1,'orci luctus et'),(65,6,8,4,'vivamus vestibulum sagittis sapien cum'),(66,4,9,3,'leo odio condimentum id luctus'),(67,1,10,1,'ante ipsum primis');
/*!40000 ALTER TABLE `hodnoceni_produktu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `mostpopularandpositiveproducts`
--

DROP TABLE IF EXISTS `mostpopularandpositiveproducts`;
/*!50001 DROP VIEW IF EXISTS `mostpopularandpositiveproducts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `mostpopularandpositiveproducts` AS SELECT 
 1 AS `nazev_zbozi`,
 1 AS `pocet_zakoupenych_ks`,
 1 AS `prumerne_hodnoceni`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `objednavka`
--

DROP TABLE IF EXISTS `objednavka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `objednavka` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Datum_tvorby` date DEFAULT NULL,
  `Trasovaci_cislo` int DEFAULT NULL,
  `Zaplaceno` tinyint(1) DEFAULT NULL,
  `Datum_uhrady` date DEFAULT NULL,
  `Stav` enum('obdrzena','pripravena','odeslana','k vyzvednuti') NOT NULL,
  `FK_zakaznik` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`),
  UNIQUE KEY `Trasovaci_cislo` (`Trasovaci_cislo`),
  KEY `FK_zakaznik` (`FK_zakaznik`),
  CONSTRAINT `objednavka_ibfk_1` FOREIGN KEY (`FK_zakaznik`) REFERENCES `zakaznik` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objednavka`
--

LOCK TABLES `objednavka` WRITE;
/*!40000 ALTER TABLE `objednavka` DISABLE KEYS */;
INSERT INTO `objednavka` VALUES (1,'2023-01-23',8774,1,'2022-12-20','odeslana',1),(2,'2022-10-04',4899,0,'2022-08-25','pripravena',2),(3,'2022-12-15',8309,0,'2022-09-30','odeslana',3),(4,'2021-09-29',1560,0,'2022-10-11','obdrzena',4),(5,'2022-07-14',5490,0,'2022-08-22','odeslana',5),(6,'2021-10-05',9370,0,'2022-02-19','odeslana',6),(7,'2021-12-19',3913,0,'2022-10-30','k vyzvednuti',7),(8,'2022-09-08',9048,0,'2022-11-21','pripravena',8),(9,'2021-09-27',1295,0,'2022-05-10','odeslana',9),(10,'2022-02-09',7712,0,'2022-12-10','obdrzena',10),(11,'2022-12-08',8754,0,'2022-06-30','odeslana',1),(12,'2022-05-27',9871,1,'2022-10-30','obdrzena',2),(13,'2021-11-11',7051,0,'2022-12-31','pripravena',3),(14,'2022-11-18',5029,0,'2022-11-30','pripravena',4),(15,'2021-11-01',7802,0,'2022-07-10','k vyzvednuti',5);
/*!40000 ALTER TABLE `objednavka` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `pocet_prodanych_ks_podle_vyrobce`
--

DROP TABLE IF EXISTS `pocet_prodanych_ks_podle_vyrobce`;
/*!50001 DROP VIEW IF EXISTS `pocet_prodanych_ks_podle_vyrobce`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `pocet_prodanych_ks_podle_vyrobce` AS SELECT 
 1 AS `Nazev`,
 1 AS `COUNT(o.FK_zbozi)`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `vazba_objednavka_zbozi`
--

DROP TABLE IF EXISTS `vazba_objednavka_zbozi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vazba_objednavka_zbozi` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Pocet_ks` int DEFAULT NULL,
  `FK_objednavka` int NOT NULL,
  `FK_zbozi` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`),
  KEY `FK_objednavka` (`FK_objednavka`),
  KEY `FK_zbozi` (`FK_zbozi`),
  CONSTRAINT `vazba_objednavka_zbozi_ibfk_1` FOREIGN KEY (`FK_objednavka`) REFERENCES `objednavka` (`ID`),
  CONSTRAINT `vazba_objednavka_zbozi_ibfk_2` FOREIGN KEY (`FK_zbozi`) REFERENCES `zbozi` (`ID`),
  CONSTRAINT `vazba_objednavka_zbozi_chk_1` CHECK (((`Pocet_ks` > 0) and (`Pocet_ks` <= 5)))
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vazba_objednavka_zbozi`
--

LOCK TABLES `vazba_objednavka_zbozi` WRITE;
/*!40000 ALTER TABLE `vazba_objednavka_zbozi` DISABLE KEYS */;
INSERT INTO `vazba_objednavka_zbozi` VALUES (11,1,1,1),(12,3,2,2),(13,2,3,3),(14,2,4,3),(15,2,5,2),(16,3,6,5),(17,3,7,2),(18,2,8,4),(19,1,9,3),(20,2,10,2),(21,3,11,2),(22,1,12,4),(23,3,13,3),(24,2,14,5),(25,2,15,4),(26,3,1,6),(27,3,2,3),(28,1,3,6),(29,3,4,6),(30,2,5,1),(31,1,6,1),(32,3,7,4),(33,2,8,4),(34,1,9,6),(35,3,10,2);
/*!40000 ALTER TABLE `vazba_objednavka_zbozi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vyrobce`
--

DROP TABLE IF EXISTS `vyrobce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vyrobce` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nazev` varchar(20) NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Telefon` varchar(40) CHARACTER SET ucs2 COLLATE ucs2_general_ci DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`),
  UNIQUE KEY `Nazev` (`Nazev`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vyrobce`
--

LOCK TABLES `vyrobce` WRITE;
/*!40000 ALTER TABLE `vyrobce` DISABLE KEYS */;
INSERT INTO `vyrobce` VALUES (1,'Thoughtstorm','habbado0@cnn.com','+7 811 309 6963'),(2,'Kazio','chenlon1@myspace.com','+46 139 590 3462'),(3,'Rhynyx','hbristoe2@lulu.com','+46 998 354 3106');
/*!40000 ALTER TABLE `vyrobce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zakaznik`
--

DROP TABLE IF EXISTS `zakaznik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zakaznik` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Jmeno` varchar(20) NOT NULL,
  `Prijmeni` varchar(20) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Telefon` varchar(40) CHARACTER SET ucs2 COLLATE ucs2_general_ci DEFAULT NULL,
  `Pohlavi` enum('F','M','N') DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zakaznik`
--

LOCK TABLES `zakaznik` WRITE;
/*!40000 ALTER TABLE `zakaznik` DISABLE KEYS */;
INSERT INTO `zakaznik` VALUES (1,'Enrika','Swynfen','eswynfen0@wikimedia.org','2584120604','F'),(2,'Parsifal','Zorzi','pzorzi1@quantcast.com','3716456188','F'),(3,'Bernelle','Jerok','bjerok2@miitbeian.gov.cn','8766889355','N'),(4,'Torrance','Matschoss','tmatschoss3@multiply.com','9946093044','M'),(5,'Nananne','Basler','nbasler4@aboutads.info','4528761734','M'),(6,'Finlay','Deniscke','fdeniscke5@google.com.au','9224267646','F'),(7,'Colan','Affleck','caffleck6@ebay.co.uk','4594089344','F'),(8,'Chauncey','O\' Culligan','coculligan7@imageshack.us','6387572364','F'),(9,'Raven','Czapla','rczapla8@godaddy.com','2036916677','N'),(10,'Thurstan','Paule','tpaule9@mlb.com','8592379183','N');
/*!40000 ALTER TABLE `zakaznik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zbozi`
--

DROP TABLE IF EXISTS `zbozi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zbozi` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nazev` varchar(15) DEFAULT NULL,
  `Pocet_ks_na_sklade` int DEFAULT NULL,
  `Cena_ks_Euro` float DEFAULT NULL,
  `Typ` enum('kalhoty','bunda','sako','mikina','saty','triko') NOT NULL,
  `Strih` enum('F','M','N') DEFAULT NULL,
  `FK_vyrobce` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`),
  KEY `FK_vyrobce` (`FK_vyrobce`),
  CONSTRAINT `zbozi_ibfk_1` FOREIGN KEY (`FK_vyrobce`) REFERENCES `vyrobce` (`ID`),
  CONSTRAINT `zbozi_chk_1` CHECK ((`Cena_ks_Euro` > 0.5))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zbozi`
--

LOCK TABLES `zbozi` WRITE;
/*!40000 ALTER TABLE `zbozi` DISABLE KEYS */;
INSERT INTO `zbozi` VALUES (1,'Gina Tricot',50,13.5,'kalhoty','F',1),(2,'Her',10,20.99,'sako','F',2),(3,'Phyllis',24,10,'triko','F',3),(4,'Prechodna bunda',21,50.99,'bunda','M',1),(5,'Billly',56,20.99,'mikina','M',2),(6,'Miss pap',60,100.99,'saty','F',2);
/*!40000 ALTER TABLE `zbozi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `mostpopularandpositiveproducts`
--

/*!50001 DROP VIEW IF EXISTS `mostpopularandpositiveproducts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `mostpopularandpositiveproducts` AS select `zbozi`.`Nazev` AS `nazev_zbozi`,count(`voz`.`FK_zbozi`) AS `pocet_zakoupenych_ks`,avg(`hp`.`Pocet_hvezd`) AS `prumerne_hodnoceni` from ((`zbozi` left join `vazba_objednavka_zbozi` `voz` on((`zbozi`.`ID` = `voz`.`FK_zbozi`))) left join `hodnoceni_produktu` `hp` on((`zbozi`.`ID` = `hp`.`FK_produkt`))) group by `zbozi`.`Nazev` order by ((0 <> avg(`hp`.`Pocet_hvezd`)) and (0 <> count(`voz`.`FK_zbozi`))) desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `pocet_prodanych_ks_podle_vyrobce`
--

/*!50001 DROP VIEW IF EXISTS `pocet_prodanych_ks_podle_vyrobce`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `pocet_prodanych_ks_podle_vyrobce` AS select `vyrobce`.`Nazev` AS `Nazev`,count(`o`.`FK_zbozi`) AS `COUNT(o.FK_zbozi)` from ((`vyrobce` join `zbozi` `z` on((`vyrobce`.`ID` = `z`.`FK_vyrobce`))) join `vazba_objednavka_zbozi` `o` on((`z`.`ID` = `o`.`FK_zbozi`))) group by `vyrobce`.`Nazev` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-03 11:32:04
