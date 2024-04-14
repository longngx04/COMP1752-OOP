import tkinter as tk
from video_library import get_name, get_rating, get_play_count, set_rating

# UpdateVideos class for the Update Videos section
class UpdateVideos:
    def __init__(self, window):
        window.geometry("600x300")
        window.title("Update Videos")

        # Create label for entering video number
        self.video_number_lbl = tk.Label(window, text="Enter Video Number:")
        self.video_number_lbl.pack(pady=10)

        # Create entry field for video number
        self.video_number_entry = tk.Entry(window)
        self.video_number_entry.pack()

        # Create label for entering new rating
        self.new_rating_lbl = tk.Label(window, text="Enter New Rating:")
        self.new_rating_lbl.pack(pady=10)

        # Create entry field for new rating
        self.new_rating_entry = tk.Entry(window)
        self.new_rating_entry.pack()

        # Create button to update rating
        self.update_button = tk.Button(window, text="Update Rating", command=self.update_rating)
        self.update_button.pack(pady=10)

        # Create label to display the result of the update
        self.result_label = tk.Label(window, text="", fg="blue")
        self.result_label.pack(pady=10)

    # Function to handle the Update Rating button click
    def update_rating(self):
        video_number = self.video_number_entry.get()
        new_rating = self.new_rating_entry.get()

        video_name = get_name(video_number)

        if video_name is not None:
            try:
                new_rating = int(new_rating)
                set_rating(video_number, new_rating)  # Update the video rating
                play_count = get_play_count(video_number)  # Get the play count of the video
                self.result_label.config(text=f"Video: {video_name}\nNew Rating: {new_rating}\nPlay Count: {play_count}", fg="blue")
            except ValueError:
                self.result_label.config(text="Invalid rating. Please enter a valid integer.", fg="red")
        else:
            self.result_label.config(text=f"Video {video_number} not found", fg="red")


if __name__ == "__main__":
    window = tk.Tk()  # Create a Tkinter window
    UpdateVideos(window)  # Initialize the UpdateVideos class
    window.mainloop()  # Run the Tkinter main loop to handle GUI interactions
