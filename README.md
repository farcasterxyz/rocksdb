# rocksdb

This fork's sole purpose is to add prebuilds for Linux ARM to reduce install time on ARM-based systems.

Add to your project using:

```bash
yarn add @farcaster/rocksdb
```

```typescript
import AbstractRocksDB from '@farcaster/rocksdb';
```

### Git Submodules

This project uses Git Submodules. This means that you should clone it recursively if you're planning on working on it:

```bash
$ git clone --recurse-submodules https://github.com/Level/rocksdb.git
```

Alternatively, you can initialize submodules after cloning:

```bash
$ git submodule update --progress --init --recursive
```

### Publishing

1. Increment the version: `npm version ..`
2. Push to GitHub: `git push --follow-tags`
3. Wait for CI to complete
4. Download prebuilds into `./prebuilds`: `npm run download-prebuilds`
5. Optionally verify loading a prebuild: `npm run test-prebuild`
6. Optionally verify which files npm will include: `canadian-pub`
7. Finally: `npm publish`

## License

[MIT](LICENSE)

_`rocksdb` builds on the excellent work of the LevelDB and Snappy teams from Google and additional contributors to the LevelDB fork by Facebook. LevelDB and Snappy are both issued under the [New BSD License](http://opensource.org/licenses/BSD-3-Clause). A large portion of `rocksdb` Windows support comes from the [Windows LevelDB port](http://code.google.com/r/kkowalczyk-leveldb/) (archived) by [Krzysztof Kowalczyk](http://blog.kowalczyk.info/) ([`@kjk`](https://twitter.com/kjk)). If you're using `rocksdb` on Windows, you should give him your thanks!_
