def validate_recieved_data(recieved_data):
    return {
        "name": recieved_data.get("name")
        if len(recieved_data.get("name")) < 100
        else recieved_data.get("name")[0:100],
        "time": recieved_data.get("time")
        if float(recieved_data.get("time")) < 600
        else 600,
        "coffee": recieved_data.get("coffee")
        if float(recieved_data.get("coffee")) < 100
        else 100,
        "water": recieved_data.get("water")
        if float(recieved_data.get("water")) < 1000
        else 1000,
        "description": recieved_data.get("description")
        if len(recieved_data.get("description")) < 500
        else recieved_data.get("description")[0:500],
    }
