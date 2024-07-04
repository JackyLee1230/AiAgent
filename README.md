# General AI Agent Framework with CrewAI

*Example AI Agent using [CrewAI](https://www.crewai.com/) and Local LLMS (LM Studio/Ollama)*

## Features

- **Flexible Task Management**: Supports a wide range of tasks, including data analysis, report generation, and more.
- **Modular Design**: Easily extendable to include new AI models and tools.
- **Detailed Logging**: Offers verbose logging options for thorough process tracking.

## How It Works

The framework operates by defining `Tasks` that are processed by `Agents`. Each task can specify its requirements, such as the AI model to use, the expected output, and any necessary tools:

1. **Define Tasks**: Users define tasks with specific goals, inputs, and expected outputs.
2. **Configure Agents**: Agents are configured with the necessary models and tools to perform the tasks.
3. **Process Tasks**: The framework processes tasks sequentially or in parallel, depending on the configuration.
4. **Generate Results**: Outputs, such as analysis reports, can be displayed in different formats, including MarkDown and PDF, for easy dissemination.

## Example Use Case: Game Analysis

As an example, this framework can analyze the gaming industry, identifying key trends and successful elements of recent game releases. This involves tasks like data collection, analysis using the Mistral7b model, and compiling findings into a Markdown report.

## Usage

To use the framework, follow these steps:

1. **Setup**: Ensure all dependencies, including LM Studio (with a model running using local server feature) and CrewAI, are correctly installed and configured.
2. **Define Tasks**: Create tasks according to your specific requirements.
3. **Run Framework**: Execute the framework to process the defined tasks.
4. **Review Reports**: Check the generated Markdown reports for insights and findings.

## Installation

This framework requires Python 3.10 or later. Dependencies can be installed via `pip`:

Modify the `.env` file to change the model and server settings.
```bash
OPENAI_MODEL_NAME='TheBloke/Mistral-7B-Instruct-v0.2-GGUF'
OPENAI_API_BASE="http://localhost:1234/v1"
```

```bash
pip install -r requirements.txt
```

```bash
python main.py
```