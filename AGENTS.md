# AGENTS.md — Guía para LLMs sobre el proyecto Actividades FPB Comercio

Este archivo ayuda a cualquier agente LLM (opencode, Claude, ChatGPT, etc.) a entender la estructura y convenciones del proyecto y a trabajar de forma efectiva.

---

## 📋 Descripción del proyecto

Web de **actividades para la FPB de Comercio** (alumnado de 16-17 años) en dos grandes secciones:

- 🤝 **Sección 1 · Tutoría — Modo coop**: unidades de convivencia para las tutorías (12 unidades).
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
- **Sin PDF/EPUB ni diagramas Excalidraw por ahora** (tablas, listas y emojis cubren la necesidad visual)

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

## 📚 Temario completo (35 unidades pequeñas)

Filosofía: **unidades pequeñas** (índice + 2-4 puntos). Cada tema del encargo es su propia unidad. **NO hay bloque de Aules** (decisión del usuario: eliminado).

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
| 9 | 🎁 Kudo Cards | `09-kudo-cards` | Tarjetas de agradecimiento (Management 3.0): qué son y por qué funcionan, Kudo Box vs Kudo Wall, las 6 reglas de oro, cómo escribir un kudo |
| 10 | 🖨️ Banco de Kudo Cards | `10-banco-de-kudo-cards` | +50 tarjetas listas para imprimir en 8 categorías, plantillas en blanco y herramienta digital de envío (mailto + copiar + imprimir) |
| 11 | 🎙️ Tu sesión en 50 minutos | `11-tu-sesion-en-50-minutos` | Guión de tutoría (tema libre: dinámicas, música, baile, deporte…) con título, objetivo, intro para compañeros, paso a paso, material y conclusiones. En Aules o en papel |
| 12 | 📆 Turnos del aula | `12-turnos-del-aula` | Lista de responsables diarios: plantilla para imprimir y firmar |

### 💻 Sección 2 · Contenidos

> Renumeradas +2 tras la inserción de Kudo Cards (antes eran 11-33; ahora 13-35).

#### 🧠 Estudiar sin sufrir

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 13 | 📖 Leer y entender | `13-leer-y-entender` | Lectura comprensiona del temario antes de subrayar |
| 14 | ✏️ Subrayado | `14-subrayado` | Qué subrayar, con qué, y el subrayado que no sirve |
| 15 | 🗂️ Esquemas y resúmenes | `15-esquemas-y-resumenes` | Mapas mentales, esquemas de flechas, resumen propio |
| 16 | 📄 Textos en papel | `16-textos-en-papel` | Trabajar el temario impreso: marcadores, post-its, repaso manuscrito |
| 17 | 🧠 Memorizar de verdad | `17-memorizar-de-verdad` | Leer, copiar, grabarse y decir en voz alta la lección |
| 18 | ✅ Examen en blanco | `18-examen-en-blanco` | Practicar autoevaluación sin apuntes |
| 19 | 🤖 IA: copiloto de estudio | `19-ia-copiloto-de-estudio` | IA para dudas, entender y memorizar con ejemplos reales; NO copiar y pegar |

#### 🎨 Modo creativo

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 20 | 🎤 Monta tu presentación | `20-monta-tu-presentacion` | Buscar → recopilar → seleccionar → crear presentación propia |
| 21 | 💡 Creatividad | `21-creatividad` | Qué es, cómo se estimula, actividades |
| 22 | 🔍 Webgrafía | `22-webgrafia` | Qué es, fiabilidad de fuentes, cómo se elabora |
| 23 | 🖼️ Bancos de imágenes libres | `23-bancos-de-imagenes-libres` | Pexels, Unsplash, Pixabay… |
| 24 | ⚖️ Copyright | `24-copyright` | Qué es, licencias CC, uso educativo |

#### 💬 Hablar y escribir como un pro

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 25 | 📧 Correos que funcionan | `25-correos-que-funcionan` | Enviar correos bien escritos |
| 26 | ↩️ Responder sin quemarse | `26-responder-sin-quemarse` | Responder, también al cliente enfadado |
| 27 | 🆘 Incidencias de clientes | `27-incidencias-de-clientes` | Presencial, correo y redes sociales + guión de tarea |
| 28 | 📰 Noticias de actualidad | `28-noticias-de-actualidad` | Guión tarea: recopilar, seleccionar y comentar noticias de comercio |
| 29 | 🎬 Vídeos motivacionales | `29-videos-motivacionales` | Banco de enlaces + guión de visionado (comercio/MK, informática, IA, desarrollo personal, habilidades sociales). Sin incrustar |
| 30 | 🤖 IA informática | `30-ia-informatica` | Qué es la IA, herramientas, aplicaciones prácticas |

#### 💶 Dinero, nóminas y curro (IPE II)

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 31 | 📑 El contrato de trabajo | `31-el-contrato-de-trabajo` | Tipos, partes, derechos. El módulo se llama **IPE II** (no expandir) |
| 32 | 💰 Salario y nómina | `32-salario-y-nomina` | Partes de una nómina, bruto vs neto |
| 33 | 📊 IRPF y cultura económica | `33-irpf-y-cultura-economica` | Impuestos básicos, cultura económica |
| 34 | 🔭 Con y sin graduado | `34-con-y-sin-graduado` | Oportunidades laborales comparadas |

#### 🏪 Proyecto almacén (OAA)

| # | Unidad | Slug | Contenido |
|---|---|---|---|
| 35 | 🏪 Guión del proyecto de almacén | `35-guion-proyecto-almacen` | Guión del proyecto. El proyecto/módulo se llama **OAA** (no expandir) |

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

**Plantilla de cada punto:**

1. Frontmatter + `<p><small>…</small></p>` + breadcrumb `> 🗺️ **Estás en:** 🤝 **Nombre de la unidad** → N · Título`
2. `## 📬 En corto` — idea en una frase
3. Desarrollo con `##` temáticos
4. Cierre: `## 🧠 Mini-chequeo` (2-3 preguntas), `## ✅ Resumen en 3 frases`, `## 🐛 Vocabulario rápido`
5. Pie: `📚 [Volver al índice…] · **Anterior:** […] · **Siguiente:** […]`

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

### 🎁 Convenciones de Kudo Cards (unidades 9 y 10)

- **Solo comportamientos:** los kudos reconocen hechos observables (ayudar, incluir, esforzarse, defender sin insultar). **Nunca** apariencia física, notas, ni "eres el mejor de la clase".
- **Fórmula obligatoria:** concreto + comportamiento + impacto ("Gracias por X. Gracias a eso, Y"). Sin la línea de impacto es un cumplido, no un kudo.
- **Anónimo solo con tensión:** si el grupo tiene conflictos vivos o "uno contra el grupo", las tarjetas se firman anónimas; cuando el clima mejora, vuelve la firma.
- **Rotación:** ningún compañero recibe más de dos kudos por ronda; todos reciben al menos uno.
- **Cantidad libre:** nunca por turno obligatorio (mata la técnica); sí estreno colectivo inicial en la dinámica "Primer kudo de la clase".
- **Kudo hacia la profe:** válido y bienvenido (correo con la herramienta digital del punto 4 del banco).
- **Herramienta digital:** frontend puro (JS inline en la página `04-tu-kudo-en-digital`), sin backend: mailto prellenado, copiar al portapapeles e imprimir. El correo del destinatario lo escribe el usuario.

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

Las unidades de guiones y turnos (`09-tu-sesion-en-50-minutos`, `10-turnos-del-aula`) se pensan para imprimir: instrucciones de impresión en la propia página; `custom.css` ya tiene `@media print`.

---

## 🚀 Comandos

```bash
npm run dev       # Servidor local → http://localhost:4321
npm run build     # Build estático → dist/
npm run preview   # Previsualizar build
npm run docx      # DOCX por unidad → docx/ (requiere Pandoc en PATH)
```

---

## 🧪 Checklist para nueva unidad

- [ ] Frontmatter (title, description con emoji)
- [ ] Sin números de unidad en prosa ni títulos
- [ ] Índice: objetivo, mapa (tabla), actividades, ¿por dónde empiezo?, pie
- [ ] Cada punto: 📬 En corto, desarrollo, mini-chequeo, resumen en 3 frases, vocabulario, pie Anterior/Siguiente
- [ ] Tutoría: ≥1 dinámica 🤝 + ≥1 😬 fail de DANI + soluciones en `<details>`
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
