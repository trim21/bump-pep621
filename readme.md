# bump pep 621 version

```shell
pipx install bump-bep621
```

given current version `0.1.2`

```shell
pyproject-bump major # -> 1.0.0
pyproject-bump minor # -> 0.2.0
pyproject-bump micro # -> 0.1.3
pyproject-bump a # -> 0.1.3a0
pyproject-bump b # -> 0.1.3b0
pyproject-bump rc # -> 0.1.3rc0
```
