#promedio de duración

curso_min = 2.5
curso_max = 7
curso_promd = 4
curso_dalto = 1.5

#diferencias de duración
diferencia_con_min = 100 - curso_dalto / curso_min * 100
diferencia_con_max = 100 - curso_dalto * 1000 // curso_max / 10
diferencia_con_promd = 100 - curso_dalto / curso_promd * 100

print(f'El curso de Dalto dura un {diferencia_con_min}% menos que el rápido')
print(f'El curso de Dalto dura un {diferencia_con_max}% menos que el lento')
print(f'El curso de Dalto dura un {diferencia_con_promd}% menos que el promedio')
