"""Module for handle errors for other modules"""

from tkinter import messagebox as MessageBox

def show_error(message, note_user=None):
    """Show the error that we passed"""

    MessageBox.showwarning("Error", f"Error: {message} \n{note_user}")