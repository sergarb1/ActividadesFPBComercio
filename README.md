# Actividades FPB Comercio

> **Juegos, dinámicas y fichas para la FPB de Comercio.**
> Sección Tutoría (Modo coop: la clase que funciona) + Sección Contenidos (estudio, creatividad, comunicación, economía). CC BY-SA 4.0 — [Sergi Garcia Barea](https://github.com/sergarb1)

---

## 🌐 Web

**🧭 [https://sergarb1.github.io/ActividadesFPBComercio/](https://sergarb1.github.io/ActividadesFPBComercio/)**

---

## 🎯 Misión

Que la clase funcione: actividades cooperativas para mejorar el clima del aula (autoestima, empatía, compañerismo, respeto y cero bullying), y destrezas para aprobar y trabajar. **Sin sermones, sin juegos que expongan a nadie.**

---

## 🗂️ Estructura

| Sección | Unidades |
|---|---|
| 🤝 **Tutoría — Modo coop** | Confianza real · Ponte en su sitio · Modo equipo · Líneas rojas · El insulto no es poder · Decirlo sin liarla · Conflicto: modo sabio · Banco de juegos · Tu sesión en 50 minutos · Turnos del aula |
| 💻 **Contenidos** | Estudiar sin sufrir (leer, subrayar, esquemas, papel, memorizar, examen en blanco, IA copiloto) · Modo creativo (monta tu presentación, creatividad, webgrafía, imágenes, copyright) · Hablar y escribir como un pro (correos, incidencias, noticias, vídeos, IA) · Dinero, nóminas y curro (IPE II) · Proyecto almacén (OAA) · 🏆 Especial: El torneo del taller |

*(Progresivamente se irá publicando; el AGENTS.md detalla el temario completo de 33 unidades.)*

---

## 🧑‍🤝‍🧑 Personajes

- **ROSA** — 20 años de tienda, lo ha visto todo. Sarcasmo, pero siempre acierta.
- **DANI** — el nuevo dependiente que mete la pata. El fail siempre es suyo: aprendemos riendo del error, **nunca de un compañero**.

---

## 🛠️ Stack

| Capa | Tecnología |
|---|---|
| Framework | Astro 7 + Starlight 0.41 |
| Tema | Azul #2563eb + teal #4ecdc4 + glassmorphism |
| Fuente | Geist Sans |
| Idioma | Castellano (es-ES) |
| Despliegue | GitHub Actions → GitHub Pages |

---

## 🚀 Uso

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # build estático → dist/
npm run preview  # previsualizar build
npm run docx     # DOCX por unidad → docx/ (requiere Pandoc CLI)
```

---

## 📄 Exportación DOCX

| Formato | Cómo generarlo | Uso |
|---|---|---|
| **DOCX** | `npm run docx` | 1 `.docx` por unidad (índice + puntos) → `docx/<unidad>/` — para imprimir o editar en Word |

---

## 📄 Licencia

**CC BY-SA 4.0** — Puedes compartir y adaptar el material (incluso comercialmente) reconociendo la autoría y compartiendo las modificaciones bajo la misma licencia.
