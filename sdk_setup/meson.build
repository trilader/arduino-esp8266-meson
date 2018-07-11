assert(meson.is_cross_build(), 'ESP8266 projects can only be built in a cross build environment.')

common_cross_args = [
    '-D__ets__',
    '-DICACHE_FLASH',
    '-U__STRICT_ANSI__',
    '-DF_CPU=80000000L',
    '-DARDUINO=10605',
    '-DARDUINO_ESP8266_NODEMCU',
    '-DARDUINO_ARCH_ESP8266',
    '-DESP8266',
    '-g',
    '-ffunction-sections',
    '-fdata-sections',
    '-falign-functions=4'
]

add_global_arguments(common_cross_args + [
    '-Wpointer-arith',
    '-Wno-implicit-function-declaration',
    '-Wl,-EL',
    '-fno-inline-functions',
    '-nostdlib',
    '-mlongcalls',
    '-mtext-section-literals',
    '-std=gnu99',
    ], language: 'c')

add_global_arguments(common_cross_args + [
    '-mlongcalls',
    '-mtext-section-literals',
    '-fno-exceptions',
    '-fno-rtti',
    ], language: 'cpp')

common_cross_link_args = [
    '-nostdlib',
    '-Wl,--no-check-sections',
    '-u', 'call_user_start',
    '-Wl,-static',
    '-Teagle.flash.4m.ld',
    '-Wl,--gc-sections',
    '-Wl,-wrap,system_restart_local'
]

add_global_link_arguments(common_cross_link_args + ['-Wl,-wrap,__register_chipv6_phy'], language: 'c')
add_global_link_arguments(common_cross_link_args + ['-Wl,-wrap,spi_flash_read'], language: 'cpp')
