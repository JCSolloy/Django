from django.http import HttpResponse
from pyModbusTCP.client import ModbusClient
from django.template import loader
from .models import Dispositivo
import subprocess
import platform

def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '10', host]
    response = subprocess.call(command)
    return response
#Funcion que realiza la conexión Modbus
def Modbus(IP, Puerto, Registros, Cantidad_de_Registros, Modbus_ID):
     Regs = list()
     try: 
         c = ModbusClient(host=IP, 
                          port=Puerto,
                          unit_id=Modbus_ID,
                          debug=False,
                          auto_open=True, 
                          auto_close=True)
         Regs = c.read_holding_registers(Registros, Cantidad_de_Registros)
         if Regs:
            Communication = True
            Message = 'Registros leidos correctamente'
         else:
            Communication = False
            Message = 'Error al leer registros'
     except:
         Message = 'Error de la función'
     return Regs, Message, Communication

def index(request):
    return HttpResponse('index')

def home(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def modbus(request):
    '''
    Se obtienen los valores de la base de datos y se filtra por el ID_Labview
    el Queryset se convierte a tipo listta y el primer elemento de la lista es el diccionario de los 
    valores de cada dispositivo.
    '''
    Dispositivos = list(Dispositivo.objects.all().values())
    Cliente = 'Cliente'
    Proyecto = 'Proyecto'
    IP = '0.0.0.0'
    Registros = 0 
    Cantidad_de_Registros = 0 
    Puerto = 0
    ID_Labview = '000_000_000_0000_0000' 
    Dispositivo_de_Comunicación ='00000'
    Marca_Sensor = '00000'
    Modelo_Sensor = '00000'
    Medición = '00000'
    Modbus_ID = 0
    Com = list()
    ping = False
    state = False

    if request.method == 'POST':
        idlabview = request.POST["Dispositivo"]
        Datos = list(Dispositivo.objects.all().values().filter(ID_Labview = idlabview))
        Cliente = Datos[0].get('Cliente')
        Proyecto = Datos[0].get('Proyecto')
        IP = Datos[0].get('IP')
        Registros = int(Datos[0].get('Registros')) 
        Cantidad_de_Registros = int(Datos[0].get('Cantidad_de_Registros')) 
        Puerto = int(Datos[0].get('Puerto'))
        ID_Labview = Datos[0].get('ID_Labview')
        Dispositivo_de_Comunicación = Datos[0].get('Dispositivo_de_Comunicación')
        Marca_Sensor = Datos[0].get('Marca_Sensor')
        Modelo_Sensor = Datos[0].get('Modelo_Sensor')
        Medición = Datos[0].get('Medición')
        Modbus_ID = int(Datos[0].get('Modbus_ID'))
        
        Com = Modbus(IP, Puerto, Registros, Cantidad_de_Registros, Modbus_ID)
        state = Com[2]

        context = {
            'Dispositivos' :Dispositivos,
            'Cliente' : Cliente,
            'Proyecto' : Proyecto,
            'IP' : IP,
            'Registros' : Registros,
            'Cantidad_de_Registros' : Cantidad_de_Registros,
            'Puerto' : Puerto,
            'ID_Labview' : ID_Labview,
            'Dispositivo_de_Comunicación' : Dispositivo_de_Comunicación,
            'Marca_Sensor' : Marca_Sensor,
            'Modelo_Sensor' : Modelo_Sensor,
            'Medición' : Medición,
            'Modbus_ID' : Modbus_ID,
            'Com' : Com,
            'state' : state,
            }
    else:
        context = {
            'Dispositivos' :Dispositivos,
            'Cliente' : Cliente,
            'Proyecto' : Proyecto,
            'IP' : IP,
            'Registros' : Registros,
            'Cantidad_de_Registros' : Cantidad_de_Registros,
            'Puerto' : Puerto,
            'ID_Labview' : ID_Labview,
            'Dispositivo_de_Comunicación' : Dispositivo_de_Comunicación,
            'Marca_Sensor' : Marca_Sensor,
            'Modelo_Sensor' : Modelo_Sensor,
            'Medición' : Medición,
            'Modbus_ID' : Modbus_ID,
            'Com' : Com,
            'state' : state,
            }

    template = loader.get_template('modbus.html')
    return HttpResponse(template.render(context, request))
