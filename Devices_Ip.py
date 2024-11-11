"""
Este modulo escanea la red y muestra los dispositivos conectados
"""

import os
import subprocess
import sys
import platform
import re
import hashlib
 
#Funcion para instalar librerias
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
 
#Ve si la libreria esta instalada
try:
    from scapy.all import ARP, Ether, srp
except ImportError:
    print("Scapy not installed. Installing...")
    install("scapy")
    from scapy.all import ARP, Ether, srp
 
 
def get_default_gateway():
    #Comando para windows
    if platform.system() == "Windows":
        output = os.popen('ipconfig').read()
        gateway = re.search(r'Puerta de enlace predeterminada[^\d]*(\d+\.\d+\.\d+\.\d+)', output)
        gateway = gateway.group(1)
    else:
        #Comando para Unix
        gateway = os.popen("ip route | grep default | awk '{print $3}'").read().strip()
    return gateway
 
def scan_network(ip_range):
    #Escanea la red y muestra los dispositivos conectados
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=0)[0]
 
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
 
    return devices

def Print_Terminal():
    n = 'DireccionesIp.txt'
    f = open(n, 'rb')
    file_bytes = f.read()
    f.close()
    m = hashlib.sha256()
    m.update(file_bytes)
    hash = m.hexdigest()
    dir_actual = os.path.dirname(os.path.abspath('DireccionesIp.txt'))
    print(f'Se guardo el documento con el nombre: {n}')
    print(f'Se guardo en la ubicacion: {dir_actual}')
    print('Hash del archivo: {}'.format(hash))
 
def Devices_IP():
    #Obtiene la red predeterminada del dispositivo
    gateway_ip = get_default_gateway()
    ip_range = f"{gateway_ip}/24"
    devices = scan_network(ip_range)
    with open('DireccionesIp.txt', mode='w') as file_object:
        print(devices, file=file_object)
    Print_Terminal()
    
    # Asumir que la subred es /24
    ip_range = f"{gateway_ip}/24"  # Crear el rango de IP basado en la puerta de enlace
    devices = scan_network(ip_range)  # Escanear la red
    print_devices(devices)  # Imprimir los dispositivos encontrados
