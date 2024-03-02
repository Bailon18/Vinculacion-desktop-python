
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




DROP PROCEDURE IF EXISTS ListarVinculaciones;
DELIMITER $$
CREATE PROCEDURE ListarVinculaciones(
    IN limite INT
)
BEGIN
    SELECT
        vinculaciones.vinculacion_id AS `Vinculación ID`,
        DATE_FORMAT(vinculaciones.fecha_inicio, '%Y-%m-%d') AS `Fecha Inicio`,
        estudiantes.nombres_apellidos AS `Nombre del Estudiante`,
        vinculaciones.periodo_academico AS `Período Académico`,
        CONCAT(usuarios.nombre, ' ', usuarios.apellido) AS `Nombre del Tutor`,
        vinculaciones.estado
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
        estudiantes.nombres_apellidos AS `Nombre del Estudiante`,
        DATE_FORMAT(vinculaciones.fecha_inicio, '%Y-%m-%d') AS `Fecha Inicio`,
        vinculaciones.periodo_academico AS `Período Académico`,
        CONCAT(usuarios.nombre, ' ', usuarios.apellido) AS `Nombre del Tutor`,
        vinculaciones.estado
    FROM
        vinculaciones
    INNER JOIN
        estudiantes ON vinculaciones.estudiante_id = estudiantes.estudiante_id
    INNER JOIN
        usuarios ON vinculaciones.identificacion_tutor = usuarios.user_id
    WHERE
        usuarios.nombre LIKE CONCAT('%', criterio_busqueda, '%') OR
        usuarios.apellido LIKE CONCAT('%', criterio_busqueda, '%') OR
        estudiantes.identificacion LIKE CONCAT('%', criterio_busqueda, '%') OR
        estudiantes.nombres_apellidos LIKE CONCAT('%', criterio_busqueda, '%') OR
        vinculaciones.estado LIKE CONCAT('%', criterio_busqueda, '%') OR
        DATE_FORMAT(vinculaciones.fecha_inicio, "%Y-%m-%d") LIKE CONCAT('%', criterio_busqueda, '%') OR
        vinculaciones.periodo_academico LIKE CONCAT('%', criterio_busqueda, '%')
    ORDER BY `Vinculación ID` DESC
    LIMIT limite; 
END $$
DELIMITER ;



DROP PROCEDURE IF EXISTS ObtenerDatos;
DELIMITER $$
CREATE PROCEDURE ObtenerDatos()
BEGIN
	
    SELECT id_carrera, nombre_carrera FROM carreras;
    SELECT id, nombre_institucion FROM instituciones_educativas where estado = 'Activo';
    SELECT id_proyecto, nombre_proyecto FROM  proyectos  where estado = 'Activo';
    SELECT user_id , CONCAT(nombre, ' ', apellido) as tutor FROM usuarios WHERE  role_id = 2;

END $$
DELIMITER ;


DROP PROCEDURE IF EXISTS ObtenerDatosVinculacion;
DELIMITER $$
CREATE PROCEDURE ObtenerDatosVinculacion(IN vinculacion_id INT)
BEGIN
    SELECT 
        e.nombres_apellidos, 
        e.tipo_identificacion, 
        e.identificacion, 
        e.codigo_carrera, 
        v.codigo_institucion, 
        v.periodo_academico, 
        v.fecha_inicio, 
        v.fecha_fin,  
        v.numero_horas, 
        v.codigo_ies, 
        v.campo_especifico, 
        v.identificacion_tutor, 
        v.id_proyecto,
        v.estado
    FROM vinculaciones v
    INNER JOIN estudiantes e ON v.estudiante_id = e.estudiante_id
    WHERE v.vinculacion_id = vinculacion_id;
END $$
DELIMITER ;


DROP PROCEDURE IF EXISTS EliminarVinculacion;
DELIMITER $$
CREATE PROCEDURE EliminarVinculacion(
    IN vinculacion_id_param INT
)
BEGIN
    DECLARE estudiante_id_val INT;

    -- Obtener el ID del estudiante asociado a la vinculación
    SELECT estudiante_id INTO estudiante_id_val FROM vinculaciones WHERE vinculacion_id = vinculacion_id_param;

    -- Eliminar el registro del estudiante
    DELETE FROM estudiantes WHERE estudiante_id = estudiante_id_val;

    -- Eliminar los registros de seguimientos asociados a la vinculación
    DELETE FROM seguimientos WHERE vinculacion_id = vinculacion_id_param;
    
    -- Finalmente, eliminar la vinculación
    DELETE FROM vinculaciones WHERE vinculacion_id = vinculacion_id_param;
END $$
DELIMITER ;



DROP PROCEDURE IF EXISTS InsertarEstudianteYVinculacion;
DELIMITER $$
CREATE PROCEDURE InsertarEstudianteYVinculacion(
    IN tipo_identificacion_param VARCHAR(50),
    IN identificacion_param VARCHAR(50),
    IN nombres_apellidos_param VARCHAR(255),
    IN codigo_carrera_param INT,
    IN periodo_academico_param VARCHAR(50),
    IN codigo_ies_param INT,
    IN fecha_inicio_param DATE,
    IN fecha_fin_param DATE,
    #IN numero_horas_param INT,
    IN campo_especifico_param VARCHAR(255),
    IN identificacion_tutor_param INT,
    IN codigo_institucion_param INT,
    IN id_proyecto_param INT
)
BEGIN
    DECLARE estudiante_id_param INT;

    -- Insertar el estudiante
    INSERT INTO estudiantes (tipo_identificacion, identificacion, nombres_apellidos, codigo_carrera)
    VALUES (tipo_identificacion_param, identificacion_param, nombres_apellidos_param, codigo_carrera_param);

    -- Obtener el ID del estudiante insertado
    SET estudiante_id_param = LAST_INSERT_ID();

    -- Insertar la vinculación asociada al estudiante
    INSERT INTO vinculaciones (estudiante_id, periodo_academico, codigo_ies, fecha_inicio, fecha_fin, campo_especifico, identificacion_tutor, codigo_institucion, id_proyecto)
    VALUES (estudiante_id_param, periodo_academico_param, codigo_ies_param, fecha_inicio_param, fecha_fin_param, campo_especifico_param, identificacion_tutor_param, codigo_institucion_param, id_proyecto_param);
    
    -- Confirmar el final de la transacción
    COMMIT;
END $$
DELIMITER ;


DROP PROCEDURE IF EXISTS ActualizarEstudianteYVinculacion;
DELIMITER $$
CREATE PROCEDURE ActualizarEstudianteYVinculacion(
    IN tipo_identificacion_param VARCHAR(50),
    IN identificacion_param VARCHAR(50),
    IN nombres_apellidos_param VARCHAR(255),
    IN codigo_carrera_param INT,
    IN periodo_academico_param VARCHAR(50),
    IN codigo_ies_param INT,
    IN fecha_inicio_param DATE,
    IN fecha_fin_param DATE,
    #IN numero_horas_param INT,
    IN campo_especifico_param VARCHAR(255),
    IN identificacion_tutor_param INT,
    IN codigo_institucion_param INT,
    IN id_proyecto_param INT,
	IN vinculacion_id_param INT
)
BEGIN
    DECLARE estudiante_id_param INT;

    -- Obtener el ID del estudiante asociado a la vinculación
    SELECT estudiante_id INTO estudiante_id_param
    FROM vinculaciones
    WHERE vinculacion_id = vinculacion_id_param;

    -- Actualizar los datos del estudiante
    UPDATE estudiantes
    SET tipo_identificacion = tipo_identificacion_param,
        identificacion = identificacion_param,
        nombres_apellidos = nombres_apellidos_param,
        codigo_carrera = codigo_carrera_param
    WHERE estudiante_id = estudiante_id_param;

    -- Actualizar los datos de la vinculación asociada al estudiante
    UPDATE vinculaciones
    SET periodo_academico = periodo_academico_param,
        codigo_ies = codigo_ies_param,
        fecha_inicio = fecha_inicio_param,
        fecha_fin = fecha_fin_param,
        #numero_horas = numero_horas_param,
        campo_especifico = campo_especifico_param,
        identificacion_tutor = identificacion_tutor_param,
        codigo_institucion = codigo_institucion_param,
        id_proyecto = id_proyecto_param
    WHERE vinculacion_id = vinculacion_id_param;
    
    -- Confirmar el final de la transacción
    COMMIT;
END $$
DELIMITER ;

DROP PROCEDURE IF EXISTS ObtenerSeguimientosPorVinculacionId;
DELIMITER $$
CREATE PROCEDURE ObtenerSeguimientosPorVinculacionId(
    IN vinculacion_id_param INT
)
BEGIN
    SELECT fecha_seguimiento, observaciones
    FROM seguimientos
    WHERE vinculacion_id = vinculacion_id_param;
END $$
DELIMITER ;


DROP TRIGGER IF EXISTS after_insert_seguimiento;
DELIMITER $$
CREATE TRIGGER after_insert_seguimiento
AFTER INSERT ON seguimientos
FOR EACH ROW
BEGIN
    DECLARE total_horas INT;

    -- Actualizar horas en la vinculación
    UPDATE vinculaciones
    SET numero_horas = numero_horas + NEW.horas_seguimiento
    WHERE vinculacion_id = NEW.vinculacion_id;

    -- Obtener el total de horas actualizado
    SELECT numero_horas INTO total_horas
    FROM vinculaciones
    WHERE vinculacion_id = NEW.vinculacion_id;

    -- Cambiar el estado a "Pendiente" si las horas son cero
    IF total_horas = 0 THEN
        UPDATE vinculaciones
        SET estado = 'Pendiente'
        WHERE vinculacion_id = NEW.vinculacion_id;
    -- Cambiar el estado a "Culminado" si se supera el tope de horas (96 horas)
    ELSEIF total_horas >= 96 THEN
        UPDATE vinculaciones
        SET estado = 'Culminado'
        WHERE vinculacion_id = NEW.vinculacion_id;
    ELSE
        -- Cambiar el estado a "En progreso" si no se ha alcanzado el tope de horas
        UPDATE vinculaciones
        SET estado = 'En progreso'
        WHERE vinculacion_id = NEW.vinculacion_id;
    END IF;
END $$
DELIMITER ;



DROP PROCEDURE IF EXISTS ObtenerSeguimientosConEstudiantes;
DELIMITER $$
CREATE PROCEDURE ObtenerSeguimientosConEstudiantes(IN tutor_id_param INT, IN limit_param INT)
BEGIN
    SELECT
        v.vinculacion_id AS 'id-vinculacion',
        e.nombres_apellidos AS 'nombreestudiante',
        DATE_FORMAT(v.fecha_registro, '%Y-%m-%d') AS 'fecha-seguimiento',
        v.numero_horas 'horas_seguimiento',
        v.estado AS 'estado vinculacion'
    FROM
        vinculaciones v
    JOIN
        estudiantes e ON v.estudiante_id = e.estudiante_id
    JOIN
        usuarios u ON v.identificacion_tutor = u.user_id
    WHERE
        u.role_id = 2  
        AND u.user_id = tutor_id_param  
    ORDER BY
        v.fecha_registro DESC
    LIMIT limit_param;
END $$
DELIMITER ;


DROP PROCEDURE IF EXISTS filtrarSeguimientosConEstudiantes;
DELIMITER $$
CREATE PROCEDURE filtrarSeguimientosConEstudiantes(
    IN tutor_id_param INT,
    IN limit_param INT,
    IN criterio_busqueda VARCHAR(255)
)
BEGIN
    SELECT
        v.vinculacion_id AS 'id-vinculacion',
        e.nombres_apellidos AS 'nombreestudiante',
        DATE_FORMAT(v.fecha_registro, '%Y-%m-%d') AS 'fecha-seguimiento',
        v.numero_horas AS 'horas_seguimiento',
        v.estado AS 'estado_vinculacion'
    FROM
        vinculaciones v
    JOIN
        estudiantes e ON v.estudiante_id = e.estudiante_id
    JOIN
        usuarios u ON v.identificacion_tutor = u.user_id
    WHERE
        u.role_id = 2  
        AND u.user_id = tutor_id_param
        AND (
            e.nombres_apellidos LIKE CONCAT('%', criterio_busqueda, '%') OR
            e.identificacion LIKE CONCAT('%', criterio_busqueda, '%') OR
            DATE_FORMAT(v.fecha_registro, '%Y-%m-%d') LIKE CONCAT('%', criterio_busqueda, '%') OR
            v.estado LIKE CONCAT('%', criterio_busqueda, '%') OR
            CAST(v.vinculacion_id AS CHAR) LIKE CONCAT('%', criterio_busqueda, '%') OR
            CAST(v.numero_horas AS CHAR) LIKE CONCAT('%', criterio_busqueda, '%')
        )
    ORDER BY
        v.fecha_registro DESC
    LIMIT limit_param;
END $$

DELIMITER ;


DROP PROCEDURE IF EXISTS InsertarSeguimientoTutor;
DELIMITER $$
CREATE PROCEDURE InsertarSeguimientoTutor(
    IN vinculacion_id_param INT,
    IN fecha_seguimiento_param TIMESTAMP,
    IN observaciones_param TEXT,
    IN tutor_id_param INT,
    IN horas_seguimiento_param INT
)
BEGIN
    INSERT INTO seguimientos (vinculacion_id, fecha_seguimiento, observaciones, tutor_id, horas_seguimiento)
    VALUES (vinculacion_id_param, fecha_seguimiento_param, observaciones_param, tutor_id_param, horas_seguimiento_param);
END $$
DELIMITER ;



DROP PROCEDURE IF EXISTS ObtenerSeguimientosPorTutorYEstudiante;
DELIMITER $$
CREATE PROCEDURE ObtenerSeguimientosPorTutorYEstudiante(
    IN tutor_id_param INT,
    IN vinculacion_param INT
)
BEGIN
    DECLARE estudiante_id2 INT;

    -- Obteniendo el estudiante_id de la tabla vinculaciones
    SELECT estudiante_id INTO estudiante_id2
    FROM vinculaciones
    WHERE vinculacion_id = vinculacion_param;

    -- Consulta para obtener los seguimientos por tutor_id y estudiante_id
    SELECT
        s.seguimiento_id,
        DATE_FORMAT(s.fecha_seguimiento, '%Y-%m-%d') AS 'fecha-seguimiento',
        s.horas_seguimiento
    FROM
        seguimientos s
    JOIN
        vinculaciones v ON s.vinculacion_id = v.vinculacion_id
    WHERE
        s.tutor_id = tutor_id_param
        AND v.estudiante_id = estudiante_id2
    ORDER BY s.fecha_seguimiento DESC;
END $$
DELIMITER ;



DROP PROCEDURE IF EXISTS ObtenerSeguimientoPorId;
DELIMITER $$
CREATE PROCEDURE ObtenerSeguimientoPorId(
    IN seguimiento_id_param INT
)
BEGIN
    SELECT
        s.seguimiento_id,
        DATE_FORMAT(s.fecha_seguimiento, '%Y-%m-%d') AS 'fecha-seguimiento',
        s.observaciones,
        s.horas_seguimiento
    FROM
        seguimientos s
    WHERE
        s.seguimiento_id = seguimiento_id_param;
END $$
DELIMITER ;



DROP TRIGGER IF EXISTS after_delete_seguimiento;
DELIMITER $$

CREATE TRIGGER after_delete_seguimiento
AFTER DELETE ON seguimientos
FOR EACH ROW
BEGIN
    DECLARE total_horas INT;

    -- Restar horas en la vinculación
    UPDATE vinculaciones
    SET numero_horas = numero_horas - OLD.horas_seguimiento
    WHERE vinculacion_id = OLD.vinculacion_id;

    -- Obtener el total de horas actualizado
    SELECT numero_horas INTO total_horas
    FROM vinculaciones
    WHERE vinculacion_id = OLD.vinculacion_id;

    -- Cambiar el estado a "Pendiente" si las horas son cero
    IF total_horas = 0 THEN
        UPDATE vinculaciones
        SET estado = 'Pendiente'
        WHERE vinculacion_id = OLD.vinculacion_id;
    -- Cambiar el estado a "Culminado" si se supera el tope de horas (96 horas)
    ELSEIF total_horas >= 96 THEN
        UPDATE vinculaciones
        SET estado = 'Culminado'
        WHERE vinculacion_id = OLD.vinculacion_id;
    ELSE
        -- Cambiar el estado a "En progreso" si no se ha alcanzado el tope de horas
        UPDATE vinculaciones
        SET estado = 'En progreso'
        WHERE vinculacion_id = OLD.vinculacion_id;
    END IF;
END $$
DELIMITER ;

DROP TRIGGER IF EXISTS BuscarSeguimientosPorFecha;
DELIMITER $$
CREATE PROCEDURE BuscarSeguimientosPorFecha(
    IN fecha_inicio DATE,
    IN fecha_fin DATE
)
BEGIN
    SELECT *
    FROM seguimientos
    WHERE fecha_seguimiento BETWEEN fecha_inicio AND fecha_fin;
END $$
DELIMITER ;





DROP PROCEDURE IF EXISTS ObtenerSeguimientosPorRangoFechas;
DELIMITER $$
CREATE PROCEDURE ObtenerSeguimientosPorRangoFechas(
    IN tutor_id_param INT,
    IN vinculacion_param INT,
    IN fecha_inicio DATE,
    IN fecha_fin DATE
)
BEGIN
    DECLARE estudiante_id2 INT;

    -- Obteniendo el estudiante_id de la tabla vinculaciones
    SELECT estudiante_id INTO estudiante_id2
    FROM vinculaciones
    WHERE vinculacion_id = vinculacion_param;

    -- Consulta para obtener los seguimientos por tutor_id, estudiante_id y rango de fechas
    SELECT
        s.seguimiento_id,
        DATE_FORMAT(s.fecha_seguimiento, '%Y-%m-%d') AS 'fecha-seguimiento',
        s.horas_seguimiento
    FROM
        seguimientos s
    JOIN
        vinculaciones v ON s.vinculacion_id = v.vinculacion_id
    WHERE
        s.tutor_id = tutor_id_param
        AND v.estudiante_id = estudiante_id2
        AND s.fecha_seguimiento BETWEEN fecha_inicio AND fecha_fin
    ORDER BY s.fecha_seguimiento DESC;
END $$
DELIMITER ;



DROP PROCEDURE IF EXISTS ActualizarSeguimientoTutor;
DELIMITER $$
CREATE PROCEDURE ActualizarSeguimientoTutor(
    IN seguimiento_id_param INT,
    IN fecha_seguimiento_param TIMESTAMP,
    IN observaciones_param TEXT,
    IN horas_seguimiento_param INT
)
BEGIN
    UPDATE seguimientos
    SET
        fecha_seguimiento = fecha_seguimiento_param,
        observaciones = observaciones_param,
        horas_seguimiento = horas_seguimiento_param
    WHERE
        seguimiento_id = seguimiento_id_param;
END $$
DELIMITER ;


DROP TRIGGER IF EXISTS after_update_seguimiento;
DELIMITER $$
CREATE TRIGGER after_update_seguimiento
AFTER UPDATE ON seguimientos
FOR EACH ROW
BEGIN
    DECLARE total_horas INT;

    -- Restar las horas anteriores en la vinculación
    UPDATE vinculaciones
    SET numero_horas = numero_horas - OLD.horas_seguimiento
    WHERE vinculacion_id = OLD.vinculacion_id;

    -- Sumar las nuevas horas actualizadas en la vinculación
    UPDATE vinculaciones
    SET numero_horas = numero_horas + NEW.horas_seguimiento
    WHERE vinculacion_id = NEW.vinculacion_id;

    -- Obtener el total de horas actualizado
    SELECT numero_horas INTO total_horas
    FROM vinculaciones
    WHERE vinculacion_id = NEW.vinculacion_id;

    -- Cambiar el estado según el total de horas actualizado
    IF total_horas = 0 THEN
        UPDATE vinculaciones
        SET estado = 'Pendiente'
        WHERE vinculacion_id = NEW.vinculacion_id;
    ELSEIF total_horas >= 96 THEN
        UPDATE vinculaciones
        SET estado = 'Culminado'
        WHERE vinculacion_id = NEW.vinculacion_id;
    ELSE
        UPDATE vinculaciones
        SET estado = 'En progreso'
        WHERE vinculacion_id = NEW.vinculacion_id;
    END IF;
END $$
DELIMITER ;


DROP PROCEDURE IF EXISTS ListarUsuarios;
DELIMITER $$

CREATE PROCEDURE ListarUsuarios()
BEGIN
    SELECT usuarios.user_id,
		   CONCAT(usuarios.nombre,' ',usuarios.apellido) as nombre,
           usuarios.identificacion,
           roles.role_name,
           usuarios.correo_electronico,
           DATE_FORMAT(usuarios.fecha_registro, '%Y-%m-%d %H:%i:%s') AS fecha_registro_formato,
           usuarios.estado
    FROM usuarios
    INNER JOIN roles ON usuarios.role_id = roles.role_id
    ORDER BY usuarios.fecha_registro DESC; 
END $$
DELIMITER ;


DROP PROCEDURE IF EXISTS InsertarUsuario;
DELIMITER $$
CREATE PROCEDURE InsertarUsuario(
    IN p_contrasena VARCHAR(100),
    IN p_identificacion VARCHAR(50),
    IN p_role_id INT,
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_correo_electronico VARCHAR(100),
    IN p_estado VARCHAR(100)
)
BEGIN
    INSERT INTO usuarios (
        contrasena,
        identificacion,
        role_id,
        nombre,
        apellido,
        correo_electronico,
        estado
    ) VALUES (
        p_contrasena,
        p_identificacion,
        p_role_id,
        p_nombre,
        p_apellido,
        p_correo_electronico,
        p_estado
    );
END $$
DELIMITER ;

DROP PROCEDURE IF EXISTS ActualizarUsuario;
DELIMITER $$
CREATE PROCEDURE ActualizarUsuario(
    IN p_contrasena VARCHAR(100),
    IN p_identificacion VARCHAR(50),
    IN p_role_id INT,
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_correo_electronico VARCHAR(100),
    IN p_estado VARCHAR(100),
    IN p_user_id INT
)
BEGIN
    UPDATE usuarios
    SET contrasena = p_contrasena,
        identificacion = p_identificacion,
        role_id = p_role_id,
        nombre = p_nombre,
        apellido = p_apellido,
        correo_electronico = p_correo_electronico,
        estado = p_estado
    WHERE user_id = p_user_id;
END $$
DELIMITER ;


DROP PROCEDURE IF EXISTS BuscarUsuarioPorID;
DELIMITER $$
CREATE PROCEDURE BuscarUsuarioPorID(
    IN p_user_id INT
)
BEGIN
    SELECT user_id,
           contrasena,
           identificacion,
           role_id,
           nombre,
           apellido,
           correo_electronico,
           estado
    FROM usuarios
    WHERE user_id = p_user_id;
END $$
DELIMITER ;


DROP PROCEDURE IF EXISTS filtrarUsuarios;
DELIMITER $$
CREATE PROCEDURE filtrarUsuarios(
    IN criterio_busqueda VARCHAR(255)
)
BEGIN
    SELECT
        usuarios.user_id,
        CONCAT(usuarios.nombre, ' ', usuarios.apellido) AS nombre_completo,
        usuarios.identificacion,
        roles.role_name,
        usuarios.correo_electronico,
        DATE_FORMAT(usuarios.fecha_registro, '%Y-%m-%d %H:%i:%s') AS fecha_registro_formato,
        usuarios.estado
    FROM
        usuarios
    INNER JOIN
        roles ON usuarios.role_id = roles.role_id
    WHERE
        usuarios.identificacion LIKE CONCAT('%', criterio_busqueda, '%') OR
        roles.role_name LIKE CONCAT('%', criterio_busqueda, '%') OR
        usuarios.nombre LIKE CONCAT('%', criterio_busqueda, '%') OR
        usuarios.apellido LIKE CONCAT('%', criterio_busqueda, '%') OR
        usuarios.correo_electronico LIKE CONCAT('%', criterio_busqueda, '%') OR
        usuarios.estado LIKE CONCAT('%', criterio_busqueda, '%')
    ORDER BY
        usuarios.fecha_registro DESC;
END $$
DELIMITER ;

DROP PROCEDURE IF EXISTS ValidarInicioSesion;
DELIMITER $$
CREATE PROCEDURE ValidarInicioSesion(
    IN correo_param VARCHAR(100),
    IN contra_param VARCHAR(100)
)
BEGIN
	SELECT
		u.user_id,
		u.nombre,
		u.apellido,
		u.correo_electronico,
		u.role_id,
		r.role_name,
        u.estado
	FROM usuarios u
	INNER JOIN roles r ON u.role_id = r.role_id
	WHERE u.correo_electronico = correo_param AND u.contrasena = contra_param;
 
END$$
DELIMITER ;



--                                      MANTENIMIENTO 

DROP PROCEDURE IF EXISTS ListarInstitucionesPorEstado;
DELIMITER $$
CREATE PROCEDURE ListarInstitucionesPorEstado(
    IN estado_param VARCHAR(50)
)
BEGIN
    SELECT *
    FROM instituciones_educativas
    WHERE estado = estado_param;
END $$
DELIMITER ;


DROP PROCEDURE IF EXISTS AgregarInstitucion;
DELIMITER $$
CREATE PROCEDURE AgregarInstitucion(
    IN nombre VARCHAR(255),
    IN tipo VARCHAR(50),
    IN direccion VARCHAR(255),
    IN estado_param VARCHAR(50)
)
BEGIN
    INSERT INTO instituciones_educativas (nombre_institucion, tipo_institucion, direccion, estado)
    VALUES (nombre, tipo, direccion, estado_param);
END $$
DELIMITER ;

DROP PROCEDURE IF EXISTS ActualizarInstitucion;
DELIMITER $$
CREATE PROCEDURE ActualizarInstitucion(
    IN institucion_id INT,
    IN nuevo_nombre VARCHAR(255),
    IN nuevo_tipo VARCHAR(50),
    IN nueva_direccion VARCHAR(255),
    IN nuevo_estado VARCHAR(50)
)
BEGIN
    UPDATE instituciones_educativas
    SET nombre_institucion = nuevo_nombre,
        tipo_institucion = nuevo_tipo,
        direccion = nueva_direccion,
        estado = nuevo_estado
    WHERE id = institucion_id;
END $$
DELIMITER ;

DROP PROCEDURE IF EXISTS BuscarInstitucionPorID;
DELIMITER $$
CREATE PROCEDURE BuscarInstitucionPorID(IN institucion_id INT)
BEGIN
    SELECT id, nombre_institucion, tipo_institucion, direccion, estado
    FROM instituciones_educativas
    WHERE id = institucion_id;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS CambiarEstadoInstitucion;
DELIMITER $$
CREATE PROCEDURE CambiarEstadoInstitucion(
    IN institucion_id INT,
    IN nuevo_estado VARCHAR(50)
)
BEGIN
    UPDATE instituciones_educativas
    SET estado = nuevo_estado
    WHERE id = institucion_id;
END $$
DELIMITER ;


DROP PROCEDURE IF EXISTS ListarProyectosPorEstado;
DELIMITER $$
CREATE PROCEDURE ListarProyectosPorEstado(
    IN estado_param VARCHAR(50)
)
BEGIN
    SELECT *
    FROM proyectos
    WHERE estado = estado_param;
END $$
DELIMITER ;

-- Insertar un nuevo proyecto:

DROP PROCEDURE IF EXISTS InsertarProyecto;
DELIMITER $$
CREATE PROCEDURE InsertarProyecto(
    IN nombre_proyecto_param VARCHAR(300),
    IN estado_param VARCHAR(50)
)
BEGIN
    INSERT INTO proyectos (nombre_proyecto, estado)
    VALUES (nombre_proyecto_param, estado_param);
END $$
DELIMITER ;


-- Actualizar un proyecto:

DROP PROCEDURE IF EXISTS ActualizarProyecto;
DELIMITER $$
CREATE PROCEDURE ActualizarProyecto(
    IN p_id_proyecto INT,
    IN p_nuevo_nombre_proyecto VARCHAR(300),
    IN p_estado_param VARCHAR(50)
)
BEGIN
    UPDATE proyectos
    SET nombre_proyecto = p_nuevo_nombre_proyecto,
        estado = p_estado_param
    WHERE id_proyecto = p_id_proyecto;
END $$
DELIMITER ;


-- Cambiar estado de un proyecto:

DROP PROCEDURE IF EXISTS CambiarEstadoProyecto;
DELIMITER $$
CREATE PROCEDURE CambiarEstadoProyecto(
    IN p_id_proyecto INT,
    IN p_nuevo_estado VARCHAR(50)
)
BEGIN
    UPDATE proyectos
    SET estado = p_nuevo_estado
    WHERE id_proyecto = p_id_proyecto;
END $$
DELIMITER ;



DROP PROCEDURE IF EXISTS BuscarProyectoPorID;
DELIMITER $$
CREATE PROCEDURE BuscarProyectoPorID(IN proyecto_id INT)
BEGIN
    SELECT id_proyecto, nombre_proyecto , estado
    FROM proyectos
    WHERE id_proyecto = proyecto_id;
END$$
DELIMITER ;

-- REPORTES

-- Crear el procedimiento almacenado con parámetro y formato de fecha

DROP PROCEDURE IF EXISTS obtenerInformacionVinculacionesConEstado;
DELIMITER $$
CREATE PROCEDURE obtenerInformacionVinculacionesConEstado(
    IN estadoparametro VARCHAR(50),
    IN limit_param INT
)
BEGIN
    SELECT
        CONCAT(e.nombres_apellidos, ' - ', e.identificacion) AS 'Nombre y Apellidos Estudiante',
        DATE_FORMAT(v.fecha_registro, '%Y-%m-%d %H:%i') AS 'Fecha Vinculación',
        CONCAT(u.nombre, ' ', u.apellido) AS 'Nombre y Apellido Tutor',
        v.estado AS 'Estado Vinculación'
    FROM
        vinculaciones v
    JOIN
        estudiantes e ON v.estudiante_id = e.estudiante_id
    JOIN
        usuarios u ON v.identificacion_tutor = u.user_id
    WHERE
        v.estado = estadoparametro
    LIMIT limit_param;
END$$

DELIMITER ;

DROP PROCEDURE IF EXISTS obtenerInformacionVinculacionesConEstadoYBusqueda;
DELIMITER $$
CREATE PROCEDURE obtenerInformacionVinculacionesConEstadoYBusqueda(
    IN paramatrobusqueda VARCHAR(255)
)
BEGIN
    SELECT
        CONCAT(e.nombres_apellidos, ' - ', e.identificacion) AS 'Nombre y Apellidos Estudiante',
        DATE_FORMAT(v.fecha_registro, '%Y-%m-%d %H:%i') AS 'Fecha Vinculación',
        CONCAT(u.nombre, ' ', u.apellido) AS 'Nombre y Apellido Tutor',
        v.estado AS 'Estado Vinculación'
    FROM
        vinculaciones v
    JOIN
        estudiantes e ON v.estudiante_id = e.estudiante_id
    JOIN
        usuarios u ON v.identificacion_tutor = u.user_id
    WHERE
        (
            e.nombres_apellidos LIKE CONCAT('%', paramatrobusqueda, '%')
            OR e.identificacion LIKE CONCAT('%', paramatrobusqueda, '%')
        );
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS ObtenerInfoVinculacionPorTutor;
DELIMITER $$
CREATE PROCEDURE ObtenerInfoVinculacionPorTutor(
    IN estado_param VARCHAR(50),
    IN limite_param INT,
    IN tutor_id_param INT
)
BEGIN
    SELECT 
        e.nombres_apellidos AS nombre_estudiante,
        DATE_FORMAT(v.fecha_registro, '%Y-%m-%d %H:%i') AS vinculacion_registro,
        v.numero_horas AS horas_seguimiento,
        v.estado AS estado_vinculacion
    FROM vinculaciones v
    JOIN estudiantes e ON v.estudiante_id = e.estudiante_id
    WHERE v.identificacion_tutor = tutor_id_param
        AND (estado_param IS NULL OR v.estado = estado_param)
    ORDER BY v.fecha_registro DESC
    LIMIT limite_param;
END $$
DELIMITER ;



CALL ObtenerInfoVinculacionPorTutor('Pendiente',1, 2); 




