import tkinter as tk
import tkinter.scrolledtext as tkst

import font_manager as fonts 
import video_library as lib  

# Function to set text content in a text area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

# CreateVideoList class for the Create Video List section
class CreateVideoList():
    def __init__(self, window):
        window.geometry("900x350")
        window.title("Create Video List")

        # Create List All Videos button
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # Create Enter Video Number label
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Create Entry field for video number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Create Add to Playlist button
        add_to_playlist_btn = tk.Button(window, text="Add to Playlist", command=self.add_to_playlist_clicked)
        add_to_playlist_btn.grid(row=0, column=3, padx=10, pady=10)

        # Create Play Playlist button
        play_playlist_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist_clicked)
        play_playlist_btn.grid(row=0, column=4, padx=10, pady=10)

        # Create Reset Playlist button
        reset_playlist_btn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist_clicked)
        reset_playlist_btn.grid(row=0, column=5, padx=10, pady=10)

        # Create scrolled text area for playlist
        self.playlist_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=6, sticky="W", padx=10, pady=10)

        # Create status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=6, sticky="W", padx=10, pady=10)

        self.playlist = []  # Initialize an empty playlist
        self.list_videos_clicked()  # Call the list_videos_clicked function to display video list initially

    # Function to handle Add to Playlist button 
    def add_to_playlist_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            self.playlist.append(name)
            set_text(self.playlist_txt, "\n".join(self.playlist))
            self.status_lbl.configure(text="Video added to playlist!")
        else:
            self.status_lbl.configure(text=f"Video {key} not found")

    # Function to handle Play Playlist button 
    def play_playlist_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if key is not None:
            lib.increment_play_count(key)
        self.status_lbl.configure(text="Playlist played!")

    # Function to handle Reset Playlist button 
    def reset_playlist_clicked(self):
        self.playlist.clear()  # Clear the playlist
        set_text(self.playlist_txt, "")  # Clear the playlist text area
        self.status_lbl.configure(text="Playlist cleared!")

    # Function to list all videos
    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.playlist_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

if __name__ == "__main__":
    window = tk.Tk()  # Create a Tkinter window
    CreateVideoList(window)  # Initialize the CreateVideoList class
    window.mainloop()  # Run the Tkinter main loop to handle GUI interactions
