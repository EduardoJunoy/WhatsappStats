import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Definir los nombres de los usuarios
user2 = "usuario2"
user1 = "..."

# Crear un diccionario para almacenar los mensajes de cada usuario por fecha
user1_messages = {}
user2_messages = {}

# Abrir el archivo de chat y leer las líneas
with open("chat_usuario2.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

    # Iterar sobre las líneas del archivo
    for line in lines:
        try:
            # Extraer la fecha, el nombre de usuario y el cuerpo del mensaje
            date_str, _, rest = line.partition(" - ")
            name, _, message = rest.partition(": ")
            
            # Convertir la fecha de texto a objeto datetime
            date = datetime.strptime(date_str, "%d/%m/%y, %H:%M")
            
            # Si el mensaje es de uno de los dos usuarios, agregarlo al diccionario correspondiente
            if name == user1:
                if date in user1_messages:
                    user1_messages[date].append(message)
                else:
                    user1_messages[date] = [message]
            elif name == user2:
                if date in user2_messages:
                    user2_messages[date].append(message)
                else:
                    user2_messages[date] = [message]
        except:
            pass

# Crear dos listas para almacenar las fechas y el número de mensajes de cada usuario en orden cronológico
user1_dates = sorted(user1_messages.keys())
user1_counts = [len(user1_messages[date]) for date in user1_dates]
user2_dates = sorted(user2_messages.keys())
user2_counts = [len(user2_messages[date]) for date in user2_dates]

# Crear un gráfico de líneas con las fechas y el número de mensajes de cada usuario
#plt.plot(user1_dates, user1_counts, label=user1, alpha=0.7, color='tab:blue')
#plt.plot(user2_dates, user2_counts, label=user2, alpha=0.7, color='tab:red')

# Crear un gráfico de barras con las fechas y el número de mensajes de cada usuario
bar_width = timedelta(days=1)
plt.bar(user1_dates, user1_counts, width=bar_width, align='edge', label=user1, alpha=0.7, color='tab:blue')
plt.bar(user2_dates, user2_counts, width=bar_width, align='edge', label=user2, alpha=0.5, color='tab:red')


# Configurar la leyenda, anotaciones y los ejes
plt.legend(loc='upper left')
plt.xlabel('Fecha')
plt.ylabel('Número de mensajes')
plt.annotate('Mensajes totales de '+ user1 + ': ' + (str)(len(user1_counts)), xy=(0.95, 0.95), xycoords='axes fraction', ha='right', va='top')
plt.annotate('Mensajes totales de '+ user2 + ': ' + (str)(len(user2_counts)), xy=(0.95, 0.90), xycoords='axes fraction', ha='right', va='top')
plt.xticks(rotation=45)

# Mostrar la gráfica
plt.show()
