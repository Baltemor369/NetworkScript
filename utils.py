import json

def int_input(question:str, min=None, max:int=None):
    while True:
        try:
            number = int(input(question))
        except:
            number = None
        if number:
            if (min is None or min <= number) and (max is None or number <= max):
                return number
        else:
            print("Please enter a valid answer.")

def closed_question(question:str, answers:list[str]):
    _ = input(question)
    
    for answer in answers:
        if _ and _ in answer:
            return answer
    
    return None

def subnet_mask_to_cidr(mask: str) -> str:
    """
    Convertit un masque de sous-réseau en notation CIDR.

    Args:
        mask (str): Masque de sous-réseau au format '255.255.255.0'.

    Returns:
        str: Notation CIDR correspondante (ex: '/24').
    """
    # Convertir chaque octet en binaire et compter les bits à 1
    cidr = sum(bin(int(octet)).count('1') for octet in mask.split('.'))
    return f"/{cidr}"

def save_config(file:str, data:dict):
    # Écriture dans un fichier JSON
    with open(file, "w") as fichier:
        json.dump(data, fichier, indent=4)  # `indent=4` pour une meilleure lisibilité

def load_config(file: str) -> dict:
    # Lecture depuis le fichier JSON
    with open(file, "r") as fichier:
        return json.load(fichier)