cmake_minimum_required(VERSION 3.20...3.22)

project(sample
    LANGUAGES C CXX
    DESCRIPTION "Sample project to test Cython coverage support"
)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

add_subdirectory(tasket)
