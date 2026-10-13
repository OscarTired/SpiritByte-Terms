# SpiritByte · Privacidad y términos

Web estática en **español e inglés** para SpiritByte Android. Responsable: **Octa_Dev**. Contacto público: **oscar@octa-dev.com**.

No necesita instalar dependencias ni compilar. Los documentos se entregan completos en HTML y siguen disponibles sin JavaScript. Las rutas relativas funcionan tanto en un dominio propio como en un repositorio de GitHub Pages.

## Páginas

- `index.html`: portada y acceso a los documentos.
- `privacy.html`: política de privacidad para el campo de Google Play.
- `terms.html`: términos y condiciones de uso.
- `en/index.html`, `en/privacy.html` y `en/terms.html`: versiones completas en inglés.
- `assets/`: zorro, fuente local y licencias.
- `content/es.json` y `content/en.json`: textos editables de ambos idiomas.
- `scripts/build.py`: generador compartido de las seis páginas, sin dependencias externas.

El selector **Español / English** conserva el documento actual. Si JavaScript está disponible, también conserva la sección enlazada. El idioma se identifica en `html lang`, enlaces `hreflang`, metadatos, navegación y controles. No se utilizan redirecciones automáticas según el navegador: cada URL entrega su idioma completo sin JavaScript.

La web no incluye analítica, anuncios, formularios ni cookies propias. JavaScript solo añade el selector de las cinco paletas de la app y el botón de impresión. El navegador recuerda la paleta mediante localStorage; esto se explica en la política.

## Publicar con GitHub Pages

1. Crea tu repositorio y sube estos archivos, incluida la carpeta `.github`.
2. En GitHub, abre **Settings → Pages → Build and deployment → Source** y elige **GitHub Actions**.
3. Sube los archivos a `main` o `master`. Si los subiste antes de activar Pages, abre **Actions → Publish to GitHub Pages → Run workflow**.
4. Espera a que el workflow termine correctamente. GitHub mostrará la URL publicada en **Settings → Pages** y en el entorno **github-pages**.
5. Comprueba la URL en una ventana privada, sin iniciar sesión. La política debe ser accesible públicamente.

Repositorio: [OscarTired/SpiritByte-Terms](https://github.com/OscarTired/SpiritByte-Terms). Con GitHub Pages activado, las URLs previstas son:

```text
https://oscartired.github.io/SpiritByte-Terms/privacy.html
https://oscartired.github.io/SpiritByte-Terms/en/privacy.html
https://oscartired.github.io/SpiritByte-Terms/terms.html
https://oscartired.github.io/SpiritByte-Terms/en/terms.html
```

Usa la URL de **privacy.html** en Play Console → Contenido de la aplicación → Política de privacidad. El nombre de desarrollador de la ficha debe corresponder con el responsable indicado aquí.

También puedes publicar desde **Deploy from a branch → main → /(root)** porque el sitio ya está compilado. En ese caso, elimina el workflow antes de subirlo para no ejecutar dos métodos de publicación. Con GitHub Free, utiliza un repositorio público.

Documentación oficial: [workflows de GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Vista previa local

Puedes abrir `index.html` directamente. Para una vista por HTTP, desde esta carpeta ejecuta:

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

Abre `http://127.0.0.1:4173/` y detén el servidor con Ctrl+C.

## Antes de enviar la app a revisión

- Añade una opción de **Política de privacidad** en SpiritByte Android que muestre el texto o abra la URL pública. Crear esta web no modifica la app ni incorpora automáticamente el enlace.
- Confirma que el correo público recibe mensajes y que las prácticas de soporte siguen lo descrito.
- Completa Seguridad de los datos de Play Console conforme al binario y los SDK que realmente publiques. Procesar datos solo en el dispositivo y exportar un archivo a petición del usuario debe distinguirse de enviarlos al desarrollador.
- Revisa el público objetivo que declararás. El apartado sobre menores no sustituye los requisitos de Google para aplicaciones dirigidas a niños.
- Revisa también el AAB de publicación, su firma, API objetivo y compatibilidad de bibliotecas nativas. Esta web atiende la documentación de privacidad, no el resto de los requisitos técnicos de publicación.

Los textos reflejan el código local revisado el 13 de octubre de 2026: Android sin permiso de Internet, sin SDK de analítica o anuncios, bóveda y respaldo cifrados con Argon2id/XChaCha20-Poly1305, bloqueo local, exportación manual y copia de la frase de recuperación al portapapeles.

Referencias oficiales: [Datos de usuario de Google Play](https://support.google.com/googleplay/android-developer/answer/10144311?hl=es), [Seguridad de los datos](https://support.google.com/googleplay/android-developer/answer/10787469?hl=es), [privacidad de GitHub](https://docs.github.com/es/site-policy/privacy-policies/github-general-privacy-statement).

## Mantenimiento

Edita los textos en `content/es.json` y `content/en.json` cuando cambien las funciones, los datos, el responsable o el contacto. Mantén equivalentes las dos versiones. Después regenera el HTML:

```powershell
python scripts/build.py
python scripts/build.py --check
```

Sube tanto las fuentes como los seis HTML regenerados. El workflow comprueba que coincidan y que los enlaces y anclas locales existan antes de publicar. No edites únicamente el HTML generado, porque la siguiente generación reemplazaría esa edición.

Actualiza también la fecha del documento: el texto está en los JSON y la fecha ISO en `scripts/build.py`. Si cambias el proveedor de alojamiento, actualiza el apartado de privacidad del sitio. Si cambias el dominio, actualiza `BASE` en el generador y vuelve a generar para corregir los enlaces canónicos y alternativos. Conserva las rutas públicas para que el enlace de Google Play siga funcionando.

Las licencias de la fuente Geist Pixel y del software SpiritByte están en `assets/Geist-OFL.txt` y `assets/SpiritByte-MIT.txt`. El zorro procede del repositorio de la aplicación. Las capturas de verificación y las herramientas temporales no se publican.
