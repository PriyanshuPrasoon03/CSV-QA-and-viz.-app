import pandas as pd
import gradio as gr
import matplotlib.pyplot as plt
import ollama
from pydantic import BaseModel
from pydantic_ai import Agent

# Define a structured response model using Pydantic
class QueryModel(BaseModel):
    question: str
    answer: str

# Define a Pydantic AI Agent
class CSVAgent(Agent):
    def __init__(self, df):
        super().__init__()
        self.df = df

    def ask(self, question: str) -> QueryModel:
        context = self.df.head().to_string()
        prompt = f"Given the following dataset:\n{context}\nAnswer this question: {question}"

        response = ollama.chat(model="llama3:8b", messages=[{"role": "user", "content": prompt}])
        answer = response["message"]["content"]

        return QueryModel(question=question, answer=answer)

# CSV validation and loading
def validate_csv(file):
    try:
        df = pd.read_csv(file.name)  # Use file.name
        return df, "CSV file uploaded successfully!"
    except Exception as e:
        return None, f"Error: {str(e)}"

# Function to process the query with the Pydantic AI agent
def answer_question(df, question):
    try:
        agent = CSVAgent(df)
        response = agent.ask(question)
        return response.answer
    except Exception as e:
        return f"Error in LLM processing: {e}"

# Graph plotting function
def plot_graph(df, x_column, y_column, plot_type="line"):
    try:
        plt.figure()
        if plot_type == "line":
            plt.plot(df[x_column], df[y_column])
        elif plot_type == "bar":
            plt.bar(df[x_column], df[y_column])
        elif plot_type == "scatter":
            plt.scatter(df[x_column], df[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{plot_type.capitalize()} Plot: {x_column} vs {y_column}")
        plt.tight_layout()
        return plt.gcf()
    except Exception as e:
        return f"Error generating plot: {str(e)}"

# Main processing function
def process_csv(file, question, x_column, y_column, plot_type):
    df, message = validate_csv(file)
    if df is None:
        return message, None

    # Answer the question
    answer = answer_question(df, question)

    # Generate the plot
    plot = plot_graph(df, x_column, y_column, plot_type)

    # Return results
    return answer, plot if isinstance(plot, plt.Figure) else None

# Gradio Interface
with gr.Blocks() as app:
    gr.Markdown("# CSV Question Answering and Visualization with Pydantic AI")

    with gr.Row():
        file_input = gr.File(label="Upload CSV File")
        question_input = gr.Textbox(label="Ask a Question")

    with gr.Row():
        x_column = gr.Dropdown(label="X-Axis Column", choices=[])
        y_column = gr.Dropdown(label="Y-Axis Column", choices=[])
        plot_type = gr.Radio(choices=["line", "bar", "scatter"], label="Plot Type")

    with gr.Row():
        answer_output = gr.Textbox(label="Answer")
        plot_output = gr.Plot(label="Graph")

    submit_button = gr.Button("Submit")

    # Update column dropdowns based on uploaded CSV
    def update_columns(file):
        df, _ = validate_csv(file)
        if df is not None:
            return gr.Dropdown(choices=df.columns.tolist()), gr.Dropdown(choices=df.columns.tolist())
        return gr.Dropdown(choices=[]), gr.Dropdown(choices=[])

    file_input.change(update_columns, inputs=file_input, outputs=[x_column, y_column])

    # Process inputs on button click
    submit_button.click(
        process_csv,
        inputs=[file_input, question_input, x_column, y_column, plot_type],
        outputs=[answer_output, plot_output]
    )

# Launch the app
app.launch()
