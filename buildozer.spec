[app]
title = Pakulla Union
package.name = pakullaunion
package.domain = com.pakulla.union
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
version.regex = __version__ = ['"]([^'"]*)['"]
version.filename = %(source.dir)s/main.py
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2
android.accept_sdk_license_agreements = True
p4a.bootstrap = sdl2
# এই ২টা লাইন খুব জরুরি
android.gradle_dependencies = 
p4a.whitelist = 