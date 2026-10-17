import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// ============================================================
// Actividades FPB Comercio
// Sección 1: 🤝 Tutoría (Modo coop) — unidades 01-12
// Sección 2: 💻 Contenidos — unidades 13-35 (se añaden poco a poco)
// IMPORTANTE: el sidebar solo puede enlazar páginas que existan.
// Al crear una unidad nueva, añadirla aquí ANTES de comprobar el build.
// ============================================================

// --- Sección 1 · Tutoría (unidades creadas; añadir las nuevas aquí) ---
const tutoriaItems = [
  {
    label: '1 · 🌱 Confianza real',
    collapsed: true,
    items: [
      { slug: '01-confianza-real', label: 'Índice' },
      { slug: '01-confianza-real/01-que-es-la-confianza-real', label: '1 · Qué es la confianza real' },
      { slug: '01-confianza-real/02-como-se-cuida', label: '2 · Cómo se cuida' },
      { slug: '01-confianza-real/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '2 · 🎭 Ponte en su sitio',
    collapsed: true,
    items: [
      { slug: '02-ponte-en-su-sitio', label: 'Índice' },
      { slug: '02-ponte-en-su-sitio/01-que-es-la-empatia', label: '1 · Qué es la empatía' },
      { slug: '02-ponte-en-su-sitio/02-como-practicarla', label: '2 · Cómo se practica' },
      { slug: '02-ponte-en-su-sitio/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '3 · 🧩 Modo equipo',
    collapsed: true,
    items: [
      { slug: '03-modo-equipo', label: 'Índice' },
      { slug: '03-modo-equipo/01-companerismo', label: '1 · Qué es el compañerismo' },
      { slug: '03-modo-equipo/02-gestos-que-se-notan', label: '2 · Gestos que se notan' },
      { slug: '03-modo-equipo/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  // 4 · 🛡️ Líneas rojas (en preparación)
  // 5 · 🔓 El insulto no es poder (en preparación)
  // 6 · 🗣️ Decirlo sin liarla (en preparación)
  // 7 · ⚖️ Conflicto: modo sabio (en preparación)
  // 8 · 🎲 Banco de juegos (en preparación)
  {
    label: '9 · 🎁 Kudo Cards',
    collapsed: true,
    items: [
      { slug: '09-kudo-cards', label: 'Índice' },
      { slug: '09-kudo-cards/01-que-son-y-por-que-funcionan', label: '1 · Qué son y por qué funcionan' },
      { slug: '09-kudo-cards/02-caja-o-mural', label: '2 · La caja o el mural' },
      { slug: '09-kudo-cards/03-las-6-reglas-de-oro', label: '3 · Las 6 reglas de oro' },
      { slug: '09-kudo-cards/04-como-escribir-un-kudo', label: '4 · Cómo escribir un kudo' },
    ],
  },
  {
    label: '10 · 🖨️ Banco de Kudo Cards',
    collapsed: true,
    items: [
      { slug: '10-banco-de-kudo-cards', label: 'Índice' },
      { slug: '10-banco-de-kudo-cards/01-como-usar-el-banco', label: '1 · Cómo usar el banco' },
      { slug: '10-banco-de-kudo-cards/02-tarjetas-listas', label: '2 · 🖨️ Tarjetas listas' },
      { slug: '10-banco-de-kudo-cards/03-plantillas-en-blanco', label: '3 · Plantillas en blanco' },
      { slug: '10-banco-de-kudo-cards/04-tu-kudo-en-digital', label: '4 · 📧 Tu kudo en digital' },
    ],
  },
  // 11 · 🎙️ Tu sesión en 50 minutos (en preparación)
  // 12 · 📆 Turnos del aula (en preparación)
];

// --- Sección 2 · Contenidos (unidades 13-35, se añaden poco a poco) ---
// const contenidosItems = [ … ];

export default defineConfig({
  site: 'https://sergarb1.github.io/ActividadesFPBComercio',
  base: '/ActividadesFPBComercio',
  integrations: [
    starlight({
      title: 'Actividades FPB Comercio',
      description:
        'Juegos, dinámicas y fichas para la FPB de Comercio — Modo coop para la tutoría y destrezas para aprobar. CC BY-SA 4.0 — Sergi Garcia Barea',
      customCss: ['./src/styles/custom.css', '@fontsource/geist-sans'],
      locales: {
        root: { label: 'Castellano', lang: 'es' },
      },
      defaultLocale: 'root',
      tableOfContents: false,
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/sergarb1/ActividadesFPBComercio' },
      ],
      head: [
        { tag: 'meta', attrs: { name: 'theme-color', content: '#2563eb' } },
        { tag: 'link', attrs: { rel: 'icon', type: 'image/svg+xml', href: '/ActividadesFPBComercio/favicon.svg' } },
      ],
      sidebar: [
        { slug: 'index', label: 'Inicio' },
        {
          label: '🤝 Tutoría — Modo coop',
          items: tutoriaItems,
        },
        // {
        //   label: '💻 Contenidos',
        //   items: contenidosItems,
        // },
      ],
    }),
  ],
});
