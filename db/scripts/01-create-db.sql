-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: portafalio_db
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `REGION`
--
-- Eliminar tablas si existen
DROP TABLE IF EXISTS `USUARIOS`;
DROP TABLE IF EXISTS `PROFESORES`;
DROP TABLE IF EXISTS `ESTUDIANTES`;
DROP TABLE IF EXISTS `CURSOS`;
DROP TABLE IF EXISTS `INSCRIPCIONES`;
DROP TABLE IF EXISTS `MATERIALES`;
DROP TABLE IF EXISTS `NOTAS`;
DROP TABLE IF EXISTS `COMENTARIOS`;
DROP TABLE IF EXISTS `DISCUSIONES`;
DROP TABLE IF EXISTS `POSTS`;
DROP TABLE IF EXISTS `REGIONES`;
DROP TABLE IF EXISTS `PROVINCIAS`;
DROP TABLE IF EXISTS `COMUNAS`;
DROP TABLE IF EXISTS `NOTICIAS`;

-- Crear tabla de Usuarios
CREATE TABLE `USUARIOS` (
  `user_id` INT AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `correo_electronico` VARCHAR(255) NOT NULL,
  `contrasena` VARCHAR(255) NOT NULL,
  `tipo_usuario` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla de Profesores
CREATE TABLE `PROFESORES` (
  `teacher_id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `asignatura_que_ensena` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`teacher_id`),
  FOREIGN KEY (`user_id`) REFERENCES `USUARIOS`(`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla de Alumnos
CREATE TABLE `ESTUDIANTES` (
  `student_id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `ano_de_ingreso` INT NOT NULL,
  `nivel_de_educacion` VARCHAR(100) NOT NULL,
  `comuna_id` INT NOT NULL,
  PRIMARY KEY (`student_id`),
  FOREIGN KEY (`user_id`) REFERENCES `USUARIOS`(`user_id`),
  FOREIGN KEY (`comuna_id`) REFERENCES `COMUNAS`(`commune_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla de Cursos
CREATE TABLE `CURSOS` (
  `course_id` INT AUTO_INCREMENT,
  `nombre_del_curso` VARCHAR(255) NOT NULL,
  `descripcion` TEXT,
  `asignatura` VARCHAR(100) NOT NULL,
  `nivel_del_curso` VARCHAR(100) NOT NULL,
  `teacher_id` INT NOT NULL,
  PRIMARY KEY (`course_id`),
  FOREIGN KEY (`teacher_id`) REFERENCES `PROFESORES`(`teacher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla de Inscripciones
CREATE TABLE `INSCRIPCIONES` (
  `enrollment_id` INT AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`enrollment_id`),
  FOREIGN KEY (`student_id`) REFERENCES `ESTUDIANTES`(`student_id`),
  FOREIGN KEY (`course_id`) REFERENCES `CURSOS`(`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla de Materiales del Curso
CREATE TABLE `MATERIALES` (
  `material_id` INT AUTO_INCREMENT,
  `course_id` INT NOT NULL,
  `titulo_del_material` VARCHAR(255) NOT NULL,
  `descripcion_del_material` TEXT,
  `archivo_adjunto` VARCHAR(255),
  PRIMARY KEY (`material_id`),
  FOREIGN KEY (`course_id`) REFERENCES `CURSOS`(`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla de Calificaciones
CREATE TABLE `NOTAS` (
  `grade_id` INT AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  `calificacion` DECIMAL(5, 2) NOT NULL,
  `fecha_de_calificacion` DATE NOT NULL,
  PRIMARY KEY (`grade_id`),
  FOREIGN KEY (`student_id`) REFERENCES `ESTUDIANTES`(`student_id`),
  FOREIGN KEY (`course_id`) REFERENCES `CURSOS`(`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
-- Crear tabla de Comentarios del Curso
CREATE TABLE `COMENTARIOS` (
  `comment_id` INT AUTO_INCREMENT,
  `course_id` INT NOT NULL,
  `student_id` INT NOT NULL,
  `comentario` TEXT NOT NULL,
  `fecha_de_comentario` DATETIME NOT NULL,
  PRIMARY KEY (`comment_id`),
  FOREIGN KEY (`course_id`) REFERENCES `CURSOS`(`course_id`),
  FOREIGN KEY (`student_id`) REFERENCES `ESTUDIANTES`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla de Foros de Discusión
CREATE TABLE `DISCUSIONES` (
  `forum_id` INT AUTO_INCREMENT,
  `nombre_del_foro` VARCHAR(255) NOT NULL,
  `descripcion` TEXT,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`forum_id`),
  FOREIGN KEY (`course_id`) REFERENCES `CURSOS`(`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla de Publicaciones del Foro
CREATE TABLE `POSTS` (
  `post_id` INT AUTO_INCREMENT,
  `forum_id` INT NOT NULL,
  `student_id` INT NOT NULL,
  `contenido_del_post` TEXT NOT NULL,
  `fecha_de_publicacion` DATETIME NOT NULL,
  PRIMARY KEY (`post_id`),
  FOREIGN KEY (`forum_id`) REFERENCES `DISCUSIONES`(`forum_id`),
  FOREIGN KEY (`student_id`) REFERENCES `ESTUDIANTES`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla de Regiones
CREATE TABLE `REGIONES` (
  `region_id` INT AUTO_INCREMENT,
  `nombre_de_la_region` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`region_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla de Provincias
CREATE TABLE `PROVINCIAS` (
  `province_id` INT AUTO_INCREMENT,
  `nombre_de_la_provincia` VARCHAR(255) NOT NULL,
  `region_id` INT NOT NULL,
  PRIMARY KEY (`province_id`),
  FOREIGN KEY (`region_id`) REFERENCES `REGIONES`(`region_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla de Comunas
CREATE TABLE `COMUNAS` (
  `commune_id` INT AUTO_INCREMENT,
  `nombre_de_la_comuna` VARCHAR(255) NOT NULL,
  `province_id` INT NOT NULL,
  PRIMARY KEY (`commune_id`),
  FOREIGN KEY (`province_id`) REFERENCES `PROVINCIAS`(`province_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla de Noticias
CREATE TABLE `NOTICIAS` (
  `news_id` INT AUTO_INCREMENT,
  `titulo_de_la_noticia` VARCHAR(255) NOT NULL,
  `contenido_de_la_noticia` TEXT NOT NULL,
  `fecha_de_publicacion` DATETIME NOT NULL,
  PRIMARY KEY (`news_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `REGIONES`
--

LOCK TABLES `REGIONES` WRITE;
/*!40000 ALTER TABLE `REGIONES` DISABLE KEYS */;
INSERT INTO REGIONES (nombre_de_la_region) VALUES
('Región de Arica y Parinacota'),
('Región de Tarapacá'),
('Región de Antofagasta'),
('Región de Atacama'),
('Región de Coquimbo'),
('Región de Valparaíso'),
('Región Metropolitana de Santiago'),
('Región del Libertador General Bernardo O''Higgins'),
('Región del Maule'),
('Región del Ñuble'),
('Región del Biobío'),
('Región de La Araucanía'),
('Región de Los Ríos'),
('Región de Los Lagos'),
('Región de Aysén del General Carlos Ibáñez del Campo'),
('Región de Magallanes y de la Antártica Chilena');
/*!40000 ALTER TABLE `REGIONES` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `PROVINCIAS` WRITE;
/*!40000 ALTER TABLE `PROVINCIAS` DISABLE KEYS */;
INSERT INTO PROVINCIAS (nombre_de_la_provincia, region_id) VALUES
('Arica', 1),
('Parinacota', 1),
('Iquique', 2),
('Tamarugal', 2),
('Antofagasta', 3),
('El Loa', 3),
('Tocopilla', 3),
('Chañaral', 4),
('Copiapó', 4),
('Huasco', 4),
('Elqui', 5),
('Choapa', 5),
('Limarí', 5),
('Valparaíso', 6),
('Isla de Pascua', 6),
('Los Andes', 6),
('Petorca', 6),
('Quillota', 6),
('San Antonio', 6),
('San Felipe de Aconcagua', 6),
('Marga Marga', 6),
('Santiago', 7),
('Cordillera', 7),
('Chacabuco', 7),
('Maipo', 7),
('Melipilla', 7),
('Talagante', 7),
('Cachapoal', 8),
('Cardenal Caro', 8),
('Colchagua', 8),
('Curicó', 9),
('Diguillín', 9),
('Linares', 9),
('Talca', 9),
('Itata', 10),
('Diguillín', 10),
('Punilla', 10),
('Arauco', 11),
('Biobío', 11),
('Concepción', 11),
('Ñuble', 10),
('Cautín', 12),
('Malleco', 12),
('Valdivia', 13),
('Ranco', 13),
('Osorno', 14),
('Llanquihue', 14),
('Chiloé', 14),
('Palena', 14),
('Aysén', 15),
('Capitán Prat', 15),
('Coihaique', 15),
('General Carrera', 15),
('Magallanes', 16),
('Antártica Chilena', 16),
('Tierra del Fuego', 16),
('Última Esperanza', 16);
/*!40000 ALTER TABLE `PROVINCIAS` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `COMUNAS` WRITE;
/*!40000 ALTER TABLE `COMUNAS` DISABLE KEYS */;
INSERT INTO COMUNAS (nombre_de_la_comuna, province_id) VALUES
('Arica', 1),
('Camarones', 1),
('Putre', 2),
('General Lagos', 2),
('Iquique', 3),
('Alto Hospicio', 3),
('Pozo Almonte', 4),
('Camiña', 4),
('Colchane', 4),
('Huara', 4),
('Pica', 4),
('Antofagasta', 5),
('Mejillones', 5),
('Sierra Gorda', 5),
('Taltal', 5),
('Calama', 6),
('Ollagüe', 6),
('San Pedro de Atacama', 6),
('Tocopilla', 7),
('María Elena', 7),
('Copiapó', 8),
('Caldera', 8),
('Tierra Amarilla', 8),
('Chañaral', 9),
('Diego de Almagro', 9),
('Vallenar', 10),
('Alto del Carmen', 10),
('Freirina', 10),
('Huasco', 10),
('La Serena', 11),
('Coquimbo', 11),
('Andacollo', 11),
('La Higuera', 11),
('Paihuano', 11),
('Vicuña', 11),
('Illapel', 12),
('Canela', 12),
('Los Vilos', 12),
('Salamanca', 12),
('Ovalle', 13),
('Combarbalá', 13),
('Monte Patria', 13),
('Punitaqui', 13),
('Río Hurtado', 13),
('Isla de Pascua', 14),
('Calle Larga', 15),
('Los Andes', 15),
('Rinconada', 15),
('San Esteban', 15),
('La Ligua', 16),
('Cabildo', 16),
('Papudo', 16),
('Petorca', 16),
('Zapallar', 16),
('Quillota', 17),
('Calera', 17),
('Hijuelas', 17),
('La Cruz', 17),
('Nogales', 17),
('San Antonio', 18),
('Algarrobo', 18),
('Cartagena', 18),
('El Quisco', 18),
('El Tabo', 18),
('Santo Domingo', 18),
('San Felipe', 19),
('Catemu', 19),
('Llaillay', 19),
('Panquehue', 19),
('Putaendo', 19),
('Santa María', 19),
('Valparaíso', 20),
('Casablanca', 20),
('Concón', 20),
('Juan Fernández', 20),
('Puchuncaví', 20),
('Quilpué', 20),
('Quintero', 20),
('Villa Alemana', 20),
('Viña del Mar', 20),
('Isla de Maipo', 21),
('El Monte', 21),
('Padre Hurtado', 21),
('Peñaflor', 21),
('Talagante', 21),
('Codegua', 22),
('Coínco', 22),
('Coltauco', 22),
('Doñihue', 22),
('Graneros', 22),
('Las Cabras', 22),
('Machalí', 22),
('Malloa', 22),
('Mostazal', 22),
('Olivar', 22),
('Peumo', 22),
('Pichidegua', 22),
('Quinta de Tilcoco', 22),
('Rancagua', 22),
('Requínoa', 22),
('Rengo', 22),
('San Vicente', 22),
('La Estrella', 23),
('Litueche', 23),
('Marchihue', 23),
('Navidad', 23),
('Peredones', 23),
('Pichilemu', 23),
('Chépica', 24),
('Chimbarongo', 24),
('Lolol', 24),
('Nancagua', 24),
('Palmilla', 24),
('Peralillo', 24),
('Placilla', 24),
('Pumanque', 24),
('San Fernando', 24),
('Santa Cruz', 24),
('Cauquenes', 25),
('Chanco', 25),
('Longaví', 25),
('Parral', 25);
/*!40000 ALTER TABLE `COMUNAS` ENABLE KEYS */;
UNLOCK TABLES;
--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$QZU96Zk7h9LHSdoQMMy5Am$CPbDc1DfmMfxsb5X3TjuOiIt8aoGuynrI6equ+6+AUc=',NULL,1,'admin','','','admin@admin.cl',1,1,'2024-04-20 00:00:35.844174');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-04-19 23:57:07.504316'),(2,'auth','0001_initial','2024-04-19 23:57:08.662459'),(3,'admin','0001_initial','2024-04-19 23:57:08.949871'),(4,'admin','0002_logentry_remove_auto_add','2024-04-19 23:57:08.973872'),(5,'admin','0003_logentry_add_action_flag_choices','2024-04-19 23:57:08.997043'),(6,'contenttypes','0002_remove_content_type_name','2024-04-19 23:57:09.248868'),(7,'auth','0002_alter_permission_name_max_length','2024-04-19 23:57:09.342090'),(8,'auth','0003_alter_user_email_max_length','2024-04-19 23:57:09.390883'),(9,'auth','0004_alter_user_username_opts','2024-04-19 23:57:09.404261'),(10,'auth','0005_alter_user_last_login_null','2024-04-19 23:57:09.531634'),(11,'auth','0006_require_contenttypes_0002','2024-04-19 23:57:09.544116'),(12,'auth','0007_alter_validators_add_error_messages','2024-04-19 23:57:09.566726'),(13,'auth','0008_alter_user_username_max_length','2024-04-19 23:57:09.693140'),(14,'auth','0009_alter_user_last_name_max_length','2024-04-19 23:57:09.791677'),(15,'auth','0010_alter_group_name_max_length','2024-04-19 23:57:09.815976'),(16,'auth','0011_update_proxy_permissions','2024-04-19 23:57:09.830420'),(17,'auth','0012_alter_user_first_name_max_length','2024-04-19 23:57:09.956120'),(18,'sessions','0001_initial','2024-04-19 23:57:10.042263');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

DELIMITER //
DROP trigger IF EXISTS after_usuario_insert;
DELIMITER //
CREATE TRIGGER after_usuario_insert
AFTER INSERT ON USUARIOS
FOR EACH ROW
BEGIN
    IF NEW.tipo_usuario = 1 THEN
        INSERT INTO ESTUDIANTES (user_id, ano_de_ingreso, nivel_de_educacion, comuna_id)
        VALUES (NEW.user_id, '2024', 'Cuarto Medio', '5');
    END IF;
END //
DELIMITER ;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-19 20:03:39
