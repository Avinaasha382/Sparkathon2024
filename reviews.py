import requests 
import json
import os 
import dotenv

dotenv.load_dotenv()
API_KEY = os.getenv("SERPAPI_APIKEY")

web_data = requests.get(url=f"https://serpapi.com/search?engine=walmart_product_reviews&product_id=706770009&api_key={API_KEY}")
web_data.raise_for_status()
data = web_data.json()
# print(data)

reviews = []
try:
    top_positive_review = data["top_positive"]
except:
    print("Ok")
else:

    try:
        reviews.append(
            {
                "title":top_positive_review["title"],
                "text":top_positive_review["text"],
                "rating":top_positive_review["rating"]
            }
        )
    except:
        reviews.append(
            {
                "text":top_positive_review["text"],
                "rating":top_positive_review["rating"]
            }
        )

try:
    top_negative_review = data["top_negative"]
except:
    print("Ok")
else:
    try:
        reviews.append(
            {
                "title":top_negative_review["title"],
                "text":top_negative_review["text"],
                "rating":top_negative_review["rating"]
            }
        )
    except:
        reviews.append(
            {
                "text":top_negative_review["text"],
                "rating":top_negative_review["rating"]
            }
        )

#print(data["reviews"][0]["title"])


for review in data["reviews"]:
    #print(review)
    try:
        reviews.append(
        {
            "title":review["title"],
            "text":review["text"],
            "rating":review["rating"]
        }
        )
    except:
        try:
            reviews.append({
                "text":review["text"],
                "rating":review["rating"]
            })
        except:
            reviews.append({
                "rating":review["rating"]
            })
         
        
            
            
        






review_data = {
    "19": {
    "product_id":"706770009",
    "reviews":reviews
    }
}

with open("data.json",mode = "r") as fp:
    json_data = json.load(fp)
    json_data.update(review_data)

# print("***")

# print(json_data)

with open("data.json","w") as fp:
    json.dump(json_data,fp,indent=4)



