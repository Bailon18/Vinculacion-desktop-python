
-------------------------- ADMINISTRACION ------------------------------------------


-- Procedimiento para listar registros de la tabla carrera en orden descendente por id
DROP PROCEDURE IF EXISTS listar_carreras;
DELIMITER //
CREATE PROCEDURE listar_carreras(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombre, estado FROM carrera ORDER BY id DESC
	LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;

-- Procedimiento para listar registros de la tabla estudiantes con paginación
DROP PROCEDURE IF EXISTS listar_estudiantes;
DELIMITER //
CREATE PROCEDURE listar_estudiantes(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombres, apellidos, nro_identificacion, correo  FROM estudiantes
    ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;

-- Procedimiento para listar registros de la tabla institucion en orden descendente por id
DROP PROCEDURE IF EXISTS listar_institucion;
DELIMITER //
CREATE PROCEDURE listar_institucion(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombre, telefono, estado FROM institucion ORDER BY id DESC
    LIMIT p_limit OFFSET p_offset;
END //
DELIMITER ;

-- Procedimiento para listar registros de la tabla proyecto en orden descendente por id
DROP PROCEDURE IF EXISTS listar_proyectos;
DELIMITER //
CREATE PROCEDURE listar_proyectos(IN p_offset INT, IN p_limit INT)
BEGIN
    SELECT id, nombre, estado FROM proyecto ORDER BY id DESC
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
    SELECT nombre , tipo_institucion, estado, direccion , telefono FROM institucion WHERE id = p_id;
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
    IN p_telefono VARCHAR(50)
)
BEGIN
    UPDATE institucion
    SET nombre = p_nombre,
        tipo_institucion = p_tipo_institucion,
        estado = p_estado,
        direccion = p_direccion,
        telefono = p_telefono
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
    IN p_telefono VARCHAR(50)
)
BEGIN
    INSERT INTO institucion (nombre, tipo_institucion, estado, direccion, telefono)
    VALUES (p_nombre, p_tipo_institucion, p_estado, p_direccion, p_telefono);
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
        telefono LIKE CONCAT('%', param_busqueda, '%') OR
        descripcion LIKE CONCAT('%', param_busqueda, '%') 
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
        telefono LIKE CONCAT('%', param_busqueda, '%') OR
        descripcion LIKE CONCAT('%', param_busqueda, '%') ;
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

call ObtenerDetalleVinculacion(1)