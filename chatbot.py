import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sympy import symbols, Eq, solve

tokenizer = AutoTokenizer.from_pretrained("./math_tutor_model")
model = AutoModelForSeq2SeqLM.from_pretrained("./math_tutor_model")


def solve_math_question(question: str):
    try:
        # 4 işlem soruları için override
        expression = re.findall(r"[\d\+\-\*/\(\)\.\s]+", question)

        # x'i bulma tarzı sorular için sympy ile override
        if "x" in question:
            return solve_equation_from_text(question)
        
        if expression:
            result = eval(expression[0])
            return round(result, 4)
        
        # havuz problemi, araba hızı tarzı problemler için override
        if "car" in question and "km" in question:
            match = re.findall(r'(\d+)\s*km.*?(\d+)\s*km/h.*?(\d+)\s*km/h', question)
            if match:
                dist, sp1, sp2 = map(int, match[0])
                time = dist / (sp1 + sp2)
                return round(time, 2)

        if "pool" in question and "minute" in question:
            match = re.findall(r'(\d+)\s*liters?.*?(\d+)\s*minutes?', question)
            if match:
                rate, time = map(int, match[0])
                return rate * time


    except:
        return None

def solve_equation_from_text(text):
    match = re.search(r"(\d*)x\s*\+\s*(\d+)\s*=\s*(\d+)", text)
    if match:
        a, b, c = map(int, match.groups())
        x = symbols('x')
        eq = Eq(a*x + b, c)
        solution = solve(eq, x)
        steps = f"Step 1: Start with equation {a}x + {b} = {c}\n"
        steps += f"Step 2: Subtract {b} from both sides: {a}x = {c - b}\n"
        steps += f"Step 3: Divide both sides by {a}: x = {(c - b)/a}\n"
        return f"The solution is x = {solution[0]}\n\n{steps}"
    return "Sorry, I couldn't parse the equation."
    
def override_answer(llm_text, correct_answer):
    #Eğer llm cevabı yanlış ise doğru cevap ile değiştirme
    return re.sub(r'(-?\d+\.?\d*)(?!.*\d)', str(correct_answer), llm_text)


print(" \n\n\n\n\n\n Welcome to Math Tutor Chat! Type 'exit' to quit.\n")

def get_llm_response(question: str):
    inputs = tokenizer(f"Question: {question} Answer:", return_tensors="pt")
    outputs = model.generate(**inputs, max_length=128)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def final_answer(question: str):
    llm_ans = get_llm_response(question)
    correct = solve_math_question(question)

    if correct is not None and str(correct) not in llm_ans:
        return f"{correct}\n\n"
    return f"{llm_ans}"

while True:
    question = input("You: ")
    if question.lower() == "exit":
        print("?? Goodbye!")
        break

    correct = solve_math_question(question)

    prompt = f"Question: {question} Answer:"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=128)
    outputs = model.generate(**inputs, max_length=128, num_beams=2, do_sample=False)
    final_answer(question)
