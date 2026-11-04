# VideosIA fork: local-first changes

Upstream: harry0703/MoneyPrinterTurbo, reviewed base
`c8dbf96e9dfee43b30f7c3f440175d6bd4de61de`.

This fork is used by https://github.com/al2242000122/VideosIA as a pinned submodule.
Its first workflow uses local media, an existing local WAV, no BGM, no remote
script generation and no automatic posting. Use the VideosIA wrapper; an arbitrary
upstream WebUI configuration can still invoke external services.

Changes:

- API listens on 127.0.0.1 by default and rejects protected requests if no API
  key is configured. CLI and WebUI do not require starting the HTTP API.
- Normal logs default to WARNING; complete generated/supplied script logging in
  the two reviewed paths has been removed. Other debug traces may still include
  content; do not enable request diagnostics for private material.
- Background WebUI release checking is opt-in through `MPT_CHECK_UPDATES=1`.
- YouTube uploads always include `containsSyntheticMedia=true`, independently of
  optional generated metadata. This is conservative disclosure, not a promise of
  monetization. The VideosIA wrapper does not upload or publish.
- Updated OSV-affected locked packages: multidict, pyasn1, python-multipart,
  setuptools. Check the resolved lock before future installs/updates.

Data flows that still exist when deliberately enabled: prompts to selected LLMs,
speech text to cloud TTS (including Edge TTS), visual prompts to generators,
search terms to stock providers, finished media to Upload-Post and model/catalog
downloads. Local secrets/config and exports must be kept private. There remain
provider URL/SSRF risks in the online download paths; do not expose to untrusted
users or configure untrusted providers.

No antivirus or static review certifies the absence of malware. A venv is not a
sandbox. For a network boundary use the VideosIA Docker run with `--network none`
and only the specified local mounts. Installation/build itself needs network.
