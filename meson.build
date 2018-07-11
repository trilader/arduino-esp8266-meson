project('arduino-esp8266-meson', 'cpp', default_options: ['buildtype=minsize', 'cpp_std=c++11'])
subdir('sdk_setup')

# There currently is no build type that combines -Os and -g so we specify -g heŕe exlplicitly (the debug information is required to be able to use the ESP8266 stacktrace analyser for debugging crashes)
add_global_arguments(['-g', '-Wno-non-virtual-dtor', ], language: 'cpp')
add_global_arguments(['-g'], language: 'c')

sdk=subproject('esp8266_sdk')

blinky_exe = executable('blinky.elf', ['blinky.cpp'], dependencies: [sdk.get_variable('core')])

blinky_bin = custom_target('blinky.bin',
  input : blinky_exe,
  output : 'blinky.bin',
  command : sdk.get_variable('esptoolize'),
  build_by_default: true,
)
