
import openai 

openai.api_key = "sk-XK79YiFEaCqjHvnx7qMgT3B1bkFJSWdR1LmgkXAHMxVbZ731"
system_rol = '''Hace de cuenta que sos analizador de sentimientos.
                Yo te paso sentimientos y vos analizas el sentimiento de los mensajes
                y me das una respuesta con al menos 1 caracter y como máximo 4 caracteres
                SOLO RESPUESTAS NUMÉRICAS. donde -1 es negatividad máxima, 0 es neutral y 1 es positividad máxima.
                Podes ir entre esos rangos, es decir 0.3 0.5 etc tambien son validos
                (Podes responder  solo con ints o floats)'''
                
mensajes = [{"role": "system", "content": system_rol}]

class AnalizadorDeSentimiento:
    def analizar_sentimiento(self, polaridad):
        if polaridad > -0.6 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[0;37m"
        elif polaridad > -0.3 and polaridad < -0.1:
            return "\x1b[1;31m" + "Algo Negativo" + "\x1b[0;37m"
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        elif polaridad >= 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo Positivo" + "\x1b[0;37m"
        elif polaridad >= 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[0;37m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy Positivo" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "Muy Negativo" + "\x1b[0;37m"


analizador = AnalizadorDeSentimiento()
# resultado = analizador.analizar_sentimiento(-2)

while True:
    user_prompt = input("\x1b[1;33m" + "\nEscribe algo: " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})
    
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )
    
    respuesta = completion.choices[0].message["content"] # respuesta del chat Box
    mensajes.append({"role": "assistant", "content": respuesta})
    
    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    
    print(sentimiento)
