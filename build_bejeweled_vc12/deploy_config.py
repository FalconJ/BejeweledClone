# -*- coding: utf-8 -*-
# Deployment settings for Bejeweled.
# This file is autogenerated by the mkb system and used by the s3e deployment
# tool during the build process.

config = {}
cmdline = ['C:/Marmalade/7.7/s3e/makefile_builder/mkb.py', '--buildenv=VC12', 'g:/Desktop/eli/Bejeweled/Bejeweled.mkb', '--default-buildenv=vc12x', '--msvc-project', '--deploy-only']
mkb = 'g:/Desktop/eli/Bejeweled/Bejeweled.mkb'
mkf = ['c:\\marmalade\\7.7\\s3e\\s3e-default.mkf', 'c:\\marmalade\\7.7\\modules\\iw2d\\iw2d.mkf', 'c:\\marmalade\\7.7\\modules\\iwgx\\iwgx.mkf', 'c:\\marmalade\\7.7\\modules\\iwgl\\iwgl.mkf', 'c:\\marmalade\\7.7\\modules\\iwutil\\iwutil.mkf', 'c:\\marmalade\\7.7\\modules\\third_party\\libjpeg\\libjpeg.mkf', 'c:\\marmalade\\7.7\\modules\\third_party\\libpng\\libpng.mkf', 'c:\\marmalade\\7.7\\modules\\third_party\\zlib\\zlib.mkf', 'c:\\marmalade\\7.7\\modules\\iwgeom\\iwgeom.mkf', 'c:\\marmalade\\7.7\\modules\\iwresmanager\\iwresmanager.mkf', 'c:\\marmalade\\7.7\\extensions\\pvrtextool\\pvrtextool.mkf', 'c:\\marmalade\\7.7\\modules\\iwgxfont\\iwgxfont.mkf', 'c:\\marmalade\\7.7\\modules\\third_party\\tiniconv\\tiniconv.mkf', 'c:\\marmalade\\7.7\\modules\\iw2dscenegraph\\iw2dscenegraph.mkf', 'c:\\marmalade\\7.7\\modules\\iw2dscenegraphcore\\iw2dscenegraphcore.mkf', 'c:\\marmalade\\7.7\\modules\\iwtween\\iwtween.mkf', 'g:\\desktop\\eli\\bejeweled\\modules\\soundengine\\soundengine.mkf']

class DeployConfig(object):
    pass

######### ASSET GROUPS #############

assets = {}

assets['Default'] = [
    ('g:/Desktop/eli/Bejeweled/data', '.', 0),
    ('g:/Desktop/eli/Bejeweled/data/audio', 'audio', 0),
    ('g:/Desktop/eli/Bejeweled/data/textures', 'textures', 0),
    ('g:/Desktop/eli/Bejeweled/data/fonts', 'fonts', 0),
    ('g:/Desktop/eli/Bejeweled/data-ram/data-gles1,g:/Desktop/eli/Bejeweled/data', '.', 0),
]

######### DEFAULT CONFIG #############

class DefaultConfig(DeployConfig):
    embed_icf = -1
    name = 'Bejeweled'
    pub_sign_key = 0
    priv_sign_key = 0
    caption = 'Bejeweled'
    long_caption = 'Bejeweled'
    version = [0, 0, 0]
    config = ['g:/Desktop/eli/Bejeweled/data/app.icf']
    data_dir = 'g:/Desktop/eli/Bejeweled/data'
    mkb_dir = 'g:/Desktop/eli/Bejeweled'
    iphone_link_lib = []
    osx_ext_dll = ['c:/marmalade/7.7/extensions/pvrtextool/lib/osx/libPVRTexTool.dylib']
    wp81_extra_pri = []
    ws8_ext_capabilities = []
    android_external_res = []
    win32_ext_dll = ['c:/marmalade/7.7/extensions/pvrtextool/lib/win32/PVRTexTool.dll']
    wp8_ext_capabilities = []
    ws8_extra_res = []
    ws81_ext_managed_dll = []
    iphone_link_libdir = []
    android_extra_application_manifest = []
    ws8_ext_native_dll = []
    android_external_assets = []
    blackberry_extra_descriptor = []
    android_ext_target_sdk_version = []
    android_extra_manifest = []
    wp81_ext_sdk_ref = []
    iphone_link_libdirs = []
    wp81_ext_device_capabilities = []
    linux_ext_lib = []
    android_ext_min_sdk_version = []
    ws8_ext_managed_dll = []
    ws8_ext_sdk_manifest_part = []
    ws8_ext_device_capabilities = []
    ws81_extra_pri = []
    android_external_jars = []
    win8_winrt_extra_res = []
    wp81_ext_sdk_manifest_part = []
    android_supports_gl_texture = []
    wp81_extra_res = []
    wp81_ext_managed_dll = []
    wp81_ext_capabilities = []
    iphone_extra_plist = []
    ws81_ext_sdk_manifest_part = []
    ws81_ext_device_capabilities = []
    ws8_ext_sdk_ref = []
    iphone_extra_string = []
    tizen_so = []
    wp8_ext_native_dll = []
    win8_phone_extra_res = []
    win8_store_extra_res = []
    iphone_link_opts = []
    ws81_ext_sdk_ref = []
    wp8_extra_res = []
    ws81_ext_native_dll = []
    ws8_extra_pri = []
    wp8_ext_managed_dll = []
    android_extra_packages = []
    android_so = []
    wp8_ext_sdk_ref = []
    osx_extra_res = []
    ws81_extra_res = []
    wp81_ext_native_dll = []
    ws81_ext_capabilities = []
    iphone_link_libs = []
    target = {
         'mips' : {
                   'debug'   : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Debug_Bejeweled_VC12_gcc_mips/Bejeweled.so',
                   'release' : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Release_Bejeweled_VC12_gcc_mips/Bejeweled.so',
                 },
         'gcc_x86' : {
                   'debug'   : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Debug_Bejeweled_VC12_gcc_x86/Bejeweled.so',
                   'release' : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Release_Bejeweled_VC12_gcc_x86/Bejeweled.so',
                 },
         'gcc_x86_tizen' : {
                   'debug'   : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Debug_Bejeweled_VC12_gcc_x86_tizen/Bejeweled.s86',
                   'release' : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Release_Bejeweled_VC12_gcc_x86_tizen/Bejeweled.s86',
                 },
         'firefoxos' : {
                   'debug'   : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Debug_Bejeweled_VC12_firefoxos/Bejeweled.js',
                   'release' : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Release_Bejeweled_VC12_firefoxos/Bejeweled.js',
                 },
         'mips_gcc' : {
                   'debug'   : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Debug_Bejeweled_VC12_gcc_mips/Bejeweled.so',
                   'release' : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Release_Bejeweled_VC12_gcc_mips/Bejeweled.so',
                 },
         'arm_gcc' : {
                   'debug'   : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Debug_Bejeweled_VC12_gcc_arm/Bejeweled.s3e',
                   'release' : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Release_Bejeweled_VC12_gcc_arm/Bejeweled.s3e',
                 },
         'naclx86_64' : {
                   'debug'   : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Debug_Bejeweled_VC12_gcc_naclx86_64/Bejeweled.so.s64',
                   'release' : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Release_Bejeweled_VC12_gcc_naclx86_64/Bejeweled.so.s64',
                 },
         'aarch64_gcc' : {
                   'debug'   : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Debug_Bejeweled_VC12_gcc_aarch64/Bejeweled.s3e',
                   'release' : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Release_Bejeweled_VC12_gcc_aarch64/Bejeweled.s3e',
                 },
         'gcc_x86_android' : {
                   'debug'   : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Debug_Bejeweled_VC12_gcc_x86_android/Bejeweled.so',
                   'release' : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Release_Bejeweled_VC12_gcc_x86_android/Bejeweled.so',
                 },
         'arm' : {
                   'debug'   : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Debug_Bejeweled_VC12_arm/Bejeweled.s3e',
                   'release' : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Release_Bejeweled_VC12_arm/Bejeweled.s3e',
                 },
         'x86' : {
                   'debug'   : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Debug_Bejeweled_VC12_x86/Bejeweled.s86',
                   'release' : r'g:/Desktop/eli/Bejeweled/build_bejeweled_vc12/Release_Bejeweled_VC12_x86/Bejeweled.s86',
                 },
        }
    arm_arch = ''
    assets_original = assets
    assets = assets['Default']

default = DefaultConfig()
