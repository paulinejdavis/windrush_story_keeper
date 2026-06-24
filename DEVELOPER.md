**Developer Checklist**

Quick reference for running the project and adding/updating agents, tasks, and tools.

- **Ollama setup**
  - Pull model (one-time):
    - `ollama pull llama3.2:3b`
  - Confirm model available: `ollama list`
  - Start HTTP API (keep this terminal open): `ollama serve`
  - (Optional background): `nohup ollama serve > ~/ollama.log 2>&1 &`
  - Test API:
    ```bash
    curl -sS -X POST 'http://localhost:11434/api/generate' \
      -H 'Content-Type: application/json' \
      -d '{"model":"llama3.2:3b","prompt":"Hello","max_tokens":20}'
    ```

- **Project environment & run (from repo root)**
  - Activate venv: `source .venv/bin/activate` (or your env)
  - (If deps changed) install editable package: `python -m pip install -e .`
  - Run crew with demo inputs: `PYTHONPATH=src python -m windrush_story_keeper.main`

- **When adding/updating an agent or task**
  1. Add or update config entries in `src/windrush_story_keeper/config/agents.yaml` and `src/windrush_story_keeper/config/tasks.yaml`.
  2. Add `*.agent.md` spec files in `src/windrush_story_keeper/config/` for complex agents.
  3. Add agent wrappers (`@agent`) and task wrappers (`@task`) in `src/windrush_story_keeper/crew.py` mirroring existing patterns.
  4. If you add Python modules (tools/helpers), put them under `src/windrush_story_keeper/tools/` and import where needed.
  5. If task descriptions use templated variables (e.g., `{life_events}`), ensure kickoff `inputs` include placeholders in `main.py` before running tasks. Example:
     ```py
     inputs.setdefault("life_events", "")
     inputs.setdefault("themes", "")
     ```
  6. Run the smoke-check script and the crew (see below).

- **Smoke-check & troubleshooting**
  - Use `scripts/smoke_check.sh` to run the basic environment and API checks.
  - Common fixes:
    - Template KeyError: add placeholders to kickoff inputs or update task templates.
    - 404 / missing API: stop any `ollama run` sessions and start `ollama serve`.
    - Model not found: check `ollama list` and update the `model=` string in `crew.py`.
    - `crewai` import error: activate the correct venv and run `python -m pip install -e .`.

- **Commit & docs**
  - Add small, focused commits for config/code changes.
  - Update `DEVELOPER.md` or add short notes to the agent's `.agent.md` when behaviour or required inputs change.

Files:

- `src/windrush_story_keeper/crew.py` — agent/task wiring
- `src/windrush_story_keeper/config/*.yaml` — agent/task configs
- `src/windrush_story_keeper/config/*.agent.md` — agent specs
- `scripts/smoke_check.sh` — environment & API smoke checks

If you want, I can also add a GitHub Actions workflow that runs the smoke-check (without calling Ollama) on PRs.
