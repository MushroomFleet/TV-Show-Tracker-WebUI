# 📺 TV Show Progress Tracker

A user-friendly Gradio application to track your TV show watching progress, manage your watch list, and maintain backups of your viewing history.

## 🌟 Features

### 📝 Track Progress
- Keep track of which episode and season you're on for multiple TV shows
- Add optional notes for each show (supports URLs)
- Auto-saving functionality ensures your progress is never lost
- Visual progress indicators show whether you've moved forward (⏩) or backward (⏪) in a series

### 👀 Watch List Management
- View all your currently watching shows in one place
- Easy-to-read format with emoji indicators:
  - 🆕 New shows (Season 1, Episodes 1-3)
  - 🌟 Long-running shows (Season 3+)
  - 🎬 Regular shows
- Delete shows you've finished or no longer want to track
- One-click list refresh
- Notes preview with clickable URLs

### 💾 Backup Management
- Create timestamped backups of your watch list
- Import backups with automatic safety features:
  - Validates backup file format
  - Creates an automatic backup of current data before import
  - Supports JSON file format

## 🚀 Getting Started

1. Install the required dependencies:
```bash
./install.bat
```

2. Run the application:
```bash
./run-gradio.bat
```

The application will start on `http://127.0.0.1:7861`

## 💡 Usage

### Adding/Updating a Show
1. Go to the "📝 Track Progress" tab
2. Enter the show name
3. Select the season and episode using the sliders
4. (Optional) Add any notes about the show or episode
5. Click "📌 Track Progress"

### Viewing Your Watch List
1. Navigate to the "👀 Currently Watching" tab
2. View all your shows with their current progress
3. Click "🔄 Refresh List" to update the display
4. To remove a show, enter its name and click "🗑️ Remove Show"

### Managing Backups
1. Go to the "💾 Backup Management" tab
2. Click "💾 Create Backup" to save your current progress
3. To restore from a backup:
   - Select a backup file using the file picker
   - Click "📥 Import Backup"
   - A safety backup of your current data will be created automatically

## 📋 Data Storage
- Progress is stored in `tv_show_progress.json`
- Backups are saved with timestamps (e.g., `tv_show_progress_backup_20250130_225845.json`)
- All data is stored locally on your machine

## ⚠️ Notes
- The application runs in local-only mode for security
- Maximum supported values:
  - Seasons: 1-20
  - Episodes: 1-30
  - Notes: Unlimited length with URL support
