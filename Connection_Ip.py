from scapy.all import ARP, Ether, srp
import os

def get_default_gateway():

    gateway = os.popen("ip route | grep default | awk '{print $3}'").read().strip()
    return gateway

def scan_network(ip_range):

    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def print_devices(devices):

    print("Dispositivos conectados:")
    print("IP\t\t\tMAC")
    print("-------------------------")
    for device in devices:
        print(f"{device['ip']}\t{device['mac']}")

if __name__ == "__main__":

    gateway_ip = get_default_gateway()
    

    ip_range = f"{gateway_ip}/24"
    devices = scan_network(ip_range)
    print_devices(devices)
