import scapy.all as scapy
from time import time


def escan(Direccion_Ip):
    scapy.arping(Direccion_Ip)

escan("192.168.1.9")