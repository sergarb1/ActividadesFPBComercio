# HANDOFF — Traspaso de sesión

> Documento para que otro modelo o una sesión futura continúe el trabajo sin redescubrir el contexto.
> Se **sobrescribe** en cada sesión; el histórico queda en los commits (git log HANDOFF.md).
> La guía permanente del proyecto es [AGENTS.md](AGENTS.md): este fichero solo añade el estado puntual.

**Fecha del traspaso:** 17 de octubre de 2026 (lote 14-15 añadido)
**Proyecto:** Actividades FPB Comercio — `https://github.com/sergarb1/ActividadesFPBComercio`

---

## 📍 Situación

- Repo local: `C:\Users\serga\Desktop\ActividadesFPBComercio` (clonado desde `C:\Users\serga\Desktop\Ofimatica`, que era otro clon del mismo repo).
- Rama `main` en el commit `1b76376` + **cambios sin commitear** (ver abajo).
- Stack: Astro 7 + Starlight 0.41, base `/ActividadesFPBComercio`, despliegue GitHub Pages. Pandoc 3.8.3 en PATH.

## ✅ Hecho en esta sesión

1. **Migración completa** del repo (historial, remoto y cambios pendientes del usuario preservados).
2. **Unidad 12 · 📖 Leer y entender** publicada en formato ficha:
   - `src/content/docs/12-leer-y-entender.md`
   - `12-leer-y-entender/01-leer-no-es-ojear.md`
   - `12-leer-y-entender/02-el-metodo-antes-de-subrayar.md`
   - `12-leer-y-entender/03-juegos-y-retos.md`
3. **Unidad 13 · ✏️ Subrayado** publicada en formato ficha:
   - `src/content/docs/13-subrayado.md`
   - `13-subrayado/01-que-subrayar-y-que-no.md`
   - `13-subrayado/02-como-subrayar-de-verdad.md`
   - `13-subrayado/03-juegos-y-retos.md`
4. **Unidad 14 · 🗂️ Esquemas y resúmenes** y **Unidad 15 · 📄 Textos en papel** publicadas en formato ficha:
   - `src/content/docs/14-esquemas-y-resumenes.md` + `14-esquemas-y-resumenes/{01-de-subrayado-a-esquema,02-el-resumen-propio,03-juegos-y-retos}.md`
   - `src/content/docs/15-textos-en-papel.md` + `15-textos-en-papel/{01-marcar-sin-destrozar,02-repaso-a-mano,03-juegos-y-retos}.md`
5. **Sidebar** (`astro.config.mjs`): `contenidosItems` con las unidades 12-15 y padre `💻 Contenidos` activado.
6. **Landing** (`src/content/docs/index.md`): cards de las unidades 12-15 + lista "En camino" actualizada.
7. **Imágenes Excalidraw reales** (con el CLI del skill `excalidraw-skill` de `C:\Users\serga\Desktop\PresentacionesEducativas`, funciona headless):
   - `public/img/12-leer-y-entender/01-ojear-vs-leer.{svg,png}`
   - `public/img/12-leer-y-entender/02-metodo-4-pasos.{svg,png}`
   - `public/img/13-subrayado/01-regla-del-20.{svg,png}`
   - `public/img/13-subrayado/02-colores-margen.{svg,png}`
   - `public/img/14-esquemas-y-resumenes/{01-subrayado-a-esquema,02-resumen-propio}.{svg,png}`
   - `public/img/15-textos-en-papel/{01-pagina-de-trabajo,02-repaso-manuscrito}.{svg,png}`
   - Fuentes: `public/img/fuentes/{12-leer-y-entender-ficha1,12-leer-y-entender-ficha2,13-subrayado-ficha1,13-subrayado-ficha2,14-esquemas-y-resumenes-ficha1,14-esquemas-y-resumenes-ficha2,15-textos-en-papel-ficha1,15-textos-en-papel-ficha2}.excalidraw`
8. **`AGENTS.md`**: estado actual, flujo Excalidraw (sustituye al "sin diagramas"), comandos del CLI y checklist de ficha.

## ✅ Verificaciones pasadas

- `npm run build` → exit 0, **36 páginas**.
- `npm run docx` → exit 0, **8 DOCX, 0 fallos** (incluye las unidades 12-15).
- Enlaces internos de las fichas 14-15 verificados: todos apuntan a páginas existentes.
- SVG exportados con `svg-source:excalidraw` y Excalifont embebida (idéntico formato al existente en el proyecto).
- Canvas del usuario restaurado tras exportar (snapshot `postit-user`: diagrama "Post-it sorpresa").

## ⏳ Pendiente

- **Siguiente lote:** 16 · Memorizar de verdad y 17 · Examen en blanco.
- **Criterio del usuario para todo lo que venga:** el repo es de **actividades para hacer en clase**, así que cada ficha debe traer algo que el alumnado haga (plantilla, dinámica, reto, ejercicio con huecos). La teoría, al mínimo. Lo "viejo" (unidades anteriores) no corre prisa: primero material de aula.

## 🗂️ Estado de git

- Commit del lote 12-15 (fichas, imágenes, DOCX, sidebar, landing y estos documentos) hecho y **pusheado a `main`**, con despliegue automático a GitHub Pages.
- Árbol de trabajo limpio: el siguiente lote empieza desde cero.

## 🧰 Comandos

```bash
npm run dev / build / preview / docx

# Excalidraw (skill de PresentacionesEducativas)
npx -y mcp-excalidraw-server add elem.json
npx -y mcp-excalidraw-server export --out x.excalidraw
npx -y mcp-excalidraw-server screenshot --format svg --out x.svg
npx -y mcp-excalidraw-server screenshot --out x.png
npx -y mcp-excalidraw-server snapshot save|restore <nombre>
npx -y mcp-excalidraw-server clear --yes
```

## 📐 Recordatorios críticos

- Formato ficha obligatorio (ver `AGENTS.md`): 📬 En corto → 💡 Lo que hay que saber → cabecera Nombre/Fecha/Grupo → ✍️ A por ellos → soluciones en `<details>` → 🔑 Para el profe → pie.
- Sin números de unidad en prosa ni títulos; sin enlaces a páginas inexistentes.
- ROSA se ríe de la tontería, nunca del compañero; el fail es siempre de DANI.
- Tras editar contenido: `npm run build`, `npm run docx` y commitear los DOCX.
