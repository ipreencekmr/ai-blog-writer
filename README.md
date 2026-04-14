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

## Running the Application

### Command-Line Usage

Run the application with optional arguments:

```bash
python src/main.py [--topic "Your Topic"] [--to_email "recipient@example.com"]
```

- `--topic`: (Optional) Specify a custom topic for the blog post. If not provided, the Topic Finder Agent will identify a trending tech topic.
- `--to_email`: (Optional) Specify the recipient email address. If not provided, uses the `EMAIL_TO` environment variable.

#### Examples

- Run with a custom topic and email:
  ```bash
  python src/main.py --topic "Kubernetes" --to_email "user@example.com"
  ```

- Run with only a custom topic (uses `EMAIL_TO` from `.env`):
  ```bash
  python src/main.py --topic "Docker"
  ```

- Run without arguments (finds topic and uses `EMAIL_TO` from `.env`):
  ```bash
  python src/main.py
  ```

### GitHub Workflow

The project includes a GitHub Actions workflow for automated blog generation. To use it:

1. Go to your repository's **Actions** tab.
2. Select **Generate Blog** workflow.
3. Click **Run workflow**.
4. Provide optional inputs:
   - **topic**: Custom topic (leave blank to auto-generate).
   - **to_email**: Recipient email (leave blank to use repository secret `EMAIL_TO`).
5. Ensure the following secrets are set in repository settings:
   - `OPENAI_API_KEY`
   - `SERPER_API_KEY`
   - `SENDGRID_API_KEY`
   - `EMAIL_FROM`
   - `EMAIL_TO` (fallback if not provided in workflow)

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