# Airbnb Clone - The Console

## Description

This project is part of the ALX Software Engineering curriculum, aiming to recreate a simple clone of the Airbnb application. The initial phase is building a command-line interpreter that lays the groundwork for the later stages, including HTML/CSS templating, database storage, API, and front-end integration. The console will be used to manage objects for the Airbnb Clone website, including creating, updating, and destroying persisted objects, and managing the JSON serialization/deserialization processes.

## Command Interpreter

### How to Start It

To start the console, navigate to the project directory and run the `console.py` file with Python:

```bash
$ ./console.py
```

Upon execution, the command interpreter will display a prompt (hbnb), indicating that it is ready to accept commands.

### How to Use It

The command interpreter can interpret several commands to manage the application's data effectively:

```bash
create: Creates a new instance of a specified class and prints the id of the new instance.
$ (hbnb) create BaseModel

show: Displays the information of a specific instance based on its class name and id.
$ (hbnb) show BaseModel 1234-1234-1234

destroy: Deletes a specified instance based on its class name and id.
$ (hbnb) destroy BaseModel 1234-1234-1234

all: Displays all instances of a class or all instances of every class if no class name is specified.
$ (hbnb) all BaseModel

update: Updates an instance based on its class name and id by adding or updating attributes.
$ (hbnb) update BaseModel 1234-1234-1234 email "aibnb@holberton.com"
```

### Examples

Below are some examples of how to use the command interpreter:

```bash
Creating a new instance of BaseModel:
$ (hbnb) create BaseModel
$ 1234-1234-1234-1234

Showing an instance of BaseModel by id:
$ (hbnb) show BaseModel 1234-1234-1234-1234
$ [BaseModel] (1234-1234-1234-1234) {'id': '1234-1234-1234-1234', 'created_at': datetime, 'updated_at': datetime}

Deleting an instance of BaseModel:
$ (hbnb) destroy BaseModel 1234-1234-1234-1234

Displaying all instances of BaseModel:
$ (hbnb) all BaseModel
$ ["[BaseModel] (1234-1234-1234-1234) {'id': '1234-1234-1234-1234', 'created_at': datetime, 'updated_at': datetime}"]

Updating an instance of BaseModel:
$ (hbnb) update BaseModel 1234-1234-1234-1234 email "example@example.com"
```