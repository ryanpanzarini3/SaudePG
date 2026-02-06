@echo off
REM Script para gerar ícones PNG do SaúdePG
REM Requer ImageMagick ou conversor online

echo 🎨 Gerando ícones PNG...
echo.
echo Opção 1: Usando conversor online
echo   1. Visite: https://convertio.co/svg-png/
echo   2. Upload do arquivo: imagens/icon.svg
echo   3. Configuração:
echo      - Tamanho 1: 192x192 (salve como icon-192x192.png)
echo      - Tamanho 2: 512x512 (salve como icon-512x512.png)
echo   4. Repita para: icon-maskable-192x192.png e icon-maskable-512x512.png
echo.
echo Opção 2: Usando ImageMagick (se instalado)
echo   magick convert -resize 192x192 imagens/icon.svg imagens/icon-192x192.png
echo   magick convert -resize 512x512 imagens/icon.svg imagens/icon-512x512.png
echo.
pause
