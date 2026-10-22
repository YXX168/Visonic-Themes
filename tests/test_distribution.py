"""Check installed CSS dependencies and exercise the Unix installer in isolation."""
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class DistributionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)

    @unittest.skipIf(os.name == 'nt', 'Bash installer is for macOS/Linux')
    def test_install_preserves_other_themes_backs_up_bridge_and_copies_dependencies(self):
        target = self.base / 'custom themes'
        target.mkdir()
        (target / 'other.css').write_text('user theme')
        (target / 'github.user.css').write_text('user bridge')
        result = subprocess.run(['bash', str(ROOT / 'install.sh'), str(target)], cwd=self.base,
                                capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual((target / 'other.css').read_text(), 'user theme')
        self.assertEqual((target / 'github.user.css.bak').read_text(), 'user bridge')
        self.assertIn('visonic-streamer-nebula.css', (target / 'github.user.css').read_text())
        documented = set(re.findall(r'`(visonic-[\w-]+\.css)`', (ROOT / 'README.md').read_text()))
        self.assertEqual({p.name for p in target.glob('visonic-*.css')}, documented)
        for source in [*ROOT.glob('themes/*.css'), *ROOT.glob('visonic-fonts/**/*.css')]:
            installed = target / source.relative_to(ROOT / 'themes' if source.parent.name == 'themes' else ROOT)
            self.assertEqual(installed.read_bytes(), source.read_bytes())
            text = re.sub(r'/\*.*?\*/', '', source.read_text(), flags=re.S)
            # Consume a complete quoted data URL, including SVG's nested url().
            refs = [next((value for value in match if value), '') for match in
                    re.findall(r'url\(\s*(?:"([^"]*)"|\'([^\']*)\'|([^)]*))\s*\)', text)]
            refs += re.findall(r'@import\s+[\'"]([^\'"]+)', text)
            for ref in refs:
                url = urlsplit(ref)
                if not url.scheme and not url.netloc and url.path and not ref.startswith('#'):
                    self.assertTrue((installed.parent / unquote(url.path)).is_file(), f'{installed.name}: missing {ref}')

    @unittest.skipIf(os.name == 'nt', 'Bash installer is for macOS/Linux')
    def test_linux_uses_xdg_config_home(self):
        bin_dir = self.base / 'bin'
        bin_dir.mkdir()
        uname = bin_dir / 'uname'
        uname.write_text('#!/bin/sh\nprintf "Linux\\n"\n')
        uname.chmod(0o755)
        config = self.base / 'xdg config'
        env = dict(os.environ, PATH=str(bin_dir) + os.pathsep + os.environ['PATH'], XDG_CONFIG_HOME=str(config))
        result = subprocess.run(['bash', str(ROOT / 'install.sh')], env=env, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((config / 'Typora/themes/visonic-streamer-nebula.css').is_file())

    @unittest.skipIf(os.name == 'nt', 'Bash installer is for macOS/Linux')
    def test_empty_distribution_fails_before_creating_target(self):
        shutil.copy2(ROOT / 'install.sh', self.base / 'install.sh')
        (self.base / 'themes').mkdir()
        (self.base / 'visonic-fonts').mkdir()
        target = self.base / 'must not exist'
        result = subprocess.run(['bash', str(self.base / 'install.sh'), str(target)], capture_output=True, text=True, timeout=30)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('No Visonic theme CSS files', result.stderr)
        self.assertFalse(target.exists())


if __name__ == '__main__':
    unittest.main()
