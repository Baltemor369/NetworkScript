class Server:
    def __init__(self, name: str, ip: str, mac: str, subnet: str) -> None:
        """
        Initialise un objet Host.

        Args:
            name (str): Nom du host.
            ip (str): Adresse IP du host.
            mac (str): Adresse MAC du host.
            subnet (str): Masque de sous-réseau du host.
        """
        self.name = name
        self.ip = ip
        self.subnet = subnet
