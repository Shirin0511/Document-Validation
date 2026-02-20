import re
from datetime import datetime
from typing import Dict
from .common_validation import extract_dob, extract_name, validate_dob, validate_name

PAN_REGEX= r"[A-Z]{5}[0-9]{4}[A-Z]"

def extract_pan(ocr_text : str):

    for line in ocr_text.splitlines():
        if "PAN" in line.upper():
            parts= line.split(":")
            if len(parts)>1:
                return parts[1].strip().upper()
    return None



def validate_pan(pan: str):
    if not pan:
        return None
    return bool(re.fullmatch(PAN_REGEX, pan))



def validate_pan_pipeline(ocr_text: str) :

    pan = extract_pan(ocr_text)
    pan_valid = validate_pan(pan)


    name = extract_name(ocr_text)
    name_valid = validate_name(name)

    dob = extract_dob(ocr_text)
    dob_valid = validate_dob(dob)

    if not pan:
        decision = "REJECT"
        reason = "PAN Missing"

    elif not pan_valid:
        decision = "Manual Review"
        reason = "Invalid PAN Format"

    elif not name_valid:
        decision = "Manual Review"
        reason = "Name is invalid or missing" 

    elif not dob_valid:
        decision = "Manual Review"
        reason = "DOB is invalid or missing" 

    else:
        decision = "AUTO PASS"
        reason = "PAN Validation is successful"  

    return {
        "document_type" : "PAN",
        "pan_number" : pan,
        "pan_valid" : pan_valid,
        "name" : name,
        "name_valid" : name_valid,
        "dob" : dob,
        "dob_valid" : dob_valid,
        "decision" : decision,
        "reason" : reason
    }           



    

    


if __name__=="__main__":

    sample_input= """
    INCOME TAX DEPARTMENT
    GOVERNMENT OF INDIA

    Name: TAMMY BELTRAN
    DOB: 18/11/1969
    PAN: GHDOA8008B

    """

    result= validate_pan_pipeline(sample_input)

    for k, v in result.items():
        print(f"{k} : {v}")


    
