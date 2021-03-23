load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_runtime_pair")
load("@poetry//:dependencies.bzl", "dependency")

py_binary(
    name = "bin_a",
    srcs = glob(["**/*.py"]),
    srcs_version = "PY3",
    deps = [
        "//lib_a:lib_a",
    ],
)

filegroup(
    name = "srcs",
    srcs = ["BUILD"] + glob(["**/*.py"]),
)