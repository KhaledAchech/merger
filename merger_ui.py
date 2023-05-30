from tkinter import Tk, Button, Label, filedialog
from PyPDF2 import PdfMerger


def select_pdf_files():
    # Prompt the user to select PDF files
    pdf_files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])

    if pdf_files:
        merge_pdfs(pdf_files)
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
window.mainloop()
