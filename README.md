# Django migrations git conflicts

Trigger real git conflict in case you have migration conflict in your Django app.

# Installation

Install python package:

```
pip install django_migrations_git_conflicts
```

And then add this to `INSTALLED_APPS` in your `settings.py` file:

```
INSTALLED_APPS = [
    ...,
    migrations_git_conflicts
]
```

# Usage 

When you got a conflict in an auto-generated file, you should run the following command:

```bash
$ manage.py makemigrations --merge
```

Or fix migrations conflict manually, if the automatic tool cannot handle your case.

# How it works:


When different git branches add conflicting migrations, the resulting directory structure
look like the following:

```
.
+-- migrations
|   +-- 0001_initial.py
|   +-- ...
|   +-- 0042_changes_a.py
|   +-- 0042_changes_b.py
+-- ...
```

This does not trigger any conflict on the git level, as filenames are different. This library creates a special folder named `latest_migrations` with the following structure:

```
.
+-- latest_migrations
|   +-- django_app_foo
|   +-- django_app_bar
|   +-- ...
+-- ...
```

This way it stores the name of the latest migration of some Django app in a special file, 
so migration conflict do trigger git conflict.

# Acknowledgment

Core implementation was done by Vsevolod Ryabykh. Packaged and tested by Roman Skurikhin.
