vc = [5,6,7,10,9,8,10]

tam = len(vc)
suma = 0
c = 0

for i in range(tam):
    suma = suma + vc [i]

    promedio = suma + vc[i]


    if vc[i]>= promedio:
        c = c + 1

    cal = int(input(f"Dame la calificación {i+1}:"))
    vc.append(cal)

for i in range(tam):
    print(f"La calificación: {i+1} = {vc(i)}")