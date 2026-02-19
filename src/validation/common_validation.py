import re
from datetime import datetime

DOB_REGEX = r"\b\d{2}/\d{2}/\d{4}\b"


# Extraction Methods

def extract_name(ocr_text : str):

    for line in ocr_text.splitlines():
        if "NAME" in line.upper():
            parts= line.split(":")
            if len(parts) > 1:
                return parts[1].strip()
    return None        

def extract_dob(ocr_text : str):

    match = re.search(DOB_REGEX, ocr_text)
    return match.group() if match else None



#Validation Methods

def validate_name(name: str):

    if not name:
        return False
    
    return len(name.strip())>=3


def validate_dob(dob : str):

    try:
        parsed_dob = datetime.strptime(dob,"%d/%m/%Y")
        return parsed_dob < datetime.now()
    
    except:
        return False