import tkinter as tk

# Import custom modules
import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideoList
from update_video import UpdateVideos


# Function to handle "Check Videos" button click
def check_videos_clicked():
    status_lbl.configure(text="Check Videos button was clicked!")
    CheckVideos(tk.Toplevel(window))
# Function to handle "Create Video List" button click
def create_video_list_clicked():
    status_lbl.configure(text="Create Video List button was clicked!")
    CreateVideoList(tk.Toplevel(window))
# Function to handle "Update Videos" button click
def update_video_clicked():
    status_lbl.configure(text="Update Video button was clicked!")
    UpdateVideos(tk.Toplevel(window))
    
# Create the main program window
window = tk.Tk()
window.geometry("520x150")
window.title("Video Player")

# Configure custom fonts
fonts.configure()

# Header label
header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Buttons to open different program sections
check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_video_list_btn = tk.Button(window, text="Create Video List", command=create_video_list_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_videos_btn = tk.Button(window, text="Update Videos", command=update_video_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

# Status label to show button click information
status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
