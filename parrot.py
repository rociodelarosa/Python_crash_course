"""Ejemplo 1"""
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

"""Ejemplo 2: while"""
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

"""Ejemplo 3: flag"""
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

activate = True
while activate:
    message = input(prompt)

    if message == 'quit':
        activate = False
    else:
        print(message)