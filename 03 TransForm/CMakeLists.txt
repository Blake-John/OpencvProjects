cmake_minimum_required(VERSION 3.10)
project(TRANS)

add_subdirectory(transform)

add_executable(main main.cpp)

target_link_libraries(main transform)
target_include_directories(main PUBLIC transform)