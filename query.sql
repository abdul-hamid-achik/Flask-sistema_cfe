insert into competencias(nombre) values ("Obtiene Resultados");
insert into competencias(nombre) values ("Adaptable");
insert into competencias(nombre) values ("Ambiocioso/a");
insert into competencias(nombre) values ("Accesible");
insert into competencias(nombre) values ("Concilia La Vida Personal Y Laboral");
insert into competencias(nombre) values ("Inteligente");
insert into competencias(nombre) values ("Trabaja Bien En Equipo");
insert into competencias(nombre) values ("Se Siente Cómodo/a Con La Incertidumbre");
insert into competencias(nombre) values ("Se Comunica Bien (Verbalmente)");
insert into competencias(nombre) values ("Se Comunica Bien (Por Escrito)");
insert into competencias(nombre) values ("Calmado/a");
insert into competencias(nombre) values ("Posee Confiansa En Sí Mismo/a");
insert into competencias(nombre) values ("Tiene Coraje");
insert into competencias(nombre) values ("Creativo/a");
insert into competencias(nombre) values ("Orientado/a Al Cliente");
insert into competencias(nombre) values ("Decisivo/a");
insert into competencias(nombre) values ("Juicioso/a");
insert into competencias(nombre) values ("Orientado/a Al Detalle");
insert into competencias(nombre) values ("Perseverante");
insert into competencias(nombre) values ("Desarrolla A Otras Personas");
insert into competencias(nombre) values ("Se Desarrolla A Sí Mismo/a");
insert into competencias(nombre) values ("Diplomático/a");
insert into competencias(nombre) values ("Dirige A Las Personas");
insert into competencias(nombre) values ("Empático/a");
insert into competencias(nombre) values ("Sabe Delegar");
insert into competencias(nombre) values ("Ético/a");
insert into competencias(nombre) values ("Experimentador");
insert into competencias(nombre) values ("Justo/a");
insert into competencias(nombre) values ("Establece Prioridades");
insert into competencias(nombre) values ("Pensador Global");
insert into competencias(nombre) values ("Mejora Los Procesos");
insert into competencias(nombre) values ("Informa A Otras Personas");
insert into competencias(nombre) values ("Inspira Un Futuro");
insert into competencias(nombre) values ("Capaz De Escuchar");
insert into competencias(nombre) values ("Gestiona El Conflicto");
insert into competencias(nombre) values ("Gestiona Las Ideas De Otras Personas");
insert into competencias(nombre) values ("Buen Negociador/a");
insert into competencias(nombre) values ("Gestiona El Bajo Rendimiento");
insert into competencias(nombre) values ("Gestiona El Tiempo");
insert into competencias(nombre) values ("Posee Conocimiento Del Mercado");
insert into competencias(nombre) values ("Modesto/a");
insert into competencias(nombre) values ("Gestiona El Trabajo");
insert into competencias(nombre) values ("Motiva A Las Personas");
insert into competencias(nombre) values ("Tiene Facilidad Para Establecer Relaciones");
insert into competencias(nombre) values ("Comparte Información Personal");
insert into competencias(nombre) values ("Abierto/a De Mente");
insert into competencias(nombre) values ("Paciente");
insert into competencias(nombre) values ("Planifica El Trabajo");
insert into competencias(nombre) values ("Políticamente Hábil");
insert into competencias(nombre) values ("Resuelve Problemas");
insert into competencias(nombre) values ("Reconoce El Talento Y El Potencial En Las Personas");
insert into competencias(nombre) values ("Consciente De Sí Mismo/a");
insert into competencias(nombre) values ("Estratega");
insert into competencias(nombre) values ("Toma Responsabilidad");
insert into competencias(nombre) values ("Toma Iniciativa");
insert into competencias(nombre) values ("Posee Conocimientos Técnicos");
insert into competencias(nombre) values ("Experto/a En Tecnología");
insert into competencias(nombre) values ("Digno/a De Confianza");
insert into competencias(nombre) values ("Unifica A Las Personas");
insert into competencias(nombre) values ("Tiene Una Buena Relación Con Su Jefe");








insert into jerarquia(nombre, superior) values('Gerente', '');
insert into jerarquia(nombre, superior) values('Subgerente', 'Gerente');
insert into jerarquia(nombre, superior) values('Jefe de Dpto', 'Subgerente');
insert into jerarquia(nombre, superior) values('Jefe de oficina', 'Jefe de Dpto');
insert into jerarquia(nombre, superior) values('Supervisor', 'Jefe de oficina');
insert into jerarquia(nombre, superior) values('Superintendente', 'Gerente');
insert into jerarquia(nombre, superior) values('Jefe de Dpto', 'Superintendente');
insert into jerarquia(nombre, superior) values('Administrador', 'Superintendente');
insert into jerarquia(nombre, superior) values('Jefe de oficina', 'Jefe de Dpto');





INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('79020','Rivera Rodríguez Pedro','Gerente','Gerencia','pedro.rivera@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('79140','Arjona López Victor Manuel','Subgerente','Subestaciones y Líneas','victor.arjona@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9AGC8','Cabello Reyna Enrique','Subgerente','Comunicaciones','enrique.cabello@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9A28N','Castillo Caldera Mario','Subgerente','Control','mario.castillo@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('80960','Galicia Castillo Ernesto','Subgerente','Modernización y puesta en servicio','ernesto.galicia@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('80838','Rodríguez Guillén Josefina','Subgerente','Administración','josefina.rodriguez@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9AG6T','Torrero Pérez Gustavo','Subgerente','Protección y Medición','gustavo.torrero@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0H6','Altamirano Torres Luz María','Jefa de departamento','Adquisiciones','luzmaria.altamirano@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9A28G','Amozurrutia Carson Earl','Jefe de departamento','Control de Gestión e Informática','earl.amozurrutia@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0CH','Ávalos Cárdenas José Ángel','Jefe de departamento','Líneas','angel.avalos@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0M6','Ávila Flores Omar','Jefe de departamento','Jurídico','omar.avila01@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0LG','Ávila Martínez Juan Francisco','Jefe de departamento','Control','francisco.avila01@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9AG8G','Calderón Mendoza Humberto','Jefe de departamento','Protección y Medición','humberto.calderon@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0KA','Cárdenas Meza Luis Salvador','Jefe de departamento','Planta Regeneradora de Aceite','salvador.cardenas04@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('47399','Cruz Soto José Guadalupe','Jefe de departamento','Contabilidad y Gestión Financiera','jose.cruz01@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0L1','García Alba Alejandro','Jefe de departamento','Comunicaciones','alejandro.garcia07@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('82439','Hernández Toscano Edgar','Jefe de departamento','Modernización y puesta en servicio','edgar.hernandez@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('94772','Juárez Gómez Héctor','Jefe de departamento','Capacitación, Seguridad e Higiene','hector.juarez@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9A2D6','López Martínez Ambrocio','Jefe de departamento','Metrología','ambrosio.lopez@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0G9','Nájera Montelongo Daniel','Jefe de departamento','Recursos Humanos','daniel.najera@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0CG','Ortega González Antonio','Jefe de departamento','Seguimiento de Programas y Mejora de Procesos','antonio.ortega@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9A29K','Rodríguez Ozaeta Oscar','Jefe de departamento','Subestaciones','oscar.rodriguez02@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0DY','Rosales Tovar José Ventura','Jefe de departamento','Comunicaciones','ventura.rosales@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9AAT0','Ruiz Haros Isidro','Jefe de departamento','Protección y Medición','isidro.ruiz@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0EK','Solís Corral David','Jefe de departamento','Subestaciones','david.solis@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9AG86','Tinoco Alcázar Andrés','Jefe de departamento','Comunicaciones','andres.tinoco@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0KC','Triana Domínguez Pablo','Jefe de departamento','Comunicaciones','pablo.triana@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('CG404','Zamora Barrientos Rafael','Jefe de departamento','Comunicaciones','rafael.zamora01@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0KD','Zapata Galindo Marisol','Jefe de oficina','Planta Regeneradora de Aceite','marisol.zapata@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9JFW5','Almeida Reyes Clemente','Jefe de oficina','Subestaciones','clemente.almeida01@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('CG420','Acosta Casanova Arturo','Jefe de oficina','Adquisiciones','arturo.acosta@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('J058R','De la Rosa Díaz Manuel','Jefe de oficina','Jurídico','manuel.delarosa@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0D1','Del Rivero Ibarra Rodrigo','Jefe de oficina','Obra pública','rodrigo.delrivero@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('J062R','García Carrillo Jesús Roberto','Jefe de oficina','Capacitación, Seguridad e Higiene','roberto.garcia15@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B9NP','García Kanagusico Ángel','Jefe de oficina','Capacitación, Seguridad e Higiene','angel.garcia02@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0L9','Gómez Villalobos Alejandro','Jefe de oficina','Lineas','alejandro.gomez05@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0NJ','Güereca García Alejandro','Jefe de oficina','Contabilidad y Gestión Financiera','alejandro.guereca@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0DG','Madrid Orozco Raúl','Jefe de oficina','Almácen','raul.madrid@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0DM','Maldonado Hernández Gustavo','Jefe de oficina','Modernización y puesta en servicio','gustavo.maldonado@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('CG484','Maya Carrizales Luis Javier','Jefe de oficina','Comunicaciones','luis.maya01@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0C0','Medina Hernández Magdalena','Jefe de oficina','Recursos Humanos','magdalena.medina@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9APAF','Moreno Valero Martín Andrés','Jefe de oficina','Control','martin.moreno01@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0ER','Ortiz Rivera Olga Elvira','Jefe de oficina','Control de Gestión e Informática','olga.ortiz@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0FA','Palacios Silva Javier Dionisio','Jefe de oficina','Planta Regeneradora de Aceite','javier.palacios01@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('J001R','Ramírez Reyes Luis Enrique','Jefe de oficina','Modernización y puesta en servicio','enrique.ramirez09@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0J0','Ramos Álvarez Mariana','Jefe de oficina','Recursos Humanos','mariana.ramos@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0HU','Reyes Rivera Enrique','Jefe de oficina','Contabilidad y Gestión Financiera','enrique.reyes03@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('86050','Rodríguez Romo Canto Juan','Jefe de oficina','Recursos Humanos','juan.rodriguez36@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9AAJY','Silva Dorado Jaime Humberto','Jefe de oficina','Seguimiento de Programas y Mejora de Procesos','humberto.silva@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('CG380','Torres Galindo Francisco','Jefe de oficina','Líneas','francisco.torres05@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('CG503','Álvarez Jerkov José Heriberto','Supervisor','Protección y Medición','jose.alvarez19@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('J064R','Maldonado Velázquez Alejandro','Supervisor','Modernización y puesta en servicio','alejandro.maldonado@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('9B0RY','Salazar Galindo Iván','Supervisor','Seguimiento de Programas y Mejora de Procesos','ivan.salazar@cfe.gob.mx','GTZN');
INSERT INTO usuario(rpe,nombre,puesto,departamento,correo,zona) VALUES ('SK119','Valdez Hernández Bernardo','Supervisor','Recursos Humanos','bernardo.valdez01@cfe.gob.mx','GTZN');
