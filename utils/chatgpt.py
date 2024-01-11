import openai

class ChatGPT:
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_code(self, code):
        # Split the code into chunks (you may need to adjust the chunk size)
        chunk_size = 4000
        code_chunks = [code[i:i + chunk_size] for i in range(0, len(code), chunk_size)]

        # Initialize the analysis result
        analysis_result = ""

        # Request analysis for each code chunk

        for chunk in code_chunks:
            prompt = f"Develop unit tests for individual functions and classes within this code to improve modularity  and isolation for independent testing.: {chunk}" #(for test case development)

            # prompt = f"Analyze this code and provide me with suggestion to improve and optimise it: {chunk}"
            
            # prompt = f"Evaluate the complexity of this function/class. Can it be broken down into smaller, more manageable units to improve maintainability and reduce cognitive load?: {chunk}" #(for code improvement)
            
            # prompt = f"Analyze the time complexity of this code snippet. Are there alternative approaches or algorithms 
            # # that could achieve the same functionality with higher efficiency?: {chunk}" #(for code optimization)
        

            # prompt = f"Analyze this code for potential bugs or vulnerabilities based on common coding errors and 
            # security best practices: {chunk}" #(for bug fixes)


            completion_length = 200  # Adjust as needed

            response = openai.Completion.create(
                model="gpt-3.5-turbo-instruct",  # Replace with the correct model name
                prompt=prompt,
                max_tokens=completion_length,
            )

            # Concatenate the generated text from each response
            analysis_result += response.choices[0].text.strip()

        return analysis_result
