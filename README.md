# Cold Email Generator
Cold Email Generator is a tool built with Ollama, LangChain, and Streamlit that automates personalized outreach for service-based businesses.

This tool allows users to input the URL of a target company's careers page, extract current job listings, and generate tailored cold emails that align with the specific hiring needs of the company. It also integrates with a vector database to attach relevant portfolio links, matching the job description with previous work samples to boost credibility and relevance.

I have used Distilled Deepseek-R1(8B) model. This can be replaced with any ollama model.

## Key Features
1. Job Extraction: Automatically scrapes job listings from a company's careers page.
2. AI-Powered Email Generation: Uses LLMs via Ollama and LangChain to craft personalized cold emails.
3. Portfolio Matching: Pulls relevant portfolio items from a vector database based on job description keywords.
4. Streamlit Frontend: User-friendly interface for inputting URLs and reviewing/generated emails.


### Imagine a scenario:

Discover Dollar needs a Data Scientist Engineer (Trained Fresher) and is spending time and resources in the hiring process, on boarding, training etc 
AtlasLabs is Software Development company can provide a dedicated data scientist engineer to Discover Dollar. So, the business development executive (Yash) from AtlasLabs is going to reach out to Discover Dollar via a cold email.


<img src="https://github.com/YRKaflay/ColdEmailGen/blob/main/img/Screenshot 2025-04-23 191916.png" width="900" title="Screenshot" alt="Preview of the Tool"/>

## Architecture
<img src="https://github.com/YRKaflay/ColdEmailGen/blob/main/img/Career Page.png" width="900" title="Architecture" alt="Architecture Diagram"/>


## Setup

Follow the steps below to get the project up and running locally:
1. Make sure you have Ollama installed on your machine. You can install it by following the instructions on their official website. Once installed, download the LLM model of your choice. For example:
`ollama run deepseek-r1`

2. Clone the repository to your device

3. Install Python Dependencies using:
`pip install -r requirements.txt`

4. Run the Streamlit App using:
`streamlit run app/main.py`