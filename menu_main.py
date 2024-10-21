import sys

# Asumiendo que los archivos están en la misma carpeta o en el PATH
import shodanAPI_module as shodan_api
import abuseipdb as abuse_ip
import Malware_analyzer_module as malware_analyzer
import Devices_Ip as devices_ip
import Cifrado_Cesar as cifrado_cesar

# Función del menú interactivo
def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Ejecutar Shodan API Module")
    print("2. Ejecutar AbuseIPDB Module")
    print("3. Ejecutar Malware Analyzer Module")
    print("4. Ejecutar Devices IP Module")
    print("5. Ejecutar Cifrado César Module")
    print("6. Salir")

def ejecutar_shodan_api():
    print("\nEjecutando Shodan API Module...")
    shodan_api.main()  # Llamada a la función principal o específica del módulo

def ejecutar_abuse_ipdb():
    print("\nEjecutando AbuseIPDB Module...")
    abuse_ip.main()  # Llamada a la función principal o específica del módulo

def ejecutar_malware_analyzer():
    print("\nEjecutando Malware Analyzer Module...")
    malware_analyzer.main()  # Llamada a la función principal o específica del módulo

def ejecutar_devices_ip():
    print("\nEjecutando Devices IP Module...")
    devices_ip.main()  # Llamada a la función principal o específica del módulo

def ejecutar_cifrado_cesar():
    print("\nEjecutando Cifrado César Module...")
    cifrado_cesar.main()  # Llamada a la función principal o específica del módulo

# Función principal que ejecuta el menú y opciones
def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-6): ")

        if opcion == "1":
            ejecutar_shodan_api()
        elif opcion == "2":
            ejecutar_abuse_ipdb()
        elif opcion == "3":
            ejecutar_malware_analyzer()
        elif opcion == "4":
            ejecutar_devices_ip()
        elif opcion == "5":
            ejecutar_cifrado_cesar()
        elif opcion == "6":
            print("\nSaliendo del programa.")
            sys.exit()
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()



