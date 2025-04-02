class Router:
    def __init__(self, hostname, nb_intf):
        self.hostname = hostname
        self.nb_intf = nb_intf
        self.interfaces = []
        self.vlans = []