from rich.console import Console
from rich.markdown import Markdown


def show_statuses_statistics():
    statistics_file = "./statistics.md"

    with open(statistics_file, "r") as f:
        Console().print(Markdown(f.read()))
