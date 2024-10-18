from scapy.all import ARP, Ether, srp  # Importar las clases necesarias de la biblioteca Scapy
import os  # Importar el módulo os para ejecutar comandos del sistema

def get_default_gateway():
    """Obtiene la dirección IP de la puerta de enlace predeterminada."""
    # Ejecutar un comando del sistema para obtener la dirección IP de la puerta de enlace
    gateway = os.popen("ip route | grep default | awk '{print $3}'").read().strip()
    return gateway  # Devolver la dirección IP de la puerta de enlace

def scan_network(ip_range):
    """Escanea la red y devuelve una lista de dispositivos conectados."""
    # Crear un paquete ARP para la dirección IP especificada
    arp = ARP(pdst=ip_range)
    # Crear un paquete Ethernet con la dirección de destino de broadcast
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combinar el paquete ARP con el paquete Ethernet
    packet = ether / arp

    # Enviar el paquete y recibir las respuestas
    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []  # Lista para almacenar los dispositivos encontrados
    for sent, received in result:
        # Agregar la dirección IP y MAC de cada dispositivo a la lista
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices  # Devolver la lista de dispositivos encontrados

def print_devices(devices):
    """Imprime la lista de dispositivos conectados."""
    print("Dispositivos conectados:")
    print("IP\t\t\tMAC")
    print("-------------------------")
    for device in devices:
        # Imprimir la dirección IP y MAC de cada dispositivo
        print(f"{device['ip']}\t{device['mac']}")

if __name__ == "__main__":
    # Obtener la puerta de enlace predeterminada
    gateway_ip = get_default_gateway()
    
    # Asumir que la subred es /24
    ip_range = f"{gateway_ip}/24"  # Crear el rango de IP basado en la puerta de enlace
    devices = scan_network(ip_range)  # Escanear la red
    print_devices(devices)  # Imprimir los dispositivos encontrados
