
-- Eliminar la base de datos si existe
DROP DATABASE IF EXISTS dbscmlul0fs4ii;

-- Crear la base de datos
CREATE DATABASE dbscmlul0fs4ii;

-- Utilizar la base de datos
USE dbscmlul0fs4ii;



-- ===============================================
-- TABLA: instituciones_educativas
-- Propósito: Almacena información sobre las instituciones educativas.
-- ===============================================
CREATE TABLE instituciones_educativas (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único de la institución
    nombre_institucion VARCHAR(255), -- Nombre de la institución
    tipo_institucion VARCHAR(50), -- Tipo de institución (ej. universidad, colegio, etc.)
    direccion VARCHAR(255), -- Dirección física de la institución
	estado VARCHAR(50) DEFAULT 'Activo' -- Estado por defecto "Activo"
);

-- ===============================================
-- TABLA: roles
-- Propósito: Almacena roles de usuarios en el sistema.
-- ===============================================
CREATE TABLE roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único del rol
    role_name VARCHAR(50) NOT NULL -- Nombre del rol (ej. Administrador, Tutor)
);

-- ===============================================
-- TABLA: proyectos
-- Propósito: Almacena información sobre los proyectos a realizar dentro de la vinculacion.
-- ===============================================
CREATE TABLE proyectos (
    id_proyecto INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único del proyecto
    nombre_proyecto VARCHAR(300) NOT NULL, -- Nombre del proyecto
    estado VARCHAR(50) DEFAULT 'Activo' -- Estado por defecto "Activo"
);

-- ===============================================
-- TABLA: carreras
-- Propósito: Almacena información sobre las carreras o programas académicos.
-- ===============================================
CREATE TABLE carreras (
    id_carrera INT PRIMARY KEY AUTO_INCREMENT, -- Identificador único de la carrera
    codigo_carrera VARCHAR(50), -- Código de la carrera (ej. 650612A-P-01)
    nombre_carrera VARCHAR(255) -- Nombre de la carrera
);

-- ===============================================
-- TABLA: usuarios
-- Propósito: Almacena información sobre los usuarios del sistema.
-- ===============================================
CREATE TABLE usuarios (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único del usuario
    contrasena VARCHAR(100) NOT NULL, -- Contraseña del usuario
    identificacion VARCHAR(50), -- Identificación del usuario (ej. -- 080374405-1)
    role_id INT, -- ID del rol asignado al usuario
    nombre VARCHAR(100), -- Nombre del usuario
    apellido VARCHAR(100), -- Apellido del usuario
    correo_electronico VARCHAR(100), -- Correo electrónico del usuario
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Fecha de registro del usuario
    estado VARCHAR(50) DEFAULT 'Activo', -- Estado por defecto "Activo"
    FOREIGN KEY (role_id) REFERENCES roles(role_id) -- Clave foránea a la tabla roles
);

-- ===============================================
-- TABLA: estudiantes
-- Propósito: Almacena información sobre los estudiantes.
-- ===============================================
CREATE TABLE estudiantes (
    estudiante_id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único del estudiante
    tipo_identificacion VARCHAR(50), -- Tipo de identificación del estudiante
    identificacion VARCHAR(50), -- Identificación del estudiante (ej. número de identificación)
    nombres_apellidos VARCHAR(255), -- Nombres y apellidos del estudiante
    codigo_carrera INT, -- Código de la carrera del estudiante
    FOREIGN KEY (codigo_carrera) REFERENCES carreras(id_carrera) -- Clave foránea a la tabla carreras
);

-- ===============================================
-- TABLA: vinculaciones
-- Propósito: Almacena información sobre las vinculaciones de los estudiantes.
-- ===============================================
CREATE TABLE vinculaciones (
    vinculacion_id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único de la vinculación
    estudiante_id INT, -- ID del estudiante vinculado
    periodo_academico VARCHAR(50), -- Periodo académico de la vinculación (ej. P1-2023)
    codigo_ies INT, -- Código de la institución educativa (ej. 1-6A)
    fecha_inicio DATE, -- Fecha de inicio de la vinculación
    fecha_fin DATE, -- Fecha de fin de la vinculación
    numero_horas INT DEFAULT 0, -- Número de horas de la vinculación
    campo_especifico VARCHAR(255), -- Descripción o campo específico de la vinculación
    identificacion_tutor INT, -- ID del tutor vinculado
    codigo_institucion INT, -- Referencia a la tabla instituciones_educativas
    id_proyecto INT, -- ID del proyecto vinculado
    estado VARCHAR(50) DEFAULT 'Pendiente', -- Estado por defecto "pendiente"
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Fecha de registro de la vinculación
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(estudiante_id) ON DELETE CASCADE,
    FOREIGN KEY (identificacion_tutor) REFERENCES usuarios(user_id), -- Clave foránea a la tabla usuarios
    FOREIGN KEY (codigo_institucion) REFERENCES instituciones_educativas(id), -- Clave foránea a instituciones_educativas
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto) -- Clave foránea a la tabla proyectos
);

-- ===============================================
-- TABLA: seguimientos
-- Propósito: Almacena información sobre los seguimientos realizados.
-- ===============================================
CREATE TABLE seguimientos (
    seguimiento_id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único del seguimiento
    vinculacion_id INT, -- ID de la vinculación relacionada con el seguimiento
    fecha_seguimiento TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Fecha del seguimiento
    observaciones TEXT, -- Observaciones del seguimiento
    tutor_id INT, -- ID del tutor relacionado con el seguimiento
    horas_seguimiento INT, -- Horas del seguimiento
    FOREIGN KEY (vinculacion_id) REFERENCES vinculaciones(vinculacion_id) ON DELETE CASCADE,
    FOREIGN KEY (tutor_id) REFERENCES usuarios(user_id) -- Clave foránea a la tabla usuarios
);


CREATE TABLE informes (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	fecha DATE,
    mes VARCHAR(255),
    periodo_academico VARCHAR(50),
    tutor_id INT,
    FOREIGN KEY (tutor_id) REFERENCES usuarios(user_id)
);

CREATE TABLE fichas (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    periodo_academico VARCHAR(50),
    is_ficha BOOLEAN,
    tutor_id INT,
    FOREIGN KEY (tutor_id) REFERENCES usuarios(user_id)
);

CREATE TABLE memorandum (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    periodo_academico VARCHAR(50),
    is_memorandum BOOLEAN,
    tutor_id INT,
    FOREIGN KEY (tutor_id) REFERENCES usuarios(user_id)
);




