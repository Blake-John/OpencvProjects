cmake_minimum_required(VERSION 3.10)
project(ONNX)

find_package(OpenCV REQUIRED)

add_executable(main test.cpp)

target_include_directories(main PUBLIC ${OpenCV_INCLUDE_DIRS})
target_link_libraries(main ${OpenCV_LIBS})