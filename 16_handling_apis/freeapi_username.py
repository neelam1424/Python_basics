import requests

def fectch_random_freeapi():
    url=""
    response=requests.get(url)
    response.json()

    if data["sucess"] and "data" in data
        user_data=data["data"]
        username=user_data["login"]["username"]
        country=user_data["location"]["country"]
        return username,country
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        username,country=fectch_random_freeapi()
        print("Username:{username} \n country:{country}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()