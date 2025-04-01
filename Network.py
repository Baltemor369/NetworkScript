class Network:
    def __init__(self, name):
        self.name = name
        self.switchs = []
    
    def add_switch(self, switch):
        self.switchs.append(switch)

    def del_switch(self, switch):
        self.switchs.remove(switch)