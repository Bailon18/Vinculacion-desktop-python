-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS vinculacion;
USE vinculacion;

-- Crear tabla carrera
CREATE TABLE IF NOT EXISTS carrera (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    estado BOOLEAN NOT NULL DEFAULT true
);

-- Crear tabla estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(255) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    tipo_identificacion VARCHAR(50) NOT NULL,
    nro_identificacion VARCHAR(50) NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    genero ENUM('M', 'F', 'Otro') NOT NULL,
    correo VARCHAR(255) NOT NULL UNIQUE,
    telefono VARCHAR(50),
    direccion TEXT,
    carrera_id INT,
    FOREIGN KEY (carrera_id) REFERENCES carrera(id)
);

-- Crear tabla institucion
CREATE TABLE IF NOT EXISTS institucion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    tipo_institucion VARCHAR(255) NOT NULL,
    estado BOOLEAN NOT NULL DEFAULT true,
    direccion TEXT,
    telefono VARCHAR(50)
);

-- Crear tabla proyecto
CREATE TABLE IF NOT EXISTS proyecto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    estado BOOLEAN NOT NULL DEFAULT true
);

-- Crear tabla tutores
CREATE TABLE IF NOT EXISTS tutores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(255) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    tipo_identificacion VARCHAR(50) NOT NULL,
    nro_identificacion VARCHAR(50) NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    genero ENUM('M', 'F', 'Otro') NOT NULL,
    correo VARCHAR(255) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    telefono VARCHAR(50),
    direccion TEXT,
    profesion VARCHAR(255),
    archivo_cv LONGBLOB
);

CREATE TABLE IF NOT EXISTS vinculacion (
  id INT NOT NULL AUTO_INCREMENT,
  fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  fecha_inicio DATE NOT NULL,
  codigo_ies VARCHAR(45) NOT NULL,
  campo_especifico VARCHAR(45) NOT NULL,
  periodo_academico VARCHAR(45) NOT NULL,
  institucion_id INT NOT NULL,
  tutores_id INT NOT NULL,
  proyecto_id INT NOT NULL,
  estado BOOLEAN NOT NULL DEFAULT TRUE,
  PRIMARY KEY (id),
  CONSTRAINT fk_vinculacion_institucion
    FOREIGN KEY (institucion_id)
    REFERENCES institucion (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_vinculacion_tutores1
    FOREIGN KEY (tutores_id)
    REFERENCES tutores (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_vinculacion_proyecto1
    FOREIGN KEY (proyecto_id)
    REFERENCES proyecto (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS estudiantes_vinculacion (
  id INT NOT NULL AUTO_INCREMENT,
  estudiantes_id INT NOT NULL,
  vinculacion_id INT NOT NULL,
  fecha_final DATE NULL DEFAULT NULL,
  estado_vinculacion ENUM('Pendiente', 'En Proceso', 'Culminado') NOT NULL DEFAULT 'Pendiente',
  nro_horas INT NOT NULL DEFAULT 0,
  PRIMARY KEY (id, estudiantes_id, vinculacion_id),
  CONSTRAINT fk_estudiantes_has_vinculacion_estudiantes1
    FOREIGN KEY (estudiantes_id)
    REFERENCES estudiantes (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_estudiantes_has_vinculacion_vinculacion1
    FOREIGN KEY (vinculacion_id)
    REFERENCES vinculacion (id)
    ON DELETE CASCADE 
    ON UPDATE NO ACTION
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


CREATE TABLE IF NOT EXISTS seguimiento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiantes_vinculacion_id INT NOT NULL,
    fecha_actividad DATE NOT NULL,
    horas_actividad INT NOT NULL,
    actividades TEXT,
    archivo_foto LONGBLOB,
    archivo_actividad LONGBLOB,
    tipo_archivo_actividad VARCHAR(50),
    observacion TEXT,
    fecha_seguimiento DATE NOT NULL,
    FOREIGN KEY (estudiantes_vinculacion_id) REFERENCES estudiantes_vinculacion(id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
);





