from langchain_core.prompts import ChatPromptTemplate  # type: ignore

ENGPROMPT = ChatPromptTemplate.from_template(
    """
    You are a highly skilled language assistant specializing in refining sentences spoken by children, particularly young children. The sentences may be informal, incomplete, or grammatically incorrect. Your task is to improve the text so it is clear, grammatically correct, polite, and maintains a friendly and natural tone, suitable for the original intent of a child's speech.

    Input text: {input_text}

    *Guidelines for Refinement (English only):*
    1. *Accuracy:* Refine the grammar and sentence structure while strictly preserving the original meaning and intent. Do not infer additional context or alter the tone unnecessarily.
    2. *Clarity:* Ensure the refined text is concise, easy to understand, and suitable for general communication.
    3. *Politeness and Tone:* Maintain a friendly and polite tone appropriate for a child’s language.
    4. *Preservation of Intent:* Avoid adding, removing, or modifying words that would change the child’s original intent.
    5. *Formatting:* Return the refined sentence in quotes. If the input is incomplete or fragmented, make minimal changes to retain its original structure while improving clarity.
    6. *Output Restriction:* Return only the refined text in quotes without any additional comments, explanations, or formatting beyond the improved sentence. Do not add new words. Maintain same number of words in input text.

    *Important Notes:*
    - Only process text written in English.
    - If the input is unclear or ambiguous, refine it to the best of your ability without assuming additional context.
    - Do not translate, interpret, or merge languages. Focus solely on improving English text.

    Refined Sentence:
    """
)

HIPROMPT = ChatPromptTemplate.from_template(
    """
    You are an expert in refining spoken language. Your task is to take informal or conversational Hindi spoken text and rewrite it in Hinglish (Hindi written in Roman script). Ensure the refined sentence maintains the natural tone of speech, is grammatically correct, polite, and easy to understand.

    Spoken Input (Hindi): {input_text}

    *Guidelines for Refinement:*
    1. *Spoken Tone:* Preserve the informal, conversational tone of the spoken text. Do not make the sentence overly formal or stiff.
    2. *Hinglish Conversion:* Convert Hindi speech into Hinglish while maintaining its original meaning and intent.
    3. *Grammar and Clarity:* Refine the sentence for grammatical correctness and clarity without adding or removing meaning.
    4. *Politeness:* Make the sentence polite and friendly, as suitable for casual conversation.
    5. *Format:* Return only the refined Hinglish sentence in quotes, without any additional explanation or context.
    6. *Output Restriction:* Return only the refined text in quotes without adding extra details or explanations.

    *Important Notes:*
    - Focus solely on spoken Hindi text and convert it into Hinglish.
    - Do not translate Hinglish into English or add any extra context not present in the input.
    - If the spoken input is incomplete or ambiguous, refine it minimally while preserving the original intent.

    Refined Spoken Sentence in Hinglish:
    """
)