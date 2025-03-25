# Chat Application with Context-Aware Responses

This is a web-based chat application that provides context-aware responses using OpenAI's GPT-4 model. The application consists of a Flask backend and a modern HTML/JavaScript frontend.

## Features

- Real-time chat interface with a clean, modern design
- Context-aware responses using vector similarity search
- Support for chat history
- Responsive design that works on both desktop and mobile
- Loading indicators for better user experience
- Error handling and graceful fallbacks

## Prerequisites

- Python 3.x
- OpenAI API key
- Required Python packages (listed in requirements.txt)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd chat-live
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

4. Start the Flask server:
```bash
python app.py
```

The server will start on `http://localhost:5001`

5. Open `index.html` in your web browser to access the chat interface.

## Project Structure

- `app.py`: Flask backend server with chat endpoint
- `index.html`: Frontend chat interface
- `vectorstore_example.py`: Vector store implementation for context retrieval
- `requirements.txt`: Python package dependencies

## API Endpoints

### POST /chat

Sends a message to the chat endpoint and receives a context-aware response.

Request body:
```json
{
    "query": "Your message here"
}
```

Response:
```json
{
    "message": "AI response here"
}
```

## Usage

1. Type your message in the input field
2. Press Enter or click the Send button
3. Wait for the AI's response
4. The conversation history will be displayed in the chat window

## Technical Details

- The application uses Flask for the backend server
- CORS is enabled to allow frontend-backend communication
- The chat interface is built with vanilla JavaScript and modern CSS
- Context retrieval is implemented using vector similarity search
- OpenAI's GPT-4 model is used for generating responses

## Error Handling

The application includes error handling for:
- Network connectivity issues
- API request failures
- Invalid responses
- Empty messages

## Contributing

Feel free to submit issues and enhancement requests! 