from data_loader import load_entire_data


def get_details(data,title):
    for item in data:
        if item.get("title")==title:
            return item
    return None


if __name__=="__main__": 
    sushi, parking = load_entire_data()
    details = get_details(sushi, "Sasou")
    print(details)