-- Insertar tres carreras en la tabla carrera
INSERT INTO carrera (nombre, descripcion, estado) VALUES
    ('Ingeniería de Sistemas', 'Descripción de Ingeniería de Sistemas', true),
    ('Medicina', 'Descripción de Medicina', true),
    ('Administración de Empresas', 'Descripción de Administración de Empresas', true);

-- Insertar veinte estudiantes en la tabla estudiantes
INSERT INTO estudiantes (nombres, apellidos, tipo_identificacion, nro_identificacion, fecha_nacimiento, genero, correo, telefono, direccion, carrera_id) VALUES
    ('Juan', 'Pérez', 'DNI', '12345678', '1990-05-15', 'M', 'juan.perez@example.com', '987654321', 'Calle 123', 1),
    ('María', 'Gómez', 'DNI', '87654321', '1992-10-20', 'F', 'maria.gomez@example.com', '123456789', 'Avenida 456', 2),
    ('Carlos', 'López', 'Pasaporte', 'A1234567', '1988-03-08', 'M', 'carlos.lopez@example.com', '987654321', 'Calle 789', 3),
    ('Ana', 'Martínez', 'Carnet de Extranjería', 'X1234567', '1991-07-25', 'F', 'ana.martinez@example.com', '123456789', 'Avenida 012', 1),
    ('Pedro', 'Rodríguez', 'DNI', '23456789', '1993-09-30', 'M', 'pedro.rodriguez@example.com', '987654321', 'Calle 345', 2),
    ('Laura', 'Hernández', 'Pasaporte', 'B1234567', '1990-12-12', 'F', 'laura.hernandez@example.com', '123456789', 'Avenida 678', 3),
    ('Luis', 'García', 'DNI', '34567890', '1992-06-18', 'M', 'luis.garcia@example.com', '987654321', 'Calle 901', 1),
    ('Sofía', 'Díaz', 'Carnet de Extranjería', 'Y1234567', '1994-01-05', 'F', 'sofia.diaz@example.com', '123456789', 'Avenida 234', 2),
    ('Miguel', 'Sánchez', 'DNI', '45678901', '1989-11-28', 'M', 'miguel.sanchez@example.com', '987654321', 'Calle 567', 3),
    ('Paola', 'Vargas', 'Pasaporte', 'C1234567', '1993-04-22', 'F', 'paola.vargas@example.com', '123456789', 'Avenida 890', 1),
    ('Andrés', 'López', 'DNI', '56789012', '1991-08-17', 'M', 'andres.lopez@example.com', '987654321', 'Calle 123', 2),
    ('Diana', 'Martínez', 'Carnet de Extranjería', 'Z1234567', '1995-02-14', 'F', 'diana.martinez@example.com', '123456789', 'Avenida 456', 3),
    ('Alejandro', 'González', 'DNI', '67890123', '1988-07-03', 'M', 'alejandro.gonzalez@example.com', '987654321', 'Calle 789', 1),
    ('Camila', 'Fernández', 'Pasaporte', 'D1234567', '1992-10-08', 'F', 'camila.fernandez@example.com', '123456789', 'Avenida 012', 2),
    ('Javier', 'Pérez', 'DNI', '78901234', '1994-03-25', 'M', 'javier.perez@example.com', '987654321', 'Calle 345', 3),
    ('Valentina', 'Hernández', 'Carnet de Extranjería', 'E1234567', '1990-06-19', 'F', 'valentina.hernandez@example.com', '123456789', 'Avenida 678', 1),
    ('Daniel', 'Rodríguez', 'DNI', '89012345', '1993-09-02', 'M', 'daniel.rodriguez@example.com', '987654321', 'Calle 901', 2),
    ('Isabella', 'Gómez', 'Pasaporte', 'F1234567', '1989-12-15', 'F', 'isabella.gomez@example.com', '123456789', 'Avenida 234', 3),
    ('Eduardo', 'Sánchez', 'DNI', '90123456', '1991-05-11', 'M', 'eduardo.sanchez@example.com', '987654321', 'Calle 567', 1);


INSERT INTO tutores (nombres, apellidos, tipo_identificacion, nro_identificacion, fecha_nacimiento, genero, correo, contrasena, telefono, direccion, profesion, archivo_cv) VALUES
('Juan', 'García', 'Cédula', '0912345678', '1980-05-12', 'M', 'juangarcia@example.com', 'contrasena123', '0998765432', 'Quito, Ecuador', 'Ingeniero en Sistemas', NULL),
('María', 'Martínez', 'Cédula', '0923456789', '1975-09-25', 'F', 'mariamartinez@example.com', 'contrasena456', '0987654321', 'Guayaquil, Ecuador', 'Desarrollador Web', NULL),
('Pedro', 'Sánchez', 'Cédula', '0934567890', '1988-03-08', 'M', 'pedrosanchez@example.com', 'contrasena789', '0976543210', 'Cuenca, Ecuador', 'Administrador de Redes', NULL),
('Ana', 'López', 'Cédula', '0945678901', '1982-11-15', 'F', 'analopez@example.com', 'contrasenaabc', '0965432109', 'Machala, Ecuador', 'Ingeniera de Software', NULL),
('Luis', 'Gómez', 'Cédula', '0956789012', '1979-07-03', 'M', 'luisgomez@example.com', 'contrasena1234', '0954321098', 'Portoviejo, Ecuador', 'Desarrollador de Aplicaciones', NULL),
('Elena', 'Pérez', 'Cédula', '0967890123', '1985-02-19', 'F', 'elenaperez@example.com', 'contrasena5678', '0943210987', 'Ambato, Ecuador', 'Ingeniero en Sistemas', NULL),
('Carlos', 'Rodríguez', 'Cédula', '0978901234', '1981-08-27', 'M', 'carlosrodriguez@example.com', 'contrasena9012', '0932109876', 'Manta, Ecuador', 'Analista de Sistemas', NULL),
('Sofía', 'Herrera', 'Cédula', '0989012345', '1973-12-01', 'F', 'sofiaherrera@example.com', 'contrasena3456', '0921098765', 'Durán, Ecuador', 'Diseñador Gráfico', NULL),
('Jorge', 'Díaz', 'Cédula', '0990123456', '1980-06-18', 'M', 'jorgediaz@example.com', 'contrasena7890', '0910987654', 'Riobamba, Ecuador', 'Desarrollador de Software', NULL),
('Isabel', 'Alvarado', 'Cédula', '0991234567', '1977-04-29', 'F', 'isabelalvarado@example.com', 'contrasena12345', '0909876543', 'Loja, Ecuador', 'Administrador de Base de Datos', NULL),
('Miguel', 'Ramírez', 'Cédula', '0992345678', '1984-10-11', 'M', 'miguelramirez@example.com', 'contrasena67890', '0998765432', 'Esmeraldas, Ecuador', 'Ingeniero en Telecomunicaciones', NULL),
('Lucía', 'González', 'Cédula', '0993456789', '1976-01-07', 'F', 'luciagonzalez@example.com', 'contrasena23456', '0987654321', 'Ibarra, Ecuador', 'Técnico en Informática', NULL),
('Gabriel', 'Silva', 'Cédula', '0994567890', '1978-11-23', 'M', 'gabrielsilva@example.com', 'contrasena78901', '0976543210', 'Santo Domingo, Ecuador', 'Ingeniero de Sistemas', NULL),
('Valentina', 'Torres', 'Cédula', '0995678901', '1983-07-14', 'F', 'valentinatorres@example.com', 'contrasena234567', '0965432109', 'Sangolquí, Ecuador', 'Analista Programador', NULL),
('Andrés', 'Reyes', 'Cédula', '0996789012', '1974-05-28', 'M', 'andresreyes@example.com', 'contrasena890123', '0954321098', 'Sangolquí, Ecuador', 'Abogada', NULL);


INSERT INTO proyecto (nombre, descripcion) VALUES
('Desarrollo de Aplicación Móvil de Salud', 'Una aplicación móvil para monitorear la salud y bienestar de los usuarios.'),
('Sistema de Gestión de Inventarios', 'Un sistema para gestionar el inventario de una empresa de manera eficiente.'),
('Plataforma de Educación en Línea', 'Una plataforma para impartir cursos y clases en línea.'),
('Sistema de Reconocimiento Facial', 'Un sistema de seguridad basado en reconocimiento facial.'),
('Desarrollo de Chatbot Inteligente', 'Un chatbot impulsado por inteligencia artificial para atención al cliente.'),
('Aplicación de Realidad Aumentada para Turismo', 'Una aplicación de realidad aumentada para mejorar la experiencia turística.'),
('Plataforma de Comercio Electrónico', 'Un sitio web para la venta de productos en línea.'),
('Sistema de Gestión de Proyectos', 'Una herramienta para la gestión de proyectos y tareas.'),
('Desarrollo de Videojuego 3D', 'Un videojuego 3D para diversas plataformas.'),
('Sistema de Control de Acceso', 'Un sistema para controlar el acceso a edificios y áreas restringidas.'),
('Aplicación de Pago Móvil', 'Una aplicación para realizar pagos a través de dispositivos móviles.'),
('Sistema de Monitoreo Ambiental', 'Un sistema para monitorear y analizar datos ambientales.'),
('Plataforma de Redes Sociales', 'Una plataforma para la interacción y conexión entre usuarios.'),
('Desarrollo de Asistente Virtual', 'Un asistente virtual basado en inteligencia artificial.'),
('Aplicación de Gestión Financiera', 'Una aplicación para la gestión de finanzas personales y empresariales.'),
('Sistema de Gestión de Recursos Humanos', 'Un sistema para la gestión de empleados y recursos humanos.'),
('Plataforma de Análisis de Datos', 'Una plataforma para el análisis y visualización de datos.'),
('Aplicación de Telemedicina', 'Una aplicación para la consulta médica a distancia.'),
('Desarrollo de Sistema IoT para Hogar Inteligente', 'Un sistema de Internet de las Cosas para automatización del hogar.'),
('Aplicación de Reservas de Restaurantes', 'Una aplicación para reservar mesas en restaurantes.');


INSERT INTO institucion (nombre, tipo_institucion, estado, direccion, telefono) VALUES 
('Instituto Tecnológico Superior', 'Tecnológico', TRUE, 'Calle Falsa 123', '1234567890'),
('Escuela Nacional de Ingenieros', 'Universidad', TRUE, 'Av. Siempre Viva 456', '0987654321'),
('Instituto de Ciencias Aplicadas', 'Tecnológico', TRUE, 'Calle 7 de Junio 789', '1122334455'),
('Centro de Estudios Avanzados', 'Universidad', TRUE, 'Calle 14 de Abril 101', '6677889900'),
('Instituto Politécnico Nacional', 'Politécnico', TRUE, 'Av. Independencia 102', '5566778899'),
('Instituto Superior de Comercio', 'Comercial', TRUE, 'Calle Comercio 103', '9988776655'),
('Academia de Ciencias Sociales', 'Universidad', TRUE, 'Calle Central 104', '4433221100'),
('Escuela Técnica Industrial', 'Técnico', TRUE, 'Calle Técnica 105', '3344556677'),
('Instituto de Investigación y Desarrollo', 'Investigación', TRUE, 'Av. Progreso 106', '2211445588'),
('Centro de Formación Profesional', 'Formación', TRUE, 'Calle Formación 107', '4455667788');


-- Insertar 5 registros en la tabla vinculacion
INSERT INTO vinculacion (fecha_inicio, codigo_ies, campo_especifico, periodo_academico, institucion_id, tutores_id, proyecto_id, estado) VALUES
('2023-01-15', '1036', '1-6A', 'P1-2024', 1, 1, 1, TRUE),
('2023-02-20', '1036', '1-6A', 'P1-2024', 2, 2, 2, TRUE),
('2023-03-25', '1036', '1-6A', 'P1-2024', 3, 3, 3, TRUE),
('2023-04-10', '1036', '1-6A', 'P1-2024', 4, 4, 4, TRUE),
('2023-05-05', '1036', '1-6A', 'P1-2024', 5, 5, 5, TRUE);

-- Insertar 3 estudiantes para cada vinculacion
INSERT INTO estudiantes_vinculacion (estudiantes_id, vinculacion_id, fecha_final, estado_vinculacion, nro_horas) VALUES
-- Estudiantes para la primera vinculacion
(1, 1, NULL, 'Pendiente', 0),
(2, 1, NULL, 'Pendiente', 0),
(3, 1, NULL, 'Pendiente', 0),

-- Estudiantes para la segunda vinculacion
(4, 2, NULL, 'Pendiente', 0),
(5, 2, NULL, 'Pendiente', 0),
(6, 2, NULL, 'Pendiente', 0),

-- Estudiantes para la tercera vinculacion
(7, 3, NULL, 'Pendiente', 0),
(8, 3, NULL, 'Pendiente', 0),
(9, 3, NULL, 'Pendiente', 0),

-- Estudiantes para la cuarta vinculacion
(10, 4, NULL, 'Pendiente', 0),
(11, 4, NULL, 'Pendiente', 0),
(12, 4, NULL, 'Pendiente', 0),

-- Estudiantes para la quinta vinculacion
(13, 5, NULL, 'Pendiente', 0),
(14, 5, NULL, 'Pendiente', 0),
(15, 5, NULL, 'Pendiente', 0);




