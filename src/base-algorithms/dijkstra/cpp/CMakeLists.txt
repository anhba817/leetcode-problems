set(TARGET_NAME base_dijkstra)

add_library(${TARGET_NAME} src/dijkstra.cpp)
target_include_directories(${TARGET_NAME} PUBLIC include)

add_executable(${TARGET_NAME}_tests tests/test_dijkstra.cpp)
target_link_libraries(${TARGET_NAME}_tests PRIVATE ${TARGET_NAME} GTest::gtest_main)

add_test(NAME ${TARGET_NAME}_tests COMMAND ${TARGET_NAME}_tests)
