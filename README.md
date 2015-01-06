session
=======

Python script to initializes a photography session directory with tree structure and blank Lightroom catalog.

Installation
------------

**Mac OS X:** 

- `chmod 755 session.py`
- `sudo ln -s /path/to/session.py /usr/bin/session`
- Edit the `_LRTEMPLATE` variable in session.py to point to an empty Lightroom catalog

Running
_______

From the Terminal:

- `cd /path/to/shoot`
- Run `session init` for a normal shoot
- Run `session init wedding` for a wedding shoot

Todo
----

- Define folder structure, commands and settings in a config file