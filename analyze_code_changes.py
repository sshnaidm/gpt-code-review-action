# Copyright 2023 Sagi Shnaidman (sshnaidm at gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import openai
import sys

# Set up OpenAI credentials
if not os.environ.get("OPENAI_API_KEY"):
    print("No OpenAI API key found")
    sys.exit(1)
openai.api_key = os.environ["OPENAI_API_KEY"]

# Analyze the code changes with OpenAI
model_engine = os.environ["MODEL"]
code = sys.stdin.read()
prompt = os.environ["PROMPT"] + "\n```\n" + code + "\n```"
if len(prompt) > 4000:
    print(f"Prompt too long for OpenAI: {len(prompt)} characters, "
          "sending only first 4000 characters")
    prompt = prompt[:4000]

kwargs = {'model': model_engine}
kwargs['temperature'] = 0.5
kwargs['max_tokens'] = 1024
kwargs['messages'] = [
    {"role": "system",
     "content": "You are a helpful assistant and code reviewer."},
    {"role": "assistant", "content": ""},
    {"role": "user", "content": prompt},
]
try:
    response = openai.ChatCompletion.create(**kwargs)
    if response.choices:
        if 'text' in response.choices[0]:
            review_text = response.choices[0].text.strip()
        else:
            review_text = response.choices[0].message.content.strip()
    else:
        review_text = f"No correct answer from OpenAI!\n{response.text}"
except Exception as e:
    review_text = f"OpenAI failed to generate a review: {e}"

print(f"{review_text}")
