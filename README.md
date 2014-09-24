XWiki Enterprise Build Script
==================

Easily build a reasy-to-use XWiki instance with this helper.

Objective
===
I often build an up-to-date version of [XWiki Enterprise](http://enterprise.xwiki.org/xwiki/bin/view/Main/WebHome) with maven. This script automates the process of creating the Jetty/HSQLDB distribution and unziping it.

By default, the generated instance is unzipped in a directory not related to the XWiki Sources. The reason is that when I run XWiki in the standard maven target directory, my IDE tries to index the files and become very slow.

Prerequisites
===
You need a Python interpreter, Maven ([correctly configured](http://dev.xwiki.org/xwiki/bin/view/Community/Building)), and the XWiki sources. The script assumes that you have cloned the (XWiki Enterprise Repository)[https://github.com/xwiki/xwiki-enterprise] in the `~/xwiki/xwiki-enterprise` directory. It will create the build in the `~/xwiki-instance` directory.

Usage
===
Just do `python make-enterprise.py`.
If a previous instance exists, it will be deleted.

Change paths
===
If you want to change the path of the sources and/or of the output, just edit the script itself and change the global variables at the begining of the file (`xe_sources`, `instance_path`).

Options
===
* `-U`: same as maven, it will force the update of the dependencies.
* `-am`: (to be implemented) means 'Also Make dependencies'. Instead of downloading them, all dependencies that have their sources in the `xwiki-enterprise` directory will be compiled. So it does not concern dependencies like `xwiki-platform`, `xwiki-rendering` and `xwiki-commons`.

Contact
===
Feel free to contact me, create issues or pull request on the github project. Thanks.
