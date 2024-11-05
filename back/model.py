# Paths to the files
model_file_path = r'C:\FluxUI\back\model.txt'
input_script_path = r'C:\FluxUI\back\temp_api.py'
output_script_path = r'C:\FluxUI\back\API_ollama.py'

# Read the new model text from model.txt
with open(model_file_path, 'r', encoding='utf-8') as model_file:
    new_model = model_file.read().strip()

# Read the content of the input script
with open(input_script_path, 'r', encoding='utf-8') as input_script:
    script_content = input_script.read()

# Replace 'gemma2:9b' with the new model text
updated_script_content = script_content.replace('gemma2:9b', new_model)

# Write the updated script content to a new file (API_ollama.py)
with open(output_script_path, 'w', encoding='utf-8') as output_script:
    output_script.write(updated_script_content)

print(f"Model updated.")
