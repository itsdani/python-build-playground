load("@rules_python//python:defs.bzl", "py_runtime_pair")
load("@bazel_tools//tools/python:toolchain.bzl", "py_runtime_pair")

# this is a fake, only py3 is bundled and used
py_runtime(
    name = "bundled-py2",
    interpreter_path = "/home/dani/work/python-build-playground/pyenv/versions/3.6.13/bin/python3.6",
    python_version = "PY2",
)

py_runtime(
    name = "bundled-py3",
    interpreter_path = "/home/dani/work/python-build-playground/pyenv/versions/3.6.13/bin/python3.6",
    python_version = "PY3",
)

py_runtime_pair(
    name = "bundled-interpreters",
    py2_runtime = ":bundled-py2",
    py3_runtime = ":bundled-py3",
)

toolchain(
    name = "bundled-interpreter",
    toolchain = ":bundled-interpreters",
    toolchain_type = "@rules_python//python:toolchain_type",
)