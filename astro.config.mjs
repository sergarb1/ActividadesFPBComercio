import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// ============================================================
// Actividades FPB Comercio
// Actividades de aula para FPB Comercio (17 unidades y creciendo)
// IMPORTANTE: el sidebar solo puede enlazar páginas que existan.
// Al crear una unidad nueva, añadirla aquí ANTES de comprobar el build.
// ============================================================

// --- Actividades (se añaden poco a poco) ---
const contenidosItems = [
  {
    label: '12 · 📖 Leer y entender',
    collapsed: true,
    items: [
      { slug: '12-leer-y-entender', label: 'Índice' },
      { slug: '12-leer-y-entender/01-leer-no-es-ojear', label: '1 · Leer no es ojear' },
      { slug: '12-leer-y-entender/02-el-metodo-antes-de-subrayar', label: '2 · El método: leer antes de subrayar' },
      { slug: '12-leer-y-entender/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '13 · ✏️ Subrayado',
    collapsed: true,
    items: [
      { slug: '13-subrayado', label: 'Índice' },
      { slug: '13-subrayado/01-que-subrayar-y-que-no', label: '1 · Qué subrayar y qué no' },
      { slug: '13-subrayado/02-como-subrayar-de-verdad', label: '2 · Cómo subrayar de verdad' },
      { slug: '13-subrayado/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '14 · 🗂️ Esquemas y resúmenes',
    collapsed: true,
    items: [
      { slug: '14-esquemas-y-resumenes', label: 'Índice' },
      { slug: '14-esquemas-y-resumenes/01-de-subrayado-a-esquema', label: '1 · De subrayado a esquema' },
      { slug: '14-esquemas-y-resumenes/02-el-resumen-propio', label: '2 · El resumen propio' },
      { slug: '14-esquemas-y-resumenes/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '15 · 📄 Textos en papel',
    collapsed: true,
    items: [
      { slug: '15-textos-en-papel', label: 'Índice' },
      { slug: '15-textos-en-papel/01-marcar-sin-destrozar', label: '1 · Marcar sin destrozar' },
      { slug: '15-textos-en-papel/02-repaso-a-mano', label: '2 · Repaso a mano' },
      { slug: '15-textos-en-papel/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '16 · 🛒 El mostrador',
    collapsed: true,
    items: [
      { slug: '16-el-mostrador', label: 'Índice' },
      { slug: '16-el-mostrador/01-guion-de-los-5-pasos', label: '1 · El guion de los 5 pasos' },
      { slug: '16-el-mostrador/02-objeciones-y-clientes-dificiles', label: '2 · Objeciones y clientes difíciles' },
      { slug: '16-el-mostrador/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '17 · 💶 La caja y el cobro',
    collapsed: true,
    items: [
      { slug: '17-caja-y-cobro', label: 'Índice' },
      { slug: '17-caja-y-cobro/01-cobrar-sin-errores', label: '1 · Cobrar sin errores' },
      { slug: '17-caja-y-cobro/02-arqueo-de-caja', label: '2 · El arqueo de caja' },
      { slug: '17-caja-y-cobro/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
];

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
          label: '💻 Contenidos',
          items: contenidosItems,
        },
      ],
    }),
  ],
});
