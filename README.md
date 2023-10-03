<h1 align=center style="font-family: 'Times New Roman', sans-serif; text-decoration: underline; color: #3047cf">
Proyecto Individual Machine Learning Operations
</h1>
<h2 align=center style="font-family: 'Times New Roman', sans-serif; text-decoration: underline">
    <em>
        "Steam-MLOPS-4"
    </em> 
</h2>
<p align= center>
    <img src="./data/assets/mlops.png" height=100>
    <img src="./data/assets/steam-logo.png" height=100>
</p>
<h3 style="text-decoration: underline">
Contenido relevante del repositorio:
</h3>

<ul>
    <li>
        <a href="https://steam-4-api.onrender.com">
            API Deployada en Render
        </a>
    </li>
    <li>
        <a href="/Exploratory-Data-Analysis.ipynb">
            Análisis exploratorio de Datos
        </a>
    </li>
    <li>
        <a href="#uso">
            Uso
        </a>
    </li>
    <li>
        <a href="#instalacion">
            Instalación de las dependencias
        </a>
    </li>
    <li>
        <a href="#descripcion">
            Descripción del proyecto
        </a>
    </li>
    <li>
        <a href="#repo">
            Archivos
        </a>
    </li>
    <li>
        <a href="#contacto">
            Contacto
        </a>
    </li>
</ul>

<h3 id="#uso" style="text-decoration: underline">
    Uso
</h3>
<p>
    Para poder interactuar con los archivos del respositorio en tu entorno local, puedes clonar el repositorio desde una terminal que contenga <strong>GIT</strong> con el siguiente comando:
</p>

```
git clone https://github.com/Mariagustin-Prg/Steam-MLOPS-4.git
```

<p>
    En caso de no tener instalado <strong>GIT</strong> en su dispositivo, puede descargar el instalador desde el siguiente link: <em><a href="https://git-scm.com/downloads">git-scm.com</a></em>.
</p>

<h3 id="#instalacion" style="text-decoration: underline">
Instalación de las dependencias
</h3>

Para poder acceder y proceder a los archivos de la misma manera en la que se procedió en este proyecto, deberá tener las dependencias que están en <a href="/requirements.txt">requirements.txt</a> instaladas en el entorno en el que trabaje.
Puede acceder a estas dependencias de la siguiente manera en su terminal:

    pip install -r requirements.txt

<h3 id="#descripcion" style="text-decoration: underline">
Descripción del proyecto
</h3>
<p>
En este proyecto, se brindan archivos con contenido de Steam <em>(juegos, reseñas e items)</em>. En el rol de Data Engineer se hace la apertura inicial de los archivos en el <a href="/segmentacion_data.ipynb">segmentacion-data notebook</a> y se segmentan los datos en distintos archivos habiendo desanidado y transformado los archivos.

Luego, debido a la complejidad de las transformaciones necesarias para realizar las funciones, en el <a href="/test_functions.ipynb">test-functions notebook</a> se realizan las transformaciones para obtener fácilmente la información necesaria para poder consultar cada endpoint de la API y exportando los archivos a la carpeta <a href="./data/data_to_functions/">data_to_functions</a>.
</p>

<h3 style="text-decoration: underline">
Archivos
</h3>
<p>
El orden en el que se incluyeron al repositorio y con el cual, es recomendado proceder es:
<ul>
    <li><a href="segmentacion_data.ipynb">
    segmentacion_data.ipynb</a></li>
    <li><a href="/segmentacion_data.ipynb">segmentacion_items.ipynb</a></li>
    <li><a href="/create_NLP_sentiement_analysis.ipynb">create_NLP_sentiment_analysis</a></li>
    <li><a href="/test_functions.ipynb">test_functions.ipynb</a></li>
    <li><a href="/main.py">main.py</a></li>
    <li><a href="/Exploratory-Data-Analysis.ipynb">Exploratory-Data-Analysis.ipynb</a></li>
</ul>
</p>

<h3 style="text-decoration: underline">
Contacto
</h3>
<strong>GitHub</strong>: <a href="https://github.com/Mariagustin-Prg">Mariagustin-Prg</a>.

<strong>E-mail</strong>: <a href="marigustin.acosta1703@gmail.com">Enviar correo electrónico</a>.

<strong>LinkedIN</strong>: <a href="www.linkedin.com/in/mariano-agustín-acosta-chico-b67584266">Cuenta de Mariano Agustin</a>.
