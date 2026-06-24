# WindrushStoryKeeper Crew

Welcome to the WindrushStoryKeeper Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

If you use a cloud LLM (for example OpenAI), add your `OPENAI_API_KEY` into the `.env` file. If you're using a local Ollama instance (recommended for offline runs), no cloud API key is required — follow the Ollama steps below.

- Modify `src/windrush_story_keeper/config/agents.yaml` to define your agents
- Modify `src/windrush_story_keeper/config/tasks.yaml` to define your tasks
- Modify `src/windrush_story_keeper/crew.py` to add your own logic, tools and specific args
- Modify `src/windrush_story_keeper/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

### Using Ollama (local LLM)

This project is preconfigured to support a local Ollama server. If you prefer running models locally, do the following:

1. Install Ollama following the instructions for macOS: https://ollama.com/docs/installation
2. Pull a model (example):

```bash
ollama pull llama3.2:3b
```

3. Start the Ollama server:

```bash
ollama serve
```

4. Confirm the server is reachable at `http://localhost:11434/api/generate` (the included `scripts/smoke_check.sh` performs this check).

Note: `src/windrush_story_keeper/crew.py` is configured to use `ollama_llm` with `base_url="http://localhost:11434"` — update if your server uses a different host/port.

## Running locally

Recommended steps to run the project locally (use your project venv if you have one):

1. Create and activate a virtual environment (or activate your existing venv):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Upgrade packaging tooling and install the project in editable mode:

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -e .
```

3. Run the smoke checks to verify `crewai` import and local Ollama API connectivity:

```bash
bash scripts/smoke_check.sh
```

If the smoke checks pass, run the crew entrypoint:

```bash
PYTHONPATH=src python -m windrush_story_keeper.main
```

Notes:

- If `python3 -m venv` fails on your machine, activate an existing venv and run step 2.
- The repo now includes a `scripts/smoke_check.sh` helper to validate the environment and Ollama HTTP API.
- I pushed recent changes (follow-up agent, tasks, and tooling) to `origin/main`.

## Related projects

- Windrush Cohort & Compensation Analysis: [paulinejdavis/postWindrush](https://github.com/paulinejdavis/postWindrush) — a BigQuery + Power BI project that models Windrush-era cohorts, analyses compensation scheme outcomes, and provides dashboards and reproducible SQL for cohort and demographic analysis. Useful for data-driven context and sourcing public datasets.
- Windrush iOS wireframes and prototype: [paulinejdavis/windrush](https://github.com/paulinejdavis/windrush) — an iOS project with visual wireframes and next-step ideas for storytelling and mobile presentation of Windrush narratives. Useful for UI inspiration and community-facing storytelling features.

This command initializes the windrush_story_keeper Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The windrush_story_keeper Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the WindrushStoryKeeper Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
