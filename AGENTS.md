# AGENTS.md

Working notes for AI coding agents in baskingspot/homebrew-tap.

## What this is

The org's Homebrew tap, and nothing else. `Casks/` holds one generated cask per program the org publishes. The release workflow of each program writes its own cask here, through `release.yml` in `baskingspot/gh-actions`. This repo has no schedule, no generator, and no logic.

## Environment

The flake is the tool contract, from `baskingspot/nix`. The justfile is the command interface: `just lint`, `just ci`.

## Rules

- Never edit a cask by hand. The next release overwrites it. Change `scripts/render_cask.py` in `gh-actions`, and its test.
- Casks, not formulae. Our releases are prebuilt tarballs, which Homebrew's policy says are casks.
- The cask token is the repo name. Two repos must not share a token.
- Only the norm App writes to `main`, through the API, so the commits are signed. Don't push casks from a laptop.
- If the tap ever needs a rule that depends on who wrote a cask, remember that any repo holding norm's key can write any cask. That is the known trade-off, and a narrower App for the tap is on the internal-hygiene list.
- Commit messages are one line, `area: summary`, and every commit is signed.
