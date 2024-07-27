# Text Summarizer CLI Tool

This is a command-line interface (CLI) tool for summarizing text into a single paragraph using a remote API service. The tool supports summarizing text either from a file or directly from command line arguments.

## Features

- Summarize text from a file or command line input.
- Handles errors and provides informative messages.

## Prerequisites

- Python 3.6 or later
- `requests` library
- `click` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/text-summarizer-cli.git
    cd text-summarizer-cli
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    Or, you can install the required packages directly:

    ```bash
    pip install requests click
    ```


## Usage


### Summarizing Text from a File

To summarize text from a file, use the `-t` option followed by the path to the text file:

  ```bash
  python script.py -t path/to/your/textfile.txt
  ```


### Summarizing Text from Command Line Arguments

To summarize text provided directly in the command line, simply provide the text as arguments:

  ```bash
  python script.py "This is the text you want to summarize."
  ```


### Examples

  #### Summarize a text file:

        python script.py -t myfile.txt

  #### Summarize text from the command line:


        python script.py "This is a sample text that will be summarized."


### Error Handling

If there are any issues with the request or input, appropriate error messages will be displayed. 

Ensure that the API endpoint is accessible and the provided text is valid.


### API Endpoint

The tool sends requests to a local API server at http://localhost:11434/api/generate. 

Ensure that the API service is running and accessible before using the CLI tool.
