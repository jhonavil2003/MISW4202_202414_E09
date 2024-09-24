INSERT INTO users (id, username)
VALUES 
(1, 'dr.villota@uniandes.edu.co'),
(2, 'jf.avila@uniandes.edu.co'),
(3, 'j.castanor@uniandes.edu.co'),
(4, 'r.negrete@uniandes.edu.co'),
(5,'ma.moreno2@uniandes.edu.co')


INSERT INTO  roles (id, nombre, tipo)
VALUES 
(1, 'Administrador', 'Administrador'),
(2, 'Coordinador', 'Administrador'),
(3, 'Coordinador Area', 'Administrador'),
(4, 'Jefe Cuenta', 'Administrador'),
(5, 'Operador', 'Operario')



insert into permisos (id, nombre, descripcion)
values  
(1, 'crear usuario', 'crear usuario'),
(2, 'editar usuario', 'editar usuario'),
(3, 'eliminar usuario', 'eliminar usuario'),
(4, 'ver usuario', 'ver usuario'),
(5, 'crear rol', 'crear rol'),
(6, 'editar rol', 'editar rol'),
(7, 'eliminar rol', 'eliminar rol'),
(8, 'ver rol', 'ver rol'),
(9, 'crear permiso', 'crear permiso'),
(10, 'editar permiso', 'editar permiso'),
(11, 'eliminar permiso', 'eliminar permiso'),
(12, 'ver permiso', 'ver permiso'),
(13, 'asignar rol', 'asignar rol'),
(14, 'quitar rol', 'quitar rol'),
(15, 'asignar permiso', 'asignar permiso'),
(16, 'quitar permiso', 'quitar permiso'),
(17, 'ver asignaciones', 'ver asignaciones'),
(18, 'ver roles', 'ver roles'),
(19, 'ver permisos', 'ver permisos'),
(20, 'ver usuarios', 'ver usuarios'),
(21, 'ver roles usuario', 'ver roles usuario'),
(22, 'ver permisos usuario', 'ver permisos usuario')


INSERT INTO  user_roles (id, user_id, role_id)
VALUES 
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5)

