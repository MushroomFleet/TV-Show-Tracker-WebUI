import gradio as gr

# Dictionary to store the progress of TV shows
tv_show_progress = {}

# Function to save or update the progress of a TV show
def track_tv_show(show_name, season, episode):
    if show_name.strip() == "":
        return "Please enter a valid show name!"
    
    # Update the dictionary with the current progress
    tv_show_progress[show_name] = {"Season": season, "Episode": episode}
    
    # Return the confirmation message
    return f"You are currently on Season {season}, Episode {episode} of '{show_name}'."

# Function to retrieve the progress of a TV show
def get_progress(show_name):
    if show_name in tv_show_progress:
        progress = tv_show_progress[show_name]
        return f"You are currently on Season {progress['Season']}, Episode {progress['Episode']} of '{show_name}'."
    else:
        return f"No progress recorded for '{show_name}'."

# Function to display the "Watching" tab content
def display_watching():
    if not tv_show_progress:
        return "You are not currently watching any shows."
    
    watching_list = []
    for show, progress in tv_show_progress.items():
        watching_list.append(f"{show}: Season {progress['Season']}, Episode {progress['Episode']}")
    
    return "\n".join(watching_list)

# Gradio Interface
with gr.Blocks() as demo:
    with gr.Tabs():
        # Tab 1: Track Progress
        with gr.Tab("Track Progress"):
            gr.Markdown("## Track Your TV Show Progress")
            
            with gr.Row():
                show_name_input = gr.Textbox(label="Enter the name of your TV show:")
                season_slider = gr.Slider(minimum=1, maximum=20, step=1, label="Select Season:")
                episode_slider = gr.Slider(minimum=1, maximum=30, step=1, label="Select Episode:")
            
            track_button = gr.Button("Track Progress")
            output_text = gr.Textbox(label="Progress Status:")
            
            # Track progress when button is clicked
            track_button.click(track_tv_show, inputs=[show_name_input, season_slider, episode_slider], outputs=output_text)
            
            with gr.Row():
                check_show_name = gr.Textbox(label="Check Progress for Show:")
                check_button = gr.Button("Check Progress")
                check_output = gr.Textbox(label="Progress Status:")
            
            # Check progress when button is clicked
            check_button.click(get_progress, inputs=check_show_name, outputs=check_output)
        
        # Tab 2: Watching
        with gr.Tab("Watching"):
            gr.Markdown("## Currently Watching")
            watching_output = gr.Textbox(label="Shows You're Watching:", lines=5)
            
            # Button to refresh the list of shows you're watching
            refresh_button = gr.Button("Refresh List")
            
            # Display the list of shows you're currently watching
            refresh_button.click(display_watching, inputs=[], outputs=watching_output)

# Launch the Gradio app in local-only mode
demo.launch(share=False, server_name="127.0.0.1", server_port=7860)