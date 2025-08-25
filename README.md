# AI LinkedIn Feed Bot

## Project Description
The AI LinkedIn Feed Bot is a Python-based application designed to automate the generation and scheduling of content for LinkedIn. It leverages AI to create engaging posts and interacts with the LinkedIn API to publish them at optimal times.

## Features
- **Content Generation**: Automatically generate LinkedIn posts using AI.
- **Scheduling**: Schedule posts to be published at specific times.
- **LinkedIn Integration**: Seamlessly interact with the LinkedIn API to publish content.

## Project Structure
```
main.py
requirements.txt
app/
    content_generator.py
    linkedin_client.py
    scheduler.py
config/
    settings.py
```

### Key Modules
- **`app/content_generator.py`**: Handles the AI-based content generation.
- **`app/linkedin_client.py`**: Manages interactions with the LinkedIn API.
- **`app/scheduler.py`**: Schedules and automates the posting of content.
- **`config/settings.py`**: Contains configuration settings for the application.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd ai-linkedin-feed-bot
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Configure the settings in `config/settings.py`.
2. Run the main script:
   ```bash
   python main.py
   ```

## Requirements
- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Inspired by the need for efficient LinkedIn content management.
- Built with Python and the LinkedIn API.
