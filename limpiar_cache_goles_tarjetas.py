#!/usr/bin/env python3
"""
Limpia de estado.json los goles/tarjetas ya calculados, para que
completar_con_actas() los recalcule en la próxima ejecución con la
función goles_y_tarjetas_de_acta() corregida (ver commit de fix del
28/09/2026: la anterior atribuía todos los goles/tarjetas del partido a
un único equipo).

No toca nada más: resultado, hora, posiciones en la tabla, acta, etc. se
quedan exactamente como estaban. Solo se borran las claves "goles" y
"tarjetas" de cada partido, así que en la siguiente ejecución del script
completar_con_actas() las vuelve a calcular desde la acta (ya con el
código corregido).

Uso:
    python3 limpiar_cache_goles_tarjetas.py estado.json

Sobrescribe el fichero indicado (guarda antes una copia si quieres
poder deshacerlo).
"""
import json
import sys


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 limpiar_cache_goles_tarjetas.py estado.json", file=sys.stderr)
        sys.exit(1)

    ruta = sys.argv[1]
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)

    partidos = datos.get("partidos", {})
    tocados = 0
    for p in partidos.values():
        if "goles" in p or "tarjetas" in p:
            p.pop("goles", None)
            p.pop("tarjetas", None)
            tocados += 1

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=1, sort_keys=True)

    print(f"Limpiados goles/tarjetas de {tocados} partido(s) en {ruta}.")
    print("En la próxima ejecución del script se recalcularán con la función corregida.")


if __name__ == "__main__":
    main()
