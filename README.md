# AI Blog Writer

This project uses Crew AI to automate daily blog writing on tech industry topics. It includes agents for topic finding, research, evaluation, formatting, and emailing the final blog post.

## Features

- **Topic Finder Agent**: Identifies trending tech industry topics.
- **Research Analyst Agent**: Gathers detailed information and facts.
- **Evaluator Agent**: Validates content and facts from multiple sources using Serper API.
- **Formatter Agent**: Formats content in Medium blog style with examples, code snippets, and citations.
- **Email Agent**: Sends the formatted blog as a document attachment via SendGrid.

## Setup

1. Ensure Python 3.10 is installed. Download from [python.org](https://www.python.org/downloads/) if needed.

2. Create a virtual environment: `python -m venv venv`

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Install dependencies: `pip install -r requirements.txt`

5. Set up environment variables: Copy `.env.example` to `.env` and fill in your API keys (OpenAI, Serper, SendGrid, email addresses).

6. Run the application once for testing: `python src/main.py`

## Daily Automation

To run the blog generation daily:

- **Locally**: Uncomment the scheduling code in `src/main.py` and run `python src/main.py` (it will run daily at 9 AM).
- **Via GitHub Actions**: Use the provided workflow in `.github/workflows/generate-blog.yml` (set up secrets in repository settings).

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `SERPER_API_KEY`: Your Serper API key
- `SENDGRID_API_KEY`: Your SendGrid API key
- `EMAIL_FROM`: Sender email
- `EMAIL_TO`: Recipient email