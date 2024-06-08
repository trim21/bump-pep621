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
@click.argument("target", nargs=-1)
def main(target: tuple[str, ...]) -> None:
    """
    TARGET: bumping target, could be major/minor/micro/a/b/rc

    example: $ pbump major
    """

    for t in target:
        assert t in orders

    assert (
        len(set(target) & {"major", "minor", "micro"}) <= 1
    ), "can not combine major/minor/micro"
    assert len(set(target) & {"a", "b", "rc"}) <= 1, "can not combine a/b/rc"

    targets = sorted(target, key=lambda k: orders[k])

    f = TOMLFile("pyproject.toml")
    data = f.read()
    old_version = data["project"]["version"]

    v = Version(old_version)

    for t in targets:
        if t == "major":
            v = next_major(v)
        elif t == "minor":
            v = next_minor(v)
        elif t == "micro":
            v = next_micro(v)
        elif t == "a":
            v = next_alpha(v)
        elif t == "b":
            v = next_beta(v)
        elif t == "rc":
            v = next_rc(v)
        else:
            raise Exception(f"unknown target {t!r}")

    click.echo(f"write new version '{v!s}'")

    data["project"]["version"] = str(v)

    f.write(data)
