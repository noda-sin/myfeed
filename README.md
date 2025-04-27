# MyFeed

A customizable news aggregator that fetches, summarizes, and delivers database-related news to your Slack workspace.

## Overview

MyFeed is an automated tool that:
1. Aggregates news from multiple database-related RSS feeds
2. Uses OpenAI to generate concise summaries
3. Delivers daily updates to a Slack channel

## Features

- Configurable RSS feed sources
- Timezone-aware news filtering (last 24 hours)
- AI-powered summarization using OpenAI's GPT models
- Slack integration for daily delivery
- Scheduled execution via GitHub Actions

## Setup

### Prerequisites

- Python 3.13+
- OpenAI API key
- Slack webhook URL

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd myfeed
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with the following variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SLACK_WEBHOOK_URL=your_slack_webhook_url
   ```

### Configuration

Edit `config.yaml` to customize your feed sources, timezone, and other settings:

```yaml
timezone: Asia/Tokyo
openai_model: "gpt-4o"
feeds:
- url: https://dbweekly.com/rss/
max_items_per_feed: 20
```

## Usage

### Local Execution

Run the script manually:

```
python main.py
```

### Automated Execution with GitHub Actions

The repository includes a GitHub Actions workflow that runs the script daily at midnight. To use this:

1. Add your API keys as GitHub repository secrets:
   - `OPENAI_API_KEY`
   - `SLACK_WEBHOOK_URL`

2. The workflow will automatically run according to the schedule, or you can trigger it manually from the Actions tab.

## Project Structure

- `main.py` - Main application entry point
- `aggregator.py` - Handles RSS feed fetching and processing
- `summarizer.py` - Generates summaries using OpenAI
- `notifier.py` - Sends notifications to Slack
- `config.yaml` - Configuration file for feeds and settings
- `.github/workflows/daily_job.yaml` - GitHub Actions workflow definition

## License

[Add license information here]
