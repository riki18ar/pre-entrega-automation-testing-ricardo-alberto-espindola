import pytest
import logging
import pathlib

@pytest.fixture(scope="session")
def api_url():
    return "https://jsonplaceholder.typicode.com"  # URL base para las peticiones HTTP de prueba



# def pytest_html_summers(prefix):
#     prefix.extend([
#         '<h2>MISION IMPOSIBLE CUMPLIDA</h2>',
#         '<div> style="background: gold"</div>'
#     ]
#         )


path_dir = pathlib.Path('logs')
path_dir.mkdir(exist_ok=True)


logging.basicConfig(
    filename = path_dir/ 'historial.log',
    level= logging.INFO,
    format= '%(asctime)s - %(levelname)s - %(message)s',
    datefmt= '%H:%M:%S'
)

logger = logging.getLogger()