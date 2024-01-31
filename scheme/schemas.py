def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "nitrogen": todo["nitrogen"],
        "phosphorous": todo["phosphorous"],
        "potassium": todo["potassium"],
        "temperature": todo["temperature"],
        "ph": todo["ph"],
    }

def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]