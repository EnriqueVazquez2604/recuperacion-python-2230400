# Control de Transporte Escolar

## Datos del estudiante
- **Nombre completo:** Enrique Vázquez Faz
- **Matrícula:** 2230400
- **Grupo:** [COMPLETAR GRUPO]
- **Número de variante:** 24

## Nombre del proyecto
**Control de Transporte Escolar**

## Descripción
Mini proyecto desarrollado en Python para administrar unidades de transporte escolar durante la ejecución del programa. Cada unidad contiene un número identificador, conductor, capacidad, cantidad de pasajeros y ruta.

## Funcionalidades
- Registrar una unidad.
- Mostrar todas las unidades.
- Buscar por número de unidad.
- Actualizar información.
- Eliminar una unidad.
- Evitar números duplicados.
- Validar capacidad y pasajeros.
- Manejar búsquedas sin resultados.
- Calcular lugares disponibles.
- Mostrar unidades llenas.
- Encontrar la unidad con mayor ocupación.
- Mostrar un resumen general.

## Requisitos
- Python 3.13 o superior.
- `uv`.
- Git.
- pytest.
- Ruff.

## Instalación
```bash
git clone https://github.com/EnriqueVazquez2604/recuperacion-python-2230400.git
cd recuperacion-python-2230400
```

## Sincronización
```bash
uv sync
```

`.venv/` se genera localmente y no debe subirse al repositorio.

## Ejecución
```bash
uv run examen-recuperacion-2230400
```

También puede utilizarse:
```bash
uv run python -m examen_recuperacion_2230400.main
```

## Pruebas
```bash
uv run pytest
```

Las pruebas cubren registro, duplicados, búsqueda, casos sin resultados, cálculos, validaciones, actualización y eliminación.

## Ruff
```bash
uv run ruff check .
uv run ruff format --check .
```
Para aplicar el formato:
```bash
uv run ruff format .
```

## Pruebas implementadas
Se incluyen pruebas para funcionamiento normal, casos límite, datos inválidos, búsqueda sin resultados, actualización y eliminación. El proyecto contiene más de las 8 pruebas mínimas solicitadas.

## Estructura del proyecto
```text
recuperacion-python-2230400/
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
├── src/
│   └── examen_recuperacion_2230400/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       └── services.py
└── tests/
    ├── __init__.py
    └── test_services.py
```

- `models.py`: representa la entidad `Unidad`.
- `services.py`: contiene la lógica de negocio, validaciones y cálculos.
- `main.py`: contiene el menú y la interacción con el usuario.
- `tests/`: contiene las pruebas automatizadas.

## Decisiones de diseño
Se separó la representación de los datos de la lógica del programa. La clase `Unidad` está en `models.py` y las operaciones están en `services.py`. La información se mantiene en una lista durante la ejecución, sin utilizar base de datos.

Las validaciones se concentran en funciones reutilizables para evitar datos inconsistentes tanto al registrar como al actualizar.

## Problemas encontrados
Durante el desarrollo se identificó que algunas operaciones estaban implementadas en `services.py`, pero no estaban disponibles desde el programa principal. Se solucionó integrando un menú de consola que permite registrar, mostrar, buscar, actualizar y eliminar unidades.

También se reforzó la validación durante las actualizaciones para evitar capacidades o cantidades de pasajeros inválidas.

## Variante asignada
**Variante 24 — Transporte escolar**

Entidad principal: `Unidad`.

Datos mínimos: número, conductor, capacidad, pasajeros y ruta.

Funciones particulares: calcular lugares disponibles, mostrar unidades llenas y encontrar la unidad con mayor ocupación.
