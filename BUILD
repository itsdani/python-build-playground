load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@poetry//:dependencies.bzl", "dependency")

py_library(
    name = "lib_a",
    srcs = glob(["lib_a/**/*.py"]),
    srcs_version = "PY3",
    deps = [dependency("numpy")]
)

py_binary(
    name = "bin_a",
    srcs = glob(["executable_a/**/*.py"]),
    srcs_version = "PY3",
    deps = [":lib_a"],
)

filegroup(
    name = "srcs",
    srcs = ["BUILD"] + glob(["**/*.py"]),
)