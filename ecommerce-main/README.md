
#  Marketplace app

## 1. Crear entorno virtual

```bash
python3 -m venv .venv
```

## 2. Activar entorno virtual

### macOS/Linux
```bash
source .venv/bin/activate
```

### Windows
```powershell
.\.venv\Scripts\activate
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4. Estructura del proyecto

- `practica_vectores/`: Ejercicios con vectores
- `practica_matrices/`: Ejercicios con matrices

Cada carpeta contiene archivos `problemaX.py` que puedes ejecutar individualmente:

```bash
python practica_vectores/problema1.py
python practica_matrices/problema1.py
```

## 5. Recomendaciones
- Activa siempre el entorno virtual antes de instalar paquetes o ejecutar scripts.
- Al instalar una dependencia nueva ejecutar:
```bash 
pip freeze > requirements.txt 
```

