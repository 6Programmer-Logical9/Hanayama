from pyowm import OWM

#Inicializa OWM con tu clave
owm = OWM("asdl")
#gestiona y cordina las solicitudes y respuestas a la API
manager = owm.weather_manager()
#realiza una solicitud
observacion = manager.weather_at_place("Caracas,VE")

consulta = observacion.weather

print(f"Estado: {consulta.detailed_status}")
print(f"Viento: {consulta.wind()}")
print(f"Humedad: {consulta.humidity}")
print(f"Temperatura: {consulta.temperature('celsius')}")
print(f"Lluvia: {consulta.rain}")
print(f"Nubes: {consulta.clouds}")