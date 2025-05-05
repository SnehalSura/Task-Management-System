# Task Management System

This project is a backend Task Management system built using Django and Django REST Framework (DRF). It allows users to create, retrieve, update, and delete tasks with features like filtering, sorting, and searching.

---

## Project Setup

Follow these steps to set up the project:

1. Clone this repository:
   ```bash
   git clone <repository-url>       
   cd <repository-name>

2. Create and activate a virtual environment:
    ```bash
    virtualenv venv
    venv\Scripts\activate

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt

4. Apply database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. Start the development server:
    ```bash
    python manage.py runserver

## Running the Project
After setting up the project, the API will be accessible at:

Base URL: http://127.0.0.1:8000/

Navigate to /tasks/ for the Task API.

## API Endpoints
    1. Task List
        URL: /tasks/

        * Methods:

        GET: Retrieves all tasks with optional filtering, searching, and sorting.

        POST: Creates a new task.

        Query Parameters for GET:
            sort_by_date: Sort tasks by date (e.g., ?sort_by_date=true).

            search_date: Filter tasks by a specific date (e.g., ?search_date=2024-01-01).

            search: Search tasks by title (e.g., ?search=meeting).

            URLs for sorted/filtered Testing:

                1. Sort by date:
                GET: /tasks/?sort_by_date=true

                2. Search by date:
                GET: /tasks/?search_date=2025-05-04

                3. Search by title:
                GET: /tasks/?search=some_title


    2. Task Detail
        URL: /tasks/<int:id>/

        * Methods:

        PATCH: Updates a task by ID (partial update).

        DELETE: Deletes a task by ID.
