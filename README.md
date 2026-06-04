
# Selenium Web Driver - Hands On (Python)

Proyecto de ejemplo para pruebas automatizadas con Selenium WebDriver en Python.

## Descripción

Pequeño proyecto de prueba que contiene una suite básica de tests para la página de login, usando Selenium para controlar el navegador y `pytest` para ejecutar los casos y generar reportes HTML.

## Requisitos

- Python 3.8+ instalado
- Un WebDriver compatible (ChromeDriver, geckodriver, etc.) disponible en el `PATH` o configurado en `utils/driver_factory.py`
- Dependencias del proyecto (ver sección Instalación)

## Instalación

1. Crear y activar un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias (si tienes un `requirements.txt`, úsalo; si no, instala `pytest` y `selenium`):

```bash
pip install -r requirements.txt || pip install pytest selenium
```

3. Asegúrate de que el WebDriver (por ejemplo `chromedriver`) esté en el `PATH` o configura la ruta en `utils/driver_factory.py`.

## Estructura del proyecto

- `pages/` - Page Objects (`base_page.py`, `login_page.py`)
- `utils/` - Utilidades (p. ej. `driver_factory.py`)
- `tests/` - Casos de prueba (`test_login.py`)
- `conftest.py` - Fixtures de pytest
- `pyproject.toml` - Metadatos del proyecto
- `report.html` - Reporte HTML generado por `pytest`

## Ejecutar los tests

Ejecuta el test de login y genera un reporte HTML con:

```bash
pytest tests/test_login.py --html=report.html
```

Al terminar, abre `report.html` en tu navegador para ver el reporte.

## Notas y consejos

- Si usas Chrome, descarga la versión de `chromedriver` que coincida con tu versión de Chrome.
- Para ejecutar todos los tests, simplemente ejecuta `pytest`.
- Si quieres ejecutar en modo headless, ajusta las opciones del navegador en `utils/driver_factory.py`.

## Contribuciones

Este es un proyecto de ejemplo; los PRs son bienvenidos. Para cambios mayores, abre un issue primero describiendo la propuesta.

## Licencia

Libre para uso educativo y de pruebas. Puedes añadir una licencia explícita si vas a publicar en un repositorio público.
