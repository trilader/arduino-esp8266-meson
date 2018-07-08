project('arduino-esp8266-meson', 'cpp', default_options: ['buildtype=minsize'])
subdir('sdk_setup')

add_global_arguments(['-Wno-non-virtual-dtor'], language: 'cpp')

sdk=subproject('esp8266_sdk')

blinky_exe = executable('blinky.elf', ['blinky.cpp'], dependencies: [sdk.get_variable('core')])

blinky_bin = custom_target('blinky.bin',
  input : blinky_exe,
  output : 'blinky.bin',
  command : sdk.get_variable('esptoolize'),
  build_by_default: true,
)
