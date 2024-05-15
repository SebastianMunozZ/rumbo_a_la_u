USE rumbo_a_la_u;

-- Eliminar tablas si existen
DROP TABLE IF EXISTS USUARIOS;
DROP TABLE IF EXISTS PROFESORES;
DROP TABLE IF EXISTS ESTUDIANTES;
DROP TABLE IF EXISTS CURSOS;
DROP TABLE IF EXISTS INSCRIPCIONES;
DROP TABLE IF EXISTS MATERIALES;
DROP TABLE IF EXISTS NOTAS;
DROP TABLE IF EXISTS COMENTARIOS;
DROP TABLE IF EXISTS DISCUSIONES;
DROP TABLE IF EXISTS POSTS;
DROP TABLE IF EXISTS REGIONES;
DROP TABLE IF EXISTS PROVINCIAS;
DROP TABLE IF EXISTS COMUNAS;
DROP TABLE IF EXISTS NOTICIAS;
DROP TABLE IF EXISTS SHOPPING_SESSION;
DROP TABLE IF EXISTS CARRO;

-- Crear tabla de Usuarios
CREATE TABLE USUARIOS (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  apellido VARCHAR(255) NOT NULL,
  correo_electronico VARCHAR(255) NOT NULL,
  contrasena VARCHAR(255) NOT NULL,
  tipo_usuario VARCHAR(50) NOT NULL
);

-- Crear tabla de Profesores
CREATE TABLE PROFESORES (
  teacher_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  nombre VARCHAR(255) NOT NULL,
  apellido VARCHAR(255) NOT NULL,
  asignatura_que_ensena VARCHAR(100) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Crear tabla de Alumnos
CREATE TABLE ESTUDIANTES (
  student_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  ano_de_ingreso INT NOT NULL,
  nivel_de_educacion VARCHAR(100) NOT NULL,
  comuna_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (comuna_id) REFERENCES communes(commune_id)
);

-- Crear tabla de Cursos
CREATE TABLE CURSOS (
  course_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_del_curso VARCHAR(255) NOT NULL,
  descripcion TEXT,
  asignatura VARCHAR(100) NOT NULL,
  nivel_del_curso VARCHAR(100) NOT NULL,
  teacher_id INT NOT NULL,
  FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- Crear tabla de Inscripciones
CREATE TABLE INSCRIPCIONES (
  enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Crear tabla de Materiales del Curso
CREATE TABLE MATERIALES (
  material_id INT AUTO_INCREMENT PRIMARY KEY,
  course_id INT NOT NULL,
  titulo_del_material VARCHAR(255) NOT NULL,
  descripcion_del_material TEXT,
  archivo_adjunto VARCHAR(255),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Crear tabla de Calificaciones
CREATE TABLE NOTAS (
  grade_id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  calificacion DECIMAL(5, 2) NOT NULL,
  fecha_de_calificacion DATE NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Crear tabla de Comentarios del Curso
CREATE TABLE COMENTARIOS (
  comment_id INT AUTO_INCREMENT PRIMARY KEY,
  course_id INT NOT NULL,
  student_id INT NOT NULL,
  comentario TEXT NOT NULL,
  fecha_de_comentario DATETIME NOT NULL,
  FOREIGN KEY (course_id) REFERENCES courses(course_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Crear tabla de Foros de Discusión
CREATE TABLE DISCUSIONES (
  forum_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_del_foro VARCHAR(255) NOT NULL,
  descripcion TEXT,
  course_id INT NOT NULL,
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Crear tabla de Publicaciones del Foro
CREATE TABLE POSTS (
  post_id INT AUTO_INCREMENT PRIMARY KEY,
  forum_id INT NOT NULL,
  student_id INT NOT NULL,
  contenido_del_post TEXT NOT NULL,
  fecha_de_publicacion DATETIME NOT NULL,
  FOREIGN KEY (forum_id) REFERENCES discussion_forums(forum_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Crear tabla de Regiones
CREATE TABLE REGIONES (
  region_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_de_la_region VARCHAR(255) NOT NULL
);

-- Crear tabla de Provincias
CREATE TABLE PROVINCIAS (
  province_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_de_la_provincia VARCHAR(255) NOT NULL,
  region_id INT NOT NULL,
  FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

-- Crear tabla de Comunas
CREATE TABLE COMUNAS (
  commune_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_de_la_comuna VARCHAR(255) NOT NULL,
  province_id INT NOT NULL,
  FOREIGN KEY (province_id) REFERENCES provinces(province_id)
);

-- Crear tabla de Noticias
CREATE TABLE NOTICIAS (
  news_id INT AUTO_INCREMENT PRIMARY KEY,
  titulo_de_la_noticia VARCHAR(255) NOT NULL,
  contenido_de_la_noticia TEXT NOT NULL,
  fecha_de_publicacion DATETIME NOT NULL
);

CREATE TABLE SHOPPING_SESSION (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT,
  create_at TIMESTAMP,
  state BOOLEAN,
  FOREIGN KEY (usuario_id) REFERENCES USUARIOS(user_id)
);

CREATE TABLE CARRO(
  precio INT,
  cantidad INT,
  curso_id INT,
  shopping_session_id INT,
  FOREIGN KEY (curso_id) REFERENCES CURSOS(course_id),
  FOREIGN KEY (shopping_session_id) REFERENCES SHOPPING_SESSION(id),
  PRIMARY KEY (curso_id, shopping_session_id)
);