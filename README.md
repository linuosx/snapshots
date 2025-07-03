# Proyecto: Snapshot de Discos de VM en Azure

Este proyecto permite crear snapshots (copias de seguridad) de los discos (OS y datos) de una máquina virtual en Microsoft Azure, utilizando Python y la SDK de Azure.

## Estructura del proyecto

```
├── LICENSE
├── README.md
├── pdm.lock
├── pyproject.toml
├── requirements.txt
└── src/
    ├── auth.py
    ├── config.py
    ├── main.py
    ├── snapshot.py
```

## Descripción de archivos principales

- `src/main.py`: Script principal que ejecuta el proceso de snapshot.
- `src/auth.py`: Funciones de autenticación y obtención del cliente de Azure.
- `src/config.py`: Configuración de parámetros como IDs, nombres de recursos y ubicación.
- `src/snapshot.py`: Lógica para crear snapshots de discos.
- `requirements.txt` / `pyproject.toml`: Dependencias del proyecto.
- `LICENSE`: Licencia MIT en inglés y español.

## Instalación

1. Clona este repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   O si usas PDM:
   ```bash
   pdm install
   ```

## Configuración

Edita el archivo `src/config.py` para definir los siguientes parámetros en el diccionario `SNAPSHOT_CONFIF`:
- `SUBSCRIPTION_ID`: ID de la suscripción de Azure.
- `SOURCE_RG`: Grupo de recursos de la VM origen.
- `VM_NAME`: Nombre de la máquina virtual.
- `TARGET_RG`: Grupo de recursos donde se guardarán los snapshots.
- `LOCATION`: Región de Azure.
- `SNAPSHOT_NAME`: Formato para el nombre del snapshot.

Todos estos parámetros, excepto `SNAPSHOT_NAME`, son obtenidos directamente de sus respectivas variables de entorno, las cuales pueden ser definidas en un archivo `.env ` dentro del mismo directorio `src`.

## Uso

Ejecuta el script principal:

```bash
python src/main.py
```

El script:
- Obtiene la VM especificada.
- Identifica los discos OS y de datos.
- Crea un snapshot para cada disco.
- Muestra logs del proceso.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE`para más detalles.

## Autor

Edgar E. Reyes T. <linuosx@gmail.com>

---

> Proyecto para automatizar snapshots de discos en Azure. Para dudas o mejoras, abre un issue o contacta al autor.
