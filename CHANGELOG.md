# Changelog

All notable changes to the 3PDD Dataset Builder project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-09

### Added
- Initial release of 3PDD Dataset Builder
- High-performance image indexing with parallel processing
- Support for three camera perspectives: body, face, and hands
- Two dataset structure types: split (train/val/test) and flat
- Interactive command-line interface
- Real-time progress tracking
- Class mapping system with JSON configuration

### Features
- Zero external dependencies (Python 3.7+ standard library only)
- Cross-platform support (Windows, Linux, macOS)
- Capable of handling 50M+ files efficiently
- Automatic class directory creation

### Notes
- Built for the Driver Monitoring Dataset (DMD) by Vicomtech
- Requires pre-extracted frames from DMD videos using DEx tool

[1.0.0]: https://github.com/azizoglu/dmd-to-3pdd-builder/releases/tag/v1.0.0
