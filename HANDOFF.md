# HANDOFF — Traspaso de sesión

> Documento para que otro modelo o una sesión futura continúe el trabajo sin redescubrir el contexto.
> Se **sobrescribe** en cada sesión; el histórico queda en los commits (git log HANDOFF.md).
> La guía permanente del proyecto es [AGENTS.md](AGENTS.md): este fichero solo añade el estado puntual.

**Fecha del traspaso:** 17 de octubre de 2026 (taller de tienda: unidades 16-17)
**Proyecto:** Actividades FPB Comercio — `https://github.com/sergarb1/ActividadesFPBComercio`

---

## 📍 Criterio del usuario (lo más importante)

El repo es de **actividades para hacer en clase**, no de apuntes. Cada ficha debe traer algo que el alumnado haga: caso, plantilla, role-play, reto, juego con roles. **La teoría, al mínimo.** Lo antiguo (unidades 1, 2, 3 y 9) se ha eliminado por decisión expresa: no se vuelve a trabajar en ello.

## ✅ Hecho en esta sesión

1. Commit `aff1498` con las unidades 12-15 (fichas, imágenes Excalidraw, DOCX, sidebar y landing) — **pusheado y desplegado**.
2. **Borradas del repo** las unidades 1 · Confianza real, 2 · Ponte en su sitio, 3 · Modo equipo y 9 · Kudo Cards: `.md`, DOCX, imágenes y entradas del sidebar. Recuperables con `git log --all`.
3. **Landing rehecha** (`src/content/docs/index.md`): solo taller de tienda + estudiar, sin las unidades viejas ni el bloque de Tutoría.
4. **Sidebar** (`astro.config.mjs`): fuera `tutoriaItems`; queda el grupo 💻 Contenidos con las unidades 12-17.
5. **Unidad 16 · 🛒 El mostrador** (`16-el-mostrador`):
   - `01-guion-de-los-5-pasos` — recibir, preguntar, acompañar, resolver, despedir + role-play del cliente mudo.
   - `02-objeciones-y-clientes-dificiles` — "es caro", "me lo pienso", "solo miro", cliente que grita + role-play con caso de auriculares.
   - `03-juegos-y-retos` — fail de DANI, mostrador a ciegas, cliente secreto, la frase que salva, logros.
6. **Unidad 17 · 💶 La caja y el cobro** (`17-caja-y-cobro`):
   - `01-cobrar-sin-errores` — orden del cobro, cambio hacia arriba con tabla, efectivo/tarjeta/móvil y cálculos de cambio.
   - `02-arqueo-de-caja` — 4 pasos del arqueo, tabla de descuadres y aviso a la encargada.
   - `03-juegos-y-retos` — caja a contrarreloj, turno imposible, frase de caja y logros.
7. **4 imágenes Excalidraw** nuevas (`.excalidraw` + `.svg` + `.png`):
   - `public/img/16-el-mostrador/{01-guion-5-pasos,02-clientes-dificiles}.{svg,png}`
   - `public/img/17-caja-y-cobro/{01-cobro-pasos,02-arqueo-caja}.{svg,png}`
   - Fuentes en `public/img/fuentes/{16-el-mostrador,17-caja-y-cobro}-ficha{1,2}.excalidraw`
   - Generadas con `scripts/gen-tienda-images.py` y `render` offline del CLI (no toca el canvas del usuario).
8. **`AGENTS.md`** reescrito en lo que respecta a temario y estado: 40 unidades, bloque 🏪 Taller de tienda 16-21, resto renumerado, retiradas documentadas.

## ✅ Verificaciones pasadas

- `npm run build` → exit 0.
- `npm run docx` → exit 0, 6 DOCX (12-17), 0 fallos.
- SVG con marca `svg-source:excalidraw` y Excalifont embebida.
- Sin enlaces a las unidades borradas en las páginas publicadas ni en el sidebar.

## ⏳ Pendiente / siguiente

- **Siguiente lote:** 18 · 🗃️ Reposición y almacén y 19 · 🧮 Inventario y stock (mismo formato actividad).
- Después: 20 · El escaparate y 21 · Devoluciones y reclamaciones.
- Revisión de tono del usuario cuando lea las fichas 16-17.

## 🧰 Comandos

```bash
npm run dev / build / preview / docx

# Imágenes: generar escenas y renderizar sin canvas
python scripts/gen-tienda-images.py
npx -y mcp-excalidraw-server render <fuente.excalidraw> --format svg --out x.svg
npx -y mcp-excalidraw-server render <fuente.excalidraw> --format png --out x.png
```

## 📐 Recordatorios críticos

- Formato ficha obligatorio (ver `AGENTS.md`): 📬 En corto → 💡 Lo que hay que saber → cabecera Nombre/Fecha/Grupo → ✍️ A por ellos → soluciones en `<details>` → 🔑 Para el profe → pie.
- **Toda ficha acaba en actividad**: si no hay nada que hacer, no es una ficha.
- Sin números de unidad en prosa ni títulos; sin enlaces a páginas inexistentes.
- ROSA se ríe de la tontería, nunca del compañero; el fail es siempre de DANI.
- Tras editar contenido: `npm run build`, `npm run docx` y commitear los DOCX.
