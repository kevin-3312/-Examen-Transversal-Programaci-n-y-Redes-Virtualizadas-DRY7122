from ncclient import manager

router = {
    "host": "192.168.56.102",
    "port": 830,
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False
}

config = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">

        <hostname>Digmann-Lipin-Miranda</hostname>

        <interface>

            <Loopback>

                <name>11</name>

                <ip>
                    <address>
                        <primary>
                            <address>11.11.11.11</address>
                            <mask>255.255.255.255</mask>
                        </primary>
                    </address>
                </ip>

            </Loopback>

        </interface>

    </native>
</config>
"""

with manager.connect(**router) as m:

    respuesta = m.edit_config(target="running", config=config)

    print(respuesta)
