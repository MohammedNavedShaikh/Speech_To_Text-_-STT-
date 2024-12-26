from app.services.logger_service import LoggerService
from app.prompt import ENGPROMPT, HIPROMPT
from app.model import LLMInitializer

logger = LoggerService.get_logger(__name__)


class RefinementService:
    @staticmethod
    def refine_text(result):
        try:
            if not isinstance(result["text"], str) or not result["text"].strip():
                logger.error("Invalid input: The 'text' value must be a non-empty string.")
                raise ValueError("The 'text' value must be a non-empty string.")
            if result["language"] not in ["en", "hi"]:
                logger.error("Unsupported language provided. Only 'en' and 'hi' are supported.")
                raise ValueError("Unsupported language. Supported languages are 'en' and 'hi'.")

            llm_initializer = LLMInitializer()
            llm = llm_initializer.initialize_llm()

            if result["language"] == "en":
                formatted_prompt = ENGPROMPT.format(input_text=result["text"])
            else:
                formatted_prompt = HIPROMPT.format(input_text=result["text"])

            logger.info(f"Refinement request received for language: {result['language']}")

            response = llm.invoke(formatted_prompt)

            if not response or not response.content.strip():
                logger.error("No valid response received from the language model.")
                raise RuntimeError("No response received from the language model.")

            logger.info("Text refinement completed successfully.")
            return response.content.strip()

        except TypeError as te:
            logger.error(f"TypeError: {te}")
            raise TypeError(f"Error: Invalid input type - {te}")

        except KeyError as ke:
            logger.error(f"KeyError: {ke}")
            raise KeyError(f"Error: Missing required input data - {ke}")

        except ValueError as ve:
            logger.error(f"ValueError: {ve}")
            raise ValueError(f"Error: Invalid input value - {ve}")

        except RuntimeError as re:
            logger.error(f"RuntimeError: {re}")
            raise RuntimeError(f"Error during language model invocation - {re}")

        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            raise Exception(f"Unexpected error occurred: {e}")

        finally:
            logger.info("Refinement process completed (success or failure).")
