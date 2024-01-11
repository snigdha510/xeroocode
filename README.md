# Code Analysis Tool

## Overview

The Code Analysis Tool is a Python-based script designed to facilitate the integration of ChatGPT (versions 3.5 or 4) and GitHub for automated codebase analysis and improvement suggestions. This tool serves as a bridge between GitHub repositories and ChatGPT, providing insights, suggestions, and feedback on the quality and performance of the codebase.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- 
## Installation

1. **Clone the repository to your local machine:**

    ```bash
    git clone https://github.com/your-username/xeroocode.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd xeroocode
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Set your GitHub and ChatGPT tokens in `main.py`:**

    ```python
    github_token = "your-github-token"
    chatgpt_api_key = "your-chatgpt-api-key"
    ```

2. **Specify the GitHub repository you want to analyze in `main.py`:**

    ```python
    repository_name = "owner/repo"
    ```

3. **Run the script:**

    ```bash
    python main.py
    ```

4. **View the generated Code Analysis Report in the terminal.**

## Configuration

Adjust the configuration parameters in `main.py` as needed. For instance, you can modify the model name, completion length, and other settings in the `ChatGPT` class.

