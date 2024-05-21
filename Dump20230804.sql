-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: python23
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `registration`
--

DROP TABLE IF EXISTS `registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration` (
  `name` varchar(30) DEFAULT NULL,
  `fathers_name` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `contact` varchar(30) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration`
--

LOCK TABLES `registration` WRITE;
/*!40000 ALTER TABLE `registration` DISABLE KEYS */;
INSERT INTO `registration` VALUES ('jatin','yograj','gargj088','6283488328','Male','148031\n');
/*!40000 ALTER TABLE `registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `signup`
--

DROP TABLE IF EXISTS `signup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `signup` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `contact` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `signup`
--

LOCK TABLES `signup` WRITE;
/*!40000 ALTER TABLE `signup` DISABLE KEYS */;
INSERT INTO `signup` VALUES (1,'user2','4567',NULL,NULL),(2,'user3','4567',NULL,NULL),(3,'user4','4567',NULL,NULL),(4,'user5','4567',NULL,NULL);
/*!40000 ALTER TABLE `signup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `roll` int NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`roll`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (2100909,'chirag'),(2100937,'JATIN'),(2100939,'kajal'),(2100942,'KRISHNA'),(2100961,'RAJVEER');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-04 18:21:17
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: vspython
-- ------------------------------------------------------
-- Server version	8.0.34

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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-04 18:21:17
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointments` (
  `p_id` int NOT NULL,
  `p_name` varchar(200) DEFAULT NULL,
  `doctor_name` varchar(200) DEFAULT NULL,
  `payment_status` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `doc_id` varchar(20) DEFAULT NULL,
  `app_id` varchar(200) DEFAULT NULL,
  `app_date` varchar(200) DEFAULT NULL,
  `app_time` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES (70419,'kajal','Dr. Sudhir verma','YES','APPROVED','2100967','2809901','2023-8-3','10:30 to 11:00'),(12345,'jatin','Dr. Balwinder singh','YES',NULL,'2100939','8163912','2023-8-3','9:30 to 10:00'),(12345,'jatin','Dr. Balwinder singh','YES',NULL,'2100939','4200861','2023-8-3','11:30 to 12:00'),(12345,'jatin','Dr. Rajesh kumar','YES','APPROVED','2100937','1032756','2023-8-3','10:00 to 10:30'),(12345,'jatin','Dr. Rajesh kumar','YES',NULL,'2100937','4438325','2023-8-3','11:30 to 12:00'),(70419,'kajal','Dr. Rajesh kumar','YES',NULL,'2100937','4048946','2023-8-3','10:30 to 11:00'),(12345,'jatin','Dr. Isha gupta','YES',NULL,'2100938','7745600','2023-8-4','9:00 to 9:30'),(12345,'jatin','Dr. Rajesh kumar','YES',NULL,'2100937','4661044','2023-8-4','9:00 to 9:30'),(12345,'jatin','Dr. Rajesh kumar',NULL,NULL,'2100937','7348230','2023-8-4','11:00 to 11:30'),(12345,'jatin','Dr. Rajesh kumar',NULL,NULL,'2100937','3387093','2023-8-4','11:30 to 12:00');
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `balwinder`
--

DROP TABLE IF EXISTS `balwinder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `balwinder` (
  `time` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `balwinder`
--

LOCK TABLES `balwinder` WRITE;
/*!40000 ALTER TABLE `balwinder` DISABLE KEYS */;
INSERT INTO `balwinder` VALUES ('9:00 to 9:30',NULL,NULL),('9:30 to 10:00',NULL,NULL),('10:00 to 10:30',NULL,NULL),('10:30 to 11:00',NULL,NULL),('11:00 to 11:30',NULL,NULL),('11:30 to 12:00',NULL,NULL);
/*!40000 ALTER TABLE `balwinder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_reset_table`
--

DROP TABLE IF EXISTS `daily_reset_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_reset_table` (
  `table_name` varchar(255) NOT NULL,
  `last_reset_date` date DEFAULT NULL,
  PRIMARY KEY (`table_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_reset_table`
--

LOCK TABLES `daily_reset_table` WRITE;
/*!40000 ALTER TABLE `daily_reset_table` DISABLE KEYS */;
INSERT INTO `daily_reset_table` VALUES ('balwinder','2023-08-04'),('isha','2023-08-04'),('nishant','2023-08-04'),('pratibha','2023-08-04'),('rajesh','2023-08-04'),('SUDHIR','2023-08-04');
/*!40000 ALTER TABLE `daily_reset_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `id` varchar(20) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `specialist` varchar(200) DEFAULT NULL,
  `contact` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `t_name` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES ('2100937','Dr. Rajesh kumar','cardiologist','9815723651','Rajesh@123','rajesh'),('2100938','Dr. Isha gupta','ENT','9315728901','Isha@123','isha'),('2100939','Dr. Balwinder singh','dentist','9815103651','Balwinder@123','balwinder'),('2100967','Dr. Sudhir verma','neurologist','9825724561','Sudhir@123','sudhir'),('2100969','Dr. Nishant passrija','psychiatrist','8872465398','Nishant@123','nishant'),('2100970','Dr. Pratibha bansal','gynecologist','8837173816','Pratibha@123','pratibha');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `isha`
--

DROP TABLE IF EXISTS `isha`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `isha` (
  `time` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `isha`
--

LOCK TABLES `isha` WRITE;
/*!40000 ALTER TABLE `isha` DISABLE KEYS */;
INSERT INTO `isha` VALUES ('9:00 to 9:30','OK'),('9:30 to 10:00',NULL),('10:00 to 10:30',NULL),('10:30 to 11:00',NULL),('11:00 to 11:30',NULL),('11:30 to 12:00',NULL);
/*!40000 ALTER TABLE `isha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nishant`
--

DROP TABLE IF EXISTS `nishant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nishant` (
  `time` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nishant`
--

LOCK TABLES `nishant` WRITE;
/*!40000 ALTER TABLE `nishant` DISABLE KEYS */;
INSERT INTO `nishant` VALUES ('9:00 to 9:30',NULL),('9:30 to 10:00',NULL),('10:00 to 10:30',NULL),('10:30 to 11:00',NULL),('11:00 to 11:30',NULL),('11:30 to 12:00',NULL);
/*!40000 ALTER TABLE `nishant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `age` varchar(200) DEFAULT NULL,
  `gender` varchar(200) DEFAULT NULL,
  `contact` varchar(200) DEFAULT NULL,
  `username` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `userid` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES (1,'jatin','19','M','6283488328',NULL,'12345','12345'),(2,'jatin','20','M','6284881234',NULL,'12345','22982'),(3,'kajal','19','F','1234567890',NULL,'12345','70419');
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pratibha`
--

DROP TABLE IF EXISTS `pratibha`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pratibha` (
  `time` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pratibha`
--

LOCK TABLES `pratibha` WRITE;
/*!40000 ALTER TABLE `pratibha` DISABLE KEYS */;
INSERT INTO `pratibha` VALUES ('9:00 to 9:30',NULL),('9:30 to 10:00',NULL),('10:00 to 10:30',NULL),('10:30 to 11:00',NULL),('11:00 to 11:30',NULL),('11:30 to 12:00',NULL);
/*!40000 ALTER TABLE `pratibha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rajesh`
--

DROP TABLE IF EXISTS `rajesh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rajesh` (
  `time` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rajesh`
--

LOCK TABLES `rajesh` WRITE;
/*!40000 ALTER TABLE `rajesh` DISABLE KEYS */;
INSERT INTO `rajesh` VALUES ('9:00 to 9:30','OK'),('9:30 to 10:00',NULL),('10:00 to 10:30',NULL),('10:30 to 11:00',NULL),('11:00 to 11:30','OK'),('11:30 to 12:00','OK');
/*!40000 ALTER TABLE `rajesh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sudhir`
--

DROP TABLE IF EXISTS `sudhir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sudhir` (
  `time` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sudhir`
--

LOCK TABLES `sudhir` WRITE;
/*!40000 ALTER TABLE `sudhir` DISABLE KEYS */;
INSERT INTO `sudhir` VALUES ('9:00 to 9:30',NULL),('9:30 to 10:00',NULL),('10:00 to 10:30',NULL),('10:30 to 11:00',NULL),('11:00 to 11:30',NULL),('11:30 to 12:00',NULL);
/*!40000 ALTER TABLE `sudhir` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-04 18:21:17
