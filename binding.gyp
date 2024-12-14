{
  // This configuration file is used by the build system to define how the 
  // native modules are compiled and linked for different operating systems.
  // It defines target-specific settings for compiling the 'leveldown' module, 
  // with custom configurations for Windows, macOS, and Linux, as well as 
  // the necessary dependencies and compiler flags.

  "targets": [
    {
      "target_name": "leveldown",  // The name of the target module to be built.
      "conditions": [
        
        // Windows-specific settings
        [
          "OS == 'win'", {
            "defines": [
              "_HAS_EXCEPTIONS=1", // Enable exception handling
              "OS_WIN=1" // Define that the OS is Windows
            ],
            "msvs_settings": {
              "VCCLCompilerTool": {
                "RuntimeTypeInfo": "false", // Disable runtime type information (RTTI)
                "EnableFunctionLevelLinking": "true", // Enable function-level linking for smaller binaries
                "ExceptionHandling": "2", // Enable exception handling (specific to MSVC)
                "DisableSpecificWarnings": [ "4355", "4530", "4267", "4244", "4506" ] // Suppress specific MSVC warnings
              },
              "VCLinkerTool": {
                "AdditionalDependencies": [
                  // Additional libraries needed for linking on Windows
                  "Shlwapi.lib",
                  "rpcrt4.lib"
                ]
              }
            }
          }
        ], 
        
        // Non-Windows OS (e.g., Linux, macOS) settings
        [
          "OS != 'win'", {
            "cflags!": [ "-fno-rtti" ], // Disable RTTI for non-Windows platforms
            "cflags_cc!": [ "-fno-rtti" ], // Disable RTTI for C++ compilation
            "cflags_cc+": [ "-frtti" ] // Enable RTTI for C++ compilation on platforms where supported
          }
        ],

        // macOS-specific settings
        [
          "OS == 'mac'", {
            "cflags+": ["-fvisibility=hidden"], // Hide symbols to avoid symbol conflicts
            "xcode_settings": {
              "GCC_SYMBOLS_PRIVATE_EXTERN": "YES", // Hide symbols in private externs
              "WARNING_CFLAGS": [
                "-Wno-sign-compare", // Suppress sign comparison warnings
                "-Wno-unused-variable", // Suppress unused variable warnings
                "-Wno-unused-function", // Suppress unused function warnings
                "-Wno-ignored-qualifiers" // Suppress ignored qualifiers warnings
              ],
              "OTHER_CPLUSPLUSFLAGS": [
                "-mmacosx-version-min=10.8", // Set the minimum macOS deployment target
                "-std=c++11", // Use C++11 standard
                "-stdlib=libc++", // Use the libc++ standard library
                "-arch x86_64", // Target 64-bit architecture
                "-arch arm64" // Target ARM64 architecture (for Apple Silicon)
              ],
              "OTHER_LDFLAGS": [
                "-stdlib=libc++", // Link against libc++ on macOS
                "-arch x86_64", // Link against 64-bit architecture
                "-arch arm64" // Link against ARM64 architecture (for Apple Silicon)
              ],
              "GCC_ENABLE_CPP_RTTI": "YES", // Enable C++ RTTI (Run-Time Type Information)
              "GCC_ENABLE_CPP_EXCEPTIONS": "YES", // Enable C++ exception handling
              "MACOSX_DEPLOYMENT_TARGET": "10.8" // Set the macOS deployment target to 10.8
            }
          }
        ],
        
        // Linux-specific settings
        [
          "OS == 'linux'", {
            "cflags": [], // No additional flags
            "cflags!": [ "-fno-tree-vrp", "-fno-exceptions" ], // Disable certain optimizations and exceptions
            "cflags_cc!": [ "-fno-exceptions" ] // Disable exceptions for C++ compilation
          }
        ]
      ],
      
      // Define dependencies for the build process
      "dependencies": [
        "<(module_root_dir)/deps/rocksdb/rocksdb.gyp:rocksdb" // RocksDB is a dependency for the leveldown module
      ],
      
      // Include directories needed for the build
      "include_dirs": [
        "<!(node -e \"require('napi-macros')\")" // Include NAPI macros for native bindings
      ],
      
      // Sources that should be compiled for this target
      "sources": [
        "binding.cc" // The main C++ source file for building the leveldown module
      ]
    }
  ],

  // Variables section for any additional configurable options
  "variables": {
    "openssl_fips": "" // Option to define whether to use OpenSSL FIPS (if applicable)
  }
}
