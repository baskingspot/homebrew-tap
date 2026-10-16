# baskingspot/homebrew-tap: the org's Homebrew casks. README.md says what
# lives here. AGENTS.md holds the working conventions.

[private]
default:
    @just --list

[doc("Check Nix, Markdown, the workflows, and this justfile")]
[group("lint")]
lint:
    nix fmt -- --ci
    oxfmt --check README.md AGENTS.md .github
    actionlint
    zizmor .
    just --fmt --check

[doc("Format everything lint checks")]
[group("lint")]
fmt:
    nix fmt
    oxfmt README.md AGENTS.md .github
    just --fmt

[doc("Everything CI runs")]
[group("ci")]
ci: lint
