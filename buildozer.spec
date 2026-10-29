[app]
title = Pakulla Union
package.name = pakullaunion
package.domain = com.pakulla.union
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
version.regex = __version__ = ['"]([^'"]*)['"]
version.filename = %(source.dir)s/main.py
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True

[buildozer]
log_level = 2
warn_on_root = 1