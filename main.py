from cine import *

print("\n--- Registro de Inventario ---")

productos = [
("Palomitas Grandes",85,"Snacks"),
("Refresco Mediano",45,"Bebidas"),
("Hot Dog",60,"Comida"),
("Nachos con Queso",70,"Snacks"),
("Chocolate Crunch",35,"Dulces"),
("Agua Ciel 600ml",30,"Bebidas"),
("Combo Pareja",210,"Combos"),
("Entrada 2D Adulto",80,"Boletos"),
("Entrada 3D Niño",65,"Boletos"),
("Cubeta Promocional",150,"Promos")
]

for i,p in enumerate(productos,1):
    print("ID", i, p[0], "Precio", p[1], "Categoria", p[2])

print("\n--- Validación de datos finalizada ---\n")

usuarios = [
Usuario(1,"Carlos Hernandez","carlos.hernandez@gmail.com","+52 2223456781",150),
Usuario(2,"Ana Lopez","ana.lopez@gmail.com","+52 2214567823",200),
Usuario(3,"Luis Martinez","luis.martinez@gmail.com","+52 2225678912",90),
Usuario(4,"Maria Rodriguez","maria.rodriguez@gmail.com","+52 2216789124",300),
Usuario(5,"Pedro Garcia","pedro.garcia@gmail.com","+52 2227891235",110),
Usuario(6,"Lucia Torres","lucia.torres@gmail.com","+52 2218902346",70),
Usuario(7,"Andres Sanchez","andres.sanchez@gmail.com","+52 2229013457",50),
Usuario(8,"Rosa Ramirez","rosa.ramirez@gmail.com","+52 2212344568",130),
Usuario(9,"Miguel Castillo","miguel.castillo@gmail.com","+52 2223455679",10),
Usuario(10,"Diana Morales","diana.morales@gmail.com","+52 2214566780",220)
]

empleados = [
Empleado(1,"Juan Perez","juan.perez@gmail.com","+52 2223001001","E01",RolEmpleado.TAQUILLERO,"mañana"),
Empleado(2,"Laura Gomez","laura.gomez@gmail.com","+52 2213001002","E02",RolEmpleado.ADMIN,"mañana"),
Empleado(3,"Jose Fernandez","jose.fernandez@gmail.com","+52 2223001003","E03",RolEmpleado.LIMPIEZA,"tarde"),
Empleado(4,"Mario Rivera","mario.rivera@gmail.com","+52 2213001004","E04",RolEmpleado.TAQUILLERO,"tarde"),
Empleado(5,"Sofia Ortega","sofia.ortega@gmail.com","+52 2223001005","E05",RolEmpleado.ADMIN,"mañana"),
Empleado(6,"Pedro Vargas","pedro.vargas@gmail.com","+52 2213001006","E06",RolEmpleado.LIMPIEZA,"noche"),
Empleado(7,"Ana Castillo","ana.castillo@gmail.com","+52 2223001007","E07",RolEmpleado.TAQUILLERO,"mañana"),
Empleado(8,"Luis Mendoza","luis.mendoza@gmail.com","+52 2213001008","E08",RolEmpleado.ADMIN,"tarde"),
Empleado(9,"Clara Jimenez","clara.jimenez@gmail.com","+52 2223001009","E09",RolEmpleado.LIMPIEZA,"tarde"),
Empleado(10,"David Romero","david.romero@gmail.com","+52 2213001010","E10",RolEmpleado.TAQUILLERO,"mañana")
]

salas = [
Sala(1,"Sala 1","Planta Baja",TipoSala.DOS_D,100,False),
Sala(2,"Sala 2","Planta Baja",TipoSala.TRES_D,120,False),
Sala(3,"Sala 3","Planta Alta",TipoSala.IMAX,150,True),
Sala(4,"Sala 4","Planta Alta",TipoSala.IMAX,150,True),
Sala(5,"Sala 5","PB",TipoSala.DOS_D,90,False),
Sala(6,"Sala 6","PB",TipoSala.TRES_D,110,False),
Sala(7,"Sala 7","PA",TipoSala.IMAX,140,True),
Sala(8,"Sala 8","PA",TipoSala.DOS_D,80,False),
Sala(9,"Sala 9","PB",TipoSala.TRES_D,100,False),
Sala(10,"Sala 10","PA",TipoSala.IMAX,160,True)
]

peliculas = [
Pelicula("Avengers Doomsday",160,"B","Accion"),
Pelicula("The Batman Part II",150,"B","Accion"),
Pelicula("Toy Story 5",110,"A","Animacion"),
Pelicula("Shrek 5",105,"A","Animacion"),
Pelicula("Super Mario Bros 2",100,"A","Animacion"),
Pelicula("Frozen 3",120,"A","Animacion"),
Pelicula("Minions 3",95,"A","Comedia"),
Pelicula("Spider Man 4",140,"B","Accion"),
Pelicula("Fast and Furious 11",150,"B","Accion"),
Pelicula("The Mandalorian and Grogu",130,"B","SciFi")
]

funciones = [
Funcion(1,peliculas[0],salas[0],"20:00",150),
Funcion(2,peliculas[1],salas[1],"18:00",150),
Funcion(3,peliculas[2],salas[2],"17:00",150),
Funcion(4,peliculas[3],salas[3],"19:00",150),
Funcion(5,peliculas[4],salas[4],"16:00",150),
Funcion(6,peliculas[5],salas[5],"21:00",150),
Funcion(7,peliculas[6],salas[6],"20:30",150),
Funcion(8,peliculas[7],salas[7],"22:00",150),
Funcion(9,peliculas[8],salas[8],"19:30",150),
Funcion(10,peliculas[9],salas[9],"18:30",150)
]

promos = [
Promocion("PROMO_ESTUDIANTE","20% desc",20,date(2026,12,31)),
Promocion("PROMO2","10%",10,date(2026,12,31)),
Promocion("PROMO3","15%",15,date(2026,12,31)),
Promocion("PROMO4","5%",5,date(2026,12,31)),
Promocion("PROMO5","25%",25,date(2026,12,31)),
Promocion("PROMO6","30%",30,date(2026,12,31)),
Promocion("PROMO7","18%",18,date(2026,12,31)),
Promocion("PROMO8","12%",12,date(2026,12,31)),
Promocion("PROMO9","22%",22,date(2026,12,31)),
Promocion("PROMO10","8%",8,date(2026,12,31))
]

print("\nIniciando Reserva\n")

usuario = usuarios[0]
funcion = funciones[0]

print("Usuario:",usuario.nombre)
print("Pelicula:",funcion.pelicula.titulo)
print("Sala:",funcion.sala.nombre)

asientos = ["A1","A3","B5"]

reserva = Reserva(995,usuario,funcion,asientos)

print("Asientos:",asientos)
print("Monto base:",reserva.montoTotal)

promo = promos[0]

print("\nAplicando promocion")

if promo.esValida():
    reserva.aplicarPromocion(promo)
    print("Codigo:",promo.codigo)
    print("Descuento:",promo.porcentajeDescuento,"%")

reserva.confirmarPago()

reserva.generarTicket() 




