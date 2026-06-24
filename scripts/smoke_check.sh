#!/usr/bin/env bash
set -euo pipefail

echo "Smoke check: environment and Ollama API"

# 1) Check venv is active (VIRTUAL_ENV set) or warn
if [ -z "${VIRTUAL_ENV:-}" ]; then
  echo "WARNING: No virtualenv detected. Activate your project venv before running full tests."
else
  echo "Virtualenv detected: $VIRTUAL_ENV"
fi

# 2) Check crewai import
echo -n "Checking crewai import... "
python - <<'PY'
try:
    import crewai
    print('OK', crewai.__version__)
except Exception as e:
    print('FAILED:', e)
    raise SystemExit(2)
PY

# 3) Test Ollama API generate endpoint
MODEL=${1:-llama3.2:3b}
echo "Testing Ollama HTTP API for model $MODEL"
curl -sS -X POST 'http://localhost:11434/api/generate' \
  -H 'Content-Type: application/json' \
  -d "{\"model\":\"$MODEL\",\"prompt\":\"Hello\",\"max_tokens\":20}" || {
  echo "\nOllama API test failed. Is 'ollama serve' running?"
  exit 3
}

echo "Ollama API responded."

echo "Smoke checks passed (venv check, crewai import, Ollama API)."
echo "You can now run: PYTHONPATH=src python -m windrush_story_keeper.main"
