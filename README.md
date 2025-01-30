# TV Show Progress Tracker

A simple and intuitive web application built with Gradio that helps you keep track of your TV show watching progress. Never lose track of which episode you're on again!

## Features

- **Track Progress**: Easily record which season and episode you're currently watching for any TV show
- **Check Progress**: Quickly look up where you left off on any show
- **Currently Watching List**: View all the shows you're currently tracking in one place
- **User-Friendly Interface**: Simple and clean interface with sliders for season and episode selection
- **Local Storage**: All data is stored locally during the session

## Prerequisites

- Python 3.7 or higher
- Windows OS (for batch files, though the app can run on any OS with Python)

## Installation

1. Clone this repository:
   ```bash
   git clone [your-repository-url]
   cd [repository-name]
   ```

2. Run the installation script:
   - On Windows: Simply double-click `install.bat`
   - On other OS:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Unix/macOS
     pip install -r requirements.txt
     ```

## Running the Application

1. Start the application:
   - On Windows: Double-click `run-gradio.bat`
   - On other OS:
     ```bash
     source venv/bin/activate  # On Unix/macOS
     python gradio_app.py
     ```

2. Open your web browser and navigate to: `http://127.0.0.1:7860`

## Usage Guide

### Tracking a New Show

1. Navigate to the "Track Progress" tab
2. Enter the TV show name in the text box
3. Use the sliders to select:
   - Season number (1-20)
   - Episode number (1-30)
4. Click "Track Progress" to save your progress
5. You'll see a confirmation message showing your current progress

### Checking Show Progress

1. In the "Track Progress" tab
2. Scroll down to the "Check Progress" section
3. Enter the name of the show you want to check
4. Click "Check Progress"
5. The system will display your last saved position for that show

### Viewing All Shows

1. Click on the "Watching" tab
2. You'll see a list of all shows you're currently tracking
3. Each entry shows the show name, current season, and episode
4. Click "Refresh List" to update the display

## Technical Details

- Built with Gradio 4.44.1 or higher
- Runs on localhost (127.0.0.1) on port 7860
- Data persists only during the current session
- No external database required

## Limitations

- Data is not permanently stored and will be reset when the application is restarted
- Maximum of 20 seasons and 30 episodes per season in the selection sliders
- Runs in local-only mode (not accessible from other devices)

## Contributing

Feel free to fork this repository and submit pull requests for any improvements you'd like to add. Some potential areas for enhancement:
- Persistent storage
- Custom number of episodes per season
- Show descriptions and metadata
- Multiple user support
- Export/import functionality

