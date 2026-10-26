# UD2.1. Actividad 3: GameAnalytics - Analizador de Bibliotecas de Steam

**Autor:** Antonio Manuel González Martínez  
**Proyecto:** Aplicación de consola para la normalización y análisis de datos de videojuegos de Steam.

---

## 📖 Descripción del Proyecto

La empresa **GameAnalytics** requiere una herramienta en Python capaz de cargar catálogos de videojuegos con datos en bruto desde archivos CSV, tratarlos mediante Programación Orientada a Objetos (POO), generar estadísticas generales e incorporar campos derivados mediante reglas de negocio para exportar un archivo CSV normalizado.

---

## 📁 Estructura del Proyecto

El proyecto sigue una arquitectura modular para separar la lógica de negocio, la interacción por consola y los datos:

```text
game_analytics/
│
├── main.py                       # Módulo principal (interfaz de menú, flujo y llamadas)
├── librerias/
│   ├── __init__.py               # Inicializador del paquete de librerías
│   └── videojuego.py             # Clase Videojuego y métodos de cálculo/transformación
│
├── datos/
│   ├── videojuegos.csv           # Archivo de entrada con los datos en bruto (>50 registros)
│   └── videojuegos_transformado.csv # Archivo resultante tras la transformación
│
└── README.md                     # Documentación del proyecto
