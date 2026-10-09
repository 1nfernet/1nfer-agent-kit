import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest


MODULE_PATH = Path(__file__).with_name('1nfer.py')
SPEC = importlib.util.spec_from_file_location('one_nfer_cli', MODULE_PATH)
cli = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cli)


class PrivateReadPermissionsTest(unittest.TestCase):
    def write_json(self, mode):
        temporary = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        self.addCleanup(lambda: os.path.exists(temporary.name) and os.unlink(temporary.name))
        with temporary:
            json.dump({'value': 'private'}, temporary)
        os.chmod(temporary.name, mode)
        return temporary.name

    def test_reads_owner_only_json_file(self):
        path = self.write_json(0o600)

        self.assertEqual(cli.private_read(path), {'value': 'private'})

    def test_rejects_group_or_world_readable_json_file(self):
        for mode in (0o640, 0o604):
            with self.subTest(mode=oct(mode)):
                path = self.write_json(mode)

                with self.assertRaises(cli.Error):
                    cli.private_read(path)


if __name__ == '__main__':
    unittest.main()
