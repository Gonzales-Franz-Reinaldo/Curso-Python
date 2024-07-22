# EJERCICIO FINAL - SIMULACO DE OPENAI 

from textblob import TextBlob

class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)
    

class AnalizadorDeSentimiento:
    def __init__(self, rangos):
        self.rangos = rangos
        
    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        # print(polaridad)
        return Sentimiento("Muy Negativo", "31")

rangos = [
    ((-0.6, -0.3), Sentimiento("Negativo", "31")),
    ((-0.3, -0.1), Sentimiento("Algo Negativo", "31")),
    ((-0.1, 0.1), Sentimiento("Neutral", "33")),
    ((0.1, 0.4), Sentimiento("Positivo", "32")),
    ((0.4, 0.9), Sentimiento("Algo Positivo", "32")),
    ((0.9, 1), Sentimiento("Muy Positivo", "32"))
]


analizador = AnalizadorDeSentimiento(rangos)

# resultado = analizador.analizar_sentimiento(-0.2)

while True:
    # Escribir solo en Ingles
    user_prompt = input("\x1b[1;33m" + "\nEscribe algo: " + "\x1b[1;37m")
    resultado = TextBlob(user_prompt)
    texto_analizado = resultado.sentiment.polarity
    
    sentimiento = analizador.analizar_sentimiento(texto_analizado)

    print(sentimiento)