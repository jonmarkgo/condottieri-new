# Condottieri

A Django-based strategy game set in Renaissance Italy.

## Features

- Turn-based strategy gameplay
- Multiple scenarios and game modes
- User profiles and messaging system
- Event tracking and notifications

## Requirements

- Python 3.11+
- PostgreSQL (recommended for production) or SQLite3 (development)
- Other dependencies listed in `requirements.txt`

## Development Setup

1. Clone the repository and its submodules:
   ```bash
   git clone --recursive https://github.com/yourusername/condottieri.git
   cd condottieri
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and configure your environment variables:
   ```
   DJANGO_DEBUG=True
   DJANGO_SECRET_KEY=your-secret-key-here
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
   DATABASE_URL=sqlite:///db.sqlite3
   DJANGO_EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

- `config/`: Project configuration (settings, URLs, etc.)
- `machiavelli/`: Core game logic
- `condottieri_profiles/`: User profile management
- `condottieri_messages/`: Messaging system
- `condottieri_events/`: Event tracking
- `condottieri_common/`: Shared utilities
- `condottieri_scenarios/`: Game scenarios
- `condottieri_notification/`: Notification system

## Testing

Run tests with:
```bash
pytest
```

## Documentation

Build documentation with:
```bash
cd doc
make html
```

## License

See the `COPYING` file for license details. 