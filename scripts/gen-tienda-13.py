#!/usr/bin/env python3
"""Escenas Excalidraw de la unidad 13 (IA: copiloto de estudio).

Reutiliza los helpers de gen-tienda-images.py.

Uso: python scripts/gen-tienda-13.py
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
AMBERF = "#fff4e0"
REDF = "#fdeaea"


def _reset():
    base._counter[0] = 0


def pregunta_bien():
    _reset()
    els = [text(60, 20, "📝 La petición a la IA, en 3 piezas", 22, BLUE)]
    piezas = [
        ("1️⃣ QUÉ", "la duda concreta:\n«no me cuadra el stock mínimo»", BLUE, "#e8f1ff"),
        ("2️⃣ PARA QUÉ", "el contexto: clase de tienda,\nprimera vez, sin práctica", BLUE, "#e8f1ff"),
        ("3️⃣ CÓMO", "el formato: en tabla,\nmáximo 5 líneas", TEAL, "#e6f7f4"),
    ]
    x, y, w, h, gap = 60, 85, 280, 115, 36
    for i, (titulo, detalle, color, fill) in enumerate(piezas):
        bx = x + i * (w + gap)
        els.append(box(bx, y, w, h, color, fill))
        els.append(text(bx + 16, y + 14, titulo, 16, color))
        els.append(text(bx + 16, y + 50, detalle, 12, GREY))
        if i < 2:
            els.append(arrow(bx + w + 3, y + h // 2, bx + w + gap - 3, y + h // 2))
    els.append(
        text(
            60,
            y + h + 28,
            "«Dame 3 ejemplos de cambio con tarjeta, en tabla y con números»",
            15,
            TEAL,
        )
    )
    els.append(
        text(
            60,
            y + h + 56,
            "Pregunte vago («explícame el tema») → muro de texto; decir el formato es la mitad de la respuesta.",
            15,
            RED,
        )
    )
    scene("13-ia-copiloto-de-estudio-ficha1.excalidraw", els)


def semaforo_uso():
    _reset()
    els = [text(60, 20, "🚦 El semáforo de usos de la IA", 22, BLUE)]
    filas = [
        (
            "🟢 VERDE",
            "Te saca material: ejemplos, preguntas de examen · corregir tu esquema con el suyo",
            GREEN,
            GREENF,
        ),
        (
            "🟡 ÁMBAR",
            "Te explica una duda puntual · vale si después la explicas tú sin ella",
            AMBER,
            AMBERF,
        ),
        (
            "🔴 ROJO",
            "Que redacte lo que entrega tu nombre · copiar y pegar es no haber estudiado",
            RED,
            REDF,
        ),
    ]
    y = 82
    for titulo, detalle, color, fill in filas:
        els.append(box(60, y, 190, 46, color, fill))
        els.append(text(76, y + 13, titulo, 16, color))
        els.append(box(250, y, 690, 46, color, "#ffffff"))
        els.append(text(266, y + 13, detalle, 13, GREY))
        y += 58
    els.append(
        text(
            60,
            y + 22,
            "La regla de la explicación: ¿puedes contarlo tú, en voz alta y sin pantalla? Si sí, era copiloto.",
            16,
            TEAL,
        )
    )
    scene("13-ia-copiloto-de-estudio-ficha2.excalidraw", els)


if __name__ == "__main__":
    pregunta_bien()
    semaforo_uso()
