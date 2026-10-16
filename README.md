<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/static/logo-dark.svg">
    <img src="docs/static/logo.svg" alt="homebrew-tap" height="48">
  </picture>
</h1>

Homebrew casks for the programs baskingspot publishes.

## Install

```sh
brew tap baskingspot/tap
brew install --cask zigdoc
```

Homebrew 6 and later asks you to trust a third-party tap before it runs the tap's code. Follow its prompt, or run `brew trust baskingspot/tap`.

Each cask installs the program's release tarball for your platform. The release binaries are not signed or notarized, so the cask clears macOS's quarantine flag after install. Check a download yourself with `gh attestation verify FILE -R baskingspot/PROGRAM`.

## Where the casks come from

This repository only holds them. Nothing here runs on a schedule, and nothing here builds anything. When a program is released, its release workflow, `release.yml` in [baskingspot/gh-actions](https://github.com/baskingspot/gh-actions), writes the cask from that release, installs it on Homebrew on Linux and on macOS, runs the program, and only then commits it to `main` as the norm bot. A cask that fails the install never gets here.

Don't edit `Casks/` by hand. The next release overwrites it. To change a cask, change the generator, `scripts/render_cask.py` in `gh-actions`.

## Work on it

`nix develop` provides the tools, and `just ci` runs the lint.

## License

MIT. See `LICENSE`. The logo files in `docs/static/` are baskingspot marks and are not covered by it. See `docs/static/LICENSE`.

## How it's made

Built with LLM assistance. [How, in detail](https://github.com/baskingspot/.github/blob/main/docs/AI.md).

<a href="https://github.com/baskingspot"><img src="https://raw.githubusercontent.com/baskingspot/.github/main/brand/assets/badge.svg" alt="baskingspot" height="24"></a>
