# Dify API
Reference: https://github.com/langgenius/dify/tree/main/api

## Docker Deployment
#### Create Virtual Environment
```bash
python -m venv .venv
```

#### Generate a UV lock file locally
```bash
pip install uv
python -m uv lock
python -m uv sync
.venv\Scripts\activate
```

#### Create Volume
```bash
docker volume create dify-api-volume
```

#### Remove Previous Leftovers
```bash
docker rm -f dify-api
```

#### Build Image
```bash
docker build -t dify-api-image:latest -f Dockerfile .
```

#### Run Container
```bash
docker run -d --name dify-api --read-only -v dify-api-volume:/tmp --env-file .env -p 5001:5001 dify-api-image:latest
```

## Packages
#### `curl`
- **Command-line tool for transferring data with URLs.**
- Supports multiple protocols like HTTP, HTTPS, FTP, etc.
- Commonly used in Docker builds to download files, check connectivity, or fetch configuration scripts from remote servers.

#### `gcc`
- **GNU Compiler Collection (C compiler)**.
- Compiles C code into binaries.
- Needed when you install Python packages that include native extensions (e.g., `numpy`, `pandas`, `cryptography`, etc.) — because they need to compile C source code.

#### `g++`
- The **C++ compiler** (part of GCC).
- Required for packages written partly in C++ (like `scikit-learn`, `xgboost`, or `opencv-python`).

#### `libc-dev` (often `libc6-dev`)
- Provides **C standard library headers and development files**.
- You need it to compile any C or C++ program that uses functions like `malloc`, `printf`, etc.
- Without it, even the simplest `#include <stdio.h>` program won’t compile.

#### `libffi-dev`
- “**Foreign Function Interface**” library for calling compiled code from dynamic languages (like Python).
- Python’s `ctypes` and `cffi` use this.
- Required for libraries like `cryptography`, `cffi`, `pyopenssl`, etc.

#### `libgmp-dev`
- **GNU Multiple Precision Arithmetic Library**.
- Handles very large integers and rational numbers efficiently.
- Used in cryptography, symbolic math (like `sympy`), and numerical computation.

#### `libmpfr-dev`
- **Multiple Precision Floating-Point Reliable Library**.
- Builds on GMP but focuses on **high-precision floating-point arithmetic**.
- Used in compilers and math libraries (e.g., GCC itself or scientific computing tools).

#### `libmpc-dev`
- **Multiple Precision Complex Library**.
- Works with complex numbers (real + imaginary parts) with arbitrary precision.
- Used internally by GCC and other math-heavy libraries.

#### `expat`
- **XML parsing library (libexpat).**
- Provides fast, low-level parsing of XML documents.
- Used by many applications and libraries that need to read configuration or data in XML (e.g., Python’s `xml.parsers.expat`, Git, Subversion).

#### `libldap-2.4-2`
- **OpenLDAP runtime library.**
- Enables applications to communicate with **LDAP (Lightweight Directory Access Protocol)** servers.
- Needed by tools or libraries that query or authenticate against directory services (e.g., Active Directory, corporate identity systems).

#### `libldap2-dev`
- **Development headers for OpenLDAP.**
- Required to **build or compile software that links against LDAP**, such as Python’s `ldap3`, or libraries like `cyrus-sasl` or `krb5`.
- Works together with `libldap-2.4-2` (the runtime library).

#### `perl`
- **High-level programming language** known for text processing and scripting.
- Often used internally by build tools, installers, or legacy system scripts.
- Installed as a dependency for software that requires Perl scripts during build/configuration (e.g., Git, OpenSSL builds, or CPAN modules).

#### `libsqlite3-0`
- **SQLite runtime library.**
- Provides an **embedded SQL database engine** — lightweight, serverless, and self-contained.
- Required by many programs and Python packages (`sqlite3`, `sqlalchemy`, etc.) that store local data or cache information.

#### `zlib1g`
- **Compression library implementing the DEFLATE algorithm.**
- Used for **gzip**, **PNG**, and other compressed data formats.
- Almost every major system and programming language (Python, Git, curl, etc.) depends on it for compression and decompression tasks.

#### `fonts-noto-cjk`
- **Google Noto CJK font family** — covers **Chinese, Japanese, and Korean (CJK)** characters.
- Provides **high-quality, Unicode-complete fonts** for rendering East Asian scripts correctly.
- Often installed in containers or web servers to ensure **proper text rendering** for multilingual applications (e.g., PDFs, web pages, or ML models generating images with text).
- Essential when generating or displaying text that includes CJK characters — prevents “tofu” (missing character boxes □□).

#### `media-types`
- **Database of MIME (Multipurpose Internet Mail Extensions) types.**
- Provides a standardized list of file type mappings — e.g., `.html → text/html`, `.jpg → image/jpeg`, `.json → application/json`.
- Used by many tools and servers (like **curl**, **web servers**, and **browsers**) to **identify file formats and set Content-Type headers** correctly.
- Ensures that applications handle files with the appropriate encoding and processing method.

#### `libmagic1`
- **Library that identifies file types based on their binary signatures (“magic numbers”).**
- Powers the Unix `file` command — determines a file’s type **by inspecting its contents**, not just its extension.
- Commonly used by tools and Python packages like `python-magic`, `mimetypes`, or `requests` to **detect MIME types automatically**.
- Useful in web servers, upload handlers, and ML preprocessing pipelines to validate or classify incoming files.

