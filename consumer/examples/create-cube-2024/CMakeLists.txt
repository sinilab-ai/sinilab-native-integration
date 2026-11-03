cmake_minimum_required(VERSION 3.20)
project(SinilabSDKConsumer2024 LANGUAGES CXX RC)
if(NOT WIN32 OR NOT DEFINED MAX2024_INCLUDE_DIR OR NOT DEFINED MAX2024_LIB_DIR)
  message(FATAL_ERROR "Windows and MAX2024_INCLUDE_DIR/MAX2024_LIB_DIR are required")
endif()
get_filename_component(PACKAGE_ROOT "${CMAKE_CURRENT_LIST_DIR}/../.." ABSOLUTE)
add_library(sinilab_native_sdk STATIC IMPORTED GLOBAL)
set_target_properties(sinilab_native_sdk PROPERTIES
  IMPORTED_LOCATION "${PACKAGE_ROOT}/sdk/lib/x64/sinilab_native_sdk.lib"
  INTERFACE_INCLUDE_DIRECTORIES "${PACKAGE_ROOT}/sdk/include")
add_library(SinilabCreateCube2024 SHARED
  plugin/collaborator_cube_2024.cpp plugin/SinilabCreateCube.rc)
set_target_properties(SinilabCreateCube2024 PROPERTIES PREFIX "" SUFFIX ".dlu")
target_compile_features(SinilabCreateCube2024 PRIVATE cxx_std_17)
target_compile_definitions(SinilabCreateCube2024 PRIVATE UNICODE _UNICODE NOMINMAX)
target_include_directories(SinilabCreateCube2024 PRIVATE "${MAX2024_INCLUDE_DIR}" "${CMAKE_CURRENT_LIST_DIR}/plugin")
target_link_directories(SinilabCreateCube2024 PRIVATE "${MAX2024_LIB_DIR}")
target_link_libraries(SinilabCreateCube2024 PRIVATE sinilab_native_sdk core geom maxutil winhttp crypt32 advapi32)
