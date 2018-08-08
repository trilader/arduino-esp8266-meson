project('esp8266_sdk', ['c', 'cpp'])

add_project_arguments('-Wno-unused-function', language: 'cpp')

esp8266_base = meson.get_cross_property('esp8266_base')
esptool = find_program(meson.get_cross_property('esptool'))

esp8266_include=include_directories([esp8266_base+'/cores/esp8266', esp8266_base+'/variants/nodemcu',
esp8266_base+'/tools/sdk/include', esp8266_base+'/tools/sdk/lwip2/include'])
esp8266_src = []
foreach s: ['abi.cpp', 'base64.cpp', 'cbuf.cpp', 'cont_util.c', 'core_esp8266_eboot_command.c', 'core_esp8266_flash_utils.c', 'core_esp8266_i2s.c', 'core_esp8266_main.cpp', 'core_esp8266_noniso.c', 'core_esp8266_phy.c', 'core_esp8266_postmortem.c', 'core_esp8266_si2c.c', 'core_esp8266_sigma_delta.c', 'core_esp8266_timer.c', 'core_esp8266_waveform.c', 'core_esp8266_wiring_analog.c', 'core_esp8266_wiring.c', 'core_esp8266_wiring_digital.c', 'core_esp8266_wiring_pulse.c', 'core_esp8266_wiring_pwm.c', 'core_esp8266_wiring_shift.c', 'debug.cpp', 'Esp.cpp', 'Esp-version.cpp', 'FS.cpp', 'FunctionalInterrupt.cpp', 'gdb_hooks.c', 'HardwareSerial.cpp', 'heap.c', 'IPAddress.cpp', 'libc_replacements.c', 'MD5Builder.cpp', 'pgmspace.cpp', 'Print.cpp', 'Schedule.cpp', 'ScheduledFunctions.cpp', 'sntp-lwip2.c', 'spiffs_api.cpp', 'spiffs_hal.cpp', 'Stream.cpp', 'StreamString.cpp', 'time.c', 'Tone.cpp', 'uart.c', 'Updater.cpp', 'WMath.cpp', 'WString.cpp', 'umm_malloc/umm_malloc.c', 'libb64/cdecode.c', 'libb64/cencode.c', 'spiffs/spiffs_cache.c', 'spiffs/spiffs_check.c', 'spiffs/spiffs_gc.c', 'spiffs/spiffs_hydrogen.c', 'spiffs/spiffs_nucleus.c', 'cont.S',]
  esp8266_src += esp8266_base+'/cores/esp8266/'+s
endforeach

search_dirs = [esp8266_base+'/tools/sdk/lib', esp8266_base+'/tools/sdk/ld', esp8266_base+'/tools/sdk/libc/xtensa-lx106-elf/lib']
compiler = meson.get_compiler('cpp')

subdir('ld')

core_lib = static_library('ESP8266Core', esp8266_src, include_directories: esp8266_include)
core=declare_dependency(include_directories: esp8266_include,
sources: [customize_sdk],
dependencies: [
    compiler.find_library('m', dirs: search_dirs),
    compiler.find_library('gcc', dirs: search_dirs),
    compiler.find_library('stdc++', dirs: search_dirs),
    compiler.find_library('c', dirs: search_dirs),
    compiler.find_library('g', dirs: search_dirs),
    compiler.find_library('hal', dirs: search_dirs),
    compiler.find_library('phy', dirs: search_dirs),
    compiler.find_library('net80211', dirs: search_dirs),
    compiler.find_library('lwip2_1460', dirs: search_dirs),
    compiler.find_library('driver', dirs: search_dirs),
    compiler.find_library('main', dirs: search_dirs),
    compiler.find_library('pp', dirs: search_dirs),
    compiler.find_library('smartconfig', dirs: search_dirs),
    compiler.find_library('wps', dirs: search_dirs),
    compiler.find_library('crypto', dirs: search_dirs),
    compiler.find_library('bearssl', dirs: search_dirs),
    compiler.find_library('axtls', dirs: search_dirs),
    compiler.find_library('espnow', dirs: search_dirs),
    compiler.find_library('wpa', dirs: search_dirs),
    compiler.find_library('airkiss', dirs: search_dirs),
    compiler.find_library('wpa2', dirs: search_dirs),
],
link_args: [ '-L'+sdk_ld_dir ],
link_with: core_lib)

esptoolize=[esptool,
  '-eo', esp8266_base+'/bootloaders/eboot/eboot.elf',
  '-bo', '@OUTPUT@',
  '-bm', 'dio',
  '-bf', '40',
  '-bz', '4M',
  '-bs', '.text',
  '-bp', '4096',
  '-ec',
  '-eo', '@INPUT@',
  '-bs', '.irom0.text',
  '-bs', '.text',
  '-bs', '.data',
  '-bs', '.rodata',
  '-bc',
  '-ec']



