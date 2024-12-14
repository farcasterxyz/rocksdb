{
  'targets': [{
    'variables': {
      # Defining a list of conditions that depend on the OS type.
      'conditions': [
        # If the OS is Linux, set the 'os_include' variable to 'linux'
        ['OS=="linux"', {'os_include': 'linux'}],
        # If the OS is macOS, set the 'os_include' variable to 'mac'
        ['OS=="mac"', {'os_include': 'mac'}],
        # If the OS is Solaris, set the 'os_include' variable to 'solaris'
        ['OS=="solaris"', {'os_include': 'solaris'}],
        # If the OS is Windows, set the 'os_include' variable to 'win32'
        ['OS=="win"', {'os_include': 'win32'}],
        # If the OS is FreeBSD, set the 'os_include' variable to 'freebsd'
        ['OS=="freebsd"', {'os_include': 'freebsd'}],
        # If the OS is OpenBSD, set the 'os_include' variable to 'openbsd'
        ['OS=="openbsd"', {'os_include': 'openbsd'}]
      ]
    },
    'target_name': 'snappy',  # The target name is 'snappy', which refers to the Snappy compression library
    'type': 'static_library',  # The target will be built as a static library
    # Create a standalone static library, fixing linker issues with thin .a files on SmartOS
    'standalone_static_library': 1,
    'include_dirs': [
      # Include directories based on the OS type using the 'os_include' variable
      '<(os_include)',
      # The path to Snappy's source code (version 1.1.7)
      'snappy-1.1.7'
    ],
    'direct_dependent_settings': {
      'include_dirs': [
        # Direct dependent include directories are the same as for the main target
        '<(os_include)',
        'snappy-1.1.7'
      ]
    },
    'defines': [
      # Define the 'HAVE_CONFIG_H' macro, typically indicating the presence of a config header file
      'HAVE_CONFIG_H=1'
    ],
    # List of conditional settings for different OS platforms
    'conditions': [
      # If the OS is Windows, set specific compiler flags for MSVC
      ['OS == "win"', {
        'defines': [
          # Disable exceptions in Windows builds with the '_HAS_EXCEPTIONS=0' flag
          '_HAS_EXCEPTIONS=0'
        ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            # Disable runtime type information and enable function-level linking
            'RuntimeTypeInfo': 'false',
            'EnableFunctionLevelLinking': 'true',
            # Set exception handling to '2' (indicating the use of SEH)
            'ExceptionHandling': '2',
            # Disable specific warnings
            'DisableSpecificWarnings': ['4355', '4530', '4267', '4244', '4506', '4018']
          }
        }
      }],
      # If the OS is Linux, FreeBSD, OpenBSD, or Solaris, set common compiler flags
      ['OS == "linux"', {
        'cflags': [
          # Disable warnings about signed-unsigned comparisons and unused functions
          '-Wno-sign-compare',
          '-Wno-unused-function'
        ],
        'cflags!': [  # Disable certain optimizations for Linux (e.g., -fno-tree-vrp)
          '-fno-tree-vrp'
        ]
      }],
      ['OS == "freebsd"', {
        'cflags': [
          '-Wno-sign-compare',
          '-Wno-unused-function'
        ]
      }],
      ['OS == "openbsd"', {
        'cflags': [
          '-Wno-sign-compare',
          '-Wno-unused-function'
        ]
      }],
      ['OS == "solaris"', {
        'cflags': [
          '-Wno-sign-compare',
          '-Wno-unused-function'
        ]
      }],
      # If the OS is macOS, set Xcode-specific settings, including architecture and warning flags
      ['OS == "mac"', {
        'xcode_settings': {
          # Disable warning flags for sign comparison and unused functions
          'WARNING_CFLAGS': [
            '-Wno-sign-compare',
            '-Wno-unused-function'
          ],
          # Set the architectures for the macOS build to support both x86_64 and arm64
          'OTHER_CFLAGS': [
            '-arch x86_64',
            '-arch arm64'
          ]
        }
      }]
    ],
    # List of source files to include in the Snappy static library
    'sources': [
      'snappy-1.1.7/snappy-internal.h',
      'snappy-1.1.7/snappy-sinksource.cc',
      'snappy-1.1.7/snappy-sinksource.h',
      'snappy-1.1.7/snappy-stubs-internal.cc',
      'snappy-1.1.7/snappy-stubs-internal.h',
      'snappy-1.1.7/snappy.cc',
      'snappy-1.1.7/snappy.h'
    ]
  }],
  # Define additional variables (e.g., for OpenSSL FIPS, although it's empty here)
  'variables': {
    'openssl_fips': ''
  }
}
