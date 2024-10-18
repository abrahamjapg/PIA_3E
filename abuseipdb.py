import requests
import json
import ModuloRegistro_Manejo

# Estos son los links del API
# CHECK IP -> https://www.abuseipdb.com/check/[IP]/json?key=[API_KEY]&days=[DAYS]
# CHECK CIDR -> https://www.abuseipdb.com/check-block/json?network=[CIDR]&key=[API_KEY]&days=[DAYS]
# REPORT IP -> https://www.abuseipdb.com/report/json?key=[API_KEY]&category=[CATEGORIES]&comment=[COMMENT]&ip=[IP]

ModuloRegistro_Manejo.establecer_loggeos()

opc = int(input("""Ingresa la opción que desees: 
                [1] Para checar si una IP ha sido colocada en la lista negra de IPs maliciosas
                [2] Para checar el CIDR ("Familia de IPs maliciosas")
                [3] Para reportar una IP maliciosa.\n"""))

if opc == 1:
    print("Usted entró a la opción de checar si la IP está en la lista negra de IPs maliciosas")
    url1 = 'https://api.abuseipdb.com/api/v2/blacklist'
    ipb = str(input("Ingresa la IP que quieres verificar si se encuentra en la lista negra: "))
    querystring = {
        'IpAddress': ipb, 
        'confidenceMinimum': '90'
    }
    #En cada uno de las opciones de los modulos vendrá estaw opción de leer el archivo txt donnde se encuientra la opción de leer la apikey,
    #tendras que guarda en el archivo donde tengas este codigo un archivo con nombre (ApiKey) y de ahi mismo lo leera.
    with open('ApiKey.txt', 'r') as archivo:
        llave = archivo.read().strip()
    headers = {
        'Accept': 'application/json',
        'Key': llave
    }
    response = requests.get(url=url1, headers=headers, params=querystring)
    decodedResponse = response.json()
    print(json.dumps(decodedResponse, sort_keys=True, indent=4))

elif opc == 2:
    print("Usted ingresó a la opción de checar la familia de la IP ingresada")
    url = 'https://api.abuseipdb.com/api/v2/check-block'
    network1=input("Ingresa la ip con la notacion CIDR (8.8.8.8/24)")
    querystring = {
        'network': network1,
        'maxAgeInDays': '15'
    }
    with open('apikey.txt', 'r') as archivo:
        llave = archivo.read().strip()
    headers = {
        'Accept': 'application/json',
        'Key': llave
    }
    response = requests.get(url=url, headers=headers, params=querystring)
    decodedResponse = response.json()
    print(json.dumps(decodedResponse, sort_keys=True, indent=4))

elif opc == 3:
    print("Usted ingresó a la opción para reportar una IP")
    url = 'https://api.abuseipdb.com/api/v2/report'
    ip = (input("Ingrese la Ip que quiere reportar: "))
    categories = input("""Ingrese el número de la categoria en la que se encuentra la IP maliciosa
                            1. Compromiso de DNS: Alteración de registros DNS que resulta en una redirección incorrecta.
                            2. Envenenamiento de DNS: Falsificación de la caché del servidor de dominio (envenenamiento de caché).
                            3. Pedidos fraudulentos: Órdenes fraudulentas.
                            4. Ataque DDoS: Participación en un ataque de denegación de servicio distribuido (usualmente parte de una botnet).
                            5. Fuerza bruta en FTP.
                            6. Ping de la muerte: Paquete IP de gran tamaño.
                            7. Phishing: Sitios web o correos electrónicos de phishing.
                            8. Fraude en VoIP.
                            9. Proxy abierto: Proxy abierto, relé abierto o nodo de salida de Tor.
                            10. Spam web: Spam en comentarios/foros, spam en HTTP referer, u otro spam en CMS.
                            11. Spam de correo electrónico: Contenido de correo electrónico spam, archivos adjuntos infectados y correos electrónicos de phishing. Nota: Limita los comentarios a solo la información relevante (en lugar de volcados de registros) y asegúrate de eliminar PII si deseas permanecer anónimo.
                            12. Spam en blogs: Spam en comentarios de blogs en CMS.
                            13. IP de VPN: Categoría conjunta.
                            14. Escaneo de puertos: Escaneo en busca de puertos abiertos y servicios vulnerables.
                            15. Hackeo.
                            16. Inyección SQL: Intentos de inyección SQL.
                            17. Suplantación: Suplantación del remitente de correo electrónico.
                            18. Fuerza bruta: Ataques de fuerza bruta de credenciales en inicios de sesión de páginas web y servicios como SSH, FTP, SIP, SMTP, RDP, etc. Esta categoría es diferente de los ataques DDoS.
                            19. Bot web malicioso: Raspado de páginas web (para direcciones de correo electrónico, contenido, etc.) y rastreadores que no respetan robots.txt. Las solicitudes excesivas y la suplantación del agente de usuario también pueden ser reportadas aquí.
                            20. Host explotado: El host probablemente esté infectado con malware y siendo utilizado para otros ataques o para alojar contenido malicioso. El propietario del host puede no estar al tanto del compromiso. Esta categoría a menudo se usa en combinación con otras categorías de ataque.
                            21. Ataque a aplicaciones web: Intentos de explorar o explotar aplicaciones web instaladas, como un CMS (sistema de gestión de contenido) como WordPress/Drupal, soluciones de comercio electrónico, software de foros, phpMyAdmin y varios otros plugins/soluciones de software.
                            22. Abuso de SSH: Abuso de Secure Shell (SSH). Usa esta categoría en combinación con otras categorías más específicas.
                            23. Objetivo IoT: El abuso fue dirigido a un dispositivo del "Internet de las cosas" (IoT). Incluye información sobre qué tipo de dispositivo fue objetivo en los comentarios. """)
    comentarios = str(input("Ingrese algún comentario acerca el comportamiento de esta ip maliciosa: "))
    params = { 
        'ip': ip,
        'categories': categories,
        'comment': comentarios
    }
    with open('apikey.txt', 'r') as archivo:
        llave = archivo.read().strip()
    headers = {
        'Accept': 'application/json',
        'Key': llave
    }
    response = requests.post(url=url, headers=headers, params=params)
    decodedResponse = response.json()
    print(json.dumps(decodedResponse, sort_keys=True, indent=4))

else:
    print("Opción no válida. Por favor ingrese una opción válida (1, 2 o 3).")
