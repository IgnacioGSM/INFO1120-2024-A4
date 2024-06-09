# Programación I
## Evaluación 2
Este proyecto consiste en generar de forma automática contratos con una plantilla preestablecida y una base de datos definida, además de poder visualizar ciertos gráficos relacionados a los datos.

## Programas necesarios
Para ejecutar este proyecto se necesita tener instalado:

- Python
-- pandas
-- python-docx
-- matplotlib
- Sqlite3

## Ejecución
Para la generación de contratos se usa el archivo **main.py**, una vez que ya esté en ejecución puede escoger entre generar uno o múltiples contratos (si escoge múltiples contratos de igual manera podrá generar un solo contrato).

Al elegir generar un solo contrato, puede seleccionar a la persona en base a su rut o su nombre completo, ya que estos datos son propios de cada uno y no se repetirán en otras personas. Para escoger a la persona debe ingresar el índice (ubicado a la izquierda del rut/nombre) correspondiente a la persona.

Al elegir generar múltiples contratos se dejará escoger algún dato en común que compartan las personas (nacionalidad, profesión o rol). Una vez escogido un criterio, se mostrará una tabla con todas las personas que cumplan con el criterio elegido y se le pedirá al usuario ingresar el rango de los índices a los que desea generar un contrato.

## Gráficos
El proyecto cuenta con tres gráficos.
- **promedio_sueldos.py** muestra un gráfico de barras con el promedio de los sueldos de cada profesión.
- **distribucion_profesiones.py** muestra un gráfico de tarta con la cantidad de personas para cada profesión.
- **distribucion_nacionalidades.py** muestra un gráfico de barras con la cantidad de personas de cada nacionalidad.