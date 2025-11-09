set(TARGET_NAME problem_3378)

add_library(${TARGET_NAME} src/lcm_connected_components.cpp)
target_include_directories(${TARGET_NAME} PUBLIC include)
target_link_libraries(${TARGET_NAME} PUBLIC disjoint_sets_utils)

add_executable(${TARGET_NAME}_tests tests/test_lcm_connected_components.cpp)
target_link_libraries(${TARGET_NAME}_tests PRIVATE ${TARGET_NAME} GTest::gtest_main)

add_test(NAME ${TARGET_NAME}_tests COMMAND ${TARGET_NAME}_tests)
