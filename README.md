# Mental Health Wellness System

A Django-based web application that supports day-to-day mental wellness through guided yoga and meditation sessions, plus a simple mood tracking workflow for authenticated users.

## Features

- User authentication (sign up, login, logout)
- Dashboard with wellness activity summary
- Yoga session catalog with detail pages
- Meditation session catalog with detail pages
- Mood tracker with one mood entry per user per day
- Mood history and basic mood count analytics
- Media support for yoga and meditation images

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (default)
- **Frontend:** Django Templates, Bootstrap 5
- **Media Handling:** Django media storage (`/media`)

## Project Structure

- `/Mental_Health` – Django project settings and URL configuration
- `/testapp` – Core app (models, views, forms, migrations)
- `/templates` – HTML templates for auth, dashboard, yoga, meditation, and mood pages
- `/media` – Uploaded/seeded media assets for wellness content
- `manage.py` – Django management entrypoint

## Setup & Installation

1. Clone the repository and move into the project folder.
2. Create and activate a virtual environment.
3. Install dependencies (inferred):

   ```bash
   pip install django pillow
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. (Optional) Create an admin user:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

- Open `http://127.0.0.1:8000/`
- Create an account at `/signup/` or login with an existing user
- Use the dashboard to navigate to Yoga, Meditation, and Mood Tracker
- Add/manage Yoga and Meditation records through Django admin (`/admin/`) if needed

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Make focused changes
4. Run relevant checks/tests
5. Open a pull request with a clear description

## License

No license file is currently present in this repository. If you plan to distribute or reuse this project, add a LICENSE file with your preferred terms.
