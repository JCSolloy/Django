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
    template = loader.get_template('modbus.html')
    if request.method == 'POST':
        Cliente = request.POST['Cliente']
        Proyecto = Dispositivo.objects.filter(Cliente='EMPAGUA').values()
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
            }
    else:

        context = {
            'Dispositivos' : Dispositivos,
            'Registros' : ' ',
            }
    return HttpResponse(template.render(context, request))
