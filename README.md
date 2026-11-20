# Warehouse Management 📦

Desktop application for managing a warehouse's **buildings, pallets and clients**, built in **Python** with a **PyQt6** graphical interface.

Team project for the Object-Oriented Programming course at Universidad Panamericana (2024), developed in three sprints.

## Features

- **Buildings:** create, delete, list and look up buildings (location and number of shelves)
- **Pallets:** register pallets, move them between buildings, delete them and look up their information
- **Clients:** create, delete, list and look up clients
- **Validations** to prevent duplicate IDs and pallets assigned to buildings or clients that don't exist
- **Persistence** in text files (`edificios.txt`, `pallets.txt`, `clientes.txt`) that are loaded when the app starts

## Tech stack

- Python 3
- PyQt6 (GUI)
- Object-oriented design: `Edificio`, `Pallet` and `Cliente` classes with encapsulated attributes, plus one window per module

## Development process

| Sprint | Focus |
|---|---|
| Sprint 1 | Understanding the domain: warehouse operations, LPN (*License Plate Number*, a pallet's unique barcode/RFID identifier), creating and validating pallets |
| Sprint 2 | Refactoring the code to OOP, designing the database schema and adding text-file persistence for clients, buildings and pallets |
| Sprint 3 | Interface design (wireframes and color palette) and the PyQt6 desktop app |

![Database schema](docs/Esquema%20base%20de%20datos.png)

The `docs/` folder contains the sprint presentations, wireframes, the database schema and the warehouse operations diagram.

## Running locally

```bash
pip install PyQt6
python Warehouse.py
```

## Team

Cecilia Gaona, Fernando Peña, Asier Siverio and Ricardo Zerón.
