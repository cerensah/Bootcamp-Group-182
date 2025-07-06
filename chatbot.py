import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("./math_tutor_model")
model = AutoModelForSeq2SeqLM.from_pretrained("./math_tutor_model")

def solve_basic_math(question):
    match = re.findall(r'(\d+\.?\d*\s*[\+\-\*/]\s*\d+\.?\d*)', question)
    if match:
        try:
            return eval(match[0])  # WARNING: Don't use eval for untrusted input
        except Exception:
            return None
    return None

def override_answer(llm_text, correct_answer):
    # Replace the last number in the LLM answer with the correct one
    return re.sub(r'(-?\d+\.?\d*)(?!.*\d)', str(correct_answer), llm_text)

print("?? Welcome to Math Tutor Chat! Type 'exit' to quit.\n")

while True:
    question = input("You: ")
    if question.lower() == "exit":
        print("?? Goodbye bestie!")
        break

    correct = solve_basic_math(question)

    prompt = f"Question: {question} Answer:"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=128)
    outputs = model.generate(**inputs, max_length=128, num_beams=4, do_sample=False)
    llm_answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    if correct is not None:
        final_answer = override_answer(llm_answer, correct)
        print(f"?? MathTutor: {final_answer} ? (corrected)")
    else:
        print(f"?? MathTutor: {llm_answer}")
