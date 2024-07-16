
-------------------------- ADMINISTRACION ------------------------------------------


-- Procedimiento para listar registros de la tabla carrera en orden descendente por id
DROP PROCEDURE IF EXISTS listar_carreras;
DELIMITER //
CREATE PROCEDURE listar_carreras(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombre, estado 
    FROM carrera
    WHERE estado = TRUE
    ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS listar_carreras_inactivas;
DELIMITER //
CREATE PROCEDURE listar_carreras_inactivas(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombre, estado 
    FROM carrera
    WHERE estado = FALSE
    ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;


-- Procedimiento para listar registros de la tabla estudiantes con paginación
DROP PROCEDURE IF EXISTS listar_estudiantes;
DELIMITER //
CREATE PROCEDURE listar_estudiantes(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombres, apellidos, nro_identificacion, correo  
    FROM estudiantes
    WHERE estado = true
    ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS listar_estudiantes_inactivos;
DELIMITER //
CREATE PROCEDURE listar_estudiantes_inactivos(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombres, apellidos, nro_identificacion, correo  
    FROM estudiantes
    WHERE estado = false
    ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;


-- Procedimiento para listar registros de la tabla institucion en orden descendente por id
DROP PROCEDURE IF EXISTS listar_institucion;
DELIMITER //
CREATE PROCEDURE listar_institucion(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombre, telefono, estado 
    FROM institucion
    WHERE estado = TRUE
    ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS listar_instituciones_inactivas;
DELIMITER //
CREATE PROCEDURE listar_instituciones_inactivas(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombre, telefono, estado 
    FROM institucion
    WHERE estado = FALSE
    ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;


-- Procedimiento para listar registros de la tabla proyecto en orden descendente por id
DROP PROCEDURE IF EXISTS listar_proyectos;
DELIMITER //
CREATE PROCEDURE listar_proyectos(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombre, estado 
    FROM proyecto
    WHERE estado = TRUE
    ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS listar_proyectos_inactivos;
DELIMITER //
CREATE PROCEDURE listar_proyectos_inactivos(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombre, estado 
    FROM proyecto
    WHERE estado = FALSE
    ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;


-- Procedimiento para listar registros de la tabla tutores en orden descendente por id
DROP PROCEDURE IF EXISTS listar_tutores;
DELIMITER //
CREATE PROCEDURE listar_tutores(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombres, apellidos, nro_identificacion, correo 
    FROM tutores
    WHERE estado = TRUE
    ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS listar_tutores_inactivos;
DELIMITER //
CREATE PROCEDURE listar_tutores_inactivos(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombres, apellidos, nro_identificacion, correo 
    FROM tutores
    WHERE estado = FALSE
    ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;


-- Procedimiento para listar registros de la tabla tutores en orden descendente por id
DROP PROCEDURE IF EXISTS listar_tutores;
DELIMITER //
CREATE PROCEDURE listar_tutores(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombres, apellidos, nro_identificacion, correo FROM tutores
	ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;



-- Procedimiento para buscar registros en la tabla carrera por id
DROP PROCEDURE IF EXISTS buscar_carrera_por_id;
DELIMITER //
CREATE PROCEDURE buscar_carrera_por_id(IN p_id INT)
BEGIN
    SELECT nombre, descripcion,  estado FROM carrera WHERE id = p_id;
END //
DELIMITER ;

-- Procedimiento para buscar registros en la tabla estudiantes por id
DROP PROCEDURE IF EXISTS buscar_estudiante_por_id;
DELIMITER //
CREATE PROCEDURE buscar_estudiante_por_id(IN p_id INT)
BEGIN
    SELECT * FROM estudiantes WHERE id = p_id;
END //
DELIMITER ;

-- Procedimiento para buscar registros en la tabla institucion por id
DROP PROCEDURE IF EXISTS buscar_institucion_por_id;
DELIMITER //
CREATE PROCEDURE buscar_institucion_por_id(IN p_id INT)
BEGIN
    SELECT nombre, tipo_institucion, estado, direccion, telefono, archivo_convenio, tipo_archivo 
    FROM institucion 
    WHERE id = p_id;
END //
DELIMITER ;


-- Procedimiento para buscar registros en la tabla proyecto por id
DROP PROCEDURE IF EXISTS buscar_proyecto_por_id;
DELIMITER //
CREATE PROCEDURE buscar_proyecto_por_id(IN p_id INT)
BEGIN
    SELECT nombre, descripcion, estado FROM proyecto WHERE id = p_id;
END //
DELIMITER ;

-- Procedimiento para buscar registros en la tabla tutores por id
DROP PROCEDURE IF EXISTS buscar_tutor_por_id;
DELIMITER //
CREATE PROCEDURE buscar_tutor_por_id(IN p_id INT)
BEGIN
    SELECT * FROM tutores WHERE id = p_id;
END //
DELIMITER ;



-- Procedimiento para actualizar un registro en la tabla carrera
DROP PROCEDURE IF EXISTS actualizar_carrera;
DELIMITER //
CREATE PROCEDURE actualizar_carrera(
    IN p_id INT,
    IN p_nombre VARCHAR(255),
    IN p_descripcion TEXT,
    IN p_estado BOOLEAN
)
BEGIN
    UPDATE carrera
    SET nombre = p_nombre,
        descripcion = p_descripcion,
        estado = p_estado
    WHERE id = p_id;
END //
DELIMITER ;

-- Procedimiento para actualizar un registro en la tabla estudiantes
DROP PROCEDURE IF EXISTS actualizar_estudiante;
DELIMITER //
CREATE PROCEDURE actualizar_estudiante(
    IN p_id INT,
    IN p_nombres VARCHAR(255),
    IN p_apellidos VARCHAR(255),
    IN p_tipo_identificacion VARCHAR(50),
    IN p_nro_identificacion VARCHAR(50),
    IN p_fecha_nacimiento DATE,
    IN p_genero ENUM('M', 'F', 'Otro'),
    IN p_correo VARCHAR(255),
    IN p_telefono VARCHAR(50),
    IN p_direccion TEXT,
    IN p_carrera_id INT
)
BEGIN
    UPDATE estudiantes
    SET nombres = p_nombres,
        apellidos = p_apellidos,
        tipo_identificacion = p_tipo_identificacion,
        nro_identificacion = p_nro_identificacion,
        fecha_nacimiento = p_fecha_nacimiento,
        genero = p_genero,
        correo = p_correo,
        telefono = p_telefono,
        direccion = p_direccion,
        carrera_id = p_carrera_id
    WHERE id = p_id;
END //
DELIMITER ;

-- Procedimiento para actualizar un registro en la tabla institucion
DROP PROCEDURE IF EXISTS actualizar_institucion;
DELIMITER //
CREATE PROCEDURE actualizar_institucion(
    IN p_id INT,
    IN p_nombre VARCHAR(255),
    IN p_tipo_institucion VARCHAR(255),
    IN p_estado BOOLEAN,
    IN p_direccion TEXT,
    IN p_telefono VARCHAR(50),
    IN p_archivo_convenio LONGBLOB,
    IN p_tipo_archivo VARCHAR(50)
)
BEGIN
    UPDATE institucion
    SET nombre = p_nombre,
        tipo_institucion = p_tipo_institucion,
        estado = p_estado,
        direccion = p_direccion,
        telefono = p_telefono,
        archivo_convenio = p_archivo_convenio,
        tipo_archivo = p_tipo_archivo
    WHERE id = p_id;
END //
DELIMITER ;


-- Procedimiento para actualizar un registro en la tabla proyecto
DROP PROCEDURE IF EXISTS actualizar_proyecto;
DELIMITER //
CREATE PROCEDURE actualizar_proyecto(
    IN p_id INT,
    IN p_nombre VARCHAR(255),
    IN p_descripcion TEXT,
    IN p_estado BOOLEAN
)
BEGIN
    UPDATE proyecto
    SET nombre = p_nombre,
        descripcion = p_descripcion,
        estado = p_estado
    WHERE id = p_id;
END //
DELIMITER ;

-- Procedimiento para actualizar un registro en la tabla tutores
DROP PROCEDURE IF EXISTS actualizar_tutor;
DELIMITER //
CREATE PROCEDURE actualizar_tutor(
    IN p_id INT,
    IN p_nombres VARCHAR(255),
    IN p_apellidos VARCHAR(255),
    IN p_tipo_identificacion VARCHAR(50),
    IN p_nro_identificacion VARCHAR(50),
    IN p_fecha_nacimiento DATE,
    IN p_genero ENUM('M', 'F', 'Otro'),
    IN p_correo VARCHAR(255),
    IN p_telefono VARCHAR(50),
    IN p_direccion TEXT,
    IN p_profesion VARCHAR(255),
    IN p_contrasena VARCHAR(255),
    IN p_archivo_cv LONGBLOB
)
BEGIN
    UPDATE tutores
    SET
        nombres = p_nombres,
        apellidos = p_apellidos,
        tipo_identificacion = p_tipo_identificacion,
        nro_identificacion = p_nro_identificacion,
        fecha_nacimiento = p_fecha_nacimiento,
        genero = p_genero,
        correo = p_correo,
        telefono = p_telefono,
        direccion = p_direccion,
        profesion = p_profesion,
        contrasena = p_contrasena,
        archivo_cv = p_archivo_cv
    WHERE id = p_id;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS actualizar_tutor_sin_archivo;
DELIMITER //
CREATE PROCEDURE actualizar_tutor_sin_archivo(
    IN p_id INT,
    IN p_nombres VARCHAR(255),
    IN p_apellidos VARCHAR(255),
    IN p_tipo_identificacion VARCHAR(50),
    IN p_nro_identificacion VARCHAR(50),
    IN p_fecha_nacimiento DATE,
    IN p_genero ENUM('M', 'F', 'Otro'),
    IN p_correo VARCHAR(255),
    IN p_telefono VARCHAR(50),
    IN p_direccion TEXT,
    IN p_profesion VARCHAR(255),
    IN p_contrasena VARCHAR(255)
)
BEGIN
    UPDATE tutores
    SET
        nombres = p_nombres,
        apellidos = p_apellidos,
        tipo_identificacion = p_tipo_identificacion,
        nro_identificacion = p_nro_identificacion,
        fecha_nacimiento = p_fecha_nacimiento,
        genero = p_genero,
        correo = p_correo,
        telefono = p_telefono,
        direccion = p_direccion,
        profesion = p_profesion,
        contrasena = p_contrasena
    WHERE id = p_id;
END //
DELIMITER ;




-- Procedimiento para eliminar un registro en la tabla carrera
DROP PROCEDURE IF EXISTS eliminar_carrera;
DELIMITER //
CREATE PROCEDURE eliminar_carrera(IN p_id INT)
BEGIN
    DELETE FROM carrera WHERE id = p_id;
END //
DELIMITER ;

-- Procedimiento para eliminar un registro en la tabla estudiantes
DROP PROCEDURE IF EXISTS eliminar_estudiante;
DELIMITER //
CREATE PROCEDURE eliminar_estudiante(IN p_id INT)
BEGIN
    DELETE FROM estudiantes WHERE id = p_id;
END //
DELIMITER ;

-- Procedimiento para eliminar un registro en la tabla institucion
DROP PROCEDURE IF EXISTS eliminar_institucion;
DELIMITER //
CREATE PROCEDURE eliminar_institucion(IN p_id INT)
BEGIN
    DELETE FROM institucion WHERE id = p_id;
END //
DELIMITER ;

-- Procedimiento para eliminar un registro en la tabla proyecto
DROP PROCEDURE IF EXISTS eliminar_proyecto;
DELIMITER //
CREATE PROCEDURE eliminar_proyecto(IN p_id INT)
BEGIN
    DELETE FROM proyecto WHERE id = p_id;
END //
DELIMITER ;

-- Procedimiento para eliminar un registro en la tabla tutores
DROP PROCEDURE IF EXISTS eliminar_tutor;
DELIMITER //
CREATE PROCEDURE eliminar_tutor(IN p_id INT)
BEGIN
    DELETE FROM tutores WHERE id = p_id;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS agregar_estudiante;
DELIMITER //
CREATE PROCEDURE agregar_estudiante(
    IN p_nombres VARCHAR(255),
    IN p_apellidos VARCHAR(255),
    IN p_tipo_identificacion VARCHAR(50),
    IN p_nro_identificacion VARCHAR(50),
    IN p_fecha_nacimiento DATE,
    IN p_genero ENUM('M', 'F', 'Otro'),
    IN p_correo VARCHAR(255),
    IN p_telefono VARCHAR(50),
    IN p_direccion TEXT,
    IN p_carrera_id INT
)
BEGIN
    INSERT INTO estudiantes (nombres, apellidos, tipo_identificacion, nro_identificacion, fecha_nacimiento, genero, correo, telefono, direccion, carrera_id)
    VALUES (p_nombres, p_apellidos, p_tipo_identificacion, p_nro_identificacion, p_fecha_nacimiento, p_genero, p_correo, p_telefono, p_direccion, p_carrera_id);
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS agregar_proyecto;
DELIMITER //
CREATE PROCEDURE agregar_proyecto(
    IN p_nombre VARCHAR(255),
    IN p_descripcion TEXT,
    IN p_estado BOOLEAN
)
BEGIN
    INSERT INTO proyecto (nombre, descripcion, estado) 
    VALUES (p_nombre, p_descripcion, p_estado);
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS agregar_carrera;
DELIMITER //
CREATE PROCEDURE agregar_carrera(
    IN p_nombre VARCHAR(255),
    IN p_descripcion TEXT,
    IN p_estado BOOLEAN
)
BEGIN
    INSERT INTO carrera (nombre, descripcion, estado) 
    VALUES (p_nombre, p_descripcion, p_estado);
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS agregar_institucion;
DELIMITER //
CREATE PROCEDURE agregar_institucion(
    IN p_nombre VARCHAR(255),
    IN p_tipo_institucion VARCHAR(255),
    IN p_estado BOOLEAN,
    IN p_direccion TEXT,
    IN p_telefono VARCHAR(50),
    IN p_archivo_convenio LONGBLOB,
    IN p_tipo_archivo VARCHAR(50)
)
BEGIN
    INSERT INTO institucion (nombre, tipo_institucion, estado, direccion, telefono, archivo_convenio, tipo_archivo)
    VALUES (p_nombre, p_tipo_institucion, p_estado, p_direccion, p_telefono, p_archivo_convenio, p_tipo_archivo);
END//
DELIMITER ;


DROP PROCEDURE IF EXISTS buscar_estudiantes;
DELIMITER //
CREATE PROCEDURE buscar_estudiantes(
    IN param_busqueda VARCHAR(255),
    IN offset_val INT,
    IN limit_val INT
)
BEGIN
    SELECT id, nombres, apellidos, nro_identificacion, correo
    FROM estudiantes
    WHERE 
        nombres LIKE CONCAT('%', param_busqueda, '%') OR
        apellidos LIKE CONCAT('%', param_busqueda, '%') OR
        nro_identificacion LIKE CONCAT('%', param_busqueda, '%') OR
        correo LIKE CONCAT('%', param_busqueda, '%') OR
        genero LIKE CONCAT('%', param_busqueda, '%') OR
        telefono LIKE CONCAT('%', param_busqueda, '%')
    LIMIT offset_val, limit_val;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS contar_estudiantes;
DELIMITER //
CREATE PROCEDURE contar_estudiantes(
    IN param_busqueda VARCHAR(255)
)
BEGIN
    SELECT COUNT(*)
    FROM estudiantes
    WHERE 
        nombres LIKE CONCAT('%', param_busqueda, '%') OR
        apellidos LIKE CONCAT('%', param_busqueda, '%') OR
        nro_identificacion LIKE CONCAT('%', param_busqueda, '%') OR
        correo LIKE CONCAT('%', param_busqueda, '%') OR
        genero LIKE CONCAT('%', param_busqueda, '%') OR
        telefono LIKE CONCAT('%', param_busqueda, '%');
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS buscar_usuarios;
DELIMITER //
CREATE PROCEDURE buscar_usuarios(
    IN param_busqueda VARCHAR(255),
    IN offset_val INT,
    IN limit_val INT
)
BEGIN
    SELECT 
        u.user_id, 
        concat(u.nombre, '' ,u.apellido) , 
        u.identificacion, 
        r.role_name AS role_name, 
		u.correo_electronico, 
        u.estado
    FROM 
        usuarios u
    JOIN 
        roles r ON u.role_id = r.role_id
    WHERE 
        u.nombre LIKE CONCAT('%', param_busqueda, '%') OR
        u.apellido LIKE CONCAT('%', param_busqueda, '%') OR
        u.correo_electronico LIKE CONCAT('%', param_busqueda, '%') OR
        u.identificacion LIKE CONCAT('%', param_busqueda, '%') OR
        r.role_name LIKE CONCAT('%', param_busqueda, '%')
    LIMIT offset_val, limit_val;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS contar_usuarios;
DELIMITER //
CREATE PROCEDURE contar_usuarios(
    IN param_busqueda VARCHAR(255)
)
BEGIN
    SELECT COUNT(*)
    FROM 
        usuarios u
    JOIN 
        roles r ON u.role_id = r.role_id
    WHERE 
        u.nombre LIKE CONCAT('%', param_busqueda, '%') OR
        u.apellido LIKE CONCAT('%', param_busqueda, '%') OR
        u.correo_electronico LIKE CONCAT('%', param_busqueda, '%') OR
        u.identificacion LIKE CONCAT('%', param_busqueda, '%') OR
        r.role_name LIKE CONCAT('%', param_busqueda, '%');
END //
DELIMITER ;




DROP PROCEDURE IF EXISTS buscar_tutores;
DELIMITER //
CREATE PROCEDURE buscar_tutores(
    IN param_busqueda VARCHAR(255),
    IN offset_val INT,
    IN limit_val INT
)
BEGIN
    SELECT id, nombres, apellidos, nro_identificacion, correo
    FROM tutores
    WHERE 
        nombres LIKE CONCAT('%', param_busqueda, '%') OR
        apellidos LIKE CONCAT('%', param_busqueda, '%') OR
        nro_identificacion LIKE CONCAT('%', param_busqueda, '%') OR
        correo LIKE CONCAT('%', param_busqueda, '%') OR
        genero LIKE CONCAT('%', param_busqueda, '%') OR
        telefono LIKE CONCAT('%', param_busqueda, '%')
    LIMIT offset_val, limit_val;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS contar_tutores;
DELIMITER //
CREATE PROCEDURE contar_tutores(
    IN param_busqueda VARCHAR(255)
)
BEGIN
    SELECT COUNT(*)
    FROM tutores
    WHERE 
        nombres LIKE CONCAT('%', param_busqueda, '%') OR
        apellidos LIKE CONCAT('%', param_busqueda, '%') OR
        nro_identificacion LIKE CONCAT('%', param_busqueda, '%') OR
        correo LIKE CONCAT('%', param_busqueda, '%') OR
        genero LIKE CONCAT('%', param_busqueda, '%') OR
        telefono LIKE CONCAT('%', param_busqueda, '%');
END //
DELIMITER ;



DROP PROCEDURE IF EXISTS buscar_proyectos;
DELIMITER //
CREATE PROCEDURE buscar_proyectos(
    IN param_busqueda VARCHAR(255),
    IN offset_val INT,
    IN limit_val INT
)
BEGIN
    SELECT id, nombre, estado
    FROM proyecto
    WHERE 
        nombre LIKE CONCAT('%', param_busqueda, '%') OR
        descripcion LIKE CONCAT('%', param_busqueda, '%') 
    LIMIT offset_val, limit_val;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS contar_proyectos;
DELIMITER //
CREATE PROCEDURE contar_proyectos(
    IN param_busqueda VARCHAR(255)
)
BEGIN
    SELECT COUNT(*)
    FROM proyecto
    WHERE 
        nombre LIKE CONCAT('%', param_busqueda, '%') OR
        descripcion LIKE CONCAT('%', param_busqueda, '%') ;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS buscar_carreras;
DELIMITER //
CREATE PROCEDURE buscar_carreras(
    IN param_busqueda VARCHAR(255),
    IN offset_val INT,
    IN limit_val INT
)
BEGIN
    SELECT id, nombre, estado
    FROM carrera
    WHERE 
        nombre LIKE CONCAT('%', param_busqueda, '%') OR
        descripcion LIKE CONCAT('%', param_busqueda, '%') 
    LIMIT offset_val, limit_val;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS contar_carreras;
DELIMITER //
CREATE PROCEDURE contar_carreras(
    IN param_busqueda VARCHAR(255)
)
BEGIN
    SELECT COUNT(*)
    FROM carrera
    WHERE 
        nombre LIKE CONCAT('%', param_busqueda, '%') OR
        descripcion LIKE CONCAT('%', param_busqueda, '%') ;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS buscar_instituciones;
DELIMITER //
CREATE PROCEDURE buscar_instituciones(
    IN param_busqueda VARCHAR(255),
    IN offset_val INT,
    IN limit_val INT
)
BEGIN
    SELECT id, nombre, telefono,  estado
    FROM institucion
    WHERE 
        nombre LIKE CONCAT('%', param_busqueda, '%') OR
        telefono LIKE CONCAT('%', param_busqueda, '%') 
    LIMIT offset_val, limit_val;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS contar_instituciones;
DELIMITER //
CREATE PROCEDURE contar_instituciones(
    IN param_busqueda VARCHAR(255)
)
BEGIN
    SELECT COUNT(*)
    FROM institucion
    WHERE 
        nombre LIKE CONCAT('%', param_busqueda, '%') OR
        telefono LIKE CONCAT('%', param_busqueda, '%') ;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS agregar_tutor;
DELIMITER //
CREATE PROCEDURE agregar_tutor(
    IN p_nombres VARCHAR(255),
    IN p_apellidos VARCHAR(255),
    IN p_tipo_identificacion VARCHAR(50),
    IN p_nro_identificacion VARCHAR(50),
    IN p_fecha_nacimiento DATE,
    IN p_genero ENUM('M', 'F', 'Otro'),
    IN p_correo VARCHAR(255),
    IN p_telefono VARCHAR(50),
    IN p_direccion TEXT,
    IN p_profesion VARCHAR(255),
    IN p_contrasena VARCHAR(255),
    IN p_archivo_cv LONGBLOB
)
BEGIN
    INSERT INTO tutores (
        nombres,
        apellidos,
        tipo_identificacion,
        nro_identificacion,
        fecha_nacimiento,
        genero,
        correo,
        telefono,
        direccion,
        profesion,
        contrasena,
        archivo_cv
    ) VALUES (
        p_nombres,
        p_apellidos,
        p_tipo_identificacion,
        p_nro_identificacion,
        p_fecha_nacimiento,
        p_genero,
        p_correo,
        p_telefono,
        p_direccion,
        p_profesion,
        p_contrasena,
        p_archivo_cv
    );
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS ObtenerListaVinculaciones;
DELIMITER //
CREATE PROCEDURE ObtenerListaVinculaciones(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT 
        v.id AS id_vinculacion,
        p.nombre AS nombre_proyecto,
        v.fecha_inicio,
        v.periodo_academico,
        COUNT(ev.estudiantes_id) AS cantidad_alumnos_asignados
    FROM 
        vinculacion v
    JOIN 
        proyecto p ON v.proyecto_id = p.id
    LEFT JOIN 
        estudiantes_vinculacion ev ON v.id = ev.vinculacion_id
    GROUP BY 
        v.id, p.nombre, v.fecha_inicio, v.periodo_academico, v.estado
    ORDER BY 
        v.id DESC LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;




DROP PROCEDURE IF EXISTS ObtenerListaVinculacionesPorFiltro;
DELIMITER //
CREATE PROCEDURE ObtenerListaVinculacionesPorFiltro(
    IN p_filtro VARCHAR(50), -- Tipo de filtro ('proyecto', 'tutor', 'periodo')
    IN p_id VARCHAR(50),     -- Valor del filtro
    IN p_offset INT, 
    IN p_limit INT
)
BEGIN
    SET @sql_query = CONCAT('
        SELECT 
            v.id AS id_vinculacion,
            p.nombre AS nombre_proyecto,
            v.fecha_inicio,
            v.periodo_academico,
            COUNT(ev.estudiantes_id) AS cantidad_alumnos_asignados
        FROM vinculacion v
        JOIN proyecto p ON v.proyecto_id = p.id
        LEFT JOIN estudiantes_vinculacion ev ON v.id = ev.vinculacion_id
        WHERE 1=1 '); -- 1=1 para facilitar la concatenación de condiciones
    
    -- Agregar la condición según el tipo de filtro
    IF p_filtro = 'proyecto' THEN
        SET @sql_query = CONCAT(@sql_query, ' AND v.proyecto_id = ', CAST(p_id AS UNSIGNED));
    ELSEIF p_filtro = 'tutor' THEN
        SET @sql_query = CONCAT(@sql_query, ' AND v.tutores_id = ', CAST(p_id AS UNSIGNED));
    ELSEIF p_filtro = 'periodo' THEN
        SET @sql_query = CONCAT(@sql_query, ' AND v.periodo_academico LIKE CONCAT("%", "', p_id, '%")');
    END IF;
    
    -- Completar la consulta
    SET @sql_query = CONCAT(@sql_query, '
        GROUP BY v.id, p.nombre, v.fecha_inicio, v.periodo_academico
        ORDER BY v.id DESC 
        LIMIT ', p_limit, ' OFFSET ', p_offset);
    
    -- Ejecutar la consulta dinámica
    PREPARE stmt FROM @sql_query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END //
DELIMITER ;



DROP PROCEDURE IF EXISTS ObtenerListaVinculacionesPorEstudiante;
DELIMITER //
CREATE PROCEDURE ObtenerListaVinculacionesPorEstudiante(
	IN p_filtro VARCHAR(50),
    IN search_term VARCHAR(100),
    IN p_offset INT,
    IN p_limit INT
)
BEGIN
    SELECT 
        v.id AS id_vinculacion,
        p.nombre AS nombre_proyecto,
        v.fecha_inicio,
        v.periodo_academico,
        COUNT(DISTINCT ev.estudiantes_id) AS cantidad_alumnos_asignados
    FROM 
        vinculacion v
        JOIN proyecto p ON v.proyecto_id = p.id
        LEFT JOIN estudiantes_vinculacion ev ON v.id = ev.vinculacion_id
        LEFT JOIN estudiantes e ON ev.estudiantes_id = e.id
    WHERE 
        v.id IN (
            SELECT DISTINCT vinculacion_id
            FROM estudiantes_vinculacion
            WHERE estudiantes_id IN (
                SELECT id
                FROM estudiantes
                WHERE nombres LIKE CONCAT('%', search_term, '%')
                    OR apellidos LIKE CONCAT('%', search_term, '%')
                    OR nro_identificacion LIKE CONCAT('%', search_term, '%')
            )
        )
    GROUP BY 
        v.id, p.nombre, v.fecha_inicio, v.periodo_academico
    ORDER BY 
        v.id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS guardar_vinculacion_procedure;
DELIMITER //
CREATE PROCEDURE guardar_vinculacion_procedure(
    IN p_fecha_inicio DATE,
    IN p_codigo_ies VARCHAR(255),
    IN p_campo_especifico VARCHAR(255),
    IN p_periodo_academico VARCHAR(255),
    IN p_intitucion_id INT,
    IN p_tutor_id INT,
    IN p_proyecto_id INT,
    IN p_estado BOOLEAN
)
BEGIN
    -- Insertar los datos de vinculación
    INSERT INTO vinculacion (
        fecha_inicio, codigo_ies, campo_especifico, periodo_academico,
        institucion_id, tutores_id, proyecto_id, estado
    ) VALUES (
        p_fecha_inicio, p_codigo_ies, p_campo_especifico, p_periodo_academico,
        p_intitucion_id, p_tutor_id, p_proyecto_id, p_estado
    );
    
END //
DELIMITER ;



DROP PROCEDURE IF EXISTS ObtenerDetalleVinculacion;
DELIMITER //
CREATE PROCEDURE ObtenerDetalleVinculacion (IN vinculacion_id INT)
BEGIN
    SELECT 
		DATE_FORMAT(v.fecha_inicio, '%Y-%m-%d') AS fecha_inicio,
        v.codigo_ies,
        v.campo_especifico,
        v.periodo_academico,
        i.nombre AS institucion_nombre,
        CONCAT(t.nombres, ' ', t.apellidos) AS tutor_nombre,
        t.nro_identificacion AS tutor_identificacion,
        t.telefono AS tutor_telefono,
        t.correo AS tutor_correo,
        t.archivo_cv AS tutor_archivo_cv,
        p.nombre AS proyecto_nombre
    FROM
        vinculacion v
        JOIN institucion i ON v.institucion_id = i.id
        JOIN tutores t ON v.tutores_id = t.id
        JOIN proyecto p ON v.proyecto_id = p.id
    WHERE
        v.id = vinculacion_id;
END //
DELIMITER ;



-- Trigger for AFTER INSERT
/* DROP TRIGGER IF EXISTS trg_seguimiento_insert;
DELIMITER //
CREATE TRIGGER trg_seguimiento_insert
AFTER INSERT ON seguimiento
FOR EACH ROW
BEGIN
    DECLARE total_horas INT;

    -- Update the nro_horas
    UPDATE estudiantes_vinculacion
    SET nro_horas = CASE 
                        WHEN nro_horas + NEW.horas_actividad > 96 THEN 96
                        ELSE nro_horas + NEW.horas_actividad
                    END
    WHERE id = NEW.estudiantes_vinculacion_id;

    -- Fetch the updated nro_horas
    SELECT nro_horas INTO total_horas
    FROM estudiantes_vinculacion
    WHERE id = NEW.estudiantes_vinculacion_id;

    -- Update the estado_vinculacion and fecha_final based on nro_horas
    IF total_horas = 0 THEN
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'Pendiente'
        WHERE id = NEW.estudiantes_vinculacion_id;
    ELSEIF total_horas < 96 THEN
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'En Proceso'
        WHERE id = NEW.estudiantes_vinculacion_id;
    ELSE
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'Culminado',
            fecha_final = CURDATE()
        WHERE id = NEW.estudiantes_vinculacion_id;
    END IF;
END//
DELIMITER ;
*/


DROP TRIGGER IF EXISTS trg_seguimiento_insert;
DELIMITER //
CREATE TRIGGER trg_seguimiento_insert
AFTER INSERT ON seguimiento
FOR EACH ROW
BEGIN
    DECLARE total_horas INT;
    DECLARE estudiante_id INT;

    -- Fetch the estudiante_id
    SELECT estudiantes_id INTO estudiante_id
    FROM estudiantes_vinculacion
    WHERE id = NEW.estudiantes_vinculacion_id;

    -- Update the nro_horas
    UPDATE estudiantes_vinculacion
    SET nro_horas = CASE 
                        WHEN nro_horas + NEW.horas_actividad > 96 THEN 96
                        ELSE nro_horas + NEW.horas_actividad
                    END
    WHERE id = NEW.estudiantes_vinculacion_id;

    -- Fetch the updated nro_horas
    SELECT nro_horas INTO total_horas
    FROM estudiantes_vinculacion
    WHERE id = NEW.estudiantes_vinculacion_id;

    -- Update the estado_vinculacion and fecha_final based on nro_horas
    IF total_horas = 0 THEN
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'Pendiente'
        WHERE id = NEW.estudiantes_vinculacion_id;
        UPDATE estudiantes
        SET estado = true
        WHERE id = estudiante_id;
    ELSEIF total_horas < 96 THEN
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'En Proceso'
        WHERE id = NEW.estudiantes_vinculacion_id;
        UPDATE estudiantes
        SET estado = true
        WHERE id = estudiante_id;
    ELSE
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'Culminado',
            fecha_final = CURDATE()
        WHERE id = NEW.estudiantes_vinculacion_id;
        UPDATE estudiantes
        SET estado = false
        WHERE id = estudiante_id;
    END IF;
END//
DELIMITER ;


DROP TRIGGER IF EXISTS trg_seguimiento_update;
DELIMITER //
CREATE TRIGGER trg_seguimiento_update
BEFORE UPDATE ON seguimiento
FOR EACH ROW
BEGIN
    DECLARE total_horas INT;
    DECLARE estudiante_id INT;

    -- Fetch the estudiante_id
    SELECT estudiantes_id INTO estudiante_id
    FROM estudiantes_vinculacion
    WHERE id = NEW.estudiantes_vinculacion_id;

    -- Update the nro_horas
    UPDATE estudiantes_vinculacion
    SET nro_horas = CASE 
                        WHEN nro_horas - OLD.horas_actividad + NEW.horas_actividad > 96 THEN 96
                        ELSE nro_horas - OLD.horas_actividad + NEW.horas_actividad
                    END
    WHERE id = NEW.estudiantes_vinculacion_id;

    -- Fetch the updated nro_horas
    SELECT nro_horas INTO total_horas
    FROM estudiantes_vinculacion
    WHERE id = NEW.estudiantes_vinculacion_id;

    -- Update the estado_vinculacion and fecha_final based on nro_horas
    IF total_horas = 0 THEN
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'Pendiente'
        WHERE id = NEW.estudiantes_vinculacion_id;
        UPDATE estudiantes
        SET estado = true
        WHERE id = estudiante_id;
    ELSEIF total_horas < 96 THEN
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'En Proceso'
        WHERE id = NEW.estudiantes_vinculacion_id;
        UPDATE estudiantes
        SET estado = true
        WHERE id = estudiante_id;
    ELSE
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'Culminado',
            fecha_final = CURDATE()
        WHERE id = NEW.estudiantes_vinculacion_id;
        UPDATE estudiantes
        SET estado = false
        WHERE id = estudiante_id;
    END IF;
END//
DELIMITER ;


DROP TRIGGER IF EXISTS trg_seguimiento_delete;
DELIMITER //
CREATE TRIGGER trg_seguimiento_delete
AFTER DELETE ON seguimiento
FOR EACH ROW
BEGIN
    DECLARE total_horas INT;
    DECLARE estudiante_id INT;

    -- Fetch the estudiante_id
    SELECT estudiantes_id INTO estudiante_id
    FROM estudiantes_vinculacion
    WHERE id = OLD.estudiantes_vinculacion_id;

    -- Update the nro_horas
    UPDATE estudiantes_vinculacion
    SET nro_horas = CASE 
                        WHEN nro_horas - OLD.horas_actividad < 0 THEN 0
                        ELSE nro_horas - OLD.horas_actividad
                    END
    WHERE id = OLD.estudiantes_vinculacion_id;

    -- Fetch the updated nro_horas
    SELECT nro_horas INTO total_horas
    FROM estudiantes_vinculacion
    WHERE id = OLD.estudiantes_vinculacion_id;

    -- Update the estado_vinculacion and fecha_final based on nro_horas
    IF total_horas = 0 THEN
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'Pendiente',
            fecha_final = NULL
        WHERE id = OLD.estudiantes_vinculacion_id;
        UPDATE estudiantes
        SET estado = true
        WHERE id = estudiante_id;
    ELSEIF total_horas < 96 THEN
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'En Proceso',
            fecha_final = NULL
        WHERE id = OLD.estudiantes_vinculacion_id;
        UPDATE estudiantes
        SET estado = true
        WHERE id = estudiante_id;
    ELSE
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'Culminado',
            fecha_final = CURDATE()
        WHERE id = OLD.estudiantes_vinculacion_id;
        UPDATE estudiantes
        SET estado = false
        WHERE id = estudiante_id;
    END IF;
END//
DELIMITER ;




/*DROP TRIGGER IF EXISTS trg_seguimiento_update;
DELIMITER //
CREATE TRIGGER trg_seguimiento_update
BEFORE UPDATE ON seguimiento
FOR EACH ROW
BEGIN
    DECLARE total_horas INT;

    -- Update the nro_horas
    UPDATE estudiantes_vinculacion
    SET nro_horas = CASE 
                        WHEN nro_horas - OLD.horas_actividad + NEW.horas_actividad > 96 THEN 96
                        ELSE nro_horas - OLD.horas_actividad + NEW.horas_actividad
                    END
    WHERE id = NEW.estudiantes_vinculacion_id;

    -- Fetch the updated nro_horas
    SELECT nro_horas INTO total_horas
    FROM estudiantes_vinculacion
    WHERE id = NEW.estudiantes_vinculacion_id;

    -- Update the estado_vinculacion and fecha_final based on nro_horas
    IF total_horas = 0 THEN
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'Pendiente'
        WHERE id = NEW.estudiantes_vinculacion_id;
    ELSEIF total_horas < 96 THEN
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'En Proceso'
        WHERE id = NEW.estudiantes_vinculacion_id;
    ELSE
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'Culminado',
            fecha_final = CURDATE()
        WHERE id = NEW.estudiantes_vinculacion_id;
    END IF;
END//
DELIMITER ;*/

-- Trigger for AFTER DELETE
/*DROP TRIGGER IF EXISTS trg_seguimiento_delete;
DELIMITER //
CREATE TRIGGER trg_seguimiento_delete
AFTER DELETE ON seguimiento
FOR EACH ROW
BEGIN
    DECLARE total_horas INT;

    -- Update the nro_horas
    UPDATE estudiantes_vinculacion
    SET nro_horas = CASE 
                        WHEN nro_horas - OLD.horas_actividad < 0 THEN 0
                        ELSE nro_horas - OLD.horas_actividad
                    END
    WHERE id = OLD.estudiantes_vinculacion_id;

    -- Fetch the updated nro_horas
    SELECT nro_horas INTO total_horas
    FROM estudiantes_vinculacion
    WHERE id = OLD.estudiantes_vinculacion_id;

    -- Update the estado_vinculacion and fecha_final based on nro_horas
    IF total_horas = 0 THEN
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'Pendiente',
            fecha_final = NULL
        WHERE id = OLD.estudiantes_vinculacion_id;
    ELSEIF total_horas < 96 THEN
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'En Proceso',
            fecha_final = NULL
        WHERE id = OLD.estudiantes_vinculacion_id;
    ELSE
        UPDATE estudiantes_vinculacion
        SET estado_vinculacion = 'Culminado',
            fecha_final = CURDATE()
        WHERE id = OLD.estudiantes_vinculacion_id;
    END IF;
END//
DELIMITER ; */



DROP PROCEDURE IF EXISTS ObtenerListaSeguimientoXEstudiante;
DELIMITER //
CREATE PROCEDURE ObtenerListaSeguimientoXEstudiante(IN p_estudiantes_vinculacion_id INT, IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT 
        id, fecha_actividad, horas_actividad 
    FROM seguimiento WHERE estudiantes_vinculacion_id = p_estudiantes_vinculacion_id 
    ORDER BY id DESC
    LIMIT p_limit 
    OFFSET p_offset;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS contar_instituciones_SeguimientoXEstudiante;
DELIMITER //
CREATE PROCEDURE contar_instituciones_SeguimientoXEstudiante(
    IN p_estudiantes_vinculacion_id INT,
    IN p_fecha_inicio DATE,
    IN p_fecha_final DATE
)
BEGIN
    SELECT COUNT(DISTINCT id) AS total_instituciones
    FROM seguimiento
    WHERE estudiantes_vinculacion_id = p_estudiantes_vinculacion_id
    AND fecha_actividad BETWEEN p_fecha_inicio AND p_fecha_final;
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS buscar_seguimiento_fechas;
DELIMITER //
CREATE PROCEDURE buscar_seguimiento_fechas(
    IN p_estudiantes_vinculacion_id INT,
    IN p_fecha_inicio DATE,
    IN p_fecha_final DATE,
    IN p_offset INT,
    IN p_limit INT
)
BEGIN
    SELECT 
        id, fecha_actividad, horas_actividad 
    FROM seguimiento 
    WHERE estudiantes_vinculacion_id = p_estudiantes_vinculacion_id
    AND fecha_actividad BETWEEN p_fecha_inicio AND p_fecha_final
    ORDER BY id DESC
    LIMIT p_limit 
    OFFSET p_offset;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS InsertarSeguimiento;
DELIMITER //
CREATE PROCEDURE InsertarSeguimiento(
    IN p_estudiantes_vinculacion_id INT,
    IN p_fecha_actividad DATE,
    IN p_horas_actividad INT,
    IN p_actividades TEXT,
    IN p_archivo_foto LONGBLOB,
    IN p_archivo_actividad LONGBLOB,
    IN p_tipo_archivo_actividad VARCHAR(50),
    IN p_observacion TEXT,
    IN p_fecha_seguimiento DATE
)
BEGIN
    INSERT INTO seguimiento (
        estudiantes_vinculacion_id,
        fecha_actividad,
        horas_actividad,
        actividades,
        archivo_foto,
        archivo_actividad,
        tipo_archivo_actividad,
        observacion,
        fecha_seguimiento
    ) VALUES (
        p_estudiantes_vinculacion_id,
        p_fecha_actividad,
        p_horas_actividad,
        p_actividades,
        p_archivo_foto,
        p_archivo_actividad,
        p_tipo_archivo_actividad,
        p_observacion,
        p_fecha_seguimiento
    );
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS listar_usuarios;
DELIMITER //
CREATE PROCEDURE listar_usuarios(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT u.user_id, concat(u.nombre, ' ',u.apellido), u.identificacion, r.role_name, u.correo_electronico, u.estado 
    FROM usuarios u inner join roles r
    on u.role_id = r.role_id
    ORDER BY u.user_id DESC
	LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS insertar_usuario;
DELIMITER //
CREATE PROCEDURE insertar_usuario(
    IN p_contrasena VARCHAR(100),
    IN p_identificacion VARCHAR(50),
    IN p_role_id INT,
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_correo_electronico VARCHAR(100),
    IN p_estado VARCHAR(50)
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
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS actualizar_usuario;
DELIMITER //
CREATE PROCEDURE actualizar_usuario(
    IN p_user_id INT,
    IN p_contrasena VARCHAR(100),
    IN p_identificacion VARCHAR(50),
    IN p_role_id INT,
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_correo_electronico VARCHAR(100),
    IN p_estado VARCHAR(50)
)
BEGIN
    UPDATE usuarios
    SET 
        contrasena = p_contrasena, 
        identificacion = p_identificacion, 
        role_id = p_role_id, 
        nombre = p_nombre, 
        apellido = p_apellido, 
        correo_electronico = p_correo_electronico, 
        estado = p_estado
    WHERE 
        user_id = p_user_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS buscar_usuario_por_id;
DELIMITER //
CREATE PROCEDURE buscar_usuario_por_id(
    IN p_user_id INT
)
BEGIN
    SELECT 
        u.user_id, 
        u.contrasena, 
        u.identificacion, 
        u.role_id, 
        u.nombre, 
        u.apellido, 
        u.correo_electronico,  
        u.estado
    FROM 
        usuarios u
    JOIN 
        roles r ON u.role_id = r.role_id
    WHERE 
        u.user_id = p_user_id;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS listar_estudiantes_vinculacion_por_estado;
DELIMITER //
CREATE PROCEDURE listar_estudiantes_vinculacion_por_estado(
    IN p_estado_vinculacion ENUM('Pendiente', 'En Proceso', 'Culminado'),
    IN p_offset INT,
    IN p_limit INT
)
BEGIN
    SELECT 
        CONCAT(e.nombres, ' ', e.apellidos) AS estudiante,
        v.fecha_inicio,
        ev.nro_horas,
        v.periodo_academico,
        CONCAT(t.nombres, ' ', t.apellidos) AS tutor,
        ev.estado_vinculacion
    FROM 
        estudiantes_vinculacion ev
    JOIN 
        estudiantes e ON ev.estudiantes_id = e.id
    JOIN 
        vinculacion v ON ev.vinculacion_id = v.id
    JOIN 
        tutores t ON v.tutores_id = t.id
    WHERE 
        ev.estado_vinculacion = p_estado_vinculacion
    ORDER BY 
        v.fecha_inicio DESC
    LIMIT 
        p_limit OFFSET p_offset;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS contar_estudiantes_vinculacion_por_estado;
DELIMITER //
CREATE PROCEDURE contar_estudiantes_vinculacion_por_estado(
    IN p_estado_vinculacion ENUM('Pendiente', 'En Proceso', 'Culminado')
)
BEGIN
    SELECT 
        COUNT(*) AS cantidad
    FROM 
        estudiantes_vinculacion ev
    JOIN 
        estudiantes e ON ev.estudiantes_id = e.id
    JOIN 
        vinculacion v ON ev.vinculacion_id = v.id
    JOIN 
        tutores t ON v.tutores_id = t.id
    WHERE 
        ev.estado_vinculacion = p_estado_vinculacion;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS filtro_estudiantes_vinculacion_por_estado;
DELIMITER //
CREATE PROCEDURE filtro_estudiantes_vinculacion_por_estado(
    IN p_estado_vinculacion ENUM('Pendiente', 'En Proceso', 'Culminado'),
    IN p_offset INT,
    IN p_limit INT,
    IN p_queryparam VARCHAR(255)
)
BEGIN
    SELECT 
        CONCAT(e.nombres, ' ', e.apellidos) AS estudiante,
        v.fecha_inicio,
        ev.nro_horas,
        v.periodo_academico,
        CONCAT(t.nombres, ' ', t.apellidos) AS tutor,
        ev.estado_vinculacion
    FROM 
        estudiantes_vinculacion ev
    JOIN 
        estudiantes e ON ev.estudiantes_id = e.id
    JOIN 
        vinculacion v ON ev.vinculacion_id = v.id
    JOIN 
        tutores t ON v.tutores_id = t.id
    WHERE 
        ev.estado_vinculacion = p_estado_vinculacion
        AND (
            e.nombres LIKE CONCAT('%', p_queryparam, '%')
            OR e.apellidos LIKE CONCAT('%', p_queryparam, '%')
            OR e.nro_identificacion LIKE CONCAT('%', p_queryparam, '%')
            OR e.correo LIKE CONCAT('%', p_queryparam, '%')
            OR e.telefono LIKE CONCAT('%', p_queryparam, '%')
        )
    ORDER BY 
        v.fecha_inicio DESC
    LIMIT 
        p_limit OFFSET p_offset;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS filtro_estudiantes_vinculacion_por_estado_contar;
DELIMITER //
CREATE PROCEDURE filtro_estudiantes_vinculacion_por_estado_contar(
    IN p_estado_vinculacion VARCHAR(20),
    IN p_queryparam VARCHAR(255)
)
BEGIN
    SELECT 
        COUNT(*) AS cantidad
    FROM 
        estudiantes_vinculacion ev
    JOIN 
        estudiantes e ON ev.estudiantes_id = e.id
    JOIN 
        vinculacion v ON ev.vinculacion_id = v.id
    JOIN 
        tutores t ON v.tutores_id = t.id
    WHERE 
        ev.estado_vinculacion = p_estado_vinculacion
        AND (
            e.nombres LIKE CONCAT('%', p_queryparam, '%')
            OR e.apellidos LIKE CONCAT('%', p_queryparam, '%')
            OR e.nro_identificacion LIKE CONCAT('%', p_queryparam, '%')
            OR e.correo LIKE CONCAT('%', p_queryparam, '%')
            OR e.telefono LIKE CONCAT('%', p_queryparam, '%')
        );
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS listar_estudiantes_vinculacion_completo;
DELIMITER //
CREATE PROCEDURE listar_estudiantes_vinculacion_completo(
)
BEGIN
    SELECT 
        -- v.id AS `Vinculación ID`,
        v.periodo_academico AS 'Periodo académico',
        ev.estado_vinculacion AS 'Estado de vinculación',
        v.codigo_ies AS 'Código IES',
        e.tipo_identificacion AS 'Tipo identificación Estudiante',
        e.nro_identificacion AS 'Identificación estudiante',
        CONCAT(e.nombres, ' ', e.apellidos) AS `Nombre del Estudiante`,
        inst.nombre AS 'Nombre de institución',
        inst.tipo_institucion AS 'Tipo de institución',
        c.nombre AS 'Nombre Carrera',
        DATE_FORMAT(v.fecha_inicio, '%Y-%m-%d') AS `Fecha Inicio`,
        DATE_FORMAT(ev.fecha_final, '%Y-%m-%d') AS `Fecha Fin`,
        ev.nro_horas AS 'Número de horas',
        v.campo_especifico AS 'Campo específico',
        t.nro_identificacion AS 'Identificación tutor',
        CONCAT(t.nombres, ' ', t.apellidos) AS `Nombre del Tutor`
    FROM 
        estudiantes_vinculacion ev
    JOIN 
        estudiantes e ON ev.estudiantes_id = e.id
    JOIN 
        vinculacion v ON ev.vinculacion_id = v.id
    JOIN 
        tutores t ON v.tutores_id = t.id
    JOIN 
        institucion inst ON v.institucion_id = inst.id
    JOIN 
        carrera c ON e.carrera_id = c.id
    ORDER BY 
        v.fecha_inicio DESC;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS listar_informes_por_periodo_academico;
DELIMITER $$
CREATE PROCEDURE listar_informes_por_periodo_academico(IN periodo_academico VARCHAR(50))
BEGIN
	SELECT
		tu.id,
		CONCAT(tu.nombres, ' ', tu.apellidos) AS Tutor,
		IFNULL(MAX(CASE WHEN i.mes = 'Enero' THEN 'SI' ELSE 'NO' END), 'NO') AS Enero,
		IFNULL(MAX(CASE WHEN i.mes = 'Febrero' THEN 'SI' ELSE 'NO' END), 'NO') AS Febrero,
		IFNULL(MAX(CASE WHEN i.mes = 'Marzo' THEN 'SI' ELSE 'NO' END), 'NO') AS Marzo,
		IFNULL(MAX(CASE WHEN i.mes = 'Abril' THEN 'SI' ELSE 'NO' END), 'NO') AS Abril,
		IFNULL(MAX(CASE WHEN i.mes = 'Mayo' THEN 'SI' ELSE 'NO' END), 'NO') AS Mayo,
		IFNULL(MAX(CASE WHEN i.mes = 'Junio' THEN 'SI' ELSE 'NO' END), 'NO') AS Junio,
		IFNULL(MAX(CASE WHEN i.mes = 'Julio' THEN 'SI' ELSE 'NO' END), 'NO') AS Julio,
		IFNULL(MAX(CASE WHEN i.mes = 'Agosto' THEN 'SI' ELSE 'NO' END), 'NO') AS Agosto,
		IFNULL(MAX(CASE WHEN i.mes = 'Setiembre' THEN 'SI' ELSE 'NO' END), 'NO') AS Setiembre,
		IFNULL(MAX(CASE WHEN i.mes = 'Octubre' THEN 'SI' ELSE 'NO' END), 'NO') AS Octubre,
		IFNULL(MAX(CASE WHEN i.mes = 'Noviembre' THEN 'SI' ELSE 'NO' END), 'NO') AS Noviembre,
		IFNULL(MAX(CASE WHEN i.mes = 'Diciembre' THEN 'SI' ELSE 'NO' END), 'NO') AS Diciembre
	FROM (
		SELECT id FROM tutores 
	) t
	LEFT JOIN informes i ON t.id = i.tutor_id AND i.periodo_academico = periodo_academico
	LEFT JOIN tutores tu ON tu.id = t.id
    WHERE tu.estado = true
	GROUP BY t.id;

END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS consulta_fichas;
DELIMITER $$
CREATE PROCEDURE consulta_fichas(IN periodo_academico_param VARCHAR(50))
BEGIN
    SELECT
		tu.id,
        concat( tu.nombres, ' ', tu.apellidos ),
        CASE
            WHEN f.is_ficha = 1 THEN 'SI'
            ELSE ''
        END AS SI,
        CASE
            WHEN f.is_ficha = 0 THEN 'NO'
            WHEN f.tutor_id IS NULL THEN 'NO'
            ELSE ''  
        END AS NO
    FROM
        tutores tu
    LEFT JOIN fichas f ON tu.id = f.tutor_id AND f.periodo_academico = periodo_academico_param
    WHERE tu.estado = true
    ;
END$$
DELIMITER ;


DROP PROCEDURE IF EXISTS consulta_memorandum;
DELIMITER $$
CREATE PROCEDURE consulta_memorandum(IN periodo_academico_param VARCHAR(50))
BEGIN
    SELECT
		tu.id,
        concat( tu.nombres, ' ', tu.apellidos ),
        CASE
            WHEN m.is_memorandum = 1 THEN 'SI'
            ELSE ''
        END AS SI,
        CASE
            WHEN m.is_memorandum = 0 THEN 'NO'
            WHEN m.tutor_id IS NULL THEN 'NO'
            ELSE ''  
        END AS NO
    FROM
        tutores tu
    LEFT JOIN memorandum m ON tu.id = m.tutor_id AND m.periodo_academico = periodo_academico_param
    WHERE tu.estado = true
    ;
END$$
DELIMITER ;


call consulta_memorandum('P1-2024')






