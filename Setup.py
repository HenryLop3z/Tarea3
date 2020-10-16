# archivo setup

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


setup(
    # Con esta linea se instala el programa
    # $ pip3 install git+https://github.com/HenryLop3z/Tarea3

    name='Tarea3DonatoLeeLopezRamirez',  # Nombre del proyecto
    version='1.0.0',  # Versión del programa
    description='Paquete para la tarea 3',
    url='git@github.com:HenryLop3z/Tarea3.git',  # Enlace al proyecto
    author='DonatoLeeLopezRamirez',
    author_email='henrylopez@estudiantec.cr',
    license='unlicense',
    package_dir={'':'T3_pkg'},  # especifica el directorio de los paquetes
    packages=['T3_pkg'],  # Encuentra los paquetes necesarios
    install_requires=['Pillow', 'tabulate', 'playsound', 'argparse'],  # Instala las librerias necesarias
    python_requires='>=3.3',  # Versión de Python compatible
    package_data={  # Archivos
        'T3_pkg': ['meca.jpg'],
    },
    # entry_points={  # crea a los scripts del proyecto
    #     'console_scripts': [
    #         'texto=texto:lector_texto',
    #         'audio=audio:presentador_de_audio',
    #         'imagen=imagen:Presentador_de_imágenes',
    #     ],
    # },

)
