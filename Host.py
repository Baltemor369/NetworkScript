from utils import subnet_mask_to_cidr
class Host:
    def __init__(self, name: str, ip: str, mac: str, mask: str) -> None:
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
        #TODO regex checking mask
        if mask.find("/"):
            self.mask = mask
        else:
            self.mask = subnet_mask_to_cidr(mask)
