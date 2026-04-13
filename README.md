# AI Blog Writer

This project uses Crew AI to automate daily blog writing on tech industry topics. It includes agents for topic finding, research, evaluation, formatting, and emailing the final blog post.

## Features

- **Topic Finder Agent**: Identifies trending tech industry topics.
- **Research Analyst Agent**: Gathers detailed information and facts.
- **Evaluator Agent**: Validates content and facts from multiple sources using Serper API.
- **Formatter Agent**: Formats content in Medium blog style with examples, code snippets, and citations.
- **Email Agent**: Sends the formatted blog as a document attachment via SendGrid.

## Setup

1. Ensure Python 3.11 or 3.12 is installed (Python 3.14 may have compatibility issues with some dependencies requiring C compiler; if using 3.14, install Microsoft Visual Studio Build Tools with C++ support).
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
4. Install dependencies: `pip install -r requirements.txt`
5. Set up environment variables in `.env` file (copy from `.env.example`)
6. Run the application: `python src/main.py`

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `SERPER_API_KEY`: Your Serper API key
- `SENDGRID_API_KEY`: Your SendGrid API key
- `EMAIL_FROM`: Sender email
- `EMAIL_TO`: Recipient email