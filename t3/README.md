# Tarea 3 - Data Compression
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

## Tablas con un símbolo

### Pixeles simples

NAME        |   Entropy     |   Expected Length |   Original Size (Bytes)   |   Compression rate
------------------------------------------------------------------------------------------------
bridge.jpg  |   7.687922    |   7.716118        |   262144                  |   1.036791
lenna.jpg   |   7.595680    |   7.625778        |   262144                  |   1.049073
miss.tif    |   5.919494    |   5.948903        |   25344                   |   1.344786
sussie.tif  |   6.954216    |   6.986458        |   262144                  |   1.14072

### Diferencia de pixeles contiguos

NAME        |   Entropy     |   Expected Length |   Original Size (Bytes)   |   Compression rate
------------------------------------------------------------------------------------------------
bridge.jpg  |   5.026389    |   5.051689        |   262144                  |   1.583629
lenna.jpg   |   4.355370    |   4.383316        |   262144                  |   1.825102
miss.tif    |   2.684717    |   2.707150        |   25344                   |   2.955138
sussie.tif  |   4.392761    |   4.413929        |   262144                  |   1.812444

En el segundo inciso se observa mayores tasas de compresión debido a que al hacer las diferencias
obtenemos una distribución m+as pequeña que la anterior, donde (debido al tamaño del diccionario y
a la "continuidad" de la imagen), se obtienen diferencias pequeñas.

---

## Tablas con doble símbolo

### Pixeles simples

NAME        |   Entropy     |   Expected Length |   Original Size (Bytes)   |   Compression rate
------------------------------------------------------------------------------------------------
bridge.jpg  |   13.499830   |   13.528284       |   262144                  |   1.182807
lenna.jpg   |   12.769751   |   12.797580       |   262144                  |   1.250236
miss.tif    |   8.734832    |   8.767312        |   25344                   |   1.824961
sussie.tif  |   11.906623   |   11.933079       |   262144                  |   1.340811

### Diferencia de pixeles contiguos

NAME        |   Entropy     |   Expected Length |   Original Size (Bytes)   |   Compression rate
------------------------------------------------------------------------------------------------
bridge.jpg  |   9.908153    |   9.936531        |   262144                  |   1.610220
lenna.jpg   |   8.510889    |   8.538714        |   262144                  |   1.873819
miss.tif    |   4.899974    |   4.931776        |   25344                   |   3.244267
sussie.tif  |   8.584557    |   8.612925        |   262144                  |   1.857673

Se observa como la razón de compresión mejora claramente en el caso de símbolos dobles, y aún más
para el caso en el que se toman las diferencias entre pixeles contiguos.

---
**License**: All the code is under the [GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html) license.
