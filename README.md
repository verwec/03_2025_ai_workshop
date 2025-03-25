# OpenAI Chat Bot

A simple Python application that interacts with OpenAI's Chat Completions API.

## Prerequisites

- Python 3.6 or higher
- OpenAI Python package
- OpenAI API key

## Installation

1. Clone this repository
2. Install the required package:
```bash
pip install openai
```

## Setting up your OpenAI API Key

Before running the application, you need to set up your OpenAI API key as an environment variable. Here's how to do it on different operating systems:

### Linux/macOS

Temporary (current terminal session only):
```bash
export OPENAI_API_KEY='your-api-key-here'
```

Permanent:
1. Open your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.):
```bash
nano ~/.bashrc  # or ~/.zshrc for Zsh
```
2. Add the following line:
```bash
export OPENAI_API_KEY='your-api-key-here'
```
3. Save and reload the configuration:
```bash
source ~/.bashrc  # or source ~/.zshrc for Zsh
```

### Windows

Temporary (current Command Prompt session only):
```cmd
set OPENAI_API_KEY=your-api-key-here
```

Permanent:
1. Using Command Prompt (Run as Administrator):
```cmd
setx OPENAI_API_KEY "your-api-key-here"
```
2. Or through Windows GUI:
   - Press Win + X and select "System"
   - Click on "Advanced system settings"
   - Click on "Environment Variables"
   - Under "User variables" click "New"
   - Variable name: OPENAI_API_KEY
   - Variable value: your-api-key-here
   - Click "OK" to save

## Usage

Run the application:
```bash
python app.py
```

## Note

Make sure to replace 'your-api-key-here' with your actual OpenAI API key. Never commit your API key to version control. If you accidentally expose your API key, immediately rotate it in your OpenAI account settings. 