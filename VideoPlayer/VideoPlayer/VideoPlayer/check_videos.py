import tkinter as tk
import tkinter.scrolledtext as tkst

import font_manager as fonts
import video_library as lib
from PIL import Image, ImageTk

# Dictionary containing paths to video images
video_images = {
    "01" : "C:\\Users\\long0\Downloads\\VideoPlayer\\VideoPlayer\\Tom and Jerry.jpg",
    "02" : "C:\\Users\\long0\Downloads\\VideoPlayer\\VideoPlayer\\Breakfast at Tiffany's.jpg",
    "03" : "C:\\Users\\long0\Downloads\\VideoPlayer\\VideoPlayer\\Casablanca.jpg",
    "04" : "C:\\Users\\long0\Downloads\\VideoPlayer\\VideoPlayer\\The sound of music.jpg",
    "05" : "C:\\Users\\long0\Downloads\\VideoPlayer\\VideoPlayer\\Gone with the wind.jpg",  
}

# Function to set text content in a text area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

# CheckVideos class for the Check Videos section
class CheckVideos():
    def __init__(self, window):
        window.geometry("750x400")
        window.title("Check Videos")

        # Create List All Videos button
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # Create Enter Video Number label
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Create Entry field for video number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Create Check Video button
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

         # Create scrolled text area for video list
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Create text area for video details
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Create status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Create label for displaying video image
        self.video_image_label = tk.Label(window)
        self.video_image_label.grid(row=1, column=3, sticky="SW", padx=10, pady=10)

         # Call the list_videos_clicked function to display video list initially
        self.list_videos_clicked()
    
     # Function to handle Check Video button click
    def check_video_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
            image_path = video_images.get(key)
            if image_path:
                self.display_image(image_path)
            else:
                self.video_image_label.config(image=None)
        else:
            set_text(self.video_txt, f"Video {key} not found")
            self.video_image_label.config(image=None)
        self.status_lbl.configure(text="Check Video button was clicked!")
    # Function to display the video image
    def display_image(self, image_path):

        thumbnail = Image.open(image_path)
        thumbnail = thumbnail.resize((200, 135), Image.LANCZOS)
        photo = ImageTk.PhotoImage(thumbnail)

        self.video_image_label.config(image=photo)
        self.video_image_label.image=photo

    # Function to list all videos
    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    CheckVideos(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
