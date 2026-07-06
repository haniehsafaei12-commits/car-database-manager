# Car Database Management System

A desktop CRUD application for managing car records built with Python, Tkinter, and SQLAlchemy.

## Features

- Add new cars (Name, Model, Color, Horse Power)
- View all cars in a table
- Update existing car records by ID
- Delete cars by ID
- MySQL database with SQLAlchemy ORM
- Clean GUI with Tkinter

## Technologies

- Python 3.x
- Tkinter (GUI)
- SQLAlchemy (ORM)
- MySQL (Database)
- MVC Architecture

## Project Structure

- MODEL.py - Database models and connection
- CONTROLLER.py - Business logic (CRUD operations)
- VIEW.py - Tkinter GUI interface

## Installation

1. Install dependencies:
   pip install sqlalchemy mysql-connector-python

2. Update database password in MODEL.py:
   password = "your_password"

3. Run MODEL.py to create database and tables

4. Run the application:
   python VIEW.py

## Database Schema

Table: Cars
- Id (Primary Key, Auto Increment)
- Name (String)
- Model (String)
- Color (String)
- Horse_Power (Integer)

## How to Use

Add a Car:
- Click "Add" button
- Fill in car details
- Click "confirmation"

Update a Car:
- Click "Update" button
- Enter car ID
- Fill in new details
- Click "confirmation"

Delete a Car:
- Enter car ID in text field
- Click "Delete" button

View All Cars:
- Click "Show All" button

## License

MIT

## Author

Hanieh safaei
