-- MySQL dump 10.13  Distrib 8.0.11, for osx10.12 (x86_64)
--
-- Host: localhost    Database: automation_history
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `browser`
--

DROP TABLE IF EXISTS `browser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `browser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `alias` varchar(100) NOT NULL,
  `version` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `browser`
--

LOCK TABLES `browser` WRITE;
/*!40000 ALTER TABLE `browser` DISABLE KEYS */;
INSERT INTO `browser` VALUES (1,'Chrome','chrome','75.0.3770.142','2019-07-31 02:46:21','2019-07-31 02:46:21'),(2,'Firefox','firefox','67.0.4','2019-07-31 02:48:37','2019-07-31 02:48:37'),(3,'Safari','Safari','12.1.2','2019-07-31 02:49:54','2019-07-31 02:49:54'),(4,'IE','internet explorer','11','2019-07-31 02:53:20','2019-07-31 02:53:20'),(5,'Edge','MicrosoftEdge','42.17134.1.0','2019-07-31 02:54:49','2019-07-31 02:54:49'),(6,'MobileBrowser','chrome','75.0.3770.142','2019-07-31 02:56:31','2019-07-31 02:56:31');
/*!40000 ALTER TABLE `browser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `case_suite`
--

DROP TABLE IF EXISTS `case_suite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `case_suite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test_suite_id` int(11) NOT NULL,
  `test_case_id` int(11) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `case_suite`
--

LOCK TABLES `case_suite` WRITE;
/*!40000 ALTER TABLE `case_suite` DISABLE KEYS */;
/*!40000 ALTER TABLE `case_suite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `device` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device`
--

LOCK TABLES `device` WRITE;
/*!40000 ALTER TABLE `device` DISABLE KEYS */;
INSERT INTO `device` VALUES (1,'Simulator','2019-07-31 06:26:04','2019-07-31 06:26:04'),(2,'Emulator','2019-07-31 06:26:24','2019-07-31 06:26:24'),(3,'MiPlus','2019-07-31 06:26:43','2019-07-31 06:26:43'),(4,'STF','2019-07-31 06:26:49','2019-07-31 06:26:49');
/*!40000 ALTER TABLE `device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `driver`
--

DROP TABLE IF EXISTS `driver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `driver` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `version` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `comment` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `driver`
--

LOCK TABLES `driver` WRITE;
/*!40000 ALTER TABLE `driver` DISABLE KEYS */;
INSERT INTO `driver` VALUES (1,'chromedriver','74.0.3729.6','2019-07-31 03:07:15','2019-07-31 03:07:15','test on macos, chrome 74 and 75.0.3770.142'),(2,'geckodriver','0.24.0','2019-07-31 03:08:09','2019-07-31 03:08:09','test on macos, firefox 67.0'),(3,'safaridriver','12607.3.10','2019-07-31 03:08:38','2019-07-31 03:08:38','test on macos, safari 12.1.2'),(4,'IEDriver','3.9.0.0','2019-07-31 03:09:00','2019-07-31 03:09:00','test on win10, ie 11.706.17134.0'),(5,'MicrosoftWebDriver\r\n','17.17134','2019-07-31 03:09:23','2019-07-31 03:09:23','test on win10, Edge 17134'),(6,'appium','1.11.1','2019-07-31 03:11:13','2019-07-31 03:11:13','test on macos 10.12.6, android 4.4.4 & 5.0.2 & 8.1.0, ios 11.2'),(7,'appium','1.13.0','2019-07-31 03:34:04','2019-07-31 03:34:04','test on macos 10.14.6, android 8.1.0, ios 12.2 & 12.4');
/*!40000 ALTER TABLE `driver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobile_os`
--

DROP TABLE IF EXISTS `mobile_os`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `mobile_os` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `version` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobile_os`
--

LOCK TABLES `mobile_os` WRITE;
/*!40000 ALTER TABLE `mobile_os` DISABLE KEYS */;
INSERT INTO `mobile_os` VALUES (1,'iOS','12.4','2019-07-31 03:21:50','2019-07-31 03:21:50'),(2,'Android','8.1.0','2019-07-31 03:22:49','2019-07-31 03:22:49');
/*!40000 ALTER TABLE `mobile_os` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `platform_os`
--

DROP TABLE IF EXISTS `platform_os`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `platform_os` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `version` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `platform_os`
--

LOCK TABLES `platform_os` WRITE;
/*!40000 ALTER TABLE `platform_os` DISABLE KEYS */;
INSERT INTO `platform_os` VALUES (1,'Windows','Windows-10-10.0.17134-SP0','2019-07-31 06:24:15','2019-07-31 06:24:15'),(2,'Macos','Darwin-16.7.0-x86_64-i386-64bit','2019-07-31 06:24:38','2019-07-31 06:24:38');
/*!40000 ALTER TABLE `platform_os` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_case`
--

DROP TABLE IF EXISTS `test_case`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `test_case` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `test_function_id` int(11) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_case`
--

LOCK TABLES `test_case` WRITE;
/*!40000 ALTER TABLE `test_case` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_case` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_case_result`
--

DROP TABLE IF EXISTS `test_case_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `test_case_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test_case_id` int(11) NOT NULL,
  `test_round_id` int(11) NOT NULL,
  `error_message` varchar(3000) DEFAULT NULL,
  `screenshot` varchar(500) DEFAULT NULL,
  `video` varchar(500) DEFAULT NULL,
  `result` varchar(100) NOT NULL,
  `data_driven` varchar(1000) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_case_result`
--

LOCK TABLES `test_case_result` WRITE;
/*!40000 ALTER TABLE `test_case_result` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_case_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_environment`
--

DROP TABLE IF EXISTS `test_environment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `test_environment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_environment`
--

LOCK TABLES `test_environment` WRITE;
/*!40000 ALTER TABLE `test_environment` DISABLE KEYS */;
INSERT INTO `test_environment` VALUES (1,'INT'),(2,'QA'),(3,'Regression'),(4,'Staging'),(5,'Production');
/*!40000 ALTER TABLE `test_environment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_function`
--

DROP TABLE IF EXISTS `test_function`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `test_function` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `script_id` int(11) NOT NULL,
  `create_time` timestamp NOT NULL,
  `update_time` timestamp NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_function`
--

LOCK TABLES `test_function` WRITE;
/*!40000 ALTER TABLE `test_function` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_function` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_round`
--

DROP TABLE IF EXISTS `test_round`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `test_round` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `project_id` int(11) NOT NULL,
  `test_suite_id` int(11) NOT NULL,
  `browser_id` int(11) DEFAULT NULL,
  `device_id` int(11) DEFAULT NULL,
  `mobile_os_id` int(11) DEFAULT NULL,
  `platform_os_id` int(11) NOT NULL,
  `test_environment_id` int(11) NOT NULL,
  `test_type_id` int(11) NOT NULL,
  `ip` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `location` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_round`
--

LOCK TABLES `test_round` WRITE;
/*!40000 ALTER TABLE `test_round` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_round` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_script`
--

DROP TABLE IF EXISTS `test_script`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `test_script` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `project_id` int(11) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_script`
--

LOCK TABLES `test_script` WRITE;
/*!40000 ALTER TABLE `test_script` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_script` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_script_brief`
--

DROP TABLE IF EXISTS `test_script_brief`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `test_script_brief` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `script_id` int(11) NOT NULL,
  `version` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `maintainer` varchar(100) DEFAULT NULL,
  `file_created` date NOT NULL,
  `file_updated` date NOT NULL,
  `tag` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_script_brief`
--

LOCK TABLES `test_script_brief` WRITE;
/*!40000 ALTER TABLE `test_script_brief` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_script_brief` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_suite`
--

DROP TABLE IF EXISTS `test_suite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `test_suite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_suite`
--

LOCK TABLES `test_suite` WRITE;
/*!40000 ALTER TABLE `test_suite` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_suite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_type`
--

DROP TABLE IF EXISTS `test_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `test_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_type`
--

LOCK TABLES `test_type` WRITE;
/*!40000 ALTER TABLE `test_type` DISABLE KEYS */;
INSERT INTO `test_type` VALUES (1,'UnitTest'),(2,'Rest'),(3,'Web'),(4,'Mobile'),(5,'Windows');
/*!40000 ALTER TABLE `test_type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-25 17:09:01
