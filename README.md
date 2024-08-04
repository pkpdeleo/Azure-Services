# Speech-to-Text Transcription and Profanity Filtering

This project demonstrates how to use Azure Speech Services for transcribing speech to text in both Tamil and English.
Additionally, it includes a Python script for filtering profanities from the transcribed text.

# Prerequisites

Before running the code, ensure you have the following:

- Python 3.6 or later
- Azure subscription and Speech Services API key
- Required Python libraries (listed below)

# Setup

- Clone the Repository
- Install Dependencies
- Create a virtual environment and install the required libraries
- Set Environment Variables
- Set the following environment variables with your Azure Speech Services credentials:
- AZURE_SPEECH_API_KEY,
- AZURE_SPEECH_REGION

# Code Details

1. tamil.py, english.py: Contains code for interacting with Azure Speech Services to transcribe speech to text.
2. profanity.py: Contains code for filtering profanities from the transcribed text.
3. recognized_speech.txt: Contains the transcribed and filtered speech.

# Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request with your changes. Make sure to follow the project's coding style and guidelines.

# License 📃

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.

## Acknowledgements

- [Azure Speech Services Documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)

- [Profanity Filtering Techniques](https://pypi.org/project/profanity-filter)
