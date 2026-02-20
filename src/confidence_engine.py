FIELD_WEIGHTS = {
    "AADHAR": {
        "aadhar_valid": 0.40,
        "name_valid": 0.25,
        "dob_valid": 0.20,
        "address_valid": 0.15,
    },
    "PAN": {
        "pan_valid": 0.50,
        "name_valid": 0.30,
        "dob_valid": 0.20,
    }
}

def calculate_confidence(result: dict):

    doc_type = result.get("document_type")

    if doc_type == "UNKNOWN":
        result['confidence_score'] = 0.0
        return result
    

    weights= FIELD_WEIGHTS.get(doc_type)

    score = sum(weight for field, weight in weights.items() if result.get(field) )

    if score >= 0.90:
        decision = "AUTO_PASS"

    elif score >= 0.60:
        decision = "MANUAL_REVIEW"

    else:
        decision = "REJECT"

    result['final_decision'] = decision
    result['confidence_score'] = score 

    return result
        