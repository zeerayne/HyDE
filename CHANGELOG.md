# Changelog

All notable changes to `HyDE` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to _Modified_ [CalVer](https://calver.org/). See [Versioning](https://github.com/HyDE-Project/HyDE/blob/master/RELEASE_POLICY.md#versioning-yymq) For more info

## [Unreleased] v25.7.3

We use a dedicated Python environment to keep HyDE clean and dependency-free. Just run your scripts with `hyde-shell`—it handles the environment for you.

Examples:  
  `hyde-shell mediaplayer.py`  
  `hyde-shell waybar`


### Added

- CHANGELOG.md to track notable changes
- Features and fixes for mediaplayer. #865
- HyDE's python environment rebuild on installation
- PyGObject for the python environment
- Mediaplayer: Add support for generic MPRIS metadata
- Mediaplayer: RIght click menu for mediaplayer
- Mediaplayer: Scroll up/down to seek

### Changed

- Launch Scripts using 'hyde-shell' instead of '$scrPath/'

### Fixed

- Waybar: Avoid multi user process conflict
- Mediaplayer: crash when player is not playing.

