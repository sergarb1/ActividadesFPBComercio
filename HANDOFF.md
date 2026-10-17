# HANDOFF — Traspaso de sesión

> Documento para que otro modelo o una sesión futura continúe el trabajo sin redescubrir el contexto.
> Se **sobrescribe** en cada sesión; el histórico queda en los commits (git log HANDOFF.md).
> La guía permanente del proyecto es [AGENTS.md](AGENTS.md): este fichero solo añade el estado puntual.

**Fecha del traspaso:** 17 de octubre de 2026 (numeración corrida + estilo ficha)
**Proyecto:** Actividades FPB Comercio — `https://github.com/sergarb1/ActividadesFPBComercio`

---

## 📍 Criterio del usuario

El repo es de **actividades de aula**, no de apuntes. Cada ficha debe traer algo que el alumnado haga (caso, plantilla, role-play, reto). **La teoría, al mínimo.** Todo el contenido va orientado a ficha imprimible.

**Estilo de ficha:** copiado del repo hermano `C:\Users\serga\Desktop\TutoriaFPB` — `ficha-cabecera` (Nombre/Fecha/Grupo), `ficha-img` con `<figcaption>`, ejercicios en `<div class="ejercicio">`, líneas de respuesta con `<span class="linea-respuesta">`, soluciones en `<details>`.

## ✅ Hecho en esta sesión

1. **Fuera el bloque de tutoría** del repo (unidades antiguas, DOCX e imágenes).
2. **Numeración corrida desde 1** (antes empezaba en 12 tras el borrado). Renombrados ficheros, slugs, carpetas de imágenes, DOCX, sidebar y enlaces:
   - `01-el-mostrador` · `02-caja-y-cobro` · `03-reposicion-y-almacen` · `04-inventario-y-stock`
   - `07-leer-y-entender` · `08-subrayado` · `09-esquemas-y-resumenes` · `10-textos-en-papel`
3. **Unidades nuevas 3 y 4** con 3 fichas cada una:
   - **Reposición y almacén:** albarán y firma con reservas · familias, FIFO y facing · juegos (recepción a contrarreloj, huecos, FIFO exprés).
   - **Inventario y stock:** recuento y diferencias · stock mínimo y punto de pedido · juegos (inventario a ciegas, pedido justo, caza la merma).
4. **4 imágenes Excalidraw nuevas** (`03-…-ficha1/2`, `04-…-ficha1/2`) generadas con `scripts/gen-tienda-2.py` y `render` offline.
5. **Estilo ficha "de hoja de trabajo"** en `src/styles/custom.css`:
   - la página se muestra como hoja blanca con etiqueta `FICHA DE AULA` (la portada queda excluida con `:has(.ficha-hero)`);
   - cabecera con rótulo `DATOS DE LA FICHA`, ejercicios recuadrados con etiqueta `EJERCICIO`, líneas de respuesta sólidas, tablas con bordes tipo plantilla;
   - impresión A4: oculta menús, evita cortar ejercicios, quita sombras.
6. **Imágenes migradas** al markup de TutoriaFPB (`<div class="ficha-img">` + `img` con `width`/`height`/`loading="lazy"` + `<figcaption>`) en las 16 fichas.
7. **`AGENTS.md`** actualizado: criterio "todo es ficha", identidad visual obligatoria, markup de imagen y temario secuencial de 29 unidades.

## ✅ Verificaciones pasadas

- `npm run build` → exit 0.
- `npm run docx` → exit 0 (8 DOCX).
- 0 enlaces internos rotos y 0 imágenes inexistentes.
- SVG con `svg-source:excalidraw` y Excalifont embebida.

## ⏳ Pendiente / siguiente

- **Siguiente lote:** 5 · 🪟 El escaparate y 6 · 🔄 Devoluciones y reclamaciones.
- Revisión visual del usuario: si la hoja de ficha necesita ajustes (ancho, tipografía, espaciado), se toca solo `src/styles/custom.css`.
- Las fichas 7-10 (estudiar) son las más "teóricas": si se quiere, se reescriben con más actividad y menos explicación.

## 🧰 Comandos

```bash
npm run dev / build / preview / docx

python scripts/gen-tienda-images.py   # escenas 1-2
python scripts/gen-tienda-2.py        # escenas 3-4
npx -y mcp-excalidraw-server render <fuente.excalidraw> --format svg --out x.svg
npx -y mcp-excalidraw-server render <fuente.excalidraw> --format png --out x.png
```

## 📐 Recordatorios críticos

- Formato y orden fijos: 📬 En corto → 💡 Lo que hay que saber → cabecera → imagen → ✍️ A por ellos → 🎭 Mini dinámica → 🔑 Para el profe → pie.
- **Toda ficha acaba en actividad**; si no hay nada que hacer, no es una ficha.
- Sin números de unidad en prosa ni títulos; sin enlaces a páginas inexistentes.
- ROSA se ríe de la tontería, nunca del compañero; el fail es siempre de DANI.
- Tras editar contenido: `npm run build`, `npm run docx` y commitear los DOCX.
