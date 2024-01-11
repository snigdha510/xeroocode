class ReportGenerator:
    def generate_report(self, analysis_results):
        print("Code Analysis Report:")
        print("=" * 30)

        for result in analysis_results:
            print(f"\nFile: {result['file']}")
            print("Analysis:")
            self.print_analysis_result(result['analysis'])
            print("-" * 30)

        print("\nReport Generation Complete.")

    def print_analysis_result(self, analysis_result):
        # Check if the analysis result is a string or a dictionary
        if isinstance(analysis_result, str):
            print(analysis_result.strip())
        else:
            # Extract and print the generated text from the OpenAI response
            generated_text = analysis_result.get('choices', [{}])[0].get('text', '')
            print(generated_text.strip())
