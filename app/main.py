import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from util import clean_text


def creation(llm, portfolio, clean_text):
    st.title("Cold Email Generator")
    url_ip = st.text_input("Enter a URL:", value = "https://ibmglobal.avature.net/en_US/careers/JobDetail?jobId=21839&source=WEB_Search_INDIA")
    submit_button = st.button("Submit")
    
    if submit_button:
        try:
            loader = WebBaseLoader([url_ip])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                emails = llm.write_mail(job, links)
                st.code(emails, language='markdown')
        except Exception as e:
            st.error(f"An Error Occured: {e}")

if __name__ == '__main__':
     chain = Chain()
     portfolio = Portfolio()
     st.set_page_config(layout='wide', page_title="Cold Email Generator", page_icon='📧')
     creation(chain,portfolio,clean_text)


