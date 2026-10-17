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
    label: '01 · 🛒 El mostrador',
    collapsed: true,
    items: [
      { slug: '01-el-mostrador', label: 'Índice' },
      { slug: '01-el-mostrador/01-guion-de-los-5-pasos', label: '1 · El guion de los 5 pasos' },
      { slug: '01-el-mostrador/02-objeciones-y-clientes-dificiles', label: '2 · Objeciones y clientes difíciles' },
      { slug: '01-el-mostrador/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '02 · 💶 La caja y el cobro',
    collapsed: true,
    items: [
      { slug: '02-caja-y-cobro', label: 'Índice' },
      { slug: '02-caja-y-cobro/01-cobrar-sin-errores', label: '1 · Cobrar sin errores' },
      { slug: '02-caja-y-cobro/02-arqueo-de-caja', label: '2 · El arqueo de caja' },
      { slug: '02-caja-y-cobro/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '03 · 🗃️ Reposición y almacén',
    collapsed: true,
    items: [
      { slug: '03-reposicion-y-almacen', label: 'Índice' },
      { slug: '03-reposicion-y-almacen/01-recibir-la-mercancia', label: '1 · Recibir la mercancía' },
      { slug: '03-reposicion-y-almacen/02-colocar-por-familias', label: '2 · Colocar por familias' },
      { slug: '03-reposicion-y-almacen/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '04 · 🧮 Inventario y stock',
    collapsed: true,
    items: [
      { slug: '04-inventario-y-stock', label: 'Índice' },
      { slug: '04-inventario-y-stock/01-contar-y-registrar', label: '1 · Contar y registrar' },
      { slug: '04-inventario-y-stock/02-stock-minimo-y-pedido', label: '2 · Stock mínimo y pedido' },
      { slug: '04-inventario-y-stock/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '05 · 🪟 El escaparate',
    collapsed: true,
    items: [
      { slug: '05-el-escaparate', label: 'Índice' },
      { slug: '05-el-escaparate/01-la-idea-y-los-3-niveles', label: '1 · La idea y los 3 niveles' },
      { slug: '05-el-escaparate/02-vestir-y-renovar', label: '2 · Vestir y renovar' },
      { slug: '05-el-escaparate/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '06 · 🔄 Devoluciones y reclamaciones',
    collapsed: true,
    items: [
      { slug: '06-devoluciones-y-reclamaciones', label: 'Índice' },
      { slug: '06-devoluciones-y-reclamaciones/01-la-devolucion-correcta', label: '1 · La devolución correcta' },
      { slug: '06-devoluciones-y-reclamaciones/02-la-hoja-de-reclamaciones', label: '2 · La hoja de reclamaciones' },
      { slug: '06-devoluciones-y-reclamaciones/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '07 · 📖 Leer y entender',
    collapsed: true,
    items: [
      { slug: '07-leer-y-entender', label: 'Índice' },
      { slug: '07-leer-y-entender/01-leer-no-es-ojear', label: '1 · Leer no es ojear' },
      { slug: '07-leer-y-entender/02-el-metodo-antes-de-subrayar', label: '2 · El método: leer antes de subrayar' },
      { slug: '07-leer-y-entender/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '08 · ✏️ Subrayado',
    collapsed: true,
    items: [
      { slug: '08-subrayado', label: 'Índice' },
      { slug: '08-subrayado/01-que-subrayar-y-que-no', label: '1 · Qué subrayar y qué no' },
      { slug: '08-subrayado/02-como-subrayar-de-verdad', label: '2 · Cómo subrayar de verdad' },
      { slug: '08-subrayado/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '09 · 🗂️ Esquemas y resúmenes',
    collapsed: true,
    items: [
      { slug: '09-esquemas-y-resumenes', label: 'Índice' },
      { slug: '09-esquemas-y-resumenes/01-de-subrayado-a-esquema', label: '1 · De subrayado a esquema' },
      { slug: '09-esquemas-y-resumenes/02-el-resumen-propio', label: '2 · El resumen propio' },
      { slug: '09-esquemas-y-resumenes/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
    ],
  },
  {
    label: '10 · 📄 Textos en papel',
    collapsed: true,
    items: [
      { slug: '10-textos-en-papel', label: 'Índice' },
      { slug: '10-textos-en-papel/01-marcar-sin-destrozar', label: '1 · Marcar sin destrozar' },
      { slug: '10-textos-en-papel/02-repaso-a-mano', label: '2 · Repaso a mano' },
      { slug: '10-textos-en-papel/03-juegos-y-retos', label: '3 · 🎮 Juegos y retos' },
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
