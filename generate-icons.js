#!/usr/bin/env node

/**
 * Script para gerar ícones PNG a partir do SVG do SaúdePG
 * Instale as dependências com: npm install sharp
 */

const fs = require('fs');
const path = require('path');

// SVG do ícone principal
const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="pinGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FF5B4D;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#E83E2B;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="circleGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#00D4FF;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0F6BFF;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <path d="M256 50 C180 50 120 110 120 186 C120 280 256 462 256 462 C256 462 392 280 392 186 C392 110 332 50 256 50 Z" fill="url(#pinGradient)" />
  <circle cx="256" cy="186" r="85" fill="url(#circleGradient)" />
  <g>
    <rect x="215" y="155" width="82" height="18" fill="#FF5B4D" rx="4" />
    <rect x="245" y="125" width="22" height="122" fill="#FF5B4D" rx="4" />
  </g>
</svg>`;

// SVG maskable (com espaçamento)
const svgMaskable = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="pinGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FF5B4D;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#E83E2B;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="circleGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#00D4FF;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0F6BFF;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <circle cx="256" cy="256" r="230" fill="white" opacity="0.1" />
  <path d="M256 80 C180 80 120 140 120 216 C120 310 256 492 256 492 C256 492 392 310 392 216 C392 140 332 80 256 80 Z" fill="url(#pinGradient)" />
  <circle cx="256" cy="216" r="85" fill="url(#circleGradient)" />
  <g>
    <rect x="215" y="185" width="82" height="18" fill="#FF5B4D" rx="4" />
    <rect x="245" y="155" width="22" height="122" fill="#FF5B4D" rx="4" />
  </g>
</svg>`;

try {
  // Tentar usar sharp se disponível
  const sharp = require('sharp');
  
  const imagesDir = path.join(__dirname, 'imagens');
  if (!fs.existsSync(imagesDir)) {
    fs.mkdirSync(imagesDir, { recursive: true });
  }

  console.log('🎨 Gerando ícones PNG...');

  const sizes = [192, 512];
  
  Promise.all([
    ...sizes.map(size =>
      sharp(Buffer.from(svg))
        .resize(size, size, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
        .png()
        .toFile(path.join(imagesDir, `icon-${size}x${size}.png`))
        .then(() => console.log(`✅ icon-${size}x${size}.png criado`))
    ),
    ...sizes.map(size =>
      sharp(Buffer.from(svgMaskable))
        .resize(size, size, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
        .png()
        .toFile(path.join(imagesDir, `icon-maskable-${size}x${size}.png`))
        .then(() => console.log(`✅ icon-maskable-${size}x${size}.png criado`))
    )
  ]).then(() => {
    console.log('\n✨ Todos os ícones foram gerados com sucesso!');
  }).catch(err => {
    console.error('❌ Erro:', err.message);
    process.exit(1);
  });

} catch (e) {
  console.log('⚠️  Sharp não está instalado.');
  console.log('Para gerar PNGs, execute: npm install sharp');
  console.log('\n💡 Alternativa: Use um conversor online:');
  console.log('   - https://convertio.co/svg-png/');
  console.log('   - Tamanhos necessários: 192x192 e 512x512');
}
