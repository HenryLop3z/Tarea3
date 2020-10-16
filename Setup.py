# archivo setup

from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()


setup(
    # Con esta linea se instala el paquete
    # $ pip3 install git+https://github.com/HenryLop3z/Tarea3

    name='Tarea3DonatoLeeLopezRamirez',  # Nombre del proyecto
    version='1.0.0',  # Versión del programa
    description='Paquete para la tarea 3',  # Descripción breve
    url='git@github.com:HenryLop3z/Tarea3.git',  # Enlace al proyecto
    author='DonatoLeeLopezRamirez',  # Autor
    author_email='henrylopez@estudiantec.cr',
    license='unlicense',
    package_dir={'T3_pkg': 'T3_pkg'},  # especifica el directorio de los paquetes
    packages=['T3_pkg'],  # Encuentra los paquetes necesarios
    install_requires=['Pillow', 'tabulate', 'playsound', 'argparse'],  # Instala las librerias necesarias
    python_requires='>=3.3',  # Versión de Python compatible
    package_data={  # Archivos extras a los paquetes
        'T3_pkg': ['meca.jpg', 'Texto_ejemplo.txt', 'Hello.mp3'],
    },
    scripts=['T3_pkg/lector_texto.py', 'T3_pkg/presentador_de_audio.py', 'T3_pkg/Presentador_de_imágenes.py'] 
)
