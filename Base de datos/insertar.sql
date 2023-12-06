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


