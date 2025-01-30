import os
os.environ['GRADIO_ANALYTICS_ENABLED'] = 'False'
import gradio as gr
import json
from datetime import datetime

# File to store TV show progress
PROGRESS_FILE = "tv_show_progress.json"

# Load progress from file or create empty dict
try:
    with open(PROGRESS_FILE, "r") as f:
        tv_show_progress = json.load(f)
except FileNotFoundError:
    tv_show_progress = {}
except json.JSONDecodeError:
    tv_show_progress = {}
    with open(PROGRESS_FILE, "w") as f:
        json.dump(tv_show_progress, f)

# Function to save or update the progress of a TV show
def track_tv_show(show_name, season, episode, notes):
    if show_name.strip() == "":
        return "⚠️ Please enter a valid show name!"
    
    # Get previous progress if it exists
    prev_progress = tv_show_progress.get(show_name, None)
    
    # Update the dictionary with the current progress
    tv_show_progress[show_name] = {
        "Season": season,
        "Episode": episode,
        "Notes": notes.strip() if notes else ""
    }
    
    # Auto-save progress
    try:
        with open(PROGRESS_FILE, "w") as f:
            json.dump(tv_show_progress, f, indent=2)
    except Exception as e:
        return f"⚠️ Error auto-saving progress: {str(e)}"
    
    # Generate progress indicator
    progress_emoji = "🆕 " if not prev_progress else "📺 "
    if prev_progress:
        if season > prev_progress["Season"] or (season == prev_progress["Season"] and episode > prev_progress["Episode"]):
            progress_emoji = "⏩ "  # Forward progress
        elif season < prev_progress["Season"] or (season == prev_progress["Season"] and episode < prev_progress["Episode"]):
            progress_emoji = "⏪ "  # Backward progress
    
    # Return the confirmation message with emoji
    return f"{progress_emoji}Updated progress for '{show_name}' - Season {season}, Episode {episode}"

# Function to retrieve the progress of a TV show
def get_progress(show_name):
    if show_name in tv_show_progress:
        progress = tv_show_progress[show_name]
        return f"You are currently on Season {progress['Season']}, Episode {progress['Episode']} of '{show_name}'."
    else:
        return f"No progress recorded for '{show_name}'."

# Function to save progress to file
def save_progress(status_output):
    try:
        with open(PROGRESS_FILE, "w") as f:
            json.dump(tv_show_progress, f, indent=2)
        return "💾 Progress saved successfully!"
    except Exception as e:
        return f"⚠️ Error saving progress: {str(e)}"

# Function to load progress from file
def load_progress(file_path, status_output):
    global tv_show_progress
    try:
        file_to_load = file_path.name if file_path else PROGRESS_FILE
        with open(file_to_load, "r") as f:
            tv_show_progress = json.load(f)
        return "📂 Progress loaded successfully!"
    except Exception as e:
        return f"⚠️ Error loading progress: {str(e)}"

# Function to export progress with timestamp
def export_progress():
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        export_file = f"tv_show_progress_backup_{timestamp}.json"
        with open(export_file, "w") as f:
            json.dump(tv_show_progress, f, indent=2)
        return f"💾 Backup saved as {export_file} 🎉"
    except Exception as e:
        return f"⚠️ Error creating backup: {str(e)}"

# Function to import backup
def import_backup(file_path, status_output):
    global tv_show_progress
    if not file_path:
        return "⚠️ Please select a backup file to import!"
    try:
        with open(file_path.name, "r") as f:
            backup_data = json.load(f)
        
        # Validate backup data structure
        if not isinstance(backup_data, dict):
            return "❌ Invalid backup file format!"
            
        # Create backup of current data before import
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_before_import = f"tv_show_progress_before_import_{timestamp}.json"
        with open(backup_before_import, "w") as f:
            json.dump(tv_show_progress, f, indent=2)
            
        # Update the progress
        tv_show_progress = backup_data
        
        # Save to main progress file
        with open(PROGRESS_FILE, "w") as f:
            json.dump(tv_show_progress, f, indent=2)
            
        return f"✨ Backup imported successfully! Previous data backed up to {backup_before_import} 🔄"
    except json.JSONDecodeError:
        return "❌ Invalid JSON file format!"
    except Exception as e:
        return f"⚠️ Error importing backup: {str(e)}"

# Function to delete a show from the watch list
def delete_show(show_name, watching_output, status_output):
    if not show_name.strip():
        return "⚠️ Please enter a show name to delete!", display_watching()
        
    if show_name not in tv_show_progress:
        return f"❌ Show '{show_name}' not found in your watch list!", display_watching()
    
    # Delete the show and auto-save
    del tv_show_progress[show_name]
    try:
        with open(PROGRESS_FILE, "w") as f:
            json.dump(tv_show_progress, f, indent=2)
        return f"✅ Successfully removed '{show_name}' from your watch list!", display_watching()
    except Exception as e:
        return f"⚠️ Error saving changes: {str(e)}", display_watching()

# Function to display the "Watching" tab content
def display_watching():
    if not tv_show_progress:
        return "📭 You are not currently watching any shows."
    
    watching_list = []
    for show, progress in sorted(tv_show_progress.items()):
        # Add emoji based on progress
        show_emoji = "🎬 "  # Default emoji
        if progress["Season"] == 1 and progress["Episode"] <= 3:
            show_emoji = "🆕 "  # New show
        elif progress["Season"] >= 3:
            show_emoji = "🌟 "  # Long-running show
            
        # Create the show entry
        entry = f"{show_emoji}{show}: Season {progress['Season']}, Episode {progress['Episode']}"
        
        # Handle notes with URL detection
        if progress.get("Notes"):
            notes = progress["Notes"]
            # Check if notes contain URLs
            import re
            url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            urls = re.findall(url_pattern, notes)
            
            if urls:
                # If URLs exist, make them clickable
                preview = notes
                for url in urls:
                    preview = preview.replace(url, f"<{url}>")
            else:
                # If no URLs, show preview with ellipsis
                preview = notes[:50] + ("..." if len(notes) > 50 else "")
            
            entry += f"\n📝 Notes: {preview}"
        
        watching_list.append(entry)
    
    return "\n\n".join(watching_list)  # Add extra newline between shows for better readability

# Create the Gradio interface using Blocks
with gr.Blocks(title="TV Show Progress Tracker") as interface:
    gr.Markdown("# 📺 TV Show Progress Tracker")
    
    with gr.Tabs():
        # Track Progress Tab
        with gr.Tab("📝 Track Progress"):
            show_input = gr.Textbox(label="Enter the name of your TV show:")
            with gr.Row():
                season_input = gr.Slider(minimum=1, maximum=20, step=1, label="Select Season:")
                episode_input = gr.Slider(minimum=1, maximum=30, step=1, label="Select Episode:")
            notes_input = gr.Textbox(label="Notes (optional):", placeholder="Add any notes about the show or episode...", lines=3)
            track_btn = gr.Button("📌 Track Progress", variant="primary")
            progress_output = gr.Textbox(label="Progress Status:")
            
            # Connect the tracking function
            track_btn.click(
                fn=track_tv_show,
                inputs=[show_input, season_input, episode_input, notes_input],
                outputs=progress_output
            )
        
        # Watching Tab
        with gr.Tab("👀 Currently Watching"):
            watching_output = gr.Textbox(label="Your Watch List:", value=display_watching(), lines=10, max_lines=15)
            refresh_btn = gr.Button("🔄 Refresh List")
            
            # Delete show section
            with gr.Row():
                delete_input = gr.Textbox(label="Enter show name to remove:")
                delete_btn = gr.Button("🗑️ Remove Show", variant="stop")
            
            status_output = gr.Textbox(label="Status:")
            
            # Connect the delete function
            delete_btn.click(
                fn=delete_show,
                inputs=[delete_input, watching_output, status_output],
                outputs=[status_output, watching_output]
            )
            
            # Connect the refresh function
            refresh_btn.click(
                fn=display_watching,
                outputs=watching_output
            )
        
        # Backup Management Tab
        with gr.Tab("💾 Backup Management"):
            gr.Markdown("### 📦 Manage Your Show Data")
            
            with gr.Row():
                backup_btn = gr.Button("💾 Create Backup", variant="primary")
                
            gr.Markdown("### 🔄 Restore from Backup")
            gr.Markdown("⚠️ Note: Importing a backup will replace your current data. A backup of your current data will be created automatically.")
            
            with gr.Row():
                backup_file = gr.File(label="Select backup file to import:", file_types=[".json"])
                import_btn = gr.Button("📥 Import Backup", variant="secondary")
            
            backup_status = gr.Textbox(label="Operation Status:", lines=3)
            
            # Connect backup operation functions
            backup_btn.click(fn=export_progress, inputs=None, outputs=backup_status)
            import_btn.click(fn=import_backup, inputs=[backup_file, backup_status], outputs=backup_status)

# Launch the Gradio app in local-only mode
interface.launch(
    share=False, 
    server_name="127.0.0.1",
    server_port=7861  # Use a different port to avoid conflicts
)
