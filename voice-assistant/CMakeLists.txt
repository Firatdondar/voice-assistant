cmake_minimum_required(VERSION 3.15)
project(VoiceAssistant VERSION 1.0.0 LANGUAGES NONE)

# ─────────────────────────────────────────────
# Voice Assistant - Python Project
# This CMakeLists.txt provides optional helpers:
#   - Install Python dependencies
#   - Run the application via cmake --build
# ─────────────────────────────────────────────

# Find Python interpreter
find_package(Python3 REQUIRED COMPONENTS Interpreter)

message(STATUS "Python found: ${Python3_EXECUTABLE}")
message(STATUS "Python version: ${Python3_VERSION}")

# ── Custom target: install dependencies ──────
add_custom_target(install_deps
    COMMAND ${Python3_EXECUTABLE} -m pip install -r ${CMAKE_SOURCE_DIR}/requirements.txt
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Installing Python dependencies from requirements.txt..."
)

# ── Custom target: run the application ───────
add_custom_target(run
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/app.py
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Starting Voice Assistant..."
)

# ── Install rule (optional) ───────────────────
install(
    FILES
        app.py
        requirements.txt
        README.md
        araba.jpg
        armut.jpeg
        bisiklet.jpeg
        elma.jpeg
    DESTINATION ${CMAKE_INSTALL_PREFIX}/voice-assistant
)

# ── Print usage instructions ──────────────────
message(STATUS "")
message(STATUS "=== Voice Assistant Build Targets ===")
message(STATUS "  cmake --build . --target install_deps   -> Install Python packages")
message(STATUS "  cmake --build . --target run            -> Launch the application")
message(STATUS "=====================================")
