from pyModbusTCP.client import ModbusClient

def Modbus(IP, Puerto, Registro, Cantidad_de_Registros, ID_Dispositivo):
    Regs = list()
    try: 
        c = ModbusClient(host=IP, 
                         port=Puerto,
                         unit_id=ID_Dispositivo,
                         debug=False,
                         auto_open=True, 
                         auto_close=True)
        Regs = c.read_holding_registers(Registro, Cantidad_de_Registros)
        Message = 'Comunicación Modbus Correcta'
    except:
        Message = 'Error de la función'
    return Regs, Message

