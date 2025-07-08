import os

def get_all_saved_data_source_scripts():
    return os.listdir(f'config\\data_loading_scripts')

def destroy_widgets(frames):
    for frame in frames:
        for widget in frame.winfo_children():
            widget.destroy()

    return None