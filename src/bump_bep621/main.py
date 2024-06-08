from __future__ import annotations

import click
from packaging.version import Version
from tomlkit.toml_file import TOMLFile

from bump_bep621.bump import (
    next_alpha,
    next_beta,
    next_major,
    next_micro,
    next_minor,
    next_rc,
)

orders = {
    "major": 0,
    "minor": 1,
    "micro": 2,
    "a": 3,
    "b": 4,
    "rc": 5,
}


@click.command(no_args_is_help=True)
@click.argument("target")
def main(target: tuple[str, ...]) -> None:
    """
    TARGET: bumping target, could be major/minor/micro/a/b/rc

    example: $ pyproject-bump major
    """

    f = TOMLFile("pyproject.toml")
    data = f.read()
    old_version = data["project"]["version"]

    v = Version(old_version)

    if target == "major":
        v = next_major(v)
    elif target == "minor":
        v = next_minor(v)
    elif target == "micro":
        v = next_micro(v)
    elif target == "a":
        v = next_alpha(v)
    elif target == "b":
        v = next_beta(v)
    elif target == "rc":
        v = next_rc(v)
    else:
        raise Exception(f"unknown target {target!r}")

    click.echo(f"write new version '{v!s}'")

    data["project"]["version"] = str(v)

    f.write(data)
