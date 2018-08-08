
script = find_program('customize_sdk.py')

customize_sdk = custom_target('Customize SDK',
    input: esp8266_base+'/tools/sdk/ld/eagle.flash.4m.ld',
    output: 'eagle.flash.4m.ld',
    depfile: 'ld.deps',
    command: [script, '@INPUT@', '@OUTPUT@', '@DEPFILE@', find_program('c', required: true, native: false)]
)

sdk_ld_dir = meson.current_build_dir()
