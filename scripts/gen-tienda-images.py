#!/usr/bin/env python3
"""Genera las escenas .excalidraw de las unidades 16 y 17 (taller de tienda).

Uso: python scripts/gen-tienda-images.py
Luego: npx -y mcp-excalidraw-server render <archivo> --format svg/png
"""
import json
import os
import random
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FUENTES = os.path.join(ROOT, "public", "img", "fuentes")

BLUE = "#2563eb"
TEAL = "#0f766e"
RED = "#b91c1c"
AMBER = "#b45309"
GREY = "#1e1e1e"

_counter = [0]


def _base(kind):
    _counter[0] += 1
    return {
        "id": f"{kind}{_counter[0]}",
        "type": kind,
        "angle": 0,
        "isDeleted": False,
        "groupIds": [],
        "frameId": None,
        "link": None,
        "locked": False,
        "opacity": 100,
        "version": 1,
        "versionNonce": random.randint(1, 2_000_000_000),
        "seed": random.randint(1, 2_000_000_000),
        "updated": int(time.time() * 1000),
    }


def text(x, y, s, size=15, color=GREY, width=None):
    e = _base("text")
    lines = s.split("\n")
    e.update(
        {
            "x": x,
            "y": y,
            "width": width if width is not None else int(len(s) * size * 0.54),
            "height": int(len(lines) * size * 1.25),
            "autoResize": True,
            "backgroundColor": "transparent",
            "boundElements": None,
            "containerId": None,
            "fillStyle": "solid",
            "fontFamily": 5,
            "fontSize": size,
            "lineHeight": 1.25,
            "originalText": s,
            "roughness": 1,
            "roundness": None,
            "strokeColor": color,
            "strokeStyle": "solid",
            "strokeWidth": 2,
            "text": s,
            "textAlign": "left",
            "verticalAlign": "top",
        }
    )
    return e


def box(x, y, w, h, stroke, fill):
    e = _base("rectangle")
    e.update(
        {
            "x": x,
            "y": y,
            "width": w,
            "height": h,
            "backgroundColor": fill,
            "boundElements": None,
            "fillStyle": "solid",
            "roughness": 1,
            "roundness": {"type": 3},
            "strokeColor": stroke,
            "strokeStyle": "solid",
            "strokeWidth": 2,
        }
    )
    return e


def arrow(x1, y1, x2, y2, color=BLUE):
    e = _base("arrow")
    e.update(
        {
            "x": x1,
            "y": y1,
            "backgroundColor": "transparent",
            "boundElements": None,
            "elbowed": False,
            "endArrowhead": "arrow",
            "endBinding": None,
            "lastCommittedPoint": None,
            "points": [[0, 0], [x2 - x1, y2 - y1]],
            "roughness": 1,
            "roundness": None,
            "startArrowhead": None,
            "startBinding": None,
            "strokeColor": color,
            "strokeStyle": "solid",
            "strokeWidth": 3,
        }
    )
    return e


def scene(name, elements):
    data = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None},
        "files": {},
    }
    out = os.path.join(FUENTES, name)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("OK", out)


def guion_5_pasos():
    _counter[0] = 0
    els = [text(60, 20, "🛒 El guion de los 5 pasos", 22, BLUE)]
    pasos = [
        ("1️⃣ Recibir", "saludo + contacto\nvisual"),
        ("2️⃣ Preguntar", "una abierta y\nuna de detalle"),
        ("3️⃣ Acompañar", "llévale al producto,\nno señales"),
        ("4️⃣ Resolver", "2 opciones +\nuna recomendación"),
        ("5️⃣ Despedir", "cierra y deja\nla puerta abierta"),
    ]
    x, y, w, h, gap = 60, 90, 200, 110, 25
    for i, (titulo, detalle) in enumerate(pasos):
        bx = x + i * (w + gap)
        els.append(box(bx, y, w, h, BLUE, "#e8f1ff"))
        els.append(text(bx + 16, y + 14, titulo, 16, BLUE))
        els.append(text(bx + 16, y + 48, detalle, 13, GREY))
        if i < 4:
            els.append(arrow(bx + w + 4, y + h / 2, bx + w + gap - 4, y + h / 2))
    els.append(
        text(
            60,
            235,
            "El que más se olvida: despedir. El que más cuesta: acompañar sin agobiar.",
            15,
            TEAL,
        )
    )
    scene("16-el-mostrador-ficha1.excalidraw", els)


def clientes_dificiles():
    _counter[0] = 0
    els = [text(60, 20, "💬 Qué responder a cada cliente", 22, BLUE)]
    filas = [
        ("«Es caro»", "compara con la opción barata:\nqué gana esta"),
        ("«Me lo pienso»", "pregunta qué le hace dudar:\n¿precio o modelo?"),
        ("«Solo estoy mirando»", "dale espacio: «mira tranquilo,\nestoy aquí si necesitas»"),
        ("Cliente que grita", "escucha, reconoce, da solución\ny un plazo concreto"),
    ]
    y = 85
    for objecion, respuesta in filas:
        els.append(box(60, y, 290, 74, RED, "#fdeaea"))
        els.append(text(78, y + 24, objecion, 15, RED))
        els.append(arrow(356, y + 37, 404, y + 37))
        els.append(box(410, y, 590, 74, TEAL, "#e6f7f4"))
        els.append(text(428, y + 20, respuesta, 14, GREY))
        y += 92
    els.append(
        text(
            60,
            y + 8,
            "Nunca discusses, nunca prometes lo que no puedes cumplir: solución + plazo.",
            15,
            TEAL,
        )
    )
    scene("16-el-mostrador-ficha2.excalidraw", els)


def cobro_pasos():
    _counter[0] = 0
    els = [text(60, 20, "💶 El cobro, siempre en el mismo orden", 22, BLUE)]
    pasos = [
        ("1 · Di el total", "«Son 12,40 €»\nen voz alta"),
        ("2 · Cobra", "efectivo, tarjeta\no móvil"),
        ("3 · Ticket", "entrégalo o\npregunta"),
        ("4 · Cambio", "cuéntalo delante\ndel cliente"),
    ]
    x, y, w, h, gap = 60, 90, 240, 100, 25
    for i, (titulo, detalle) in enumerate(pasos):
        bx = x + i * (w + gap)
        els.append(box(bx, y, w, h, BLUE, "#e8f1ff"))
        els.append(text(bx + 16, y + 12, titulo, 16, BLUE))
        els.append(text(bx + 16, y + 46, detalle, 13, GREY))
        if i < 3:
            els.append(arrow(bx + w + 4, y + h / 2, bx + w + gap - 4, y + h / 2))
    els.append(box(60, 225, 700, 90, TEAL, "#e6f7f4"))
    els.append(text(78, 240, "12,40 €  →  paga con 20 €  →  cambio 7,60 €", 17, TEAL))
    els.append(
        text(78, 275, "Cuenta hacia arriba: 12,40 → 12,50 → 13 → 20. Así no te pierdes.", 14)
    )
    scene("17-caja-y-cobro-ficha1.excalidraw", els)


def arqueo():
    _counter[0] = 0
    els = [text(60, 20, "🧮 El arqueo de caja, en 2 cuentas", 22, BLUE)]
    els.append(box(60, 85, 720, 70, BLUE, "#e8f1ff"))
    els.append(text(80, 108, "fondo inicial + ventas en efectivo = efectivo esperado", 17, BLUE))
    els.append(box(60, 175, 720, 70, BLUE, "#e8f1ff"))
    els.append(text(80, 198, "contado en el cajón − esperado = descuadre", 17, BLUE))
    resultados = [
        ("0 €", "cuadra:\nfirma y cierra", TEAL, "#e6f7f4"),
        ("+ €", "sobra:\ncobro duplicado\no ticket sin registrar", AMBER, "#fff4e0"),
        ("− €", "falta:\ncambio de más\no venta sin cobrar", RED, "#fdeaea"),
    ]
    x, y, w, h = 60, 275, 230, 100
    for i, (titulo, detalle, color, fill) in enumerate(resultados):
        bx = x + i * (w + 20)
        els.append(box(bx, y, w, h, color, fill))
        els.append(text(bx + 16, y + 12, titulo, 20, color))
        els.append(text(bx + 16, y + 46, detalle, 13, GREY))
    els.append(
        text(
            60,
            400,
            "Un descuadre explicado se arregla. Uno escondido se convierte en un problema de confianza.",
            15,
            TEAL,
        )
    )
    scene("17-caja-y-cobro-ficha2.excalidraw", els)


if __name__ == "__main__":
    random.seed(7)
    guion_5_pasos()
    clientes_dificiles()
    cobro_pasos()
    arqueo()
