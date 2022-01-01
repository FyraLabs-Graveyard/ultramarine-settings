project('ultramarine-settings',
          version: '0.1.0',
    meson_version: '>= 0.50.0',
  default_options: [ 'warning_level=2',
                   ],
)

i18n = import('i18n')

gnome = import('gnome')
i18n  = import('i18n')
python = import('python')

subdir('data')
subdir('umcfg')
subdir('po')

PROJECT_RDNN_NAME = 'org.ultramarine.settings'

meson.add_install_script('build-aux/meson/postinstall.py')
