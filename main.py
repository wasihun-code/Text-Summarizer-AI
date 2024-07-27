import json
import click  # type: ignore
import requests  # type: ignore


def summarize(input_text: str):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "qwen2:0.5b",
        "prompt": f"""Summarize the text with one paragraph inside the triple quotes
                    and return only the response ```{input_text}```""",
        "stream": False}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        # print("successful request. now parsing response")
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        return actual_response

    else:
        return "Error: " + response.status_code + response.text


@click.command()
@click.option(
    "-t",
    required=False,
    type=click.File("r"),
    help="The text to be summarized"
)
@click.argument("words", type=str, nargs=-1)
def main(t, words):
    if t:
        input_text = t.read()
        click.echo(summarize(input_text=input_text))
        return

    if words:
        input_text = ' '.join(list(words))
        click.echo(summarize(input_text=input_text))
        return

    click.echo("Nothing was provided. Please provide a paragraph or a text file to summarize.")


if __name__ == "__main__":
    main()
