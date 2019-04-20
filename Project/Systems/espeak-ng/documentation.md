## Dante's eSpeakNG notes
# Configuration
```bash
> sudo apt-get install make autoconf automake libtool pkg-config gcc libsonic-dev ruby-ronn ruby-kramdown
> cd espeak-ng && ./autogen.sh && ./configure --prefix=/usr && make && sudo make LIBDIR=/usr/lib/x86_64-linux-gnu install
```