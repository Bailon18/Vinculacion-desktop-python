
INSERT INTO instituciones_educativas (nombre_institucion, tipo_institucion, direccion)
VALUES
    ('Universidad San Francisco de Quito', 'Universidad', 'Cumbayá, Quito'),
    ('Universidad de las Américas', 'Universidad', 'Quito'),
    ('Escuela Politécnica Nacional', 'Universidad', 'Quito'),
    ('Universidad Central del Ecuador', 'Universidad', 'Quito');

-- Inserción de roles predefinidos
INSERT INTO roles (role_name) VALUES 
    ('Administrador'),
    ('Tutor');

-- Inserción de proyectos en la tabla 'proyectos'
INSERT INTO proyectos (nombre_proyecto) VALUES
    ('Manejo de desechos tecnológicos y su repercusión en la salud de los habitantes de la zona sur de Manabí (Gestión Integral de los desechos tecnológicos en la zona sur de Manabí)'),
    ('Análisis de textos de redes sociales por medio de técnicas de procesamiento del lenguaje natural.'),
    ('Herramientas de inteligencia artificial aplicadas a la transformación digital para el desarrollo socioeconómico de la zona sur de Manabí.'),
    ('Aplicación de minería de proceso a empresas, Fase II.');
    
INSERT INTO carreras (codigo_carrera, nombre_carrera)
VALUES
    ('650612A-P-01', 'Ingeniería en Sistemas'),
    ('650612A-P-02', 'Ingeniería Informática'),
    ('650612A-P-03', 'Tecnología de la Información'),
    ('650612A-P-04', 'Ciencias de la Computación'),
    ('650612A-P-05', 'Ingeniería de Software');
    
-- Inserción de usuarios tipo Tutor en la tabla 'usuarios'
INSERT INTO usuarios (contrasena, identificacion, role_id, nombre, apellido, correo_electronico)
VALUES
    ('admin', '131021797-9', 2, 'Leopoldo Vinicio', 'Venegas Loor', 'venegas@gmail.com'),
    ('admin', '130709493-6', 2, 'Roberto Wellington', 'Acuña Caicedo', 'acuna@gmail.com'),
    ('admin', '1305516740', 2, 'Antonieta Del Carmen', 'Rodriguez Gonzales', 'rodriguez@gmail.com'),
    ('admin', '1311396376', 2, 'Marlon Ruben', 'Barcia Moreira', 'barcia@gmail.com'),
    ('admin', '012345678-9', 1, 'Pedro', 'Pablo', 'admin@gmail.com');


-- Insertar estudiantes y guardar sus IDs
INSERT INTO estudiantes (tipo_identificacion, identificacion, nombres_apellidos, codigo_carrera)
VALUES
    ('Cedula', '080374405-1', 'Juan Perez', 1),
    ('Cedula', '080374405-2', 'María González', 2),
    ('Cedula', '080374405-3', 'Carlos López', 3),
    ('Cedula', '080374405-4', 'Ana Rodríguez', 4),
    ('Cedula', '080374405-5', 'Jorge Martínez', 2);

-- Insertar vinculaciones utilizando los IDs de estudiantes
INSERT INTO vinculaciones (estudiante_id, periodo_academico, codigo_ies, fecha_inicio, fecha_fin, numero_horas, campo_especifico, identificacion_tutor, codigo_institucion, id_proyecto)
VALUES
    (1, 'P1-2023', '1001', '2023-01-15', '2023-06-15', 180, '1-6A', 1, 1, 1),
    (2, 'P2-2023', '1002', '2023-02-01', '2023-07-01', 150, '2-6B', 1, 2, 2),
    (3, 'P2-2023', '1003', '2023-02-15', '2023-07-15', 200, '3-6C', 2, 3, 3),
    (4, 'P3-2023', '1004', '2023-03-01', '2023-08-01', 160, '4-6D', 2, 4, 4),
    (5, 'P3-2023', '1005', '2023-03-15', '2023-08-15', 190, '5-6E', 2, 2, 1);


DROP PROCEDURE IF EXISTS ListarVinculaciones;
DELIMITER $$
CREATE PROCEDURE ListarVinculaciones(
    IN limite INT
)
BEGIN
    SELECT
        vinculaciones.vinculacion_id AS `Vinculación ID`,
        DATE_FORMAT(vinculaciones.fecha_registro, '%Y-%m-%d %H:%i:%s') AS `Fecha de Registro de la Vinculación`,
        estudiantes.nombres_apellidos AS `Nombre del Estudiante`,
        DATE_FORMAT(vinculaciones.fecha_inicio, '%Y-%m-%d') AS `Fecha Inicio`,
        vinculaciones.periodo_academico AS `Período Académico`,
        CONCAT(usuarios.nombre, ' ', usuarios.apellido) AS `Nombre del Tutor`
    FROM
        vinculaciones
    INNER JOIN
        estudiantes ON vinculaciones.estudiante_id = estudiantes.estudiante_id
    INNER JOIN
        usuarios ON vinculaciones.identificacion_tutor = usuarios.user_id
    ORDER BY `Vinculación ID` DESC -- Ordenar por Vinculación ID de forma descendente
    LIMIT limite; -- Establecer el límite de resultados
END $$
DELIMITER ;



DROP PROCEDURE IF EXISTS BuscarVinculaciones;
DELIMITER $$
CREATE PROCEDURE BuscarVinculaciones(
    IN criterio_busqueda VARCHAR(255),
    IN limite INT -- Parámetro para establecer el límite de resultados
)
BEGIN
    SELECT
        vinculaciones.vinculacion_id AS `Vinculación ID`,
        DATE_FORMAT(vinculaciones.fecha_registro, "%Y-%m-%d %H:%i:%s") AS `Fecha de Registro de la Vinculación`,
        estudiantes.nombres_apellidos AS `Nombre del Estudiante`,
        DATE_FORMAT(vinculaciones.fecha_inicio, "%Y-%m-%d") AS `Fecha Inicio`,
        vinculaciones.periodo_academico AS `Período Académico`,
        CONCAT(usuarios.nombre, ' ', usuarios.apellido) AS `Nombre del Tutor`
    FROM
        vinculaciones
    INNER JOIN
        estudiantes ON vinculaciones.estudiante_id = estudiantes.estudiante_id
    INNER JOIN
        usuarios ON vinculaciones.identificacion_tutor = usuarios.user_id
    WHERE
        usuarios.nombre LIKE CONCAT('%', criterio_busqueda, '%') OR
        usuarios.apellido LIKE CONCAT('%', criterio_busqueda, '%') OR
        estudiantes.nombres_apellidos LIKE CONCAT('%', criterio_busqueda, '%') OR
        DATE_FORMAT(vinculaciones.fecha_registro, "%Y-%m-%d %H:%i:%s") LIKE CONCAT('%', criterio_busqueda, '%') OR
        DATE_FORMAT(vinculaciones.fecha_inicio, "%Y-%m-%d") LIKE CONCAT('%', criterio_busqueda, '%') OR
        vinculaciones.periodo_academico LIKE CONCAT('%', criterio_busqueda, '%')
    ORDER BY `Vinculación ID` DESC
    LIMIT limite; 
END $$
DELIMITER ;



CALL ListarVinculaciones(2);





