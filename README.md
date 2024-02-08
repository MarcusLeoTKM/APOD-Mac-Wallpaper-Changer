# APOD Mac Wallpaper Changer

* [Requirements](#Requirements)
* [Introduction](#Introduction)
* [Setup](#Setup)
  
## Requirements
- MacOS

  
## Introduction
Do you want your desktop wallpaper to feature the sky and the universe? This small project enables you to download images from NASA's APOD (Astronomy Picture of the Day), save them in a directory of your choice, and automatically put them as your wallpaper.


## Setup
1. Workspace setup: `cd /path/` replace `/path/` with your actual path where you wish to locate your project. Ex. `cd ~/Desktop` if you want your project to appear on the Desktop.
2. To check your current working path: `pwd`, this will be your `/path/`.
3. Create a directory: `mkdir name_of_your_directory`.
4. Your `patht` will be `/path/name_of_your_directory_created_in_step_2`. Ex. `/Users/Username/Desktop/WallpaperImage`.
5. Go to Desktop -> right click anywhere in the background -> choose `Change Wallpaper` -> scoll down to the bottom -> choose `Add folder` -> choose the directory you created in step 2 -> click on `Auto-Rotate`.
6. Clone this repository: `gh repo clone MarcusLeoTKM/APOD-Mac-Wallpaper-Changer`.
7. Go to https://api.nasa.gov, and sign up for an API key. This will be your `api_key`.
8. You should have your `patht` and `api_key`.
