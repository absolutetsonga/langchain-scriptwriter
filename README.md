# Langhchain Youtube Video Scriptwriter

This project is a YouTube title and script generator using the GPT-3.5 language model. It allows you to generate YouTube video titles and scripts based on a given topic by leveraging the power of OpenAI's GPT-3.5 model.

## Prerequisites

Before running the project, make sure you have the following dependencies installed:

- Python (version 3.6 or higher)
- `streamlit` library
- `dotenv` library
- OpenAI API key

You can install the required Python packages by running the following command:

```
pip install streamlit python-dotenv
```

## Getting Started

1. Clone the project repository:

```
git clone <repository-url>
```

2. Change into the project directory:

```
cd <project-directory>
```

3. Create a virtual environment (optional but recommended):

```
python3 -m venv venv
```

4. Activate the virtual environment:

- On macOS and Linux:

```
source venv/bin/activate
```

- On Windows:

```
venv\Scripts\activate
```

5. Install the project dependencies:

```
pip install -r requirements.txt
```

6. Set up OpenAI API key:

- Create a new file named `.env` in the project directory.
- Open the `.env` file and add the following line, replacing `<YOUR_API_KEY>` with your actual OpenAI API key:

```
OPEN_API_KEY=<YOUR_API_KEY>
```

7. Run the application:

```
streamlit run main.py
```

8. Access the application in your browser:

```
http://localhost:8501/
```

## Usage

1. Once the application is running, you will see a text input field labeled "Plug in your Youtube Topic here".
2. Enter a topic for your YouTube video in the text input field.
3. The application will generate a YouTube video title and script based on the provided topic.
4. The generated title and script will be displayed on the web page.
5. You can view the conversation history for the title and script generation by expanding the "Message History" and "Script History" sections, respectively.
6. Additionally, you can view the Wikipedia research related to the topic by expanding the "Wikipedia Research" section.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This project was developed using the following libraries:

- `os`
- `dotenv`
- `streamlit`
- `langchain.llms`
- `langchain.prompts`
- `langchain.chains`
- `langchain.memory`
- `langchain.utilities`
