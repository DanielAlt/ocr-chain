### Install on Windows

- Download and Install [Python v 3.4](https://www.python.org/download/releases/3.4.0/)
- Download and Install [Pip](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation#pip-install)

Make sure to include the executables in you windows %PATH% environment variable.

- Install ocr_chain

```bash
  cd ocr_chain
  python setup.py install
```

- Install the [pytesseract Executable](https://sourceforge.net/projects/tesseract-ocr-alt/?source=typ_redirect)

You can now use the application.

```bash
 cd /working/directory
 ocr-chain [/path/to/folder] --threads 4 log-level 0
```
