from tkinter import Tk, Button, Label, filedialog, Listbox, Scrollbar, mainloop
from PyPDF2 import PdfMerger


def rearrange_pdf_files(pdf_files):
    # Open a new window to allow the user to rearrange the files
    rearrange_window = Tk()
    rearrange_window.title("Rearrange PDF Files")
    rearrange_window.geometry("600x500")  # Set the width and height

    # Create a listbox and scrollbar
    listbox = Listbox(rearrange_window, selectmode="extended")
    scrollbar = Scrollbar(rearrange_window, command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)

    # Add selected files to the listbox
    for file in pdf_files:
        listbox.insert("end", file)

    # Pack the listbox and scrollbar
    listbox.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def move_up():
        selected_indices = listbox.curselection()
        for i in selected_indices:
            if i > 0:
                listbox.delete(i)
                listbox.insert(i - 1, pdf_files[i])

    def move_down():
        selected_indices = listbox.curselection()
        for i in reversed(selected_indices):
            if i < listbox.size() - 1:
                listbox.delete(i)
                listbox.insert(i + 1, pdf_files[i])

    def on_done():
        selected_files = listbox.get(0, "end")
        merge_pdfs(selected_files)
        rearrange_window.destroy()

    # Create buttons to move items up and down
    up_arrow = "\u25b2"  # Upwards black arrow Unicode
    down_arrow = "\u25bc"  # Downwards black arrow Unicode
    move_up_button = Button(rearrange_window, text=up_arrow,
                            command=move_up, font=("Helvetica", 14))
    move_down_button = Button(
        rearrange_window, text=down_arrow, command=move_down, font=("Helvetica", 14))
    move_up_button.pack(side="left", padx=5, pady=5)
    move_down_button.pack(side="left", padx=5, pady=5)

    # Create a button to trigger the merge operation and close the rearrange window
    done_button = Button(rearrange_window, text="Merge PDFs", command=on_done)
    done_button.pack(pady=10)

    # Run the rearrange window's event loop
    rearrange_window.mainloop()


def select_pdf_files():
    # Prompt the user to select PDF files
    pdf_files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])

    if pdf_files:
        rearrange_pdf_files(pdf_files)
    else:
        # Show an error message if no files were selected
        message_label.config(text="No PDF files selected.")


def merge_pdfs(pdf_files):
    # Create an instance of PdfFileMerger() class
    merger = PdfMerger()

    for file in pdf_files:
        # Append selected PDF files
        merger.append(file)

    # Prompt the user to select a save location for the merged PDF file
    merged_filename = filedialog.asksaveasfilename(
        defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if merged_filename:
        merger.write(merged_filename)
        merger.close()

        # Show a success message
        message_label.config(text="PDF files merged successfully!")
    else:
        # Show an error message if no save location was selected
        message_label.config(text="Merging cancelled.")


# Create the main window
window = Tk()
window.title("PDF Merger")

# Create a button to select PDF files
select_button = Button(window, text="Select PDF Files",
                       command=select_pdf_files)
select_button.pack(pady=10)

# Create a label to display messages
message_label = Label(window, text="")
message_label.pack()

# Run the main event loop
mainloop()
