from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

response_template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

structure_template = (
    "You are tasked with extracting specific information from the following text content: {extracted_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Format Structure:** Format your response in the following provided json format: {parse_structure}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)



def parse_with_groq(dom_chunks, parse_description, parse_structure, groq_api_key):
    model = ChatGroq(model='llama-3.1-8b-instant', temperature=0.5, api_key=groq_api_key)
    info_prompt = ChatPromptTemplate.from_template(response_template)
    format_prompt = ChatPromptTemplate.from_template(structure_template)

    chain1 = info_prompt | model
    chain2 = format_prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        extracted_content = chain1.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(extracted_content.content)
    
    response = chain2.invoke(
        {"extracted_content": "\n".join(parsed_results), "parse_structure": parse_structure}
    )

    return response.content