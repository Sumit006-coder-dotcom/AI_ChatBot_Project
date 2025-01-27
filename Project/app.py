from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

@app.route("/", methods=["GET", "POST"])
def home():
    response_text = None
    if request.method == "POST":
        user_input = request.form["user_input"]

        # OpenAI API call
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # You can use 'gpt-3.5-turbo' if supported
                prompt=f"User: {user_input}\nAI:",
                max_tokens=150,
                temperature=0.7
            )
            response_text = response.choices[0].text.strip()
        except Exception as e:
            response_text = f"Error: {e}"

    return render_template("home.html", response_text=response_text)

if __name__ == "__main__":
    app.run(debug=True)
