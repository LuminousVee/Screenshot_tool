# Screenshot Tool

A feature-rich desktop application built with Python and Tkinter that allows users to capture screenshots with various options including instant capture, delayed capture, and automatic interval capturing.



## Features

- 📸 **Instant Screenshot**: Capture your screen immediately
- ⏰ **Delayed Capture**: Set a countdown timer before capturing
- 🔄 **Auto Capture**: Take screenshots automatically at specified intervals
- 🪟 **Auto-minimize**: Automatically minimize the application window before capture
- 📁 **Organized Storage**: Screenshots are saved in timestamped directories
- 📊 **Statistics Tracking**: Keep track of how many screenshots you've taken
- 📝 **Status Updates**: Real-time status feedback in the application

## Prerequisites

Before running this application, ensure you have the following installed:
- Python 3.x
- PIL (Python Imaging Library)
- Tkinter (usually comes with Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/LuminousVee/screenshot_tool.git
cd screenshot_tool
```

2. Install required packages:
```bash
pip install Pillow
```

## Usage

1. Run the application:
```bash
python screenshot_tool.py
```

2. Using the different capture modes:

### Instant Capture
- Click "Take Screenshot Now" to capture immediately
- The screen will be captured instantly if auto-minimize is disabled

### Delayed Capture
- Enter the delay time in seconds
- Click "Take Delayed Screenshot"
- The screenshot will be taken after the specified delay

### Auto Capture
- Enter the interval time in seconds
- Click "Start Auto Capture" to begin automatic captures
- Click "Stop Auto Capture" to end the sequence

### Options
- Toggle "Auto-minimize before capture" to hide the application window during capture

## Output

Screenshots are saved in a directory named `screenshots_YYYYMMDD_HHMMSS` where:
- `YYYY`: Year
- `MM`: Month
- `DD`: Day
- `HH`: Hour
- `MM`: Minute
- `SS`: Second

Individual screenshots are saved as PNG files with timestamps.

## File Structure
```
screenshot_tool/
├── screenshot_tool.py
├── screenshots_20241028_123456/
│   ├── screenshot_20241028_123456.png
│   ├── screenshot_20241028_123556.png
│   └── ...
└── README.md
```

## Key Features Explained

### Auto-minimize
- Automatically minimizes the application window before taking a screenshot
- Helps capture clean screenshots without the tool interface
- Can be toggled on/off in the options

### Interval Capture
- Takes screenshots automatically at specified intervals
- Continues until manually stopped
- Useful for time-lapse or monitoring purposes

### Error Handling
- Comprehensive error messages for invalid inputs
- Safe application closure during active captures
- Directory creation and file saving safeguards

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using Python's Tkinter library
- Uses PIL for screenshot capabilities
- Inspired by the need for a flexible screenshot tool

## Troubleshooting

### Common Issues:

1. **Permission Errors**
   - Ensure you have write permissions in the application directory

2. **Screenshot Not Capturing**
   - Check if your system allows screen capture
   - Verify PIL is installed correctly

3. **GUI Not Responding**
   - Check if auto-capture interval is not too low
   - Ensure sufficient system resources are available

## Future Enhancements

- [ ] Region selection for screenshots
- [ ] Multiple monitor support
- [ ] Screenshot preview
- [ ] Custom save locations
- [ ] Hotkey support
- [ ] Image format options

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
