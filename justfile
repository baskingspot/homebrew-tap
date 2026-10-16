# baskingspot/homebrew-tap: Homebrew casks for the programs the org publishes,
# written by tools/update.py. README.md says how it works. AGENTS.md holds the
# working conventions.

[private]
default:
    @just --list

[doc("Run the generator's tests, which need no network")]
[group("test")]
test:
    cd tools && python3 -m unittest -v test_update

[doc("Check Python (ruff, ty), Nix, Markdown, the workflows, and this justfile")]
[group("lint")]
lint:
    ruff check tools
    ruff format --check tools
    ty check tools
    nix fmt -- --ci
    oxfmt --check README.md AGENTS.md .github
    actionlint
    zizmor .
    just --fmt --check

[doc("Format everything lint checks")]
[group("lint")]
fmt:
    ruff format tools
    nix fmt
    oxfmt README.md AGENTS.md .github
    just --fmt

[doc("Everything CI runs")]
[group("ci")]
ci: test lint

[doc("Write Casks/ from the org's latest releases, the way the hourly workflow does. Needs gh")]
[group("update")]
update:
    python3 tools/update.py
