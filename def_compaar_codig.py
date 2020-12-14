codebreaker=[1, 1, 666, "negro"] #bot
codemaker=["negro", "negro", "negro", "negro"] #jugador

def comparar_codigos():
    codigo_bot = codebreaker
    codigo_jugador = codemaker
    feedback=[]

    for i in range(4):

        if codigo_jugador[i] == codigo_bot[i]:
            feedback.append("x")
        else:
            if codigo_jugador[i] in codigo_bot:
                feedback.append("-")
            else:
                feedback.append("o")
    return feedback

print (comparar_codigos())
