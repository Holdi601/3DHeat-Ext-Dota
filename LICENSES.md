# Third-party licences

This tool is MIT licensed ([`LICENSE`](LICENSE)). What it uses or runs, and
under which licence; each package's own source is what counts, not this file.

| Software | Licence | How it is used |
|---|---|---|
| numpy | BSD-3-Clause | a dependency, installed by pip |
| pytest | MIT | development only: the tests |
| Source2Viewer CLI (ValveResourceFormat) | MIT | **not bundled**: the user downloads it from github.com/ValveResourceFormat/ValveResourceFormat and this tool runs it as a separate program to read the user's own installed Dota 2; none of its code is in this repository |

## The game's files

Dota 2 belongs to Valve. This repository holds no file of the game and no
level made from one; the tool reads the copy the user installed, on the user's
machine, and the level it writes stays there. See
[Terms and licence](https://holdi601.github.io/3DHeat-Ext-Dota/terms.html).
