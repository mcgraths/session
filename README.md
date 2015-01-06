session
=======

Python script to initializes a photography session directory with tree structure and blank Lightroom catalog.

It uses the shoot folder name to create the following structure for weddings:

```
Wedding Folder Name
├── Book/
├── Prints/
├── Wedding Folder Name Catalog/
│   ├── Wedding Folder Name Previews.lrdata
│   └── Wedding Folder Name.lrcat
├── Throwaways/
└── USB/
```

and the following for any other types of shoots:

```
Shoot Folder Name
├── Shoot Folder Name Catalog/
│   ├── Shoot Folder Name Previews.lrdata
│   └── Shoot Folder Name.lrcat
├── Throwaways/
└── USB/
```

Installation
------------

**Mac OS X:** 

- `chmod 755 session.py`
- `sudo ln -s /path/to/session.py /usr/bin/session`
- Edit the `_LRTEMPLATE` variable in session.py to point to an empty Lightroom catalog

Running
-------

From the Terminal:

- `cd /path/to/shoot`
- Run `session init` for a normal shoot
- Run `session init wedding` for a wedding shoot

Todo
----

- Define folder structure, commands and settings in a config file