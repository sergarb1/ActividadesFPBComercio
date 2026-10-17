#!/usr/bin/env python3
"""Escenas Excalidraw de las unidades 03 (Reposición) y 04 (Inventario).

Reutiliza los helpers de gen-tienda-images.py para que todas las imágenes
compartan el mismo estilo.

Uso: python scripts/gen-tienda-2.py
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


def recepcion():
    _reset()
    els = [text(60, 20, "📦 Recibir la mercancía, en 5 pasos", 22, BLUE)]
    pasos = [
        ("1️⃣ Preparar", "pedido a mano\ny sitio libre"),
        ("2️⃣ Contar", "bultos primero,\nluego unidades"),
        ("3️⃣ Comprobar", "cantidad, modelo,\ntalla o color"),
        ("4️⃣ Revisar", "cajas rotas,\ngolpes, fechas"),
        ("5️⃣ Firmar", "conforme o\nCON RESERVAS"),
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
            "Si falta algo, se firma con reservas y se avisa al proveedor ese mismo día.",
            15,
            TEAL,
        )
    )
    scene("03-reposicion-y-almacen-ficha1.excalidraw", els)


def lineal_familias():
    _reset()
    els = [text(60, 20, "🧱 Las 4 reglas del lineal", 22, BLUE)]
    reglas = [
        ("Por familias", "camisetas con camisetas,\nno mezclar categorías", BLUE, "#e8f1ff"),
        ("FIFO", "lo viejo DELANTE,\nlo nuevo detrás", TEAL, "#e6f7f4"),
        ("Facing + etiqueta", "frente alineado y\nprecio visible", AMBER, "#fff4e0"),
        ("El hueco se pide", "nunca se tapa con\notra referencia", RED, "#fdeaea"),
    ]
    x, y, w, h = 60, 85, 260, 110
    for i, (titulo, detalle, color, fill) in enumerate(reglas):
        bx = x + (i % 2) * (w + 30)
        by = y + (i // 2) * (h + 25)
        els.append(box(bx, by, w, h, color, fill))
        els.append(text(bx + 16, by + 14, titulo, 17, color))
        els.append(text(bx + 16, by + 48, detalle, 13, GREY))
    els.append(
        text(
            60,
            340,
            "Reponer es: sacar lo viejo, limpiar, poner lo nuevo detrás y apuntar el hueco.",
            15,
            TEAL,
        )
    )
    scene("03-reposicion-y-almacen-ficha2.excalidraw", els)


def hoja_inventario():
    _reset()
    els = [text(60, 20, "🧾 La hoja de inventario", 22, BLUE)]
    cols = [
        ("Referencia", 130),
        ("Producto", 200),
        ("Teórico", 110),
        ("Contado", 110),
        ("Diferencia", 120),
    ]
    x = 60
    for titulo, ancho in cols:
        els.append(box(x, 85, ancho, 50, BLUE, "#e8f1ff"))
        els.append(text(x + 12, 100, titulo, 15, BLUE))
        x += ancho
    fila = ["A-101", "Camiseta blanca M", "25", "23", "−2"]
    x = 60
    for (_, ancho), valor in zip(cols, fila):
        els.append(box(x, 135, ancho, 45, GREY, "#ffffff"))
        els.append(text(x + 12, 148, valor, 14))
        x += ancho
    els.append(
        text(
            60,
            205,
            "Diferencia = contado − teórico. Cada diferencia es dinero: venta sin registrar, hurto o merma.",
            15,
            TEAL,
        )
    )
    els.append(
        text(
            60,
            245,
            "Se cuenta por zonas y en orden, y se abre la caja: nunca se fía uno de la etiqueta.",
            14,
        )
    )
    scene("04-inventario-y-stock-ficha1.excalidraw", els)


def punto_pedido():
    _reset()
    els = [text(60, 20, "📉 Cuánto pedir y cuándo", 22, BLUE)]
    els.append(box(60, 85, 700, 70, BLUE, "#e8f1ff"))
    els.append(text(80, 108, "venta diaria × plazo de entrega = stock mínimo", 17, BLUE))
    els.append(box(60, 175, 700, 70, TEAL, "#e6f7f4"))
    els.append(text(80, 198, "stock mínimo + colchón = punto de pedido", 17, TEAL))
    els.append(
        text(
            60,
            275,
            "Ejemplo: 5 camisetas/día × 4 días = 20 de mínimo. Con 10 de colchón → se pide al llegar a 30.",
            14,
        )
    )
    els.append(
        text(
            60,
            315,
            "Y antes de pedir: mira lo que ya viene en camino. Pedir dos veces llena el almacén.",
            15,
            AMBER,
        )
    )
    scene("04-inventario-y-stock-ficha2.excalidraw", els)


if __name__ == "__main__":
    recepcion()
    lineal_familias()
    hoja_inventario()
    punto_pedido()
