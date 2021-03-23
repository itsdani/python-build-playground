load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@poetry//:dependencies.bzl", "dependency")

py_library(
    name = "lib_a",
    srcs = glob(["**/*.py"]),
    srcs_version = "PY3",
    deps = [
        dependency("numpy")
        ],
    visibility = ["//visibility:public"]
)

filegroup(
    name = "srcs",
    srcs = ["BUILD"] + glob(["**/*.py"]),
)