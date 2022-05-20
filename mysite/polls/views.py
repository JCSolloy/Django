from django.http import HttpResponse
from pyModbusTCP.client import ModbusClient
from django.template import loader
from .models import Dispositivo

def index(request):
    return HttpResponse('index')

def home(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def modbus(request):
    Dispositivos = Dispositivo.objects.all().values()
    Cliente = Dispositivo.objects.values_list('Proyecto').filter(Cliente='Lo de Valdez')

    Registro = Dispositivo.objects.values_list('Registros').filter(Cliente = 'EMPAGUA')
    Cantidad_de_Registros = Dispositivo.objects.values_list('Cantidad_de_Registros').filter(Cliente = 'EMPAGUA')
    IP = Dispositivo.objects.values_list('IP').filter(Cliente = 'EMPAGUA')
    Puerto = Dispositivo.objects.values_list('Puerto').filter(Cliente = 'EMPAGUA')
    ID_Labview = Dispositivo.objects.values_list('ID_Labview').filter(Cliente = 'EMPAGUA')
    Modbus_ID = Dispositivo.objects.values_list('Modbus_ID').filter(Cliente = 'EMPAGUA')

    template = loader.get_template('modbus.html')
    if request.method == 'POST':
        c = ModbusClient(
                 host="10.97.0.188",
                 port=502,
                 unit_id=0,
                 debug=False,
                 auto_open=True,
                 auto_close=True)

        regs = c.read_holding_registers(4419, 10)

        registros = 'Registros interrogados ' + str(regs) 

        context = {
            'Dispositivos' : Dispositivos,
            'Registros' : registros,
            'Cliente' : Cliente,
            'Registro' : Registro,
            'Cantidad_de_Registros' : Cantidad_de_Registros,
            'IP' : IP,
            'ID_Labview' : ID_Labview,
            'Modbus_ID' : Modbus_ID,
            }
    else:

        context = {
            'Dispositivos' : Dispositivos,
            'Registros' : ' ',
            }
    return HttpResponse(template.render(context, request))
