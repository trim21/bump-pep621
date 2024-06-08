from packaging.version import Version


def next_major(v: Version) -> Version:
    if not v.is_prerelease:
        return Version(f"{v.major + 1}.0.0")

    maybe = Version(f"{v.major}.0.0")
    if v < maybe:
        return maybe

    return Version(f"{v.major + 1}.0.0")


def next_minor(v: Version) -> Version:
    if not v.is_prerelease:
        return Version(f"{v.major}.{v.minor + 1}.0")

    maybe = Version(f"{v.major}.{v.minor}.0")
    if v < maybe:
        return maybe

    return Version(f"{v.major}.{v.minor + 1}.0")


def next_micro(v: Version) -> Version:
    if not v.is_prerelease:
        return Version(f"{v.major}.{v.minor}.{v.micro + 1}")

    maybe = Version(f"{v.major}.{v.minor}.{v.micro}")
    if v < maybe:
        return maybe

    return Version(f"{v.major}.{v.minor}.{v.micro + 1}")


def next_alpha(v: Version) -> Version:
    if not v.pre:
        return Version(str(next_micro(v)) + "a0")

    if v.pre[0] == "a":
        return Version(".".join(map(str, v.release)) + f"a{v.pre[1] + 1}")
    else:
        return Version(str(next_micro(Version(".".join(map(str, v.release))))) + "a0")


def next_beta(v: Version) -> Version:
    if not v.pre:
        return Version(str(next_micro(v)) + "b0")

    if v.pre[0] == "a":
        return Version(".".join(map(str, v.release)) + "b0")
    elif v.pre[0] == "b":
        return Version(".".join(map(str, v.release)) + f"b{v.pre[1] + 1}")
    else:
        return Version(str(next_micro(v)) + "b0")


def next_rc(v: Version) -> Version:
    if not v.pre:
        return Version(str(next_micro(v)) + "rc0")

    if v.pre[0] in ("a", "b"):
        return Version(".".join(map(str, v.release)) + "rc0")
    else:
        return Version(".".join(map(str, v.release)) + f"rc{v.pre[1] + 1}")


# def next_post(v: Version) -> Version: ...
