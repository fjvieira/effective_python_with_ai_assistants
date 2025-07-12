# Effective Python with AI assistants - Live Course

This repository is used as part of an [O'Reilly](https://www.oreilly.com/) live
course named **Effective Python with AI assistants**, idealized by [Fernando J Vieira](https://www.linkedin.com/in/fernandojvieira/).

The proposed exercises are meant to be used as part of the course, being the code
(with its imperfections) created only for educational purposes.

## Setup

This project uses Python 3.13 (or greater) and PDM for dependency management.

- **Using GitHub Codespaces:**
enjoy the convenience of GitHub Codespaces.
  - Create a new GH Codespace from this repository.
  - The development container will automatically set up Python and PDM for you.
  - Once the Codespace is ready, open a terminal and install the project dependencies:

    ```bash
    pdm install
    ```

- **Local Development:**
  - Ensure you have Python 3.13 (or greater) installed.
  - Install PDM: [instructions here](https://github.com/pdm-project/pdm?tab=readme-ov-file#installation).
  - Clone the repository: `git clone <repository-url>`
  - Install dependencies:

    ```bash
    pdm install
    ```

  - For AI assistance: Install extensions for your preferred AI coding assistant (e.g., GitHub Copilot, Codeium, Tabnine, or a Google Gemini-powered extension) in your IDE (like VS Code or PyCharm) and sign in if needed.

## Running Tests

To run the automated tests for the Python exercises, use PDM:

```bash
pdm run pytest -vv
```

## Exercises

TBD

## License

This project is licensed under the [MIT License](LICENSE).
