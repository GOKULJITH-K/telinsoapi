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

def individual_serial2(cropData) -> dict:
    return {
        "id": str(cropData["_id"]),
        "crop_prediction": cropData["crop_prediction"],
        "success_percentage": cropData["success_percentage"],
        "suggested_crop": cropData["suggested_crop"],
        "username":cropData["username"],
        "__v": 0,
    }

def list_serial2(cropData) -> list:
    return [individual_serial2(data) for data in cropData]
