# Folders and Files
- **`app/`**: Contains the core application logic.
  - **`config.py`**: Configuration settings for the application (e.g., API keys, database credentials).
  - **`controllers/`**: Handles routing and logic for different endpoints.
    - **`chatbot_controller.py`**: Manages  webhook endpoint
    - **`health_controller.py`**: Manages health check endpoint to monitor application status.
    - **`tables_controller.py`**: Handles logic related to database tables.
  - **`core/`**: Contains the main business logic for the chatbot.
    - **`robot/`**: Implements key chatbot operations.
      - **`entryPoint.py`**: Main entry point for handling messages.
      - **`saveMessage.py`**
  - **`interfaces/`**: Manages communication with external/internal systems.
    - **`api/`** Contain files for API interactions
      - **`whatsapp_api.py`**: Handles WhatsApp API interactions.
    - **`crud/`**: Manages CRUD operations for database.
    - **`generator/`**: Generates formatted messages.
      - **`msg/json_format.py`**: Handles the creation of JSON message formats.
  - **`models/`**: Defines the application's data models and database structure.
    - **`database/db.py`**: Initializes the database connection.
    - **`orm/`**: Contains ORM models to interact with the database tables.
      - **`client.py`**, **`message.py`**, **`log.py`**: Define the structure of database tables.
  - **`services/`**: Contains services to interact with the data models.
    - **`client.py`**, **`message.py`**, **`raw.py`**: Functions that handle client, message, and raw instances.
  - **`stack/`**: Holds constant values and configurations.
    - **`constant/`**: Contains static values used throughout the app (e.g., WhatsApp settings, message templates).
  - **`web/`**: Stores web interface files.
    - **`static/`**: Static files (images, css and javascript files).
    - **`templates/`**: Contains HTML files for the web interface.
- **`run.py`**: Entry point to start the Flask application and initialize the chatbot.
- **`requirements.txt`**: Lists Python dependencies required for the project (Flask, SQLAlchemy, etc.).