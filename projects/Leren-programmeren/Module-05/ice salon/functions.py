def intInput(prompt: str) -> int:
    while True:
        amount = input(prompt)
        try:
            amount = int(amount)
            return amount
        except ValueError:
            print("Sorry, dat begrijp ik niet.")

def askUser(prompt: str, data: list) -> str:
    while True:
        question = input(prompt).lower()
        if question in data:
            return question
        else:
            print("Sorry, dat begrijp ik niet.")