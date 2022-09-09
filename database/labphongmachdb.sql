-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: labphongmachdb
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `healthcertification`
--

DROP TABLE IF EXISTS `healthcertification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `healthcertification` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_date` datetime NOT NULL,
  `symptoms` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `disease_prediction` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `patient_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `patient_id` (`patient_id`),
  CONSTRAINT `healthcertification_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `healthcertification`
--

LOCK TABLES `healthcertification` WRITE;
/*!40000 ALTER TABLE `healthcertification` DISABLE KEYS */;
INSERT INTO `healthcertification` VALUES (1,'2021-05-17 10:30:00','Đau bụng và ợ chua','Viêm loét dạ dày',1),(2,'2021-05-18 10:30:00','Xây xẫm khi đứng lên','Tuột huyết áp',2),(3,'2021-06-18 10:30:00','Sưng mắt cá chân','Lệch sơmi',3),(4,'2021-12-18 10:30:00','Ho nhiều và đau họng','Viêm họng',4),(5,'2021-12-19 10:30:00','Sốt','Sốt',5);
/*!40000 ALTER TABLE `healthcertification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine`
--

DROP TABLE IF EXISTS `medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicine` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `composition` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `quantity` int NOT NULL,
  `unit` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `howtopack` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` float NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine`
--

LOCK TABLES `medicine` WRITE;
/*!40000 ALTER TABLE `medicine` DISABLE KEYS */;
INSERT INTO `medicine` VALUES (1,'Paracetamol 500mg','500mg Paracetamol cùng với một số tá dược khác như ethanol, magie stearate, gelatin,…','Dùng 1 viên/liều, mỗi liều cách nhau 6 giờ, tối đa 4 viên/ngày.',48,'Viên','Hộp 4 vỉ x 16 viên',45000,1),(2,'Panadol Extra With Optizorb','Paracetamol, caffeine','500 mg Paracetamol, 65 mg Caffeine',20,'Viên','Hộp 12 vỉ x 10 viên',5000,1),(3,'Thuốc ho Bổ phế Nam Hà','Dextromethorphan HBr, chlorpheniramine maleate, natri citrate, ammonium, glyceryl guaiacolate.','Dextromethorphane bromhydrate 5 mg, Chlorphéniramine maléate 1,33 mg,Phénylpropanolamine chlorhydrate 8,3 mg, Sodium citrate 133 mg, Ammonium chlorure 50 mg, Glycéryl guaiacolate 50 mg.',50,'Viên','Hộp 25 vỉ x 4 viên',2000,1),(4,'Panadol Extra With Optizorb','Cefuroxim (dạng Cefuroxim axetil) 500mg','500 mg Paracetamol, 65 mg Caffeine',50,'Viên','Chai 50 viên',1600,1),(5,'Thuốc dạ dày chữ P – Phosphalugel','Aluminum phosphate dạng keo.','Thuốc kháng axit dạ dày. Có tác dụng nhanh trong việc giảm đau, tạo lớp màng bảo vệ và làm lành những tổn thương của cơ quan tiêu hóa.',52,'Gói','Hộp 26 gói',3800,1);
/*!40000 ALTER TABLE `medicine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dateofbirth` datetime NOT NULL,
  `sex` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
  `idcard` varchar(12) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_of_registration` datetime DEFAULT NULL,
  `address` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone_number` varchar(11) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (1,'Nguyễn Trùm','2001-11-07 00:00:00','Nam','123456789199','2021-09-11 00:00:00','66 Âu Cơ, phường 15, quận Tân BÌnh','0986356666','boss@gmail.com'),(2,'Bùi Thị','2005-11-07 00:00:00','Nữ','123456789098','2021-10-11 00:00:00','Trần Hải, phường 15, quận Bình Tân','0777356666','btthi@gmail.com'),(3,'Trần Mỹ','2007-10-08 00:00:00','Nữ','233356789098','2021-07-11 00:00:00','Lạc Long Quân, phường 15, quận Bình Tân','0978356666','myy@gmail.com'),(4,'Triệu Lệ Dĩnh','2002-10-08 00:00:00','Nữ','100056789098','2021-07-29 00:00:00','Nguyễn Tâm, phường 15, quận Bình Tân','0794356666','ledinh@gmail.com'),(5,'Địch Lệ Nhiệt Ba','2013-03-08 00:00:00','Nữ','100056747893','2021-03-29 00:00:00','Quốc lộ, phường 15, quận Bình Chánh','0222356666','nhietba@gmail.com');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prescription`
--

DROP TABLE IF EXISTS `prescription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prescription` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `created_date` datetime NOT NULL,
  `healthCertification_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `healthCertification_id` (`healthCertification_id`),
  CONSTRAINT `prescription_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `prescription_ibfk_2` FOREIGN KEY (`healthCertification_id`) REFERENCES `healthcertification` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prescription`
--

LOCK TABLES `prescription` WRITE;
/*!40000 ALTER TABLE `prescription` DISABLE KEYS */;
INSERT INTO `prescription` VALUES (1,3,'2021-05-17 11:30:00',1),(2,3,'2021-05-18 11:30:00',2),(3,3,'2021-06-18 11:30:00',3),(4,3,'2021-12-18 11:30:00',4),(5,3,'2021-12-19 11:30:00',5);
/*!40000 ALTER TABLE `prescription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prescriptiondetail`
--

DROP TABLE IF EXISTS `prescriptiondetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prescriptiondetail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `prescription_id` int NOT NULL,
  `medicine_id` int NOT NULL,
  `quantity` int NOT NULL,
  `using` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`,`prescription_id`,`medicine_id`),
  KEY `prescription_id` (`prescription_id`),
  KEY `medicine_id` (`medicine_id`),
  CONSTRAINT `prescriptiondetail_ibfk_1` FOREIGN KEY (`prescription_id`) REFERENCES `prescription` (`id`),
  CONSTRAINT `prescriptiondetail_ibfk_2` FOREIGN KEY (`medicine_id`) REFERENCES `medicine` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prescriptiondetail`
--

LOCK TABLES `prescriptiondetail` WRITE;
/*!40000 ALTER TABLE `prescriptiondetail` DISABLE KEYS */;
INSERT INTO `prescriptiondetail` VALUES (1,1,5,9,'Uống 2 lần(Sáng, chiều) trước khi ăn 30p.'),(2,2,4,6,'Uống 3 lần 1 ngày sáng, trưa, chiều sau khi ăn.'),(3,3,1,4,'Uống 2 lần(Sáng, chiều) sau khi ăn.'),(4,4,3,3,'Uống 3 lần(Sáng, trưa, chiều) sau khi ăn.'),(5,5,1,4,'Uống 2 lần(Sáng, Tối) sau khi ăn.');
/*!40000 ALTER TABLE `prescriptiondetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipt`
--

DROP TABLE IF EXISTS `receipt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipt` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `created_id` datetime DEFAULT NULL,
  `patient_id` int NOT NULL,
  `prescription_id` int NOT NULL,
  `regulation_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `patient_id` (`patient_id`),
  KEY `prescription_id` (`prescription_id`),
  KEY `regulation_id` (`regulation_id`),
  CONSTRAINT `receipt_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `receipt_ibfk_2` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`id`),
  CONSTRAINT `receipt_ibfk_3` FOREIGN KEY (`prescription_id`) REFERENCES `prescription` (`id`),
  CONSTRAINT `receipt_ibfk_4` FOREIGN KEY (`regulation_id`) REFERENCES `regulations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipt`
--

LOCK TABLES `receipt` WRITE;
/*!40000 ALTER TABLE `receipt` DISABLE KEYS */;
INSERT INTO `receipt` VALUES (1,2,'2021-05-17 12:30:00',1,1,1),(2,2,'2021-05-18 12:30:00',2,2,1),(3,2,'2021-06-18 12:30:00',3,3,1),(4,2,'2021-12-18 12:30:00',4,4,1),(5,2,'2021-12-19 12:30:00',5,5,1);
/*!40000 ALTER TABLE `receipt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipt_detail`
--

DROP TABLE IF EXISTS `receipt_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipt_detail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `medicine_id` int NOT NULL,
  `receipt_id` int NOT NULL,
  `quantity` int NOT NULL,
  `price` float NOT NULL,
  PRIMARY KEY (`id`,`medicine_id`,`receipt_id`),
  KEY `medicine_id` (`medicine_id`),
  KEY `receipt_id` (`receipt_id`),
  CONSTRAINT `receipt_detail_ibfk_1` FOREIGN KEY (`medicine_id`) REFERENCES `medicine` (`id`),
  CONSTRAINT `receipt_detail_ibfk_2` FOREIGN KEY (`receipt_id`) REFERENCES `receipt` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipt_detail`
--

LOCK TABLES `receipt_detail` WRITE;
/*!40000 ALTER TABLE `receipt_detail` DISABLE KEYS */;
INSERT INTO `receipt_detail` VALUES (1,5,1,9,3800),(2,4,2,6,1600),(3,1,3,4,45000),(4,3,4,3,2000),(5,1,5,4,45000);
/*!40000 ALTER TABLE `receipt_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regulations`
--

DROP TABLE IF EXISTS `regulations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regulations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `create_date` datetime DEFAULT NULL,
  `quantity_patient` int NOT NULL,
  `patient_price` float NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regulations`
--

LOCK TABLES `regulations` WRITE;
/*!40000 ALTER TABLE `regulations` DISABLE KEYS */;
INSERT INTO `regulations` VALUES (1,'2021-12-19 11:14:50',30,100000,1);
/*!40000 ALTER TABLE `regulations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_of_birth` datetime NOT NULL,
  `sex` enum('Nam','Nữ') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `certificate` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `joined_date` datetime DEFAULT NULL,
  `avatar` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_role` enum('ADMIN','DOCTOR','NURSE') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Lê Phát Đạt','2001-04-27 00:00:00','Nam','422A/17 Bờ Đắp Mới, An Phú Tây, Bình Chánh','Có chứng chỉ hành nghề','admin00998','admin00998',1,'2021-12-19 09:30:00','','ADMIN'),(2,'Nguyễn Thị Tâm','2001-10-23 00:00:00','Nữ','363 Chiến Lược, Bình Trị Đông A, Bình Tân','Có chứng chỉ hành nghề','ntam231001','ntam231001',1,'2021-12-19 11:30:00','','NURSE'),(3,'Nguyễn Thành Hưng','2001-03-04 00:00:00','Nam','65 Xô Viết Nghệ Tỉnh, phường 11, Tân Bình','Có chứng chỉ hành nghề','dhung040301','dhung040301',1,'2021-12-19 13:30:00','','DOCTOR');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-09 16:32:36
