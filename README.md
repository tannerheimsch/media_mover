# Media Mover

Media Mover is a simple tool that allows users to organize their TV shows and movies by moving them to specified destination folders. It provides an easy-to-use interface for setting up destination folders for both TV shows and movies, and uses [TeraCopy](https://www.codesector.com/teracopy) for efficient and reliable file transfers.

![Media Mover Logo](https://i.gyazo.com/7c9ced6c41f957731b3c12b6cc1cc39b.png)


## Features

- Allows users to set different destination folders for TV shows and movies (*i.e. C:/Plex/TV Shows, C:/Plex/Movies)*.
- If moving a movie file, it will automatically create a folder with that name and then move it.
- Utilizes TeraCopy for fast and secure file transfers.

## Prerequisites

Before using Media Mover, make sure you have the following installed:

- [TeraCopy](https://www.codesector.com/teracopy)
- Python 3.x

## Usage

1. Put Media Mover & the `_interal` folder in the CWD, it will list and move sub-folders/media files from within it.
2. Open Media Mover with preferred file type (either as a .py/.exe)
3. Setup the destination folders respectively.
4. Setup TeraCopy.exe path if different than default
5. Start moving your TV show folders/movies with a simple GUI. No more cutting and pasting!
