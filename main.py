import click


@click.command()
@click.option("-t", required=False, type=click.File('r'), help="The text to be summarized")
@click.argument("words", type=str, nargs=-1)
def main(t, words):
    if t:
        input = t.read()
        click.echo(input)
        return True

    if words:
        print(words)
    

if __name__ == "__main__":
    main()
