#!/usr/bin/env python3
"""Escenas Excalidraw de la unidad 14 (Monta tu presentación).

Reutiliza los helpers de gen-tienda-images.py.

Uso: python scripts/gen-tienda-14.py
"""
import importlib.util
import os

BASE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "gen_tienda", os.path.join(BASE, "gen-tienda-images.py")
)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

text = base.text
box = base.box
arrow = base.arrow
scene = base.scene
BLUE, TEAL, RED, AMBER, GREY = (
    base.BLUE,
    base.TEAL,
    base.RED,
    base.AMBER,
    base.GREY,
)

GREEN = "#047857"
GREENF = "#d1fae5"
REDF = "#fdeaea"


def _reset():
    base._counter[0] = 0


def buscar_recopilar():
    _reset()
    els = [text(60, 20, "🔍 El circuito: buscar → recopilar → seleccionar → crear", 22, BLUE)]
    pasos = [
        ("1️⃣ BUSCAR", "3-4 búsquedas\n(una en inglés)", BLUE, "#e8f1ff"),
        ("2️⃣ RECOPILAR", "tabla de materiales,\nfuente al instante", BLUE, "#e8f1ff"),
        ("3️⃣ SELECCIONAR", "solo lo que cuenta\nla historia", TEAL, "#e6f7f4"),
        ("4️⃣ CREAR", "1 idea por lámina,\nmáx. 6 líneas", TEAL, "#e6f7f4"),
    ]
    x, y, w, h, gap = 60, 85, 200, 115, 26
    for i, (titulo, detalle, color, fill) in enumerate(pasos):
        bx = x + i * (w + gap)
        els.append(box(bx, y, w, h, color, fill))
        els.append(text(bx + 14, y + 14, titulo, 15, color))
        els.append(text(bx + 14, y + 50, detalle, 12, GREY))
        if i < 3:
            els.append(arrow(bx + w + 3, y + h // 2, bx + w + gap - 3, y + h // 2))
    els.append(
        text(
            60,
            y + h + 26,
            "La fuente se apunta en el MISMO segundo en que se copia el material.",
            16,
            TEAL,
        )
    )
    els.append(
        text(
            60,
            y + h + 54,
            "Material sin origen: papel mojado. Nadie puede citarlo ni defenderlo en preguntas.",
            15,
            RED,
        )
    )
    scene("14-monta-tu-presentacion-ficha1.excalidraw", els)


def lamina_que_funciona():
    _reset()
    els = [text(60, 20, "🖼️ La lámina que funciona contra el muro", 22, BLUE)]
    # Columna izquierda: el muro
    els.append(box(60, 80, 380, 170, RED, REDF))
    els.append(text(76, 92, "❌ La lámina-muro", 17, RED))
    muro = (
        "El escaparate se cambia por ciclos según estación, novedad, promoción y agotamiento "
        "de stock, y en cada ciclo hay que revisar la carta de precios, reetiquetar el maniquí "
        "central, limpiar la vitrina, reordenar los 3 niveles de altura del lineal según el "
        "facing que sale del informe de rotación semanal del almacén, y además apuntar en la "
        "hoja de renovación las piezas devueltas a almacén con su motivo y fecha, porque si "
        "no se apuntan luego el inventario no cuadra y hay que recortar de nuevo, todo en "
        "esta misma página y en párrafo único, illisible."
    )
    # envuelto a mano: el export CLI no envuelve párrafos largos
    palabras = muro.split(" ")
    lineas, actual = [], []
    for pal in palabras:
        actual.append(pal)
        if len(" ".join(actual)) > 52:
            lineas.append(" ".join(actual))
            actual = []
    if actual:
        lineas.append(" ".join(actual))
    muro = "\n".join(lineas)
    els.append(text(76, 118, muro, 9, GREY, width=340))
    els.append(text(76, 222, "= 0 ideas, todo a la vez", 14, RED))
    # Columna derecha: la lámina que funciona
    els.append(box(480, 80, 430, 170, GREEN, GREENF))
    els.append(text(496, 92, "✅ La lámina que funciona", 17, GREEN))
    lista = [
        "🧲 1 idea por lámina",
        "📏 máx. 6 líneas (y con menos, mejor)",
        "🖼️ imagen o dato grande: la vista ancla",
        "📌 fuente en la esquina (¿de dónde sale?)",
        "🗣️ el detalle lo dices tú: la lámina ancla",
    ]
    ly = 122
    for item in lista:
        els.append(text(496, ly, item, 13, GREY))
        ly += 24
    els.append(
        text(
            60,
            286,
            "Si la lámina te obliga a leer, no es lámina: es una excusa para leer. La presentación se cuenta, no se recita.",
            15,
            TEAL,
        )
    )
    scene("14-monta-tu-presentacion-ficha2.excalidraw", els)


if __name__ == "__main__":
    buscar_recopilar()
    lamina_que_funciona()
