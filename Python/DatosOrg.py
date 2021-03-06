# Source: https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/
# Script to organize data from .sav to sqlite

# loading modules
from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey, create_engine, MetaData

# Creating sqlite database engine
engine = create_engine('sqlite:///sqlalchemy_example.db')
meta = MetaData(bind=engine)

# Creating table
hogar = Table('hogar', meta,
    # Here we define columns for the table hogar
    # Notice that each column is also a normal Python instance attribute.
    Column('FORMULARIO', Integer, primary_key=False),
    Column('Depto', Integer, nullable=False),
    Column('Mun', Integer, nullable=False),
    Column('Fraccion', Integer, nullable=False),
    Column('Radio', Integer, nullable=False),
    Column('Viv', Integer, nullable=False),
    Column('NroHogar', Integer, nullable=False),
    Column('PM', Integer, nullable=False),
    Column('Zon', Integer, nullable=False),
    Column('Tip_viv', String, nullable=True),
    Column('CantidadPersonas', Integer, nullable=False),
    Column('PersonaMayorCuatro', Integer, nullable=False),
    Column('Personas_temporales', Integer, nullable=False),
    Column('CantidadCochera', Integer, nullable=False),
    Column('Hogar_Vehículo', String, nullable=False),
    Column('CantidadVehículos', String, nullable=True),
    Column('Tipo_vehículo_1', String, nullable=True),
    Column('Propiedad_vehículo_1', String, nullable=True),
    Column('MarcaVehículo_1', String, nullable=True),
    Column('Combustible_1', String, nullable=True),
    Column('Gasto_combustible_1', String, nullable=True),
    Column('GastoCochera_1', String, nullable=True),
    Column('GastoPatente_1', String, nullable=True),
    Column('GastoSeguro_1', String, nullable=True),
    Column('GastosTotal_1', String, nullable=True),
    Column('MarcaVehículo_2', String, nullable=True),
    Column('MarcaVehículo_3', String, nullable=True),
    Column('HogarMoto', String, nullable=False),
    Column('CantidadMotos', Integer, nullable=True),
    Column('HogarCiclomotor', String, nullable=False),
    Column('CantidadCiclomotores', String, nullable=True),
    Column('HogarBicicleta', String, nullable=False),
    Column('CantidadBicicletas', Integer, nullable=True),
    Column('Plan_social', String, nullable=False),
    Column('HogarIngresos', String, nullable=True),
    Column('RangoIngresos', String, nullable=True),
    Column('promedio_ingreso', String, nullable=True),
    Column('IngresoT1', String, nullable=True),
    Column('IngresoT2', String, nullable=True),
    Column('HogarGastoTotal', String, nullable=True),
    Column('RangoGastoTotal', String, nullable=True),
    Column('promedio_gastototal', String, nullable=True),
    Column('GastoT1', String, nullable=True),
    Column('GastoT2', String, nullable=True),
    Column('HogarGastosAlimentos', String, nullable=True),
    Column('RangoGastosAlimentos', String, nullable=True),
    Column('promedio_gasto_alimentos', String, nullable=True),
    Column('GastoA1', String, nullable=True),
    Column('HogarGastosTransporte', String, nullable=True),
    Column('RangoGastosTransporte', String, nullable=True),
    Column('Ingresoagregado_pers', String, nullable=True),
    Column('IngresoTotalFinal', String, nullable=True),
    Column('bienestar', String, nullable=False),
    Column('FEX', Float(6), nullable=False)
              )

miembros = Table("miembros", meta,
    Column("FORMULARIO", Integer, nullable=False),
    Column("PersNro", Integer, nullable=False),
    Column("PersID", Integer, nullable=False),
    Column("ViajeID", Integer, nullable=False),
    Column("LugarEntrevista", String, nullable=False),
    Column("TipoEntrevista", String, nullable=False),
    Column("InfNum", Integer, nullable=False),
    Column("Sexo", String, nullable=False),
    Column("Edad", Integer, nullable=False),
    Column("edad_recodif", String, nullable=False),
    Column("CapDif", String, nullable=False),
    Column("CapDifMot", String, nullable=False),
    Column("CapDifMen", String, nullable=False),
    Column("CapDifVis", String, nullable=False),
    Column("CapDifAud", String, nullable=False),
    Column("CapDifHabla", String, nullable=False),
    Column("CapDifOtras", String, nullable=False),
    Column("RelacionJefeHogar", String, nullable=False),
    Column("PSH", String, nullable=False),
    Column("NivelEstudio", String, nullable=False),
    Column("PersonaCursando", String, nullable=False),
    Column("NivelEstudioCursando", String, nullable=False),
    Column("DescripciónEstCurs", String, nullable=False),
    Column("AmbitoEstudio", String, nullable=False),
    Column("LicenciaConducir", String, nullable=False),
    Column("OcupacionPrincipal", String, nullable=False),
    Column("Desc_ocuprinc", String, nullable=False),
    Column("OtraActividad", String, nullable=False),
    Column("Cual_act", String, nullable=False),
    Column("Rel_trab", String, nullable=False),
    Column("CategoríaLaboral", String, nullable=False),
    Column("AmbitoTrabajo", String, nullable=False),
    Column("Desc_ambtrab", String, nullable=False),
    Column("IngresoPersona", String, nullable=False),
    Column("Cantidad_Dinero", Integer, nullable=False),
    Column("RangoIngresos", String, nullable=False),
    Column("promedio_ingreso", Integer, nullable=False),
    Column("IngresoTotal", Integer, nullable=False),
    Column("realizo_viajes", String, nullable=False),
    Column("CantidadViajes", Integer, nullable=False),
    Column("Enfermedad", String, nullable=False),
    Column("Vacaciones", String, nullable=False),
    Column("No_Trabajó", String, nullable=False),
    Column("No_dinero_viajar", String, nullable=False),
    Column("Trabajó_casa", String, nullable=False),
    Column("Fuera_área", String, nullable=False),
    Column("No_hay_transporte", String, nullable=False),
    Column("No_transporte_discapacitados", String, nullable=False),
    Column("Calles_intransitables", String, nullable=False),
    Column("Paro_huelga", String, nullable=False),
    Column("Sin_clases", String, nullable=False),
    Column("Mal_tiempo", String, nullable=False),
    Column("No_necesidad_viajar", String, nullable=False),
    Column("Otro_motivo", String, nullable=False),
    Column("Desc_otromotiv", String, nullable=False),
    Column("Cons_sis", String, nullable=False),
    Column("Cons_restolíneas", String, nullable=False),
    Column("Usuario_frecuente", String, nullable=False),
    Column("Razón_no_viaja", String, nullable=False),
    Column("Seguridad", Integer, nullable=False),
    Column("Limpieza", Integer, nullable=False),
    Column("Espacio", Integer, nullable=False),
    Column("Trato_conductor", Integer, nullable=False),
    Column("Forma_conducción", Integer, nullable=False),
    Column("Frecuencia", Integer, nullable=False),
    Column("Información_frecuencias", Integer, nullable=False),
    Column("Tiempo_espera", Integer, nullable=False),
    Column("Accesibilidad_Distancia", Integer, nullable=False),
    Column("Seguridad_Paradas", Integer, nullable=False),
    Column("Bienestar", String, nullable=False),
    Column("FEX", Float(6), nullable=False)
)

# viajes
viajes = Table("viajes", meta,
    Column("FORMULARIO", Integer, nullable=False),
    Column("PersNro", Integer, nullable=False),
    Column("PersID", Integer, nullable=False),
    Column("NroViaje", Integer, nullable=False),
    Column("ViajeID", Integer, nullable=False),
    Column("CantidadEtapas", Integer, nullable=False),
    Column("Inf_Int", Integer, nullable=False),
    Column("ActividadOrigen", String, nullable=False),
    Column("ActividadDestino", String, nullable=False),
    Column("LugarOrigen", String, nullable=True),
    Column("Barrio", String, nullable=True),
    Column("CalleOrigen", String, nullable=True),
    Column("AlturaOrigen", String, nullable=True),
    Column("EsquinaOrigen", String, nullable=True),
    Column("HitoOrigen", String, nullable=True),
    Column("FraccionOrigen", Integer, nullable=False),
    Column("LugarDestino", String, nullable=False),
    Column("BarrioDestino", String, nullable=True),
    Column("CalleDestino", String, nullable=True),
    Column("AlturaDestino", String, nullable=True),
    Column("EsquinaDestino", String, nullable=True),
    Column("HitoDestino", String, nullable=True),
    Column("FraccionDestino", Integer, nullable=False),
    Column("zon_origen", String, nullable=False),
    Column("zon_destino", String, nullable=False),
    Column("Loc_viaje", String, nullable=True),
    Column("Hora_inicio", Integer, nullable=False),
    Column("HORA_EXTRAIDA", Integer, nullable=True),
    Column("Hora_llegada", Integer, nullable=True),
    Column("TiempoViaje", Integer, nullable=False),
    Column("Frecuencia", String, nullable=True),
    Column("Medio_Transporte", String, nullable=True),
    Column("Medio_recod", String, nullable=False),
    Column("auto_moto", String, nullable=False),
    Column("masivo_indiv", String, nullable=False),
    Column("Tip_serv", String, nullable=True),
    Column("Sexo", String, nullable=False),
    Column("Edad", String, nullable=False),
    Column("edad_recodif", String, nullable=False),
    Column("NivelEstudioCursando", String, nullable=True),
    Column("max_nivel_recod", String, nullable=False),
    Column("OcupacionPrincipal", String, nullable=False),
    Column("motivo_sin_hogar", String, nullable=False),
    Column("motivo_recod", String, nullable=False),
    Column("Ocupacional_Personal", String, nullable=False),
    Column("Distancia", Float(4), nullable=True),
    Column("Dist_recod", String, nullable=True),
    Column("Quintil_ingreso", String, nullable=True),
    Column("bienestar", String, nullable=True),
    Column("FEX", Float(6), nullable=False)
)

# Medios
medios = Table("medios", meta,
    Column("FORMULARIO", Integer, nullable=False),
    Column("PersNro", Integer, nullable=False),
    Column("PersID", Integer, nullable=False),
    Column("NroViaje", Integer, nullable=False),
    Column("ViajeID", Integer, nullable=False),
    Column("NroEtapa", Integer, nullable=True),
    Column("EtapaID", String, nullable=True),
    Column("Medio_Transporte", String, nullable=True),
    Column("Medio_Transporte_recod", String, nullable=True),
    Column("Medio_Definitivo", String, nullable=True),
    Column("Comp_viaje", String, nullable=True),
    Column("Cantidad", Integer, nullable=True),
    Column("Costo", Integer, nullable=True),
    Column("CuadCam", Integer, nullable=True),
    Column("MotCam", String, nullable=True),
    Column("CuadCamiAntes", String, nullable=True),
    Column("Espera", String, nullable=True),
    Column("EtapaDuracion", String, nullable=True),
    Column("CuadCamDesp", String, nullable=True),
    Column("MotCamAntes", String, nullable=True),
    Column("MotCamDesp", String, nullable=True),
    Column("LineaComienzo", String, nullable=True),
    Column("BarrioAsc", String, nullable=True),
    Column("FracRadAsc", String, nullable=True),
    Column("BarrioDesc", String, nullable=True),
    Column("FracRadDesc", String, nullable=True),
    Column("TipoBoleto", String, nullable=True),
    Column("CostoBoleto", String, nullable=True),
    Column("CuadrasantesAuto", String, nullable=True),
    Column("TiempoModo", String, nullable=True),
    Column("TiempoViaje", String, nullable=True),
    Column("CuadrasDespAuto", String, nullable=True),
    Column("Motcaminóantes", String, nullable=True),
    Column("Motcaminódespués", String, nullable=True),
    Column("Estacionamiento", String, nullable=True),
    Column("TipoEst", String, nullable=True),
    Column("TipoTarifaEst", String, nullable=True),
    Column("Tarifa", String, nullable=True),
    Column("FEX", Float(6), nullable=True)
)
meta.create_all(engine)
