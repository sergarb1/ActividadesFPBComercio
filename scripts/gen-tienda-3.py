#!/usr/bin/env python3
"""Escenas Excalidraw de las unidades 05 (Escaparate) y 06 (Devoluciones).

Reutiliza los helpers de gen-tienda-images.py.

Uso: python scripts/gen-tienda-3.py
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


def tres_niveles():
    _reset()
    els = [text(60, 20, "🪟 El escaparate en 3 niveles", 22, BLUE)]
    niveles = [
        ("🔝 ALTA", "el producto estrella\ny la carta de la promo", BLUE, "#e8f1ff"),
        ("▪️ MEDIA", "la promoción con\nsu precio bien a la vista", TEAL, "#e6f7f4"),
        ("⬇️ BAJA", "complementos\ny la reposición", AMBER, "#fff4e0"),
    ]
    y = 85
    for titulo, detalle, color, fill in niveles:
        els.append(box(60, y, 300, 80, color, fill))
        els.append(text(80, y + 20, titulo, 17, color))
        els.append(arrow(366, y + 40, 414, y + 40, GREY))
        els.append(box(420, y, 380, 80, color, fill))
        els.append(text(438, y + 22, detalle, 14, GREY))
        y += 100
    els.append(
        text(
            60,
            385,
            "Menos es más: 3 productos bien elegidos venden más que 15 a la fuerza. Y todo con precio.",
            15,
            TEAL,
        )
    )
    scene("05-el-escaparate-ficha1.excalidraw", els)


def ciclo_renovacion():
    _reset()
    els = [text(60, 20, "🧹 El ciclo de renovación", 22, BLUE)]
    ciclos = [
        ("CADA SEMANA", "limpiar cristal y estante,\nmirar tarjetas de precio", BLUE, "#e8f1ff"),
        ("CADA 7-14 DÍAS", "cambiar una parte:\nun producto o un texto", TEAL, "#e6f7f4"),
        ("CADA TEMPORADA", "montaje completo,\nya fuera la cartelería vencida", AMBER, "#fff4e0"),
    ]
    x = 60
    for titulo, detalle, color, fill in ciclos:
        els.append(box(x, 90, 300, 110, color, fill))
        els.append(text(x + 18, 106, titulo, 15, color))
        els.append(text(x + 18, 140, detalle, 13, GREY))
        x += 320
    els.append(
        text(
            60,
            240,
            "Un cartel de una campaña que ya pasó es un problema de precios: hay que retirarlo.",
            15,
            RED,
        )
    )
    els.append(
        text(60, 280, "Y antes de nada, colgar la tarjeta de precio: un escaparate sin precio no vende.", 15)
    )
    scene("05-el-escaparate-ficha2.excalidraw", els)


def devolucion_pasos():
    _reset()
    els = [text(60, 20, "🔁 Devolución: 3 puertas de entrada", 22, BLUE)]
    puertas = [
        ("🎟️ Ticket", "el soporte\nde todo", BLUE, "#e8f1ff"),
        ("📅 Plazo", "los días que\ndice la política", TEAL, "#e6f7f4"),
        ("🔒 Producto", "sin usar, con\netiquetas y caja", AMBER, "#fff4e0"),
    ]
    x = 60
    for titulo, detalle, color, fill in puertas:
        els.append(box(x, 90, 220, 96, color, fill))
        els.append(text(x + 16, 104, titulo, 17, color))
        els.append(text(x + 16, 140, detalle, 13, GREY))
        x += 240
    els.append(arrow(228, 138, 252, 138))
    els.append(arrow(468, 138, 492, 138))
    els.append(box(60, 220, 700, 70, TEAL, "#e6f7f4"))
    els.append(text(80, 244, "Las tres pasan: se devuelve → el defecto entra en garantía legal (2 años)", 15, TEAL))
    els.append(
        text(
            60,
            320,
            "Si no pasa una: se explica por qué con una frase amable y una alternativa.",
            15,
            GREY,
        )
    )
    scene("06-devoluciones-y-reclamaciones-ficha1.excalidraw", els)


def hoja_reclamacion():
    _reset()
    els = [text(60, 20, "📋 La hoja de reclamaciones, paso a paso", 22, BLUE)]
    pasos = [
        ("1 · Se entrega", "cuando el cliente\nla pide: sin drama", BLUE, "#e8f1ff"),
        ("2 · Se rellena", "hechos concretos,\nfechas y lo que pide", BLUE, "#e8f1ff"),
        ("3 · Se sella", "copia al cliente\ny copia para tienda", TEAL, "#e6f7f4"),
        ("4 · Se envía", "la copia oficial va\nal organismo de consumo", TEAL, "#e6f7f4"),
    ]
    x, y, w, gap = 60, 90, 190, 22
    for i, (titulo, detalle, color, fill) in enumerate(pasos):
        bx = x + i * (w + gap)
        els.append(box(bx, y, w, 100, color, fill))
        els.append(text(bx + 12, y + 12, titulo, 14, color))
        els.append(text(bx + 12, y + 44, detalle, 12, GREY))
        if i < 3:
            els.append(arrow(bx + w + 2, y + 50, bx + w + gap - 2, y + 50))
    els.append(
        text(
            60,
            235,
            "Pedir la hoja es un derecho: escondida o dándoles guerra, es una infracción.",
            15,
            RED,
        )
    )
    els.append(text(60, 275, "Y para la tienda también gana: cada hoja enseña dónde falla el servicio.", 15, TEAL))
    scene("06-devoluciones-y-reclamaciones-ficha2.excalidraw", els)


if __name__ == "__main__":
    tres_niveles()
    ciclo_renovacion()
    devolucion_pasos()
    hoja_reclamacion()
