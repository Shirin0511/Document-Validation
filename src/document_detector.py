import re

PAN_REGEX= r"[A-Z]{5}[0-9]{4}[A-Z]"
AADHAAR_REGEX = r"\b\d{4}\s?\d{4}\s?\d{4}\b"



def detect_doc_type(text : str):

    text=text.upper()

    if re.search(PAN_REGEX, text):
        return "PAN"
    
    if re.search(AADHAAR_REGEX, text):
        return "AADHAR"
    
    return "UNKNOWN"


if __name__=="__main__":

    pan_sample = """
    INCOME TAX DEPARTMENT
    Name: Rahul Sharma
    DOB: 12/08/1998
    PAN: ABCDE1234F
    """

    aadhaar_sample = """
    GOVERNMENT OF INDIA
    Name: Rahul Sharma
    DOB: 12/08/1998
    1234 5678 9123
    """

    print(detect_doc_type(pan_sample))

    print(detect_doc_type(aadhaar_sample))
