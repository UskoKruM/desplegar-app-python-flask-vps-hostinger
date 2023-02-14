# Python: Inserción masiva de datos (en MySQL) con Python

Aprende a realizar inserciones masivas en una base de datos MySQL usando un script de Python, de una forma fácil, ordenada y funcional. Cónoce cómo generar datos de prueba, aleatorios y estructurados para registrarlos de forma masiva en una tabla perteneciente a una base de datos MySQL.

<hr/>

Actualizar los paquetes de Ubuntu:

#### `sudo apt update`
#### `sudo apt upgrade`

Instalar Apache2 (si no está instalado) y el paquete 'libapache2-mod-wsgi-py3':

#### `sudo apt install apache2`
#### `sudo apt install libapache2-mod-wsgi-py3`

Comprobar la versión de Python instalada:

#### `python3 --version`

Instalar Python (si no está instalado) y PIP (Package Installer for Python):

#### `sudo apt install python3`
#### `sudo apt install python3-pip`

Listar los paquetes instalados:

#### `pip3 list`

Instalar Flask de forma global:

#### `sudo pip3 install flask`

Crear carpeta (dentro de nuestro VPS) para los archivos de nuestro proyecto:

#### `cd /var/www/html`
#### `sudo mkdir flask_project`

Acceder a la carpeta 'sites-enabled' (de Apache) y eliminar el archivo '000-default.conf':

#### `cd /etc/apache2/sites-enabled`
#### `sudo rm 000-default.conf`

Copiar los archivos 'app.py' y 'app.wsgi' hacia la carpeta 'flask_project' creada dentro de nuestro VPS:

#### `pscp <directorio_de_tu_pc>\app.py root@<ip_vps>:/var/www/html/flask_project`

#### `pscp <directorio_de_tu_pc>\app.wsgi root@<ip_vps>:/var/www/html/flask_project`

Copiar el archivo '000-default.conf' a la carpeta 'etc/apache2/sites-enabled':

#### `pscp <directorio_de_tu_pc>\000-default.conf root@<ip_vps>:/etc/apache2/sites-enabled`

Reiniciar el servicio de Apache2:

#### `sudo service apache2 restart`

<hr/>

![](./preview1.png)
<br/><br/>
![](./preview2.PNG)
<br/><br/>
![](./preview3.PNG)

# 🌍 Por si deseas contactarme 👨‍💻 :

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Oscar_Garcia-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://pe.linkedin.com/in/uskokrum2010)
[![YouTube](https://img.shields.io/badge/YouTube-UskoKruM2010-FF0000?style=for-the-badge&logo=youtube&logoColor=white&labelColor=101010)](https://youtube.com/uskokrum2010)
[![Twitter](https://img.shields.io/badge/Twitter-@uskokrum2010-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white&labelColor=101010)](https://twitter.com/uskokrum2010)
[![Instagram](https://img.shields.io/badge/Instagram-@uskokrum2010-E4405F?style=for-the-badge&logo=instagram&logoColor=white&labelColor=101010)](https://instagram.com/uskokrum2010)
[![Facebook](https://img.shields.io/badge/Facebook-@uskokrum2010-1877F2?style=for-the-badge&logo=facebook&logoColor=white&labelColor=101010)](https://facebook.com/uskokrum2010)
[![Udemy](https://img.shields.io/badge/Udemy-Oscar_Garcia-EC5252?style=for-the-badge&logo=udemy&logoColor=white&labelColor=101010)](https://www.udemy.com/course/sql-para-administracion-de-bases-de-datos-con-mysql/)
[![Web](https://img.shields.io/badge/My_Website-uskokrum2010.com-14a1f0?style=for-the-badge&logo=dev.to&logoColor=white&labelColor=101010)](https://uskokrum2010.com)
[![Email](https://img.shields.io/badge/uskokrum2010@gmail.com-mi_email_personal-D14836?style=for-the-badge&logo=gmail&logoColor=white&labelColor=101010)](mailto:uskokrum2010@gmail.com)