import shutil
from pathlib import Path

from django.conf import settings
from django.test import TestCase
from django.core import management

from migrations_git_conflicts.management.commands.makemigrations import LATEST_MIGRATIONS_DIR_NAME


class TestMigrationsFiles(TestCase):

    def test_make_migrations_generates_files(self):
        dir = Path(settings.BASE_DIR, LATEST_MIGRATIONS_DIR_NAME)
        shutil.rmtree(dir, ignore_errors=True)  # Cleanup if last test failed
        management.call_command("makemigrations")
        with (dir / 'README').open() as readme_file:
            self.assertNotEqual(readme_file.read(), "")

        with (dir / 'tests.app_bar').open() as app_bar_file:
            self.assertIn('0001_initial', app_bar_file.read())

        with (dir / 'tests.app_foo').open() as app_foo_file:
            self.assertIn('0002_auto_20200623_0645', app_foo_file.read())
        shutil.rmtree(dir, ignore_errors=True)  # Cleanup


