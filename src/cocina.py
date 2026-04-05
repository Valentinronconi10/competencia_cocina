def calcular_total(datos):
    return datos["judge_1"] + datos["judge_2"] + datos["judge_3"]


def simular_competencia(rounds):
    tabla_posiciones = {}

    resultados = []

    for ronda in rounds:
        ganador = ""
        mejor_puntaje = 0

        for persona, datos in ronda["scores"].items():
            total = calcular_total(datos)

            if persona not in tabla_posiciones:
                tabla_posiciones[persona] = {
                    "puntaje_total": 0,
                    "rondas_ganadas": 0,
                    "mejor_ronda": 0,
                    "rondas_jugadas": 0
                }

            tabla_posiciones[persona]["puntaje_total"] += total
            tabla_posiciones[persona]["rondas_jugadas"] += 1

            if total > tabla_posiciones[persona]["mejor_ronda"]:
                tabla_posiciones[persona]["mejor_ronda"] = total

            if total > mejor_puntaje:
                mejor_puntaje = total
                ganador = persona

        tabla_posiciones[ganador]["rondas_ganadas"] += 1

        resultados.append((ronda["theme"], ganador, mejor_puntaje, tabla_posiciones.copy()))

    return resultados, tabla_posiciones