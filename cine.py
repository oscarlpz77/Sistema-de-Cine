from enum import Enum
from datetime import date

class RolEmpleado(Enum):
    TAQUILLERO = "Taquillero"
    ADMIN = "Admin"
    LIMPIEZA = "Limpieza"


class TipoSala(Enum):
    DOS_D = "2D"
    TRES_D = "3D"
    IMAX = "IMAX"


class EstadoReserva(Enum):
    PENDIENTE = "Pendiente"
    PAGADA = "Pagada"
    CANCELADA = "Cancelada"


class Persona:
    def __init__(self, idPersona, nombre, email, telefono):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def login(self):
        print(self.nombre, "ha iniciado sesión")

    def logout(self):
        print(self.nombre, "ha cerrado sesión")

    def actualizarDatos(self):
        print("Datos actualizados")


class Usuario(Persona):
    def __init__(self, idPersona, nombre, email, telefono, puntosFidelidad):
        super().__init__(idPersona, nombre, email, telefono)
        self.puntosFidelidad = puntosFidelidad
        self.historialReservas = []

    def crearReserva(self, reserva):
        self.historialReservas.append(reserva)

    def consultarPromociones(self):
        print("Consultando promociones")

    def cancelarReserva(self, reserva):
        print("Reserva cancelada")


class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, telefono, idEmpleado, rol, horario):
        super().__init__(idPersona, nombre, email, telefono)
        self.idEmpleado = idEmpleado
        self.rol = rol
        self.horario = horario

    def marcarEntrada(self):
        print(self.nombre, "marcó entrada")

    def gestionarFunciones(self):
        if self.rol == RolEmpleado.ADMIN:
            print("Gestionando funciones")


class Espacio:
    def __init__(self, idEspacio, nombre, ubicacion):
        self.idEspacio = idEspacio
        self.nombre = nombre
        self.ubicacion = ubicacion

    def verificarDisponibilidad(self):
        print("Verificando disponibilidad")

    def limpiarEspacio(self):
        print("Espacio limpio")


class Sala(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion, tipo, capacidadTotal, esVip):
        super().__init__(idEspacio, nombre, ubicacion)
        self.tipo = tipo
        self.capacidadTotal = capacidadTotal
        self.esVip = esVip

    def ajustarAforo(self):
        print("Aforo ajustado")

    def obtenerTipoSala(self):
        return self.tipo


class ZonaComida(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion):
        super().__init__(idEspacio, nombre, ubicacion)
        self.listaProductos = []
        self.stockActual = {}

    def venderProducto(self, producto):
        print("Producto vendido:", producto)

    def actualizarInventario(self):
        print("Inventario actualizado")


class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

    def obtenerSinopsis(self):
        print("Mostrando sinopsis")

    def esAptaParaTodoPublico(self):
        return self.clasificacion == "A"


class Funcion:
    def __init__(self, idFuncion, pelicula, sala, horarioInicio, precioBase):
        self.idFuncion = idFuncion
        self.pelicula = pelicula
        self.sala = sala
        self.horarioInicio = horarioInicio
        self.precioBase = precioBase

    def calcularAsientosLibres(self):
        print("Calculando asientos disponibles")

    def obtenerDetallesFuncion(self):
        print(self.pelicula.titulo, "-", self.horarioInicio)


class Promocion:
    def __init__(self, codigo, descripcion, porcentajeDescuento, fechaExpiracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentajeDescuento = porcentajeDescuento
        self.fechaExpiracion = fechaExpiracion

    def esValida(self):
        return date.today() <= self.fechaExpiracion

    def aplicarDescuento(self, monto):
        return monto - (monto * self.porcentajeDescuento / 100)


class Reserva:
    def __init__(self, idReserva, usuario, funcion, asientos):
        self.idReserva = idReserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.montoTotal = funcion.precioBase * len(asientos)
        self.estado = EstadoReserva.PENDIENTE

    def confirmarPago(self):
        self.estado = EstadoReserva.PAGADA

    def aplicarPromocion(self, promo):
        if promo.esValida():
            self.montoTotal = promo.aplicarDescuento(self.montoTotal)

    def generarTicket(self):
        print("\nResumen de Reserva #" + str(self.idReserva))
        print("Usuario:", self.usuario.nombre)
        print("Función:", self.funcion.pelicula.titulo, "-", self.funcion.horarioInicio)
        print("Asientos:", self.asientos)
        print("Total:", self.montoTotal)
        print("Estado:", self.estado.value)
        
        
        
        
        
        
        
        
        
        