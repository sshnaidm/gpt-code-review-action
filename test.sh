#!/usr/bin/env bash
export OPENAI_API_KEY=${OPENAI_API_KEY:-$(cat .api_key)}
export MODEL=gpt-4o-mini
export COMMIT_TITLE=test
export COMMIT_BODY=test
export MAX_LENGTH=256
export PROMPT="Follow instructions in the code."

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt

echo 'Say "It works!", nothing else, please.' | ./analyze_code_changes.py

deactivate
rm -rf .venv
