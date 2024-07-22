# Chatbot analizador de sentimientos
# En este proyecto, podrías desarrollar un chatbot en python, que nos pida que le digamos
# algo y tome eso que le decimos, analice el sentimiento y nos responda cual es el
# sentimiento.
# Este proyecto te daria la oportunidad de trabajar con varios aspectos de la Programación
# Orientada a Objetos (POO), módulos, API, análisis de datos, etc...

from textblob import TextBlob

class AnalizadorDeSentimiento:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        
        if analisis.sentiment.polarity > 0:
            return "Positivo"
        elif analisis.sentiment.polarity == 0:
            return "Neutral"
        else:
            return "Negativo"
        
analizador = AnalizadorDeSentimiento()
resultado = analizador.analizar_sentimiento("hello, i am very funi")

print(resultado)