# OpenAI Code Review Action

This action uses the OpenAI GPT-3 language model to review code changes in a pull request.

## Usage

To use this action, include it as a step in your workflow, after the checkout step.

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
      - uses: sshnaidm/gpt-code-review-action@v2.0
        with:
          openai-key: ${{ secrets.OPENAI_API_KEY }}
          # model: 'gpt-4.1'
          # max-length: 8000
          # prompt: 'Only suggest performance improvements for this code.'
          # post-if-error: false
          # review-title: '# My AI bot review'

```

The action will post the OpenAI review as a comment on the pull request.

### Requierements

To post comments in Pull Requests, the job requires additional permissions: `pull-requests: write`. However, since this permission implies "explicit deny," we also need to mention the default permission `contents: read`.

### Inputs

`github-token`: The token used to authenticate with the GitHub API (optional, will take a default `${{ github.token }}`).

`model`: The OpenAI language model to use for code review (optional, with a default `gpt-4.1-mini`).

`openai-key`: The OpenAI API key used for authentication (**required**).

`prompt`: The prompt to use for the analysis (optional, with a default value).

`max-length`: The diff that is send to OpenAI for review is cut off after 8000 characters by default. With this parameter you can adjust this limit.

`post-if-error`: Whether to post a comment if there was an error (optional, with a default `true`).

`review-title`: The title to use for the review comment (optional, with a default `Code Review by OpenAI`).

### Limitations

Currently, only the first 8000 characters are sent due to OpenAI's limitations. Later, we will send the text in chunks, and each part will be reviewed separately.

## Contributing

Contributions to this action are welcome! Please create an issue or pull request in the repository.

## Testing

You can run `./test.sh` that just verifies that the Python code is able to send something to the cheapest OpenAI model and get something out of it. (The model is kindly asked to tell "It works!").

The test expects you have Python 3.10 available as it is the one used in the action itself. There is an appropriate file `.python_version` for [pyenv](https://github.com/pyenv/pyenv).

## License

This action is licensed under the Apache 2.0 License. See the LICENSE file for details
