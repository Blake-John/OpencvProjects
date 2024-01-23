cmake_minimum_required(VERSION 3.10)
project(COLORDETECTOR)

find_package(OpenCV REQUIRED)

add_executable(main detect.cpp)
# add_executable(getpicture getpicture.cpp)

target_include_directories(main PUBLIC ${OpenCV_INCLUDE_DIRS})
target_link_libraries(main ${OpenCV_LIBS})


# target_include_directories(getpicture PUBLIC ${OpenCV_INCLUDE_DIRS})
# target_link_libraries(getpicture ${OpenCV_LIBS})