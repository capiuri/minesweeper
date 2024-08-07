# Buscaminas en Tkinter

Este proyecto es una implementación del clásico juego de **Buscaminas** utilizando la biblioteca `tkinter` en Python. La aplicación proporciona una interfaz gráfica para jugar al Buscaminas, donde los jugadores pueden descubrir celdas y colocar banderas para evitar minas.

## Requisitos

- Python 3.x
- Biblioteca `tkinter` (incluida con Python por defecto)

## Uso

1. **Ejecuta el script** principal para iniciar el juego:

    ```bash
    python main.py
    ```

2. **Interacción con el juego**:
   - **Clic izquierdo** en una celda para revelarla.
   - **Clic derecho** en una celda para marcarla con una bandera (F) o desmarcarla si ya está marcada.
   - La etiqueta en la parte superior muestra el número de bombas restantes que puedes colocar en el tablero.

3. **Objetivo del juego**:
   - Revela todas las celdas que no contienen minas para ganar.
   - Coloca banderas en las celdas que crees que contienen minas para evitarlas.

4. **Fin del juego**:
   - El juego termina cuando se revela una celda con una mina, mostrando todas las minas en el tablero y deshabilitando todas las celdas.
   - Si todas las celdas sin minas están reveladas, el juego muestra un mensaje de victoria.

## Cómo Funciona

- **Tablero de Juego**: Se crea un tablero de tamaño configurable (por defecto 10x10) y se colocan las minas aleatoriamente.
- **Recuento de Minas**: Cada celda muestra el número de minas adyacentes a ella.
- **Revelar Celdas**: Las celdas se revelan al hacer clic izquierdo. Si una celda contiene una mina, se muestra un asterisco rojo y el juego termina.
- **Colocar Banderas**: Usa clic derecho para colocar o quitar banderas. El número de banderas disponibles está limitado por el número de minas en el tablero.

## Personalización

Puedes ajustar el tamaño del tablero y la cantidad de minas cambiando los parámetros al crear una instancia de `Minesweeper`:
