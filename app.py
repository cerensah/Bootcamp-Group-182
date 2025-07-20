import gradio as gr
from chatbot import final_answer

from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Users\suuser\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image):
    img = Image.fromarray(image)
    text = pytesseract.image_to_string(img)
    cleaned = text.replace('\n', ' ').strip()
    return cleaned


def solve_from_input(message, image):
    if image is not None:
        question = extract_text_from_image(image)
    else:
        question = message
    answer = final_answer(question)
    return [(question, answer)]

with gr.Blocks() as demo:
    gr.Markdown("# ?? Math Tutor Chat with Image Support")

    with gr.Row():
        lang = gr.Dropdown(["English"], label="Select Language", value="English")
        clear = gr.Button("Clear Chat")

    chat = gr.Chatbot(label="Math Chat")
    msg = gr.Textbox(label="Ask a math question")
    img_input = gr.Image(type="numpy", label="Or upload image")

    msg.submit(solve_from_input, [msg, img_input], chat)
    img_input.change(solve_from_input, [msg, img_input], chat)
    clear.click(lambda: [], None, chat)

demo.launch(inbrowser=True)
