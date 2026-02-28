# Project Specification

## Overview

A Python script that generates a landscape PNG image with a centered periwinkle circle.

## Requirements

- Create a Python script `circle.py` that generates a PNG image file `output.png`
- The image must be landscape orientation with aspect ratio close to the golden ratio (1.618:1). Suggested size: 809x500 pixels.
- The background should be white
- A periwinkle-colored circle (RGB: 204, 204, 255) must be drawn at the center of the image
- The circle's diameter must equal exactly half the image height
- The circle should be filled (not just an outline)
- Include a test file `test_circle.py` that verifies:
  - `output.png` is created after running the script
  - The image dimensions have an aspect ratio within 0.01 of the golden ratio
  - The center pixel of the image is periwinkle
  - A pixel outside the circle (e.g. top-left corner) is white

## Architecture

Single-file script using Pillow (`PIL`) for image generation. Tests use `pytest` and Pillow for verification.

## Constraints

- Python 3.x with Pillow as the only external dependency
- The agent must modify `scripts/runner/Dockerfile` to add `python3` and `pip install Pillow pytest` since the base image is Node-based
- Must exit with code 0 on success
