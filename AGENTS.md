# AGENTS.md — Guía para LLMs sobre el proyecto Actividades FPB Comercio

Este archivo ayuda a cualquier agente LLM (opencode, Claude, ChatGPT, etc.) a entender la estructura y convenciones del proyecto y a trabajar de forma efectiva.

---

## 📋 Descripción del proyecto

Web de **actividades de aula para la FPB de Comercio** (alumnado de 16-17 años): fichas para hacer en clase sobre el oficio de tienda (mostrador, caja, almacén, escaparate, clientes) y las destrezas que necesitan para aprobar.

> 📌 **Criterio del usuario (17/10/2026):** el repo es de **actividades para el alumnado**, no de apuntes. Cada ficha debe terminar con algo que el grupo haga en clase (caso, plantilla, role-play, reto). La teoría, al mínimo.

Estilo visual y pedagógico idéntico al proyecto hermano **ApuntesRedes** (`C:\Users\serga\Desktop\ApuntesRedes`): Astro + Starlight + GitHub Pages, azul #2563eb + teal #4ecdc4, glassmorphism, Geist Sans, es-ES.

### 🎯 MISIÓN PRIORITARIA: mejorar el clima del aula

**El proyecto nace para ayudar a un grupo con conflictos interpersonales, conflictos de una persona contra el resto del grupo, y poco respeto entre el alumnado.** Esta misión va por delante de todo:

1. **Actividades cooperativas, nunca destructivas.** Nada de "el último que pierde se va", castigos, ridiculizaciones ni competiciones que expongan a alguien. Gana el grupo.
2. **Cero insultos, cero humillaciones.** Los conflictos se resuelven con Mensaje-Yo, escucha y acuerdos. Nunca se modela un insulto como chiste gracioso.
3. **Incluir siempre al que está solo o apartado.** Toda dinámica lleva mecanismos explícitos de inclusión (turnos, sorteo, misiones secretas, post-its anónimos cuando el grupo es muy conflictivo).
4. **Abordar de frente la dinámica "uno contra el grupo"** (chivo expiatorio): explicarla, detectarla y dar herramientas para cortarla.
5. **Los insultos no dan poder sobre ti** (unidad propia): la reacción es el premio del que insulta; se enseña a no dárselo — **pero sin normalizar el aguante**: si persiste o viene de varios, es bullying y se avisa. Este equilibrio se vigila en todo el contenido de esa unidad.
6. **El respeto se practica, no se sermona.** Cada unidad de convivencia incluye al menos una dinámica para hacer en el aula.
7. **Tono esperanzador.** Nunca se etiqueta al grupo como "mal alumno": el clima de aula se construye entre todos y se puede mejorar.

---

## 🏗️ Stack

- **Framework:** Astro 7 + Starlight 0.41
- **Idioma:** Solo castellano (es-ES). NO versión valenciana.
- **Repo/GitHub Pages:** `ActividadesFPBComercio` → base path `/ActividadesFPBComercio`, site `https://sergarb1.github.io/ActividadesFPBComercio`
- **Despliegue:** GitHub Actions → GitHub Pages en rama `main`
- **DOCX por unidad:** Pandoc 3.8+ (CLI en PATH) vía `npm run docx` → `docx/<unidad>/<unidad>.docx` (índice + puntos; el script descubre las unidades solas). **Tras editar contenido de unidades, regenerar con `npm run docx` y commitear los DOCX.** Los enlaces internos se convierten en URLs de GitHub Pages para que el DOCX quede con enlaces vivos. Los bloques `<details>` se pierden en DOCX (las soluciones aparecen sin spoiler, aceptado por diseño).
- **Imágenes Excalidraw por ficha:** SVG + PNG en `public/img/NN-nombre/` y fuente `.excalidraw` en `public/img/fuentes/`. Se generan con el CLI del skill `excalidraw-skill` del repo hermano `PresentacionesEducativas` (funciona headless): `npx -y mcp-excalidraw-server <add|export|screenshot|snapshot|restore>`. Las capturas se exportan con `screenshot --format svg` y `screenshot` (PNG).
- **Sin PDF/EPUB por ahora** (tablas, listas y emojis cubren la necesidad visual)

---

## 📁 Estructura de directorios

```
src/content/docs/            → Landing (index.md)
src/content/docs/NN-nombre/  → Puntos de cada unidad (01-…, 02-…, NN-juegos-y-retos)
src/content.config.ts        → Colección docs de Starlight (no tocar salvo actualización de Starlight)
src/styles/custom.css        → CSS del tema (azul + teal, glassmorphism, print)
public/favicon.svg           → Icono
scripts/generate-docx.mjs    → Generación DOCX por unidad (Pandoc; descubre las unidades solas)
docx/NN-nombre/              → DOCX generados (van al repo)
.github/workflows/deploy.yml → CI/CD a GitHub Pages
astro.config.mjs             → Config Astro + Starlight (sidebar con las unidades creadas)
```

---

## 🧑‍🤝‍🧑 Personajes fijos

- **ROSA** — la encargada de la tienda, 20 años viendo de todo. Cascarrabia pero con los pies en el suelo: sarcasmo, pero siempre acierta. Explica los errores típicos y las dudas.
- **DANI** — el nuevo dependiente, bien intencionado pero metepata. **El fail es siempre suyo, nunca el del alumno**: así se aprende riendo del error sin señalar a nadie del grupo. Es el truco anti-conflicto del proyecto.
- **Regla de oro de los personajes:** ROSA se burla de la *tontería*, jamás del *compañero*. El tono con el alumnado corrige el error sin humillar a la persona.
- **Ejemplos de vida real 16-17:** insta/tiktok, el grupo de WhatsApp, el primer curro, la tienda, los timos online, compararse con los demás.

---

## 📍 Estado actual (actualizar al publicar unidades)

- **Publicadas:** **1-6** (taller de tienda completa) · **7-13** (estudiar: leer, subrayar, esquemas, papel, memorizar, examen, IA copiloto).
- **Retirado:** todo el bloque de tutoría anterior (recuperable en el historial de git).
- **Siguiente lote:** 14 · Monta tu presentación y el resto del bloque creativo (15-18).
- **Especial publicada:** 🏆 El torneo del taller (`90-el-torneo-del-taller`, fuera de la numeración 1-29): liga de dinámicas por equipos con tabla en la pared y premios cooperativos.
- **Última verificación:** `npm run build` ✓ · `npm run docx` ✓ · imágenes Excalidraw de las 13 unidades + especial.
- **Traspaso de sesión:** [HANDOFF.md](HANDOFF.md) — se sobrescribe en cada sesión; el histórico queda en git.

---

## 📚 Temario (29 unidades pequeñas, en construcción)

Filosofía: **unidades pequeñas** (índice + 3 fichas) y **actividad de aula en cada una**. Publicadas: **1-6** (taller de tienda completa) y **7-13** (estudiar completo, con la IA como copiloto). Todo lo que se escriba sigue el formato ficha y termina en algo que el alumnado hace en clase.

> 🔢 **Numeración corrida desde 1** (17/10/2026): antes había huecos porque se retiraron las unidades de tutoría. Las 1-6 son el taller de tienda, las 7-13 estudiar, 14-18 creatividad, 19-24 comunicación, 25-28 IPE II y 29 el proyecto OAA.
>
> 🗑️ **Retirado (no volver a crearlo):** el antiguo bloque de tutoría (Confianza real, Empatía, Modo equipo, Kudo Cards, etc.). Queda en el historial de git, no en el repo.

#### 🏪 Taller de tienda

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 1 | 🛒 El mostrador | `01-el-mostrador` | ✅ Guion de 5 pasos, objeciones, clientes difíciles, role-play y juegos |
| 2 | 💶 La caja y el cobro | `02-caja-y-cobro` | ✅ Cobro (efectivo/tarjeta/móvil), cambio hacia arriba, arqueo y descuadres |
| 3 | 🗃️ Reposición y almacén | `03-reposicion-y-almacen` | ✅ Albarán, familias, FIFO, facing y huecos |
| 4 | 🧮 Inventario y stock | `04-inventario-y-stock` | ✅ Recuento, mermas, stock mínimo y punto de pedido |
| 5 | 🪟 El escaparate | `05-el-escaparate` | ✅ Idea en una frase, 3 niveles, tarjeta de precio y ciclo de renovación |
| 6 | 🔄 Devoluciones y reclamaciones | `06-devoluciones-y-reclamaciones` | ✅ Las 3 condiciones, garantía legal (2 años), hoja de reclamaciones y desistimiento |

#### 🧠 Estudiar sin sufrir

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 7 | 📖 Leer y entender | `07-leer-y-entender` | ✅ Lectura comprensiva antes de subrayar |
| 8 | ✏️ Subrayado | `08-subrayado` | ✅ Qué subrayar, con qué, y el subrayado que no sirve |
| 9 | 🗂️ Esquemas y resúmenes | `09-esquemas-y-resumenes` | ✅ Mapas mentales, esquemas de flechas, resumen propio |
| 10 | 📄 Textos en papel | `10-textos-en-papel` | ✅ Marcadores, post-its y repaso manuscrito |
| 11 | 🧠 Memorizar de verdad | `11-memorizar-de-verdad` | ✅ Ciclo leer→copiar→tapar→decir, semáforo del conocimiento y repaso 1-3-7 |
| 12 | ✅ Examen en blanco | `12-examen-en-blanco` | ✅ 6 preguntas propias, corrección en otro color y reparto de minutos por bloques |
| 13 | 🤖 IA: copiloto de estudio | `13-ia-copiloto-de-estudio` | ✅ Preguntas que funcionan (qué/para qué/cómo), semáforo de usos y regla de la explicación |

#### 🎨 Modo creativo

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 14 | 🎤 Monta tu presentación | `14-monta-tu-presentacion` | Buscar → recopilar → seleccionar → crear presentación propia |
| 15 | 💡 Creatividad | `15-creatividad` | Qué es, cómo se estimula, actividades |
| 16 | 🔍 Webgrafía | `16-webgrafia` | Qué es, fiabilidad de fuentes, cómo se elabora |
| 17 | 🖼️ Bancos de imágenes libres | `17-bancos-de-imagenes-libres` | Pexels, Unsplash, Pixabay… |
| 18 | ⚖️ Copyright | `18-copyright` | Qué es, licencias CC, uso educativo |

#### 💬 Hablar y escribir como un pro

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 19 | 📧 Correos que funcionan | `19-correos-que-funcionan` | Enviar correos bien escritos |
| 20 | ↩️ Responder sin quemarse | `20-responder-sin-quemarse` | Responder, también al cliente enfadado |
| 21 | 🆘 Incidencias de clientes | `21-incidencias-de-clientes` | Presencial, correo y redes sociales + guión de tarea |
| 22 | 📰 Noticias de actualidad | `22-noticias-de-actualidad` | Recopilar, seleccionar y comentar noticias de comercio |
| 23 | 🎬 Vídeos motivacionales | `23-videos-motivacionales` | Banco de enlaces + guión de visionado |
| 24 | 🤖 IA informática | `24-ia-informatica` | Qué es la IA, herramientas, aplicaciones prácticas |

#### 💶 Dinero, nóminas y curro (IPE II)

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 25 | 📑 El contrato de trabajo | `25-el-contrato-de-trabajo` | Tipos, partes, derechos. El módulo se llama **IPE II** (no expandir) |
| 26 | 💰 Salario y nómina | `26-salario-y-nomina` | Partes de una nómina, bruto vs neto |
| 27 | 📊 IRPF y cultura económica | `27-irpf-y-cultura-economica` | Impuestos básicos, cultura económica |
| 28 | 🔭 Con y sin graduado | `28-con-y-sin-graduado` | Oportunidades laborales comparadas |

#### 🏪 Proyecto almacén (OAA)

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 29 | 🏪 Guión del proyecto de almacén | `29-guion-proyecto-almacen` | Guión del proyecto. El proyecto/módulo se llama **OAA** (no expandir) |

## 📝 Convenciones para escribir unidades

### Frontmatter requerido

```yaml
---
title: Título de la página (el índice sin número; los puntos sí llevan "N —")
description: Descripción corta con emoji 😌
---
```

### Números de unidad en el texto (regla obligatoria)

El contenido **no lleva números de unidad** (`U01`, `Unidad 5`…) en prosa, títulos, migajas ni enlaces: así se reordena sin reescribir. En su lugar:

- Referencias → *"en la unidad de empatía"*, *"en el banco de juegos"*.
- **Exentos:** etiquetas del sidebar en `astro.config.mjs` y nombres de fichero/URLs (`01-el-mostrador/01-guion-de-los-5-pasos`).

### Secciones obligatorias

**Índice de cada unidad** (`src/content/docs/NN-nombre.md`):

1. `<p><small>…</small></p>` + mapa: `> 🗺️ **El mapa:** 🏪 Taller de tienda → **AQUÍ ESTÁS** → …`
2. `## 🎯 Objetivo de la unidad`
3. `## 🗺️ Mapa de la unidad` — tabla que enlaza cada punto
4. `## 🎲 Actividades y juegos de la unidad` — enlaces `<a href>` a los puntos de práctica
5. `## 🚪 ¿Por dónde empiezo?`
6. Pie: `**📍 Primer punto:** […] · **⏭️ Al acabar, continúa en […](…)**`

### 📄 Formato de ficha (obligatorio — desde la reconversión)

> **Todo el contenido son FICHAS DE AULA**: hojas para trabajar en clase, no textos para leer en casa. Cada punto = 1 ficha imprimible de 1-2 A4. Explicación mínima + ejercicios para rellenar. Si un tema crece, se parte en dos fichas.

**Identidad visual obligatoria (se vea que es una ficha):**

- La página se muestra como **hoja de trabajo**: fondo blanco, marco y etiqueta **`FICHA DE AULA`** (lo pone el CSS `.sl-markdown-content::before`; la portada queda excluida).
- **Nunca** quitar ni reordenar: `📬 En corto` → `💡 Lo que hay que saber` → **cabecera** → **imagen** → `✍️ A por ellos` → `🎭 Mini dinámica` → `🔑 Para el profe` → pie.
- Cada ejercicio va en su **`<div class="ejercicio">`** (recuadro numerado, etiqueta `EJERCICIO`).
- Las respuestas a mano van con **`<span class="linea-respuesta"></span>`** (una por línea que el alumno deba escribir).
- Las tablas son **plantillas para rellenar** (última columna vacía, filas de ejemplo): nunca tablas de teoría sin huecos.
- Al menos **un ejercicio con huecos (`___`)**, uno de **emparejar/completar tabla** y uno de **escribir 2-4 líneas**.
- En papel la ficha debe caber en **1-2 A4**; el CSS de impresión ya oculta menús y evita cortar ejercicios.

**Plantilla de cada punto (ficha):**

```markdown
---
title: N — Título de la ficha
description: Bajada corta con emoji 😌
---

<p><small>Bajada corta con emoji 😌</small></p>

> 🗺️ **Estás en:** 🤝 **Nombre de la unidad** → N · Título

## 📬 En corto

> Idea en UNA frase.

## 💡 Lo que hay que saber

Explicación breve (párrafos cortos, analogías 16-17, tablas, muchas
emojis). Máximo ~1 pantalla: el resto lo dicen los ejercicios.
![Descripción de la imagen](/ActividadesFPBComercio/img/NN-nombre/xx.svg)

<div class="ficha-cabecera">
  <span class="campo">👤 Nombre:</span>
  <span class="campo">📅 Fecha:</span>
  <span class="campo">🏫 Grupo:</span>
</div>

## ✍️ A por ellos (ejercicios)

<div class="ejercicio">**1. ✏️ Completa:** …</div>
<div class="ejercicio">**2. 🎯 Decide:** …</div>
Respuestas siempre en <details><summary>🔄 Soluciones</summary>…</details>

## 🎭 Mini dinámica (opcional, 5-10 min)

## 🔑 Para el profe (soluciones y pistas)  ← solo en DOCX/web

📚 [Volver al índice…] · **Anterior:** […] · **Siguiente:** […]
```

**Reglas de la ficha:**

1. **Cabecera imprimible:** toda ficha lleva `<div class="ficha-cabecera">` con Nombre/Fecha/Grupo.
2. **Ejercicios siempre rellenables:** completar, emparejar, decidir, escribir; usa `<div class="ejercicio">` para enmarcar cada uno y `<span class="linea-respuesta">` cuando haga falta una línea en blanco.
3. **Soluciones en `<details>`** (web) y visibles al final de la página (DOCX).
4. **1 imagen Excalidraw por ficha** en `public/img/NN-nombre/xx.svg` (+ `.png` de respaldo, fuente `.excalidraw` en `public/img/fuentes/`), insertada **con el mismo markup que TutoriaFPB** (referencia de estilo):
   ```html
   <div class="ficha-img">
     <img src="/ActividadesFPBComercio/img/NN-nombre/xx.svg" alt="Descripción" width="1120" height="254" loading="lazy">
     <figcaption>Descripción corta</figcaption>
   </div>
   ```
5. **Prosa mínima:** si una explicación supera una pantalla, se parte en dos fichas.

### 🎨 Sistema de iconos (obligatorio — muchos iconos)

| Icono | Sección / uso |
|---|---|
| 📬 | En corto (la idea en una frase) |
| 💡 | Lo que hay que saber (explicación) |
| ✍️ | Ejercicios ("A por ellos") |
| 🎭 | Mini dinámica / rol-play |
| 😬 | El fail de DANI (nota al margen) |
| 🤝 | Trabajo en equipo / dinámica |
| 🔑 | Soluciones / para el profe |
| 📌 | Idea importante (callout) |
| ⚠️ | Cuidado / error típico |
| 🏆 | Logros |
| 🎬 | Poscréditos |
| ✏️ 🎯 🔍 🧩 🗣️ 💪 🚪 🛡️ | Sub-tipo de ejercicio o categoría |

- **Un icono por idea** en tablas, listas, botones y títulos de sección.
- Los títulos de las fichas llevan siempre emoji en la description.

**Bloques de juegos** (la unidad entera debe incluir los mínimos):

- `## 🤝 Trabajo en equipo` — **dinámica para el aula** (obligatoria en toda unidad de tutoría; objetivo, material, paso a paso, tiempo, inclusión)
- `## 😬 El fail de DANI` — error típico que comete DANI y ROSA explica (obligatorio en toda unidad de tutoría)
- `## ⚔️ Cara a cara` — debate entre dos conceptos personificados
- `## 🕵️ ¿Quién soy?` — adivinanzas con `<details>`
- `## 🧠 Reto mental` — ejercicios con `<details>`
- `## 🧩 Crucigrama` — con `<details>` (opcional)
- `## ⭐ Rol-play` — variantes: `⭐ Sé el Compañero`, `⭐ Sé el Vendedor`, `⭐ Sé el Cliente`
- `## 🤷 Dudas de 10 segundos` — FAQ con ROSA
- `## 🏆 Logros` — gamificación ligera (ej.: 🏆 "Misión invisible completada")
- `## 🎬 Poscréditos` — escena cómica corta con continuidad

**Mínimo por unidad de tutoría:** ≥1 dinámica 🤝, ≥1 😬 El fail de DANI, ≥1 bloque con soluciones en `<details>`.

### Plantilla de dinámica 🤝 (formato obligatorio)

```markdown
## 🤝 Trabajo en equipo: Nombre de la dinámica

**Objetivo:** … **Tiempo:** 15 min · **Material:** …

1. Paso a paso…
2. …

> ♿ **Inclusión:** cómo se garantiza que nadie se quede fuera (sorteo, turnos, misiones secretas…).
```

### Límite de tamaño

Unidades **pequeñas**: índice + 2-4 puntos. Si un tema crece, se parte en dos unidades.

### Estilo de escritura

- Conversacional, humor ligero, es-ES, trato de tú. Ejemplos de vida real 16-17 (insta, WhatsApp, primer curro).
- Emojis en títulos de sección; `>` blockquotes para ideas clave; tablas para comparar.
- **Soluciones siempre en `<details>`:**

```html
<details>
<summary>🔄 Respuestas</summary>
1. **Empatía** — Ponerse en el lugar del otro.
</details>
```

- Formato es-ES: millares con punto (`1.000`), coma decimal. Sin LatAm ni anglicismos innecesarios.

### Páginas imprimibles

Las unidades de guiones y turnos (`09-tu-sesion-en-50-minutos`, `10-turnos-del-aula`) se piensan para imprimir: instrucciones de impresión en la propia página; `custom.css` ya tiene `@media print`.

---

## 🚀 Comandos

```bash
npm run dev       # Servidor local → http://localhost:4321
npm run build     # Build estático → dist/
npm run preview   # Previsualizar build
npm run docx      # DOCX por unidad → docx/ (requiere Pandoc en PATH)

# Imágenes Excalidraw (skill de PresentacionesEducativas; funciona headless)
npx -y mcp-excalidraw-server add elem.json        # crear elementos en el canvas
npx -y mcp-excalidraw-server export --out x.excalidraw   # fuente editable
npx -y mcp-excalidraw-server screenshot --format svg --out x.svg
npx -y mcp-excalidraw-server screenshot --out x.png
npx -y mcp-excalidraw-server snapshot save|restore <nombre>  # no perder la escena del usuario
npx -y mcp-excalidraw-server clear --yes
```

---

## 🧪 Checklist para nueva unidad

- [ ] Frontmatter (title, description con emoji)
- [ ] Sin números de unidad en prosa ni títulos
- [ ] Índice: objetivo, mapa (tabla), actividades, ¿por dónde empiezo?, pie
- [ ] Cada punto (ficha): 📬 En corto, 💡 Lo que hay que saber, cabecera Nombre/Fecha/Grupo, ✍️ A por ellos, soluciones en `<details>`, 🔑 Para el profe, pie Anterior/Siguiente
- [ ] Actividad de aula real (caso, plantilla, role-play o reto) + ≥1 😬 fail de DANI + soluciones en `<details>`
- [ ] Imagen Excalidraw de la ficha: `.svg` + `.png` en `public/img/NN-nombre/` + `.excalidraw` en `public/img/fuentes/`
- [ ] Enlaces solo a páginas existentes (contenido, sidebar y landing)
- [ ] Sidebar actualizado en `astro.config.mjs` (solo páginas existentes; el build falla con enlaces rotos)
- [ ] `npm run build` exitoso
- [ ] `npm run docx` regenerado tras editar contenido
- [ ] Comprobación lingüística es-ES
- [ ] Tono clima de aula: cooperativo, inclusivo, sin insultos modelados

---

## ⚠️ Notas importantes para el agente

1. **NO crear versiones en valenciano.**
2. **NO romper la misión de clima de aula** (ver arriba).
3. **NO enlazar páginas inexistentes** en sidebar o landing (el build falla).
4. **Al añadir un bloque nuevo** de la Sección 2: crear carpeta, índice, puntos, añadir al sidebar y actualizar el temario de este AGENTS.md.
5. **Checkpoint de tono:** el usuario revisa las primeras unidades antes de masificar el resto; si pide cambios de tono o nombres, aplicarlos primero aquí.
6. **P4QU3T3 (de ApuntesRedes) no aplica aquí:** los personajes de este proyecto son ROSA y DANI.
7. **Skills instaladas en `.agents/skills/`** (usarlas cuando toque interfaces o diagramas):
   - `ui-ux-pro-max` · `ui-styling` · `design-system` · `design` · `brand` · `slides` · `banner-design` — de `nextlevelbuilder/ui-ux-pro-max-skill`. Útil para revisar/mejorar el CSS de las fichas, la landing y la accesibilidad.
   - `excalidraw-skill` — el skill del CLI que ya usamos para las imágenes de las fichas (`npx -y mcp-excalidraw-server …`). Es la referencia canónica de su flujo (canvas, render offline, snapshot…).
   - `excalidraw-diagram` (de `coleam00/excalidraw-diagram-skill`) — metodología para diagramas que **argumentan visualmente**, con su bucle render→revisar→arreglar. Su paleta (`references/color-palette.md`) ya está adaptada a la marca del site (#2563eb + teal, Excalifont fontFamily 5, roughness 1). **El bucle de render necesita setup la primera vez**: `cd .agents/skills/excalidraw-diagram/references && uv sync && uv run playwright install chromium`. Sin ese setup, usar el `render` offline del CLI como sustituto.
