import gradio as gr
from chatbot import final_answer
import cv2
from PIL import Image
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\suuser\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(image):
    img = Image.fromarray(image)
    text = pytesseract.image_to_string(img)
    print("OCR Result:", text)
    cleaned = text.replace('\n', ' ').strip()
    return cleaned


def solve_from_input(message, image):
    extracted = extract_text_from_image(image) if image is not None else ""
    if not message and not extracted:
        return [("User", "Please provide a question or an image.")]

    combined = f"{message} {extracted}".strip()
    answer = final_answer(combined)
    return [(combined, answer)]


# UI setup
with gr.Blocks() as demo:
    gr.Markdown("## ?? Math Chatbot (Text + Image OCR Powered)")

    with gr.Row():
        lang = gr.Dropdown(["English"], label="Select Language", value="English")

    chat = gr.Chatbot()
    msg = gr.Textbox(label="Ask a math question")
    img_input = gr.Image(type="numpy", label="Upload an image (optional)")
    submit_btn = gr.Button("Submit")
    clear_btn = gr.Button("Clear Chat")

    history = []

    def respond_to_user(msg, img):
        pairs = solve_from_input(msg, img)
        history.extend(pairs)
        return history

    submit_btn.click(respond_to_user, inputs=[msg, img_input], outputs=chat)
    clear_btn.click(lambda: [], None, chat)

demo.launch(inbrowser=True)
