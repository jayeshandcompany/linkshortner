import requests
from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/' ,methods=['POST'])
def helloworld():
    data = request.get_json()
    url = str(data['queryResult']['queryText'])
    api_key = "17efd5015e4a69d287611d9121378a8fb1068"
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    print(api_url)
    # or
    # api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name=some_unique_name"
    # make the request
    data = requests.get(api_url).json()["url"]
    if data["status"] == 7:
        # OK, get shortened URL
        shortened_url = data["shortLink"]
        print("Shortened URL:", shortened_url)
    else:
        print("[!] Error Shortening URL:", data)

    response = {
        "fulfillmentText": "Shortened URL: {}".format(shortened_url)
    }
    return jsonify(response)
if __name__ == "__main__":
        app.run(debug=True)