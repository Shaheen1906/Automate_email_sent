
# Django Event Email System

## Overview

This Django API is designed to automate the process of sending event emails, such as birthday and work anniversary emails, to employees. The system retrieves event details from its database, personalizes email templates, and sends emails to the respective employees.

## Features

- Send event emails (birthdays, work anniversaries) automatically.
- Retrieve event data from the database.
- Personalize email templates with employee details.
- Log email sending status and errors encountered.

## Getting Started

### Prerequisites

- Python 3.11+
- Django 5.0.3
- Django REST Framework

### Installation

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/your/repository.git
   ```

2. Navigate to the project directory:
   ```
   cd event_email_system
   ```

3. Install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

### Configuration

1. Set up your Django project settings, including database configuration, email settings, etc., in `settings.py`.

2. Run migrations to create necessary database tables:
   ```
   python manage.py migrate
   ```

3. Create superuser for admin access:
   ```
   python manage.py createsuperuser
   ```

### Usage

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. Open a web browser and navigate to the following URL to access the browsable API interface:
   ```
   http://localhost:8000/
   ```

3. Use the provided API endpoints to:
   - Add employee details: `/employees/`
   - Schedule events (birthdays, work anniversaries): `/events/`
   - Create email templates: `/email-templates/`
   - Send event emails: `/send-event-emails/`

4. Authenticate as admin to access admin functionalities:
   - `/admin/`

### API Endpoints

- `/employees/`: Manage employee details.
- `/events/`: Schedule events (birthdays, work anniversaries).
- `/email-templates/`: Create and manage email templates.
- `/send-event-emails/`: Trigger the process of sending event emails.

### Admin Access

1. Log in as admin using the credentials created during superuser creation.

2. Access the admin panel at `/admin/` to manage database entries and monitor email sending status.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

Special thanks to the contributors and the Django community for their valuable contributions and support.

## Contact

For any inquiries or support, please contact [your email address].

---

Feel free to customize this README according to your specific project requirements. Include detailed instructions on how to set up and use your Django application, and provide clear explanations of each feature and endpoint.