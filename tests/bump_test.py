import pytest

from bump_bep621.bump import (
    Version,
    next_alpha,
    next_major,
    next_micro,
    next_minor,
)


@pytest.mark.parametrize(
    "version_string,expected",
    [
        ("0.0.1", "1.0.0"),
        ("0.1.1", "1.0.0"),
        ("1.1.1", "2.0.0"),
        ("1.1.1a1", "2.0.0"),
        ("1.1.0b10", "2.0.0"),
        ("2.0.0a1", "2.0.0"),
        ("2.0.0rc2", "2.0.0"),
        ("2.0.0b4", "2.0.0"),
        ("2.0.0b4.post1", "2.0.0"),
    ],
)
def test_next_major(version_string, expected):
    version = Version(version_string)
    next_version = next_major(version)
    assert isinstance(next_version, Version)
    assert next_version > version
    assert str(next_version) == expected


@pytest.mark.parametrize(
    "version_string,expected",
    [
        ("0.0.1", "0.1.0"),
        ("0.1.1", "0.2.0"),
        ("1.1.1", "1.2.0"),
        ("1.1.1a1", "1.2.0"),
        ("1.2.0a1", "1.2.0"),
        ("1.2.0rc2", "1.2.0"),
        ("1.2.0b4", "1.2.0"),
        ("1.2.0b4.post1", "1.2.0"),
    ],
)
def test_next_minor(version_string, expected):
    version = Version(version_string)
    next_version = next_minor(version)
    assert isinstance(next_version, Version)
    assert next_version > version
    assert str(next_version) == expected


@pytest.mark.parametrize(
    "version_string,expected",
    [
        ("0.0.1", "0.0.2"),
        ("0.1.1", "0.1.2"),
        ("1.1.1", "1.1.2"),
        ("1.2.1a1", "1.2.1"),
        ("1.2.2a1", "1.2.2"),
        ("1.2.0a1", "1.2.0"),
        ("1.2.0rc2", "1.2.0"),
        ("1.2.0b4", "1.2.0"),
        ("1.2.0b4.post1", "1.2.0"),
    ],
)
def test_next_micro(version_string, expected):
    version = Version(version_string)
    next_version = next_micro(version)
    assert isinstance(next_version, Version)
    assert next_version > version
    assert str(next_version) == expected


@pytest.mark.parametrize(
    ["version_string", "expected"],
    [
        ("0.0.1", "0.0.2a0"),
        ("0.1.1", "0.1.2a0"),
        ("1.1.1", "1.1.2a0"),
        ("1.2.1a1", "1.2.1a2"),
        ("1.2.3a1", "1.2.3a2"),
        ("1.2.1b0", "1.2.2a0"),
    ],
)
def test_next_alpha(version_string, expected):
    version = Version(version_string)
    next_version = next_alpha(version)
    assert isinstance(next_version, Version)
    assert next_version > version
    assert str(next_version) == expected
