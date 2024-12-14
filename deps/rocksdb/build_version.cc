#include "rocksdb/util/build_version.h"

// String constant to store the Git SHA of the current build.
// Typically, this would contain the hash of the latest commit in the Git repository.
// Here, it is set to "None," indicating that this information is not available or not provided.
const char* rocksdb_build_git_sha = "rocksdb_build_git_sha:None";

// String constant to store the date of the latest Git commit.
// In a typical build, this would reflect the date of the commit associated with the Git SHA.
// Here, it is set to "None," indicating that the date information is not available or not provided.
const char* rocksdb_build_git_date = "rocksdb_build_git_date:None";

// String constant to store the compilation date of the RocksDB library.
// This would normally be set during the build process to the current date and time of compilation.
// The value "None" suggests that this information was not included in the build.
const char* rocksdb_build_compile_date = "None";
