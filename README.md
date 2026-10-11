# Activate Linux

The iconic "Activate Windows" watermark, but for Linux. Because why not.

![screenshot](screenshot.png)

A floating, transparent, click-through overlay that sits in the bottom-right corner of your screen — just like the real thing.

## Features

- **Transparent** — only the text is visible, no background box
- **Click-through** — mouse events pass straight through to windows below
- **Always on top** — floats above all windows, just like Windows
- **Lightweight** — single Python script using PyQt5

## Requirements

- Python 3
- PyQt5 (`pip install PyQt5` or `apt install python3-pyqt5`)
- X11 with a compositor (for transparency)

## Usage

```bash
python3 activate-linux.py
```

## Autostart (KDE Plasma)

Copy `activate-linux.desktop` to `~/.config/autostart/`:

```bash
cp activate-linux.desktop ~/.config/autostart/
```

## Customize

Edit the text, font size, color, or position directly in `activate-linux.py`.

## License

MIT — do whatever you want with it.
