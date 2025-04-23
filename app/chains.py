import os
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

class Chain:
    def __init__(self):
        self.llm = ChatOllama(model="deepseek-r1:8b",temperature=0)

    def extract_jobs(self, cleaned_text):
        prompt_ext = PromptTemplate.from_template(
                        """
                        ### SCRAPED TEXT FROM WEBSITE:
                        {page_data}
                        ### INSTRUCTION:
                        The scraped text is from the career's page of a website.
                        Your job is to extract the job postings and return them in JSON format containing
                        the following keys: 'role', 'experience','skills' and 'description'.
                        Only return the valid JSON.
                        Skip the think part.
                        ### VALID JSON (NO PREAMBLE):
                        """
                    )
        chain_ext = prompt_ext | self.llm
        res = chain_ext.invoke(input={"page_data": cleaned_text})
        main = res.content.split('json')
        main = main[1]
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(main)
        except OutputParserException:
            raise OutputParserException("Content too big. Unable to parse jobs.")
        
        return res if isinstance(res, list) else [res]
    
    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
                        """
                        ### JOB DESCRIPTION:
                        {job_description}

                        ### INSTRUCTION:
                        You are Yash, a business development executive at AtlasLabs. AtlasLabs is an AI research company dedicated to
                        facilitating new research about seamless integration of business processes through automated tools.
                        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability,
                        process optimization, cost reduction, and heightened overall efficiency.
                        Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtlasLabs
                        in fulfilling their needs.
                        Also add the most relevant ones from the following links to showcase AtlasLabs' portfolio : {link_list}
                        Remember, you are Yash, BDE at AtlasLabs.
                        Do not provide a preamble.
                        ### EMAIL (NO PREAMBLE):
                        """
                    )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": str(links)})
        main = res.content.split('</think>')
        main = main[1]
        return main

