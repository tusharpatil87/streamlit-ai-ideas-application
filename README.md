# Streamlit AI Ideas App

This project is a Streamlit application that suggests topics for generative AI applications based on user-selected subject areas. 

## Project Structure

```
streamlit-ai-ideas-app
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   └── utils
│       └── topic_suggester.py # Contains the topic suggestion logic
├── requirements.txt          # Lists the dependencies required for the project
└── README.md                 # Documentation for the project
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-ai-ideas-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, execute the following command in your terminal:

```
streamlit run src/app.py
```

Once the application is running, open your web browser and go to `http://localhost:8501` to access the app.

## Usage

1. Select a subject area from the dropdown menu.
2. Click the "Suggest Topics" button.
3. View the suggested topics for generative AI applications related to your selected subject area.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.