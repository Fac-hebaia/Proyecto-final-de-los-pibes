create database marketplace;
use marketplace;

create table categorias (
idCategoria int primary key not null auto_increment,
nombre varchar (50) not null);

create table usuarios (
idUsuario int primary key not null auto_increment, 
dni varchar (20) not null,
telefono varchar (30) not null, contrasenia varchar (18) not null,
email varchar (30) not null,
nombres varchar (50) not null,
apellidos varchar (50) not null,
direccion varchar (50) not null,
pais varchar (30) not null,
provincia varchar (20) not null,
codigoPostal varchar (10) not null,
ciudad varchar (30), calle varchar (30), numeracion varchar (30));

create table facturas (
idFactura int primary key not null auto_increment,
fecha datetime not null,
montoTotal decimal (15,2) not null);

create table productos (
idProducto int primary key not null auto_increment,
idCategoria int not null, idUsuario int not null,
stock int not null, fechaSubido date not null,
descripcion varchar (250) not null,
precio decimal (15,2) not null,
foreign key (idCategoria) references categorias(idCategoria),
foreign key (idUsuario) references usuarios(idUsuario));

create table pedidos (
idPedido int primary key not null auto_increment,
idUsuario int not null,
idFactura int not null,
estado enum("Entregado","Pendiente","Cancelado","Enviado","Pagado","Reembolso"),
fecha datetime not null,
foreign key (idUsuario) references usuarios(idUsuario),
foreign key (idFactura) references facturas(idFactura));

create table detalles_pedido (
idProducto int not null,
idPedido int not null,
precio decimal (15,2) not null,
cantidad int not null,
Primary key (idProducto, idPedido),
Foreign key (idProducto) references productos(idProducto),
Foreign key (idPedido) references pedidos(idPedido));

INSERT INTO categorias (nombre) VALUES ('Ropa');
INSERT INTO categorias (nombre) VALUES ('Electrónica');
INSERT INTO categorias (nombre) VALUES ('Audio y Video');
INSERT INTO categorias (nombre) VALUES ('Hogar y Cocina');
INSERT INTO categorias (nombre) VALUES ('Gaming');
INSERT INTO categorias (nombre) VALUES ('Deportes y Aire Libre');
INSERT INTO categorias (nombre) VALUES ('Juguetes y Entretenimiento');
INSERT INTO categorias (nombre) VALUES ('Belleza y Cuidado Personal');
INSERT INTO categorias (nombre) VALUES ('Libros y Papelería');
INSERT INTO categorias (nombre) VALUES ('Accesorios para Vehículos');

INSERT INTO usuarios (dni, telefono, contrasenia, email, nombres, apellidos, direccion, pais, provincia, codigoPostal, ciudad, calle, numeracion)
VALUES ('39458210', '+54 381 5678912', 'contrasenia1', 'anatorres@mail.com', 'Ana', 'Torres', 'Av. Belgrano 1220', 'Argentina', 'Tucumán', '4000', 'San Miguel de Tucumán', 'Av. Belgrano', '1220');
INSERT INTO usuarios (dni, telefono, contrasenia, email, nombres, apellidos, direccion, pais, provincia, codigoPostal, ciudad, calle, numeracion)
VALUES ('41820355', '+54 11 4382910', 'Clav3Secreta', 'lucas.perez@gmail.com', 'Lucas', 'Pérez', 'calle Sucre 450', 'Argentina', 'Buenos Aires', '1706', 'Morón', 'Sucre', '450');
INSERT INTO usuarios (dni, telefono, contrasenia, email, nombres, apellidos, direccion, pais, provincia, codigoPostal, ciudad, calle, numeracion)
VALUES ('40255891', '+54 351 6972031', 'Pass123456', 'sofi_gomez@hotmail.com', 'Sofía', 'Gómez', 'Bv. San Juan 850', 'Argentina', 'Córdoba', '5000', 'Córdoba', 'Bv. San Juan', '850');
INSERT INTO usuarios (dni, telefono, contrasenia, email, nombres, apellidos, direccion, pais, provincia, codigoPostal, ciudad, calle, numeracion)
VALUES ('37891234', '+54 381 4459033', 'ClaveSegura22', 'martin.diaz@yahoo.com', 'Martín', 'Díaz', 'calle Rivadavia 310', 'Argentina', 'Tucumán', '4000', 'San Miguel de Tucumán', 'Rivadavia', '310');
INSERT INTO usuarios (dni, telefono, contrasenia, email, nombres, apellidos, direccion, pais, provincia, codigoPostal, ciudad, calle, numeracion)
VALUES ('42670988', '+54 299 5823310', 'abc123456', 'carla.ruiz@mail.com', 'Carla', 'Ruiz', 'San Martín 1500', 'Argentina', 'Neuquén', '8300', 'Neuquén', 'San Martín', '1500');
INSERT INTO usuarios (dni, telefono, contrasenia, email, nombres, apellidos, direccion, pais, provincia, codigoPostal, ciudad, calle, numeracion)
VALUES ('40562319', '+54 221 7789021', 'MiPass2024', 'federico.lopez@gmail.com', 'Federico', 'López', 'Diag. 80 925', 'Argentina', 'Buenos Aires', '1900', 'La Plata', 'Diag. 80', '925');
INSERT INTO usuarios (dni, telefono, contrasenia, email, nombres, apellidos, direccion, pais, provincia, codigoPostal, ciudad, calle, numeracion)
VALUES ('38945602', '+54 11 50123499', 'Passw0rd98', 'valentina.mendez@mail.com', 'Valentina', 'Méndez', 'calle Lima 640', 'Argentina', 'Buenos Aires', '1084', 'CABA', 'Lima', '640');
INSERT INTO usuarios (dni, telefono, contrasenia, email, nombres, apellidos, direccion, pais, provincia, codigoPostal, ciudad, calle, numeracion)
VALUES ('43120588', '+54 381 6678832', 'ClaveClave33', 'diego.farias@gmail.com', 'Diego', 'Farías', 'Av. Alem 200', 'Argentina', 'Tucumán', '4000', 'Yerba Buena', 'Av. Alem', '200');
INSERT INTO usuarios (dni, telefono, contrasenia, email, nombres, apellidos, direccion, pais, provincia, codigoPostal, ciudad, calle, numeracion)
VALUES ('41234990', '+54 261 5512030', 'Segura741', 'mariana.rios@hotmail.com', 'Mariana', 'Ríos', 'Godoy Cruz 540', 'Argentina', 'Mendoza', '5500', 'Mendoza', 'Godoy Cruz', '540');
INSERT INTO usuarios (dni, telefono, contrasenia, email, nombres, apellidos, direccion, pais, provincia, codigoPostal, ciudad, calle, numeracion)
VALUES ('39567820', '+54 381 4428999', 'Clave2025', 'juliancastro@mail.com', 'Julián', 'Castro', 'calle San Lorenzo 760', 'Argentina', 'Tucumán', '4107', 'Tafí Viejo', 'San Lorenzo', '760');

INSERT INTO productos (idCategoria, idUsuario, stock, fechaSubido, descripcion, precio)
VALUES (1, 1, 50, '2025-01-12', 'Camiseta de algodón talla M color negro', 8999.90);
INSERT INTO productos (idCategoria, idUsuario, stock, fechaSubido, descripcion, precio)
VALUES (2, 2, 15, '2025-01-08', 'Smartwatch con monitor de ritmo cardíaco', 45999.00);
INSERT INTO productos (idCategoria, idUsuario, stock, fechaSubido, descripcion, precio)
VALUES (3, 3, 8, '2025-01-10', 'Auriculares bluetooth con cancelación de ruido', 29999.50);
INSERT INTO productos (idCategoria, idUsuario, stock, fechaSubido, descripcion, precio)
VALUES (1, 4, 120, '2025-01-15', 'Pantalón jean azul clásico talla 42', 21999.00);
INSERT INTO productos (idCategoria, idUsuario, stock, fechaSubido, descripcion, precio)
VALUES (4, 5, 30, '2025-01-18', 'Juego de tenedores y cuchillos de acero inoxidable (12 piezas)', 12499.75);
INSERT INTO productos (idCategoria, idUsuario, stock, fechaSubido, descripcion, precio)
VALUES (2, 3, 5, '2025-01-19', 'Smartphone 6.5" 128GB 6GB RAM color azul', 185000.00);
INSERT INTO productos (idCategoria, idUsuario, stock, fechaSubido, descripcion, precio)
VALUES (5, 2, 20, '2025-01-11', 'Mouse gamer RGB con 7 botones programables', 15499.99);
INSERT INTO productos (idCategoria, idUsuario, stock, fechaSubido, descripcion, precio)
VALUES (3, 1, 10, '2025-01-09', 'Teclado mecánico retroiluminado switches red', 34999.00);
INSERT INTO productos (idCategoria, idUsuario, stock, fechaSubido, descripcion, precio)
VALUES (6, 4, 40, '2025-01-16', 'Botella térmica de acero inoxidable 750ml', 8999.00);
INSERT INTO productos (idCategoria, idUsuario, stock, fechaSubido, descripcion, precio)
VALUES (4, 5, 12, '2025-01-17', 'Olla antiadherente 24cm con recubrimiento cerámico', 25999.90);



