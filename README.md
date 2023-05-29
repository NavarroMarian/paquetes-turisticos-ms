# paquetes-turisticos-ms
Trabajo Práctico grupal


A continuación, se presentan algunas instrucciones básicas para utilizar Git. Estas instrucciones te ayudarán a colaborar de manera eficiente en proyectos compartidos.

# Configuración inicial:

1 - Asegúrate de tener Git instalado en tu máquina.

2 - Crea una cuenta en un servicio de alojamiento de repositorios en línea, como GitHub o GitLab.

3 - Configura tu nombre de usuario y dirección de correo electrónico en Git usando el siguiente comando:

git config --global user.name "Tu nombre"

git config --global user.email "tu@email.com"

# Crear un repositorio:

Uno de los miembros del grupo debe crear un nuevo repositorio en el servicio en línea y compartir el enlace con los demás.
Los otros miembros pueden clonar el repositorio en su máquina local utilizando el siguiente comando:

git clone enlace-del-repositorio
  
# Trabajar en el código:
Cada miembro del grupo trabaja en su propia rama para evitar conflictos.
  
Antes de comenzar a trabajar, crea una nueva rama local utilizando el siguiente comando:

git checkout -b nombre-de-la-rama
  
# Realiza los cambios necesarios en los archivos de código.
Cuando hayas terminado, agrega los archivos modificados al área de preparación utilizando el siguiente comando:

git add nombre-del-archivo
  
Realiza un commit de los cambios utilizando el siguiente comando:

git commit -m "Mensaje descriptivo del commit"
  
# Sincronización con el repositorio remoto:

Sube tus cambios al repositorio remoto utilizando el siguiente comando:
  
git push origin nombre-de-la-rama
  
# Integración de cambios:
Si otros miembros del grupo han realizado cambios y los han subido al repositorio remoto, puedes incorporar esos cambios en tu rama utilizando el siguiente comando:

git pull origin nombre-de-la-rama
  
Si hay conflictos entre los cambios locales y los cambios remotos, Git te pedirá que los resuelvas manualmente.

# Solicitar cambios en el repositorio principal:
Cuando estés listo para que tus cambios se integren en el repositorio principal, puedes crear una solicitud de extracción (pull request) en el servicio en línea.
Describe los cambios realizados y solicita a los otros miembros del grupo que revisen y aprueben tus cambios.
