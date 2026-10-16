"""Tests for update.py. They need no network: the pure parts only."""

import unittest

import update

PROGRAM = update.Program(
    repo="zigdoc",
    binary="zigdoc",
    description="A tool to view docs",
    homepage="https://example.com/zigdoc",
    targets=[
        update.Target("linux", "intel", "linux-x64"),
        update.Target("linux", "arm", "linux-arm64"),
        update.Target("macos", "arm", "macos-arm64"),
    ],
)
SUMS = {
    "zigdoc-v1.2.3-linux-x64.tar.gz": "a" * 64,
    "zigdoc-v1.2.3-linux-arm64.tar.gz": "b" * 64,
    "zigdoc-v1.2.3-macos-arm64.tar.gz": "c" * 64,
}


class RenderTest(unittest.TestCase):
    def test_a_cask_has_every_platform_with_its_hash(self) -> None:
        cask = update.render(PROGRAM, "v1.2.3", SUMS)
        self.assertIn('cask "zigdoc" do', cask)
        self.assertIn('version "1.2.3"', cask)
        for char in "abc":
            self.assertIn(f'sha256 "{char * 64}"', cask)
        self.assertIn("on_macos do\n    on_arm do", cask)
        self.assertIn("on_linux do\n    on_intel do", cask)
        self.assertIn('binary "zigdoc-v#{version}-macos-arm64/zigdoc"', cask)

    def test_the_url_follows_the_version_so_a_bump_changes_one_field(self) -> None:
        cask = update.render(PROGRAM, "v1.2.3", SUMS)
        self.assertIn(
            "/releases/download/v#{version}/zigdoc-v#{version}-linux-x64.tar.gz", cask
        )

    def test_there_is_no_intel_mac_block_when_no_target_builds_for_it(self) -> None:
        cask = update.render(PROGRAM, "v1.2.3", SUMS)
        macos = cask.split("on_macos do")[1].split("on_linux do")[0]
        self.assertNotIn("on_intel", macos)

    def test_macos_quarantine_is_removed_after_install(self) -> None:
        cask = update.render(PROGRAM, "v1.2.3", SUMS)
        self.assertIn("com.apple.quarantine", cask)
        self.assertIn("if OS.mac?", cask)

    def test_a_missing_checksum_stops_the_cask(self) -> None:
        sums = dict(SUMS)
        del sums["zigdoc-v1.2.3-linux-arm64.tar.gz"]
        with self.assertRaises(ValueError):
            update.render(PROGRAM, "v1.2.3", sums)

    def test_the_marker_is_the_first_line(self) -> None:
        self.assertTrue(
            update.render(PROGRAM, "v1.2.3", SUMS).startswith(update.MARKER)
        )


class ParseTest(unittest.TestCase):
    def test_sums_by_file_name(self) -> None:
        text = f"{'a' * 64}  one.tar.gz\n{'b' * 64} *two.tar.gz\nnot a sum\n"
        self.assertEqual(
            update.parse_sums(text), {"one.tar.gz": "a" * 64, "two.tar.gz": "b" * 64}
        )

    def test_zig_targets_map_to_platforms(self) -> None:
        self.assertEqual(update.platform_of("x86_64-linux-musl"), ("linux", "intel"))
        self.assertEqual(update.platform_of("aarch64-linux-gnu"), ("linux", "arm"))
        self.assertEqual(update.platform_of("aarch64-macos"), ("macos", "arm"))

    def test_an_unknown_target_is_an_error_not_a_skip(self) -> None:
        with self.assertRaises(ValueError):
            update.platform_of("riscv64-linux-musl")

    def test_program_from_config_drops_the_trailing_period(self) -> None:
        repo = {
            "name": "x",
            "description": "Does a thing.",
            "homepage": "",
            "html_url": "https://github.com/o/x",
        }
        config = {
            "binary": "x",
            "targets": [{"target": "aarch64-macos", "asset": "macos-arm64"}],
        }
        program = update.program_from(repo, config)
        self.assertEqual(program.description, "Does a thing")
        self.assertEqual(program.homepage, "https://github.com/o/x")


if __name__ == "__main__":
    unittest.main()
