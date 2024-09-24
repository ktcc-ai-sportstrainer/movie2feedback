# AI Sports Trainer for Middle School Baseball

This project implements an AI-powered sports trainer system designed for middle school baseball teams. It uses language models (LLMs) to interact with users, create personalized training plans, and provide motivational support.

## Features

- Interactive conversation to gather user information
- Personalized training plan generation
- Motivational support messages
- Supports multiple LLM providers (OpenAI and Anthropic's Claude)

## Project Structure

```
ai_sports_trainer/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── interact_agent.py
│   │   ├── plan_agent.py
│   │   └── support_agent.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── user_data.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── llm_client.py
│   │   ├── openai_client.py
│   │   ├── claude_client.py
│   │   └── logger.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   └── main.py
├── data/
│   └── prompts/
│       ├── interact_prompt.json
│       ├── plan_prompt.json
│       └── support_prompt.json
├── .env
├── requirements.txt
└── run_main.sh
```

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-sports-trainer.git
   cd ai-sports-trainer
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables by creating a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_openai_api_key
   CLAUDE_API_KEY=your_claude_api_key
   LLM_PROVIDER=openai  # or 'claude'
   ```

## Usage

1. Ensure your virtual environment is activated.

2. Run the main script:
   ```
   ./run_main.sh
   ```
   or
   ```
   python src/main.py
   ```

3. Follow the prompts to interact with the AI Sports Trainer.

## Customization

- Modify the prompt files in `data/prompts/` to customize the behavior of each agent.
- Adjust the `Config` class in `src/config/config.py` to change default settings.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.