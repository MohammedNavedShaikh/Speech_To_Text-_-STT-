# app\services\refinement_service.py
from logger import get_logger
from app.prompt import prompt

logger = get_logger(__name__)

def refine_text(text, llm):
    try:
        if not isinstance(text, str) or not text.strip():
            logger.warning("Invalid input: The input text must be a non-empty string.")
            raise ValueError("Input text must be a non-empty string.")
        
        formatted_prompt = prompt.format(input_text=text)
        response = llm.invoke(formatted_prompt)

        if not response or not response.content.strip():
            logger.error("No valid response received from the language model.")
            raise RuntimeError("No response received from the language model.")

        logger.info("Text refinement successful.")
        return response.content.strip()
    
    except ValueError as ve:
        logger.error(f"ValueError: {ve}")
        raise ValueError(f"Error: Invalid input - {ve}")
    
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        raise Exception(f"Unexpected error occurred: {e}")
