# AGENTS.md — Guía para LLMs sobre el proyecto Actividades FPB Comercio

Este archivo ayuda a cualquier agente LLM (opencode, Claude, ChatGPT, etc.) a entender la estructura y convenciones del proyecto y a trabajar de forma efectiva.

---

## 📋 Descripción del proyecto

Web de **actividades para la FPB de Comercio** (alumnado de 16-17 años) en dos grandes secciones:

- 🤝 **Sección 1 · Tutoría — Modo coop**: unidades de convivencia para las tutorías (11 unidades).
- 💻 **Sección 2 · Contenidos**: destrezas y módulos (estudio, creatividad, comunicación, IPE II, proyecto de almacén OAA) (23 unidades).

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

- **Publicadas en formato ficha:** 1 · Confianza real · 2 · Ponte en su sitio · 3 · Modo equipo (en reconversión) · 9 · Kudo Cards · **12 · Leer y entender** · **13 · Subrayado** · **14 · Esquemas y resúmenes** · **15 · Textos en papel**.
- **Siguiente lote acordado:** 16 · Memorizar de verdad y 17 · Examen en blanco (lotes de 1-2 unidades, con checkpoint de tono del usuario).
- **Última verificación:** `npm run build` ✓ (36 páginas) · `npm run docx` ✓ (8 DOCX, 0 fallos) · imágenes Excalidraw de las unidades 12-15 en los 3 formatos.
- **Prioridad editorial (usuario):** cada ficha debe ser una **actividad de aula para el alumnado** (plantilla, dinámica, reto, ejercicio con huecos), no teoría. Lo "viejo" importa menos: si hay que elegir, primero materiales que se usen en clase.
- **Traspaso de sesión:** [HANDOFF.md](HANDOFF.md) — se sobrescribe en cada sesión; el histórico queda en git.

---

## 📚 Temario completo (34 unidades pequeñas)

Filosofía: **unidades pequeñas** (índice + 2-4 puntos = fichas). Cada tema del encargo es su propia unidad. **NO hay bloque de Aules** (decisión del usuario: eliminado).

> 🔄 **En reconversión a fichas:** unidades 1, 2, 3 y 9 se están convirtiendo al formato de ficha (índice + puntos). Las nuevas unidades se escriben ya en formato ficha desde el primer borrador. **✅ Publicadas en ficha: 12 (`leer-y-entender`) y 13 (`subrayado`).**

### 🤝 Sección 1 · Tutoría — Modo coop: la clase que funciona

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 1 | 🌱 Confianza real | `01-confianza-real` | Autoestima: qué es, cómo se cuida, dejar de decirse "no sirvo para nada" |
| 2 | 🎭 Ponte en su sitio | `02-ponte-en-su-sitio` | Empatía: sentirla, practicarla, cyberempatía |
| 3 | 🧩 Modo equipo | `03-modo-equipo` | Compañerismo: nadie se queda solo, gestos que se notan |
| 4 | 🛡️ Líneas rojas | `04-lineas-rojas` | Respeto, límites personales y cero bullying (tipos, señales, "uno contra el grupo") |
| 5 | 🔓 El insulto no es poder | `05-el-insulto-no-es-poder` | No dar al insulto la reacción que busca; el límite: persiste → se avisa |
| 6 | 🗣️ Decirlo sin liarla | `06-decirlo-sin-liarla` | Asertividad: Mensaje-Yo, escuchar y responder sin insultar |
| 7 | ⚖️ Conflicto: modo sabio | `07-conflicto-modo-sabio` | Anatomía del conflicto, resolución paso a paso, acuerdos de clase |
| 8 | 🎲 Banco de juegos | `08-banco-de-juegos` | Dinámicas de cohesión y de calma de conflictos, con fichas (objetivo, material, pasos, tiempo) |
| 9 | 🎁 Kudo Cards | `09-kudo-cards` | **Unidad única (guía + banco):** qué son y las 6 reglas de oro, la caja o el mural + 5 reglas del banco, cómo escribir un kudo (fórmula + plantillas), banco de +50 tarjetas listas en 8 categorías y herramienta digital de envío (mailto + copiar + imprimir) |
| 10 | 🎙️ Tu sesión en 50 minutos | `10-tu-sesion-en-50-minutos` | Guión de tutoría (tema libre: dinámicas, música, baile, deporte…) con título, objetivo, intro para compañeros, paso a paso, material y conclusiones. En Aules o en papel |
| 11 | 📆 Turnos del aula | `11-turnos-del-aula` | Lista de responsables diarios: plantilla para imprimir y firmar |

### 💻 Sección 2 · Contenidos

> Renumeradas +1 tras unificar Kudo Cards en una sola unidad (antes eran 13-35; ahora 12-34).

#### 🧠 Estudiar sin sufrir

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 12 | 📖 Leer y entender | `12-leer-y-entender` | Lectura comprensiva del temario antes de subrayar |
| 13 | ✏️ Subrayado | `13-subrayado` | Qué subrayar, con qué, y el subrayado que no sirve |
| 14 | 🗂️ Esquemas y resúmenes | `14-esquemas-y-resumenes` | Mapas mentales, esquemas de flechas, resumen propio |
| 15 | 📄 Textos en papel | `15-textos-en-papel` | Trabajar el temario impreso: marcadores, post-its, repaso manuscrito |
| 16 | 🧠 Memorizar de verdad | `16-memorizar-de-verdad` | Leer, copiar, grabarse y decir en voz alta la lección |
| 17 | ✅ Examen en blanco | `17-examen-en-blanco` | Practicar autoevaluación sin apuntes |
| 18 | 🤖 IA: copiloto de estudio | `18-ia-copiloto-de-estudio` | IA para dudas, entender y memorizar con ejemplos reales; NO copiar y pegar |

#### 🎨 Modo creativo

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 19 | 🎤 Monta tu presentación | `19-monta-tu-presentacion` | Buscar → recopilar → seleccionar → crear presentación propia |
| 20 | 💡 Creatividad | `20-creatividad` | Qué es, cómo se estimula, actividades |
| 21 | 🔍 Webgrafía | `21-webgrafia` | Qué es, fiabilidad de fuentes, cómo se elabora |
| 22 | 🖼️ Bancos de imágenes libres | `22-bancos-de-imagenes-libres` | Pexels, Unsplash, Pixabay… |
| 23 | ⚖️ Copyright | `23-copyright` | Qué es, licencias CC, uso educativo |

#### 💬 Hablar y escribir como un pro

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 24 | 📧 Correos que funcionan | `24-correos-que-funcionan` | Enviar correos bien escritos |
| 25 | ↩️ Responder sin quemarse | `25-responder-sin-quemarse` | Responder, también al cliente enfadado |
| 26 | 🆘 Incidencias de clientes | `26-incidencias-de-clientes` | Presencial, correo y redes sociales + guión de tarea |
| 27 | 📰 Noticias de actualidad | `27-noticias-de-actualidad` | Guión tarea: recopilar, seleccionar y comentar noticias de comercio |
| 28 | 🎬 Vídeos motivacionales | `28-videos-motivacionales` | Banco de enlaces + guión de visionado (comercio/MK, informática, IA, desarrollo personal, habilidades sociales). Sin incrustar |
| 29 | 🤖 IA informática | `29-ia-informatica` | Qué es la IA, herramientas, aplicaciones prácticas |

#### 💶 Dinero, nóminas y curro (IPE II)

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 30 | 📑 El contrato de trabajo | `30-el-contrato-de-trabajo` | Tipos, partes, derechos. El módulo se llama **IPE II** (no expandir) |
| 31 | 💰 Salario y nómina | `31-salario-y-nomina` | Partes de una nómina, bruto vs neto |
| 32 | 📊 IRPF y cultura económica | `32-irpf-y-cultura-economica` | Impuestos básicos, cultura económica |
| 33 | 🔭 Con y sin graduado | `33-con-y-sin-graduado` | Oportunidades laborales comparadas |

#### 🏪 Proyecto almacén (OAA)

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 34 | 🏪 Guión del proyecto de almacén | `34-guion-proyecto-almacen` | Guión del proyecto. El proyecto/módulo se llama **OAA** (no expandir) |

---

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
- **Exentos:** etiquetas del sidebar en `astro.config.mjs` y nombres de fichero/URLs (`01-confianza-real/02-como-se-cuida`).

### Secciones obligatorias

**Índice de cada unidad** (`src/content/docs/NN-nombre.md`):

1. `<p><small>…</small></p>` + mapa: `> 🗺️ **El mapa:** 🤝 Tutoría → **AQUÍ ESTÁS** → …`
2. `## 🎯 Objetivo de la unidad`
3. `## 🗺️ Mapa de la unidad` — tabla que enlaza cada punto
4. `## 🎲 Actividades y juegos de la unidad` — enlaces `<a href>` a los puntos de práctica
5. `## 🚪 ¿Por dónde empiezo?`
6. Pie: `**📍 Primer punto:** […] · **⏭️ Al acabar, continúa en […](…)**`

### 📄 Formato de ficha (obligatorio — desde la reconversión)

> **Todo el contenido son FICHAS DE AULA**: hojas para trabajar en clase, no textos para leer en casa. Cada punto = 1 ficha imprimible de 1-2 A4. Explicación mínima + ejercicios para rellenar. Si un tema crece, se parte en dos fichas.

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
4. **1 imagen Excalidraw por ficha** en `public/img/NN-nombre/xx.svg` (+ `.png` de respaldo, fuente `.excalidraw` en `public/img/fuentes/`), insertada con `<div class="ficha-img">`.
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

### 🎁 Convenciones de Kudo Cards (unidad 9)

- **Solo comportamientos:** los kudos reconocen hechos observables (ayudar, incluir, esforzarse, defender sin insultar). **Nunca** apariencia física, notas, ni "eres el mejor de la clase".
- **Fórmula obligatoria:** concreto + comportamiento + impacto ("Gracias por X. Gracias a eso, Y"). Sin la línea de impacto es un cumplido, no un kudo.
- **Anónimo solo con tensión:** si el grupo tiene conflictos vivos o "uno contra el grupo", las tarjetas se firman anónimas; cuando el clima mejora, vuelve la firma.
- **Rotación:** ningún compañero recibe más de dos kudos por ronda; todos reciben al menos uno.
- **Cantidad libre:** nunca por turno obligatorio (mata la técnica); sí estreno colectivo inicial en la dinámica "Primer kudo de la clase".
- **Kudo hacia la profe:** válido y bienvenido (correo con la herramienta digital del punto 5).
- **Herramienta digital:** frontend puro (JS inline en la página `09-kudo-cards/05-tu-kudo-en-digital`), sin backend: mailto prellenado, copiar al portapapeles e imprimir. El correo del destinatario lo escribe el usuario.
- **Estructura de la unidad:** unidad única con 5 puntos (no dos unidades): guía + banco + herramienta juntos. Los puntos se mantienen largos y completos; no fragmentar en puntos cortos.

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
- [ ] Tutoría: ≥1 dinámica 🤝 + ≥1 😬 fail de DANI + soluciones en `<details>`
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
