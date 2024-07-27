import json
import click
import requests


def summarize(input_text: str) -> str:
    """
    Summarize the given text into a single paragraph.

    Parameters:
    - input_text (str): The text to be summarized.

    Returns:
    - str: The summarized text or an error message if the request fails.
    """
    
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "qwen2:0.5b",
        "prompt": (
            f"Summarize the following text into a single paragraph:\n"
            f"```{input_text}```"
        ),
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an HTTPError for bad responses
        response_data = response.json()
        return response_data.get("response", "No response field in the data")

    except requests.RequestException as e:
        return f"Request failed: {str(e)}"


@click.command()
@click.option(
    "-t", "--text-file",
    type=click.File("r"),
    help="Path to a text file containing the text to be summarized."
)
@click.argument("text", nargs=-1)
def main(text_file, text):
    """
    CLI tool for summarizing text from a file or directly from command line arguments.

    Parameters:
    - text_file (file): The file to read the text from.
    - text (tuple of str): Text to be summarized provided as command line arguments.
    """
    if text_file:
        input_text = text_file.read()
    elif text:
        input_text = ' '.join(text)
    else:
        click.echo("Error: No input provided. Use -t for a file or provide text arguments.")
        return

    summary = summarize(input_text)
    click.echo(summary)


if __name__ == "__main__":
    main()
