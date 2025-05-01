cmake_minimum_required(VERSION 3.8)
project(my_cpp_nodes)

# ── 1. ビルドオプション ────────────────────────────────
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU" OR
   CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# ── 2. 依存パッケージ ────────────────────────────────
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# ── 3. 実行ファイル ────────────────────────────────
add_executable(talker_cpp src/talker.cpp)
ament_target_dependencies(talker_cpp rclcpp std_msgs)

# ── 4. インストール ────────────────────────────────
install(TARGETS
  talker_cpp
  DESTINATION lib/${PROJECT_NAME}
)

# ── 5. Lint / テストオプション ───────────────────────
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

# ── 6. パッケージ宣言 ───────────────────────────────
ament_package()