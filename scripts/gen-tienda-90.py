#!/usr/bin/env python3
"""Escenas Excalidraw de la unidad especial 90 (El torneo del taller).

Reutiliza los helpers de gen-tienda-images.py.

Uso: python scripts/gen-tienda-90.py
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


def _reset():
    base._counter[0] = 0


def tabla_torneo():
    _reset()
    els = [text(60, 20, "📋 La tabla del torneo, en la pared", 22, BLUE)]
    cols = [
        ("SEMANA", 190),
        ("DINÁMICA", 250),
        ("E1", 90),
        ("E2", 90),
        ("E3", 90),
        ("E4", 90),
        ("OBSERVACIONES", 210),
    ]
    x = 60
    for titulo, ancho in cols:
        els.append(box(x, 85, ancho, 45, BLUE, "#e8f1ff"))
        els.append(text(x + 12, 98, titulo, 13, BLUE))
        x += ancho
    filas = [
        ["1", "Guion de 5 pasos", "", "", "", "", ""],
        ["2", "Cambio a contrarreloj", "", "", "", "", ""],
        ["3", "Recepción a contrarreloj", "", "", "", "", ""],
        ["4", "Turno imposible", "", "", "", "", ""],
        ["🏁 FINAL", "PUNTOS DOBLES (x2)", "", "", "", "", "💥 vale el doble"],
    ]
    y = 130
    for fila in filas:
        x = 60
        for (_, ancho), valor in zip(cols, fila):
            col = GREEN if valor.startswith("🏁") else GREY
            fill = GREENF if valor.startswith("🏁") else "#ffffff"
            els.append(box(x, y, ancho, 40, col, fill))
            if valor:
                els.append(text(x + 10, y + 12, valor, 12, col))
            x += ancho
        y += 40
    els.append(
        text(
            60,
            y + 15,
            "Los puntos se cuentan en voz alta al terminar. Los escriben los contadores con revisión cruzada.",
            15,
            TEAL,
        )
    )
    scene("90-el-torneo-del-taller-ficha2.excalidraw", els)


def gran_final():
    _reset()
    els = [text(60, 20, "🏆 La gran final, en 4 fases", 22, BLUE)]
    fases = [
        ("1 · Recuento", "público, con\nla tabla delante", BLUE, "#e8f1ff"),
        ("2 · Dinámica x2", "la elige el\nequipo 1º", BLUE, "#e8f1ff"),
        ("3 · Ceremonia", "premios en menos\nde 5 minutos", TEAL, "#e6f7f4"),
        ("4 · Evaluación", "qué sirvió, qué falló\n(¡sin nombres!)", TEAL, "#e6f7f4"),
    ]
    x, y, w, gap = 60, 90, 230, 24
    for i, (titulo, detalle, color, fill) in enumerate(fases):
        bx = x + i * (w + gap)
        els.append(box(bx, y, w, 100, color, fill))
        els.append(text(bx + 14, y + 14, titulo, 15, color))
        els.append(text(bx + 14, y + 48, detalle, 12, GREY))
        if i < 3:
            els.append(arrow(bx + w + 2, y + 50, bx + w + gap - 2, y + 50))
    premios = [
        ("🥇 1º", "elige dinámica\ny música", AMBER, "#fff4e0"),
        ("🤝 Equipazo", "rotación y\nnadie fuera", GREEN, "#d1fae5"),
        ("🌟 Fallo bien tomado,", "votado por\nescrito", RED, "#fdeaea"),
    ]
    x = 60
    for titulo, detalle, color, fill in premios:
        els.append(box(x, 225, 300, 90, color, fill))
        els.append(text(x + 16, 240, titulo, 16, color))
        els.append(text(x + 16, 274, detalle, 13, GREY))
        x += 320
    els.append(
        text(
            60,
            350,
            "Nunca premios con nota, dinero ni castigos: eso compra participación con moneda falsa.",
            15,
            RED,
        )
    )
    scene("90-el-torneo-del-taller-ficha1.excalidraw", els)


if __name__ == "__main__":
    tabla_torneo()
    gran_final()
