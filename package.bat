python -m nuitka ^
--enable-plugin=anti-bloat --noinclude-pytest-mode=nofollow --noinclude-setuptools-mode=nofollow ^
--mingw64 --standalone --show-progress --show-memory ^
--plugin-enable=tk-inter --plugin-enable=numpy ^
--include-data-dir=F:\\Repos\\Circulation\\module=module ^
--include-data-file=F:\\Repos\\Circulation\\img\\blank.png=img\\blank.png ^
Circulation.py
