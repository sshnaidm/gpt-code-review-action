# OpenAI Code Review Action

This action uses the OpenAI GPT-3 language model to review code changes in a pull request.

## Usage

To use this action, include it as a step in your workflow, after the checkout step. The action takes no inputs.

```yaml

on: [pull_request]

jobs:
  code-review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
      # This step checks out a copy of your repository.
      - uses: actions/checkout@v3
      # This step references the directory that contains the action.
      - uses: sshnaidm/gpt-code-review-action@v1
        with:
          openai-key: ${{ secrets.OPENAI_API_KEY }}
          # model: 'text-davinci-002'
          # prompt: 'You are helpful assistant is here to review the code. Please review the code change below and provide feedback.'

```

The action will post the OpenAI review as a comment on the pull request.

## Contributing

Contributions to this action are welcome! Please create an issue or pull request in the repository.

## License

This action is licensed under the Apache 2.0 License. See the LICENSE file for details
