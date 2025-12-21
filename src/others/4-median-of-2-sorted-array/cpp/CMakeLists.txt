set(TARGET_NAME problem_4)

add_library(${TARGET_NAME} src/median_of_2_sorted_array.cpp)
target_include_directories(${TARGET_NAME} PUBLIC include)

add_executable(${TARGET_NAME}_tests tests/test_median_of_2_sorted_array.cpp)
target_link_libraries(${TARGET_NAME}_tests PRIVATE ${TARGET_NAME} GTest::gtest_main)

add_test(NAME ${TARGET_NAME}_tests COMMAND ${TARGET_NAME}_tests)
