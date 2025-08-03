import gradio as gr
import wolframalpha

# WolframAlpha client setup
app_id = "K39W4234KH"
client = wolframalpha.Client(app_id)

# List of keywords that indicate a likely math question
MATH_KEYWORDS = ["calculate", "solve", "simplify", "integrate", "derive", "equation", "probability", "function", "plot", "+", "-", "*", "/", "^", "=", "area", "volume", "perimeter", "square", "circle", "triangle", "limit", "mean", "median", "mode"]

def is_math_question(question: str) -> bool:
    question_lower = question.lower()
    return any(keyword in question_lower for keyword in MATH_KEYWORDS)


def ask_wolfram(query: str) -> str:
    try:
        res = client.query(query, timeout=20)  # 20 seconds timeout

        # Check if WolframAlpha says it succeeded
        if res['@success'] == 'false':
            return "I couldn't solve this question. Please try rephrasing it."

        # Iterate through pods and subpods to find plaintext answers
        for pod in res.pods:
            if pod.title and 'result' in pod.title.lower():
                for sub in pod.subpods:
                    if sub.plaintext:
                        return sub.plaintext

        # If no "Result" pod, fallback to first pod with plaintext
        for pod in res.pods:
            for sub in pod.subpods:
                if sub.plaintext:
                    return sub.plaintext

        return "Sorry, I couldn't find a result."

    except Exception as e:
        import traceback
        traceback.print_exc()
        return "⚠️ An error occurred while contacting WolframAlpha."


import requests

def ask_wolfram_steps(query):
    url = "https://api.wolframalpha.com/v2/query"
    params = {
        "input": query,
        "appid": app_id,
        "output": "json",
        "podstate": "Step-by-step solution"
    }

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        if not data.get("queryresult") or not data["queryresult"].get("success"):
            return "❌ WolframAlpha couldn't understand the question."

        pods = data["queryresult"].get("pods", [])
        if not pods:
            return "❌ No information available for this query."

        # Step-by-step or Solution pods
        step_pods = [
            pod for pod in pods
            if 'step' in pod['title'].lower() or 'solution' in pod['title'].lower()
        ]

        if step_pods:
            texts = []
            for pod in step_pods:
                for sub in pod.get('subpods', []):
                    if sub.get('plaintext'):
                        texts.append(sub['plaintext'])
            return "\n\n".join(texts) or "✅ Found a pod, but it had no readable steps."

        # Fallback to Result pod
        for pod in pods:
            if 'result' in pod['title'].lower():
                for sub in pod.get('subpods', []):
                    if sub.get('plaintext'):
                        return sub['plaintext']

        return "⚠️ No step-by-step or result found."

    except Exception as e:
        return f"⚠️ Error contacting WolframAlpha: {str(e)}"


def final_answer(user_input: str) -> str:

    if not is_math_question(user_input):
        return "Please ask math-related questions only, such as solving equations, geometry, arithmetic, etc."
    
    answer = ask_wolfram_steps(user_input)
    return f"**Answer**:\n{answer}"



