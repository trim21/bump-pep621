# bump pep 621 version

```shell
pipx install bump-bep621
```

given current version `0.1.2`

```shell
pbump major # -> 1.0.0
pbump major # -> 1.0.0a0
pbump minor # -> 0.2.0
pbump minor rc # -> 0.2.0rc0
pbump micro # -> 0.1.3
pbump micro a # -> 0.1.3a0
pbump a # -> 0.1.3a0
pbump b # -> 1.0.0
pbump rc # -> 1.0.0
```