# Ejercicio 2 : Tarea 2 - Data Compression
### José Joaquín Zubieta Rico (09-05-2018)

**Description**

a) Codificar Miss, Sussie, Barbara y Puente. Mostrar una tabla comparativa con los siguientes campos:

 - Tamaño Original
 - Entropía
 - Longitud de Código Esperado
 - Razón de Compresión
 - Bits-Per-Pixel(bpp)

e interpretar los resultados obtenidos.
b) Realizar lo mismo tomando la diferencia entre pixeles vecinos.

---

NAME        |   Entropy     |   Expected Length |   Original Size (Bytes)   |   Compression rate
------------------------------------------------------------------------------------------------
bridge.jpg  |   7.687922    |   7.716118        |   262144                  |   1.036791
lenna.jpg   |   7.595680    |   7.625778        |   262144                  |   1.049073
miss.tif    |   5.919494    |   5.948903        |   25344                   |   1.344786
sussie.tif  |   6.954216    |   6.986458        |   262144                  |   1.14072

NAME        |   Entropy     |   Expected Length |   Original Size (Bytes)   |   Compression rate
------------------------------------------------------------------------------------------------
bridge.jpg  |   5.026389    |   5.051689        |   262144                  |   1.583629
lenna.jpg   |   4.355370    |   4.383316        |   262144                  |   1.825102
miss.tif    |   2.684717    |   2.707150        |   25344                   |   2.955138
sussie.tif  |   4.392761    |   4.413929        |   262144                  |   1.812444

en el segundo inciso se observa mayores tasas de compresión debido a que al hacer las diferencias
obtenemos una distribución m+as pequeña que la anterior, donde (debido al tamaño del diccionario y
a la "continuidad" de la imagen), se obtienen diferencias pequeñas.

---

**License**: All the code is under the [GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html) license.
