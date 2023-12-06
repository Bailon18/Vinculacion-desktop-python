

DELIMITER //
CREATE PROCEDURE ListarVinculaciones()
BEGIN
    SELECT
        vinculaciones.vinculacion_id AS `Vinculación ID`,
        vinculaciones.fecha_registro AS `Fecha de Registro de la Vinculación`,
        estudiantes.nombres_apellidos AS `Nombre del Estudiante`,
        vinculaciones.fecha_inicio AS `Fecha Inicio`,
        vinculaciones.periodo_academico AS `Período Académico`,
        CONCAT(usuarios.nombre, ' ', usuarios.apellido) AS `Nombre del Tutor`
    FROM
        vinculaciones
    INNER JOIN
        estudiantes ON vinculaciones.estudiante_id = estudiantes.estudiante_id
    INNER JOIN
        usuarios ON vinculaciones.identificacion_tutor = usuarios.user_id;

END //
DELIMITER ;

CALL ListarVinculaciones();


