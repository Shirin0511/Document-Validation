import re
from .common_validation import validate_dob, validate_name, extract_dob, extract_name
from typing import Dict


AADHAAR_REGEX = r"\b\d{4}\s?\d{4}\s?\d{4}\b"


def extract_aadharno(text: str):

    match= re.search(AADHAAR_REGEX, text)

    if match:
        return match.group().replace(" ","")
    else:
        return None
    

def extract_address(text: str):

    capture= False
    address=[]

    for line in text.splitlines():

        if "ADDRESS" in line.upper():
            capture= True
            continue

        if capture:
            if line.strip()==" ":
                break
            address.append(line.split())

    if address:
        return " ".join(address)    

    return None



def validate_aadharno(aadhar: str):

    return bool( aadhar and len(aadhar)==12 and aadhar.isdigit())


def validate_address(address: str):

    if not address:
        return False
    
    return len(address.strip())>10


def validate_aadhar_pipeline(ocr_text: str):

    name = extract_name
    dob = extract_dob
    aadhar = extract_aadharno
    address = extract_address

    valid_name = validate_name(name)
    valid_dob = validate_dob(dob)
    valid_aadhar = validate_aadharno(aadhar)
    valid_address = validate_address(address)

    if not aadhar:
        decision = "REJECT"
        reason = "Aadhaar number missing"

    elif not valid_aadhar:
        decision = "MANUAL_REVIEW"
        reason = "Invalid Aadhaar format"

    elif not valid_name:
        decision = "MANUAL_REVIEW"
        reason = "Name missing or unclear"

    elif not valid_dob:
        decision = "MANUAL_REVIEW"
        reason = "DOB invalid or missing"

    elif not valid_address:
        decision = "MANUAL_REVIEW"
        reason = "Address unclear"

    else:
        decision = "AUTO_PASS"
        reason = "Aadhaar validated successfully"
    

    return{
        "document_type" : "AADHAR",
        "aadhar_number" : aadhar,
        "aadhar_valid" : valid_aadhar,
        "name" : name,
        "name_valid" : valid_name,
        "dob" : dob,
        "dob_valid" : valid_dob,
        "address" : address,
        "address_valid" : valid_address,
        "decision" : decision,
        "reason" : reason

    } 



if __name__ == "__main__":

    ocr_text = """
    GOVERNMENT OF INDIA

    Name: RAHUL SHARMA
    DOB: 21/05/1998

    1234 5678 9123

    Address:
    22 MG Road
    Bangalore
    Karnataka
    """

    result= validate_aadhar_pipeline(ocr_text)

    for k,v in result.items():
        print(f"{k} : {v}")



    