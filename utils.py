def int_input(question:str, min:int=None, max:int=None):
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