# Proyecto de Blog en Django

Este es un proyecto de blog web creado con el framework Django, que incluye funcionalidades de autenticación de usuarios, manejo de publicaciones, comentarios y perfiles de usuario.

## Funcionalidades

- **Autenticación de Usuarios**: Registro y login de usuarios.
- **Gestión de Publicaciones**: Crear, listar, y ver detalles de las publicaciones.
- **Comentarios**: Añadir comentarios a las publicaciones.
- **Perfiles de Usuario**: Ver y editar perfiles de usuario.
- **Página "Sobre mí"**: Una sección informativa acerca del autor o la aplicación.

## Estructura del Código

- **Autenticación**:
  - `login_request(request)`: Maneja el inicio de sesión de los usuarios.
  - `register_view(request)`: Maneja el registro de nuevos usuarios.
- **Publicaciones**:
  - `home(request)`: Renderiza la página principal del blog.
  - `post_list(request)`: Muestra una lista de todas las publicaciones.
  - `post_detail(request, post_id)`: Muestra el detalle de una publicación específica junto con sus comentarios.
  - `create_post(request)`: Permite a los usuarios crear una nueva publicación.
- **Perfil de Usuario**:
  - `profile(request)`: Muestra el perfil del usuario autenticado.
  - `edit_profile(request)`: Permite a los usuarios editar su perfil.
- **Otras Vistas**:
  - `sobre_mi(request)`: Muestra la página "Sobre mí".

## Requisitos

- Python 3.x
- Django (Versión compatible con el proyecto)
# Proyecto de Blog en Django

Este es un proyecto de blog web creado con el framework Django, que incluye funcionalidades de autenticación de usuarios, manejo de publicaciones, comentarios y perfiles de usuario.

## Funcionalidades

- **Autenticación de Usuarios**: Registro y login de usuarios.
- **Gestión de Publicaciones**: Crear, listar, y ver detalles de las publicaciones.
- **Comentarios**: Añadir comentarios a las publicaciones.
- **Perfiles de Usuario**: Ver y editar perfiles de usuario.
- **Página "Sobre mí"**: Una sección informativa acerca del autor o la aplicación.

## Estructura del Código

- **Autenticación**:
  - `login_request(request)`: Maneja el inicio de sesión de los usuarios.
  - `register_view(request)`: Maneja el registro de nuevos usuarios.
- **Publicaciones**:
  - `home(request)`: Renderiza la página principal del blog.
  - `post_list(request)`: Muestra una lista de todas las publicaciones.
  - `post_detail(request, post_id)`: Muestra el detalle de una publicación específica junto con sus comentarios.
  - `create_post(request)`: Permite a los usuarios crear una nueva publicación.
- **Perfil de Usuario**:
  - `profile(request)`: Muestra el perfil del usuario autenticado.
  - `edit_profile(request)`: Permite a los usuarios editar su perfil.
- **Otras Vistas**:
  - `sobre_mi(request)`: Muestra la página "Sobre mí".

## Requisitos

- Python 3.x
- Django (Versión compatible con el proyecto)
http://127.0.0.1:8000/

## video de la pagina 
https://youtu.be/UsetysZ8E00 
