import click  # type: ignore


def summarize(input_text: str):
    # summarize the book
    summary = input_text + "summarized_"
    return summary


@click.command()
@click.option(
    "-t", required=False, type=click.File("r"), help="The text to be summarized"
)
@click.argument("words", type=str, nargs=-1)
def main(t, words):
    if t:
        input = t.read()
        summary = summarize(input)
        click.echo(summary)
        return True

    if words:
        print(words)
        return

    click.echo(
        "Nothing was provided. Please provide a paragraph or a text file to summarize."
    )


if __name__ == "__main__":
    main()
