[app]

# (str) 应用标题
title = 星妍AI

# (str) 包名
package.name = xingyai

# (str) 包域名（Android/iOS打包需要）
package.domain = org.xingyai

# (str) 源代码目录（main.py所在位置）
source.dir = .

# (list) 要包含的源文件扩展名（留空表示包含所有文件）
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) 使用模式匹配包含的源文件
source.include_patterns = resources/*

# (list) 要排除的源文件扩展名（留空表示不排除任何内容）
#source.exclude_exts = spec

# (list) 要排除的目录列表（留空表示不排除任何内容）
#source.exclude_dirs = tests, bin, venv

# (list) 使用模式匹配排除的内容
#source.exclude_patterns = license,images/*/*.jpg

# (str) 应用版本（方法1）
version = 0.1

# (str) 应用版本（方法2）
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) 应用依赖项
# 逗号分隔，例如 requirements = sqlite3,kivy
requirements = python3,kivy,pillow

# (str) 依赖项的自定义源文件夹
# 为任何带有recipes的依赖项设置自定义源
# requirements.source.kivy = ../../kivy

# (str) 应用启动画面
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) 应用图标
#icon.filename = %(source.dir)s/data/icon.png

# (str) 支持的方向（landscape, sensorLandscape, portrait 或 all）
orientation = portrait

# (list) 要声明的服务列表
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX 特定设置
#

#
# author = © Copyright Info

# 应用使用的Python主要版本
osx.python_version = 3

# 使用的Kivy版本
osx.kivy_version = 1.9.1

#
# Android 特定设置
#

# (bool) 指示应用是否应该全屏
fullscreen = 0

# (string) 启动画面背景颜色（用于android工具链）
# 支持的格式：#RRGGBB #AARRGGBB
#android.presplash_color = #FFFFFF

# (string) 使用Lottie格式的启动动画。
# 示例见 https://lottiefiles.com/，文档见 https://airbnb.design/lottie/
# Lottie文件可以使用各种工具创建，如Adobe After Effect或Synfig。
#android.presplash_lottie = "path/to/lottie/file.json"

# (list) 权限
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) 功能（向manifest添加uses-feature标签）
#android.features = android.hardware.usb.host

# (int) 目标Android API，应尽可能高
android.api = 30

# (int) APK支持的最低API
android.minapi = 21

# (int) 使用的Android SDK版本
android.sdk = 24

# (str) 使用的Android NDK版本
android.ndk = 19c

# (int) 使用的Android NDK API。这是您的应用支持的最低API，通常应与android.minapi匹配。
android.ndk_api = 21

# (bool) 使用--private数据存储（True）或--dir公共存储（False）
#android.private_storage = True

# (str) Android NDK目录（如果为空，将自动下载）
#android.ndk_path =

# (str) Android SDK目录（如果为空，将自动下载）
#android.sdk_path =

# (str) ANT目录（如果为空，将自动下载）
#android.ant_path =

# (bool) 如果为True，则跳过尝试更新Android sdk
# 当更新到期且您只想测试/构建包时，这可能有助于避免过多的Internet下载或节省时间
# android.skip_update = False

# (bool) 如果为True，则自动接受SDK许可协议
# 这仅用于自动化。如果设置为False（默认值），
# 首次运行buildozer时将显示许可证。
# android.accept_sdk_license = False

# (str) Android入口点，对于基于Kivy的应用默认值为ok
#android.entrypoint = org.renpy.android.PythonActivity

# (str) Android应用主题，对于基于Kivy的应用默认值为ok
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) 整个项目的白名单模式
#android.whitelist =

# (str) 自定义白名单文件的路径
#android.whitelist_src =

# (str) 自定义黑名单文件的路径
#android.blacklist_src =

# (list) 要添加到libs的Java .jar文件列表，以便pyjnius可以访问
# 它们的类。不要添加不需要的jar，因为额外的jar可能会减慢
# 构建过程。允许通配符匹配，例如：
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) 要添加到android项目的Java文件列表（可以是java或
# 包含文件的目录）
#android.add_src =

# (list) 要添加的Android AAR归档
#android.add_aars =

# (list) 要添加的Gradle依赖项
#android.gradle_dependencies =

# (list) 添加java编译选项
# 例如，在使用'android.gradle_dependencies'选项导入某些java库时，这可能是必要的
# 有关更多信息，请参见https://developer.android.com/studio/write/java8-support
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) 要添加的Gradle存储库{可能对某些android.gradle_dependencies是必要的}
# 请用双引号括起来
# 例如 android.gradle_repositories = "maven { url 'https://kotlin.bintray.com/ktor' }"
#android.add_gradle_repositories =

# (list) 要添加的打包选项
# 参见https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# 可能需要解决gradle_dependencies中的冲突
# 请用双引号括起来
# 例如 android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'", "exclude 'META-INF/*.kotlin_module'"
#android.add_packaging_options =

# (list) 要作为活动添加到清单的Java类
#android.add_activities = com.example.ExampleActivity

# (str) OUYA控制台类别。应该是GAME或APP之一
# 如果留空，将不启用OUYA支持
#android.ouya.category = GAME

# (str) OUYA控制台图标的文件名。必须是732x412 png图像。
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) 在<activity>标签中包含为意图过滤器的XML文件
#android.manifest.intent_filters =

# (str) 为主活动设置的launchMode
#android.manifest.launch_mode = standard

# (list) 要复制到libs/armeabi的Android附加库
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) 指示屏幕是否应保持开启
# 如果将此设置为True，请不要忘记添加WAKE_LOCK权限
#android.wakelock = False

# (list) 要设置的Android应用元数据（key=value格式）
#android.meta_data =

# (list) 要添加的Android库项目（将自动添加到
# project.properties中）
#android.library_references =

# (list) 将使用<uses-library>标签添加到AndroidManifest.xml的Android共享库
#android.uses_library =

# (str) 要使用的Android logcat过滤器
#android.logcat_filters = *:S python:D

# (bool) 复制库而不是制作libpymodules.so
#android.copy_libs = 1

# (str) 要构建的Android架构，选择：armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (int) 覆盖自动versionCode计算（用于build.gradle）
# 这与应用版本不同，只有在您知道自己在做什么时才应编辑
# android.numeric_version = 1

#
# Python for android (p4a) 特定设置
#

# (str) 要使用的python-for-android分支，默认为上游（kivy）
#p4a.fork = kivy

# (str) 要使用的python-for-android分支，默认为master
#p4a.branch = master

# (str) python-for-android git克隆目录（如果为空，将自动从github克隆）
#p4a.source_dir =

# (str) python-for-android应该查找您自己的构建配方的目录（如果有）
#p4a.local_recipes =

# (str) p4a的钩子文件名
#p4a.hook =

# (str) 用于android构建的引导程序
# p4a.bootstrap = sdl2

# (int) 端口号，用于指定显式--port= p4a参数（例如用于bootstrap flask）
#p4a.port =

#
# iOS 特定设置
#

# (str) 自定义kivy-ios文件夹的路径
#ios.kivy_ios_dir = ../kivy-ios
# 或者，指定git检出的URL和分支：
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# 另一个平台依赖：ios-deploy
# 取消注释以使用自定义检出
#ios.ios_deploy_dir = ../ios_deploy
# 或指定URL和分支
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0

# (bool) 是否签名代码
ios.codesign.allowed = false

# (str) 用于签名调试版本的证书名称
# 获取可用身份列表：buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) 用于签名发布版本的证书名称
#ios.codesign.release = %(ios.codesign.debug)s

[buildozer]

# (int) 日志级别（0 = 仅错误，1 = 信息，2 = 调试（带命令输出））
log_level = 2

# (int) 如果buildozer以root身份运行则显示警告（0 = False，1 = True）
warn_on_root = 1

# (str) 构建工件存储的路径，相对于spec文件的绝对或相对路径
# build_dir = ./.buildozer

# (str) 构建输出（即.apk，.ipa）存储的路径
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    列表作为部分
#
#    您可以将所有"列表"定义为[section:key]。
#    每行将被视为列表的一个选项。
#    以[app] / source.exclude_patterns为例。
#    不要这样做：
#
#[app]
#source.exclude_patterns = license,data/audio/*.wav,data/images/original/*
#
#    这可以转换为：
#
#[app:source.exclude_patterns]
#license
#data/audio/*.wav
#data/images/original/*
#

#    -----------------------------------------------------------------------------
#    配置文件
#
#    您可以使用配置文件扩展部分/键
#    例如，您想部署应用程序的演示版本，而不包含
#    HD内容。您可以首先更改标题，在名称中添加"(demo)"，
#    并扩展排除的目录以删除HD内容。
#
#[app@demo]
#title = My Application (demo)
#
#[app:source.exclude_patterns@demo]
#images/hd/*
#
#    然后，使用"demo"配置文件调用命令行：
#
#buildozer --profile demo android debug
