#!/usr/bin/env python3
"""Escenas Excalidraw de las unidades 11 (Memorizar) y 12 (Examen en blanco).

Reutiliza los helpers de gen-tienda-images.py.

Uso: python scripts/gen-tienda-4.py
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


def _reset():
    base._counter[0] = 0


def ciclo_memorizar():
    _reset()
    els = [text(60, 20, "🧠 El ciclo de memorizar, en 4 pasos", 22, BLUE)]
    pasos = [
        ("1️⃣ Leen corto", "un bloque\ncon tu subrayado"),
        ("2️⃣ Copiar con ideas", "a mano,\nno frase entera"),
        ("3️⃣ Tapar todo", "libro y papel\nfuera de la mesa"),
        ("4️⃣ Decir en voz alta", "como a un cliente,\nsin apoyos"),
    ]
    x, y, w, h, gap = 60, 90, 240, 100, 25
    for i, (titulo, detalle) in enumerate(pasos):
        bx = x + i * (w + gap)
        els.append(box(bx, y, w, h, BLUE, "#e8f1ff"))
        els.append(text(bx + 14, y + 12, titulo, 15, BLUE))
        els.append(text(bx + 14, y + 48, detalle, 13, GREY))
        if i < 3:
            els.append(arrow(bx + w + 4, y + h / 2, bx + w + gap - 4, y + h / 2))
    els.append(
        text(
            60,
            235,
            "Si algo falla al decir: se mira solo eso, se tapa y se repite esa parte.",
            15,
            TEAL,
        )
    )
    scene("11-memorizar-de-verdad-ficha1.excalidraw", els)


def repaso_1_3_7():
    _reset()
    els = [text(60, 20, "📅 El repaso 1-3-7", 22, BLUE)]
    dias = [
        ("DÍA 1", "3-5 min", "repaso completo:\ntapar y decir todo", BLUE, "#e8f1ff"),
        ("DÍA 3", "2-4 min", "solo lo que falló\nel día 1", TEAL, "#e6f7f4"),
        ("DÍA 7", "1-2 min", "comprobación:\ndecirlo otra vez", AMBER, "#fff4e0"),
    ]
    x = 60
    for titulo, mins, detalle, color, fill in dias:
        els.append(box(x, 85, 300, 110, color, fill))
        els.append(text(x + 18, 99, titulo, 16, color))
        els.append(text(x + 18, 130, mins, 13, color))
        els.append(text(x + 18, 160, detalle, 13, GREY))
        x += 320
    sem = [
        ("🟢 Verde", "lo cuento entero\nsin dudar", TEAL, "#e6f7f4"),
        ("🟡 Amarillo", "salta, pero\ncon dudas", AMBER, "#fff4e0"),
        ("🔴 Rojo", "se me cae\npor la mitad", RED, "#fdeaea"),
    ]
    x = 60
    for titulo, detalle, color, fill in sem:
        els.append(box(x, 230, 300, 76, color, fill))
        els.append(text(x + 18, 244, titulo, 16, color))
        els.append(text(x + 18, 276, detalle, 13, GREY))
        x += 320
    els.append(
        text(
            60,
            330,
            "El verde no vuelve a gastarse el tiempo. El rojo vuelve al ciclo completo.",
            15,
            TEAL,
        )
    )
    scene("11-memorizar-de-verdad-ficha2.excalidraw", els)


def examen_blanco():
    _reset()
    els = [text(60, 20, "📝 El examen en blanco, en 5 pasos", 22, BLUE)]
    pasos = [
        ("1 · Elige", "un tema verde\no amarillo"),
        ("2 · 6 preguntas", "3 memoria · 2 razonar\n· 1 caso"),
        ("3 · Hazlo en blanco", "sin apuntes,\ncon cronómetro"),
        ("4 · Corrige en color", "✅ · ½ · ❌\ncon apuntes delante"),
        ("5 · Anota lo rojo", "directo a la hoja\nde repaso"),
    ]
    x, y, w, h, gap = 60, 90, 210, 100, 22
    for i, (titulo, detalle) in enumerate(pasos):
        bx = x + i * (w + gap)
        els.append(box(bx, y, w, h, BLUE, "#e8f1ff"))
        els.append(text(bx + 12, y + 12, titulo, 14, BLUE))
        els.append(text(bx + 12, y + 46, detalle, 12, GREY))
        if i < 4:
            els.append(arrow(bx + w + 2, y + h / 2, bx + w + gap - 2, y + h / 2))
    els.append(
        text(
            60,
            235,
            "Si no puedes preguntar por una rama del esquema, esa rama no la tienes clara.",
            15,
            AMBER,
        )
    )
    scene("12-examen-en-blanco-ficha1.excalidraw", els)


def reparto_tiempo():
    _reset()
    els = [text(60, 20, "⏱️ 45 minutos, 4 bloques", 22, BLUE)]
    bloques = [
        ("0-5", "leer el examen\nentero y anotar el valor", BLUE, "#e8f1ff"),
        ("5-25", "las que sé:\nfáciles en orden", TEAL, "#e6f7f4"),
        ("25-40", "las que cuestan:\nesquema y a escribir", AMBER, "#fff4e0"),
        ("40-45", "revisar: nombre,\nhuecos y erratas", RED, "#fdeaea"),
    ]
    x = 60
    for titulo, detalle, color, fill in bloques:
        els.append(box(x, 90, 250, 100, color, fill))
        els.append(text(x + 16, 104, titulo + " min", 17, color))
        els.append(text(x + 16, 142, detalle, 13, GREY))
        x += 270
    els.append(
        text(
            60,
            225,
            "El reparto se decide NADA MÁS leer el examen, no a mitad de la pregunta 1.",
            15,
            RED,
        )
    )
    els.append(
        text(60, 265, "Y si una pregunta no arranca: se salta (apuntada) y se vuelve al final con el esqueleto.", 14)
    )
    scene("12-examen-en-blanco-ficha2.excalidraw", els)


if __name__ == "__main__":
    ciclo_memorizar()
    repaso_1_3_7()
    examen_blanco()
    reparto_tiempo()
