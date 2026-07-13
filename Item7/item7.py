from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.102",
    "username": "admin",
    "password": "admin",
    "secret": "admin"
}

conexion = ConnectHandler(**router)
conexion.enable()

configuracion = [

    "router eigrp REDES",

    "address-family ipv4 autonomous-system 100",

    "network 192.168.56.0 0.0.0.255",

    "af-interface GigabitEthernet1",
    "passive-interface",

    "exit-af-interface",

    "exit-address-family",

    "address-family ipv6 autonomous-system 100",

    "af-interface GigabitEthernet1",
    "passive-interface",

    "exit-af-interface",

    "exit-address-family"

]

print("Configurando EIGRP...\n")

salida = conexion.send_config_set(configuracion)

print(salida)

print("\n==============================")
print("CONFIGURACION EIGRP")
print("==============================")

print(conexion.send_command(
    "show running-config | section eigrp"
))

print("\n==============================")
print("INTERFACES")
print("==============================")

print(conexion.send_command(
    "show ip interface brief"
))

print("\n==============================")
print("RUNNING CONFIG")
print("==============================")

print(conexion.send_command(
    "show running-config"
))

print("\n==============================")
print("SHOW VERSION")
print("==============================")

print(conexion.send_command(
    "show version"
))

conexion.disconnect()
