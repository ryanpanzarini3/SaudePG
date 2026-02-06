#!/usr/bin/env python3
"""
Script para gerar ícones PNG a partir do SVG do SaúdePG
Instale as dependências com: pip install cairosvg pillow
"""

import os
import sys
from pathlib import Path

try:
    import cairosvg
    from PIL import Image
    import io
except ImportError:
    print("⚠️  Dependências não encontradas.")
    print("Para gerar PNGs, execute: pip install cairosvg pillow")
    print("\n💡 Alternativa: Use um conversor online:")
    print("   - https://convertio.co/svg-png/")
    print("   - Tamanhos necessários: 192x192 e 512x512")
    sys.exit(1)

# SVG do ícone principal
SVG_CONTENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
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
</svg>"""

SVG_MASKABLE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
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
</svg>"""

def generate_icons():
    """Gera ícones PNG a partir dos SVGs"""
    images_dir = Path(__file__).parent / 'imagens'
    images_dir.mkdir(exist_ok=True)
    
    sizes = [192, 512]
    
    print("🎨 Gerando ícones PNG...")
    
    try:
        for size in sizes:
            # Ícone regular
            png_data = io.BytesIO()
            cairosvg.svg2png(bytestring=SVG_CONTENT.encode(), write_to=png_data, output_width=size, output_height=size)
            with open(images_dir / f'icon-{size}x{size}.png', 'wb') as f:
                f.write(png_data.getvalue())
            print(f"✅ icon-{size}x{size}.png criado")
            
            # Ícone maskable
            png_data = io.BytesIO()
            cairosvg.svg2png(bytestring=SVG_MASKABLE.encode(), write_to=png_data, output_width=size, output_height=size)
            with open(images_dir / f'icon-maskable-{size}x{size}.png', 'wb') as f:
                f.write(png_data.getvalue())
            print(f"✅ icon-maskable-{size}x{size}.png criado")
        
        print("\n✨ Todos os ícones foram gerados com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao gerar ícones: {e}")
        return False

if __name__ == '__main__':
    if not generate_icons():
        sys.exit(1)
