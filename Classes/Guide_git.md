Guía básica para el uso de Git

1. Descargar Git desde el enlace: https://git-scm.com/downloads e instalarlo según tu sistema operativo.

2. Configurar tu nombre de usuario y correo electrónico (solo la primera vez):

    ```bash
    git config --global user.name "Tu Nombre"
    git config --global user.email "tuemail@ejemplo.com"
    ```

3. Crear una nueva carpeta para tu proyecto y entrar en ella:

    ```bash
    mkdir mi-proyecto
    cd mi-proyecto
    ```

4. Inicializar un repositorio Git en la carpeta:

    ```bash
    git init
    ```

5. Crear un archivo (por ejemplo, `README.md`) y guardarlo. (Pero se podría hacer con cualquier archivo que se arrastre a la carpeta)

6. Ver el estado de los archivos:

    ```bash
    git status
    ```

7. Agregar archivos al área de preparación (staging):

    ```bash
    git add README.md
    ```

8. Hacer un commit (guardar los cambios en el historial):

    ```bash
    git commit -m "Primer commit"
    ```

9. Conectar tu repositorio local con uno remoto (por ejemplo, en GitHub, para esto primero se debe crear un repositorio en GitHub):

    ```bash
    git remote add origin https://github.com/usuario/mi-proyecto.git
    ```

10. Subir los cambios al repositorio remoto:

     ```bash
     git push -u origin master
     ```

11. Para descargar cambios del repositorio remoto:

     ```bash
     git pull
     ```

Estos son los pasos básicos para comenzar a usar Git en tus proyectos.