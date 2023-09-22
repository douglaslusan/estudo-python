def break_seconds(seconds):
    days = seconds // 86400
    seconds = seconds % 86400
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{days} dias, {hours} horas, {minutes} minutos e {seconds} segundos"

seconds = int(input('Por favor, entre com o número de segundos que deseja converter: '))

print(break_seconds(seconds))