load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.1.0/rules_python-0.1.0.tar.gz",
    sha256 = "b6d46438523a3ec0f3cead544190ee13223a52f6a6765a29eae7b7cc24cc83a0",
)

http_archive(
    name = "com_sonia_rules_poetry",
    sha256 = "8a7a6a5d2ef859ba4309929f3b4d61031f2a4bfed6f450f04ab09443246a4b5c",
    strip_prefix = "rules_poetry-ecd0d9c66b89403667304b11da3bd99764797a63",
    urls = ["https://github.com/soniaai/rules_poetry/archive/ecd0d9c66b89403667304b11da3bd99764797a63.tar.gz"],
)

load("@rules_python//python:pip.bzl", "pip_install")
load("@com_sonia_rules_poetry//rules_poetry:defs.bzl", "poetry_deps")
poetry_deps()
load("@com_sonia_rules_poetry//rules_poetry:poetry.bzl", "poetry")

pip_install(
   name = "common_deps",
   requirements = "//:requirements.txt",
)


poetry(
    name = "poetry",
    lockfile = "//:poetry.lock",
    pyproject = "//:pyproject.toml",
    # optional, if you would like to pull from pip instead of a Bazel cache
    # tags = ["no-remote-cache"],
)
