<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/static/logo-dark.svg">
    <img src="docs/static/logo.svg" alt="homebrew-tap" height="48">
  </picture>
</h1>

Homebrew casks for the programs baskingspot publishes, written and tested automatically from each release.

## Install

```sh
brew tap baskingspot/tap
brew install --cask zigdoc
```

Homebrew 6 asks you to trust a third-party tap before it runs the tap's code. Follow its prompt, or run `brew trust baskingspot/tap`.

Each cask installs the program's release tarball for your platform. The release binaries are not signed or notarized, so the cask clears macOS's quarantine flag after install. Check a download yourself with `gh attestation verify FILE -R baskingspot/PROGRAM`.

## How a program gets a cask

It doesn't ask. A baskingspot repo that publishes releases has `.github/release.yaml`, which lists its targets. Every hour, `update.yml` in this repo finds each such repo, reads its latest release and `SHA256SUMS`, and writes `Casks/<repo>.rb`. It then installs every changed cask on Homebrew itself, on Linux and on macOS, runs the program, checks the quarantine flag is gone, and commits to `main` only if all of that passes. A bad cask never lands, and the run goes red.

Nothing in the program's repo, and no token, is involved. A new release shows up here within the hour.

`Casks/` is generated. Don't edit it. Change `tools/update.py`.

## Work on it

`nix develop` provides the tools, and `just ci` runs the generator's tests and the lint. `just update` writes `Casks/` from the live releases, the way the workflow does, and needs `gh`.

## License

MIT. See `LICENSE`. The logo files in `docs/static/` are baskingspot marks and are not covered by it. See `docs/static/LICENSE`.

## How it's made

Built with LLM assistance. [How, in detail](https://github.com/baskingspot/.github/blob/main/docs/AI.md).

<a href="https://github.com/baskingspot"><img src="https://raw.githubusercontent.com/baskingspot/.github/main/brand/assets/badge.svg" alt="baskingspot" height="24"></a>
