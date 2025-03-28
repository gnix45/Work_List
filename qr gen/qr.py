import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

# Function to generate QR Code
def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter text or select an image")
        return

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    qr_img.save("qrcode.png")

    display_qr(qr_img)

# Function to display QR code
def display_qr(qr_img):
    qr_img_tk = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_img_tk)
    qr_label.image = qr_img_tk

# Function to select image
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

# Function to save QR code
def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        try:
            qr_img = Image.open("qrcode.png")
            qr_img.save(file_path)
            messagebox.showinfo("Success", "QR Code saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save QR Code: {e}")

# Setup main window
root = tk.Tk()
root.title("Elegant QR Code Generator")
root.geometry("400x500")
root.config(bg="#f8f9fa")  # Soft background color

# Main frame for content
frame = tk.Frame(root, bg="white", bd=2, relief="flat")
frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=450)

# Title
title = tk.Label(frame, text="QR Code Generator", font=("Arial", 14, "bold"), bg="white", fg="#333")
title.pack(pady=10)

# Input field
entry = tk.Entry(frame, width=30, font=("Arial", 12), bd=2, relief="solid", justify="center")
entry.pack(pady=10)

# Buttons with rounded corners
btn_style = {"font": ("Arial", 12), "fg": "white", "bg": "#6c757d", "bd": 0, "relief": "flat", "width": 20, "height": 1}

generate_btn = tk.Button(frame, text="Generate QR Code", command=generate_qr, **btn_style)
#generate_btn = tk.Button(root, text="Generate QR Code", command=generate_qr, font=("Arial", 12))
generate_btn.pack(pady=5)

image_btn = tk.Button(frame, text="Select Image", command=select_image, **btn_style )
image_btn.pack(pady=5)

save_btn = tk.Button(frame, text="Save QR Code", command=save_qr, **btn_style)
save_btn.pack(pady=5)

# QR Code Display
qr_label = tk.Label(frame, bg="white")
qr_label.pack(pady=10)

# Run the main loop
root.mainloop()
