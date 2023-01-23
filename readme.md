# Directory Renam-er

A short python script that renames the files in a directory systematically. 

## Description

I wrote this script to solve a problem I am facing while developing a reusable digital gallery in Vue 3. I will be uploading various libraries of images and videos that need to be named with a consistent pattern in order to avoid hardcoding each image. The script asks the user to provide a target directory and a prefix to name each file with. Using the "os" library to avoid the following files: ".DS_Store", ".", ".."; it also only renames files with the following extensions: ".jpg", ".png", ".mp4".

