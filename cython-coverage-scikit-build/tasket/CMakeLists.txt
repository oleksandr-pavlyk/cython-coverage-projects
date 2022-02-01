
add_cython_target(
    _comp
    ${CMAKE_CURRENT_SOURCE_DIR}/_comp.pyx CXX
    OUTPUT_VAR _generated_src
)
add_library(_comp MODULE ${_generated_src})

target_compile_definitions(_comp PRIVATE CYTHON_TRACE=1 CYTHON_TRACE_NOGIL=1)
python_extension_module(_comp)

install(TARGETS _comp LIBRARY DESTINATION tasket)
