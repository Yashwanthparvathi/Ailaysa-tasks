from celery import shared_task
import os

@shared_task
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except Exception as e:
        # Handle any exceptions, such as file not found or permission errors
        print(f"An error occurred while processing the file: {str(e)}")
        return None