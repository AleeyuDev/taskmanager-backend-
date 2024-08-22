
### Backend

- **Django**: A high-level Python web framework that encourages rapid development.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs.

## Installation and Setup

### Backend (Django)

1. **Navigate to the backend directory**:

   ```bash
   cd backend
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use`venv\Scripts\activate
   ```

3. Install dependencies:

```bash
  pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```
