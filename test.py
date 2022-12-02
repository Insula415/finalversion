import requests
import json
# get products -> scrape through csvs -> upload all products to shopify -> collect customer data -> send email

# OKAY SO: make products have no images, then individually upload the images using the product id

# post request: create product
def create_product():

    # balls = """
    # {
    #     "src": "",
    #     "alt": ""
    # }    
    # """
    # test = json.loads(balls)
    # json_string = f"""
    # {
    #     "images": [
    #         {test}
    #     ]
    # }
    # """
    
    # data = json.loads(json_string)
    # # data = ["images:"[{'a':'balls', 'b':'bs'}]]
    # with open('test.json', 'w') as f:
    #     json.dump(data, f, indent=4)
    # tags = ["one","two"]
    # images = ['"src":"image.jpg"']
    with open('payload.json', 'r') as f:
        payload = json.load(f)

    # payload["product"]["tags"] = tags
    # images.replace('src', ' ')
    # images = [item.replace("'", "") for item in images]
    # payload["product"]["images"]
    # payload[["product"]["vendor"]] = 'Apple'
    print(payload["product"]["images"])
    print([i["images"] for i in payload["product"]])
    with open('payload.json', 'w') as f:
        json.dump(payload, f, indent=4)

    quit()
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    r = requests.post("https://2c45a4287c745e241ee4b9590b30fd3f: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@tegshop-6399.myshopify.com/admin/products.json", json=payload,  headers=headers)

    print(r.json())

# get request: retrieve all products
def get_all_products():

    r = requests.get("https://2c45a4287c745e241ee4b9590b30fd3f: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@tegshop-6399.myshopify.com/admin/products.json")

    print(r.json())


# get request: retrieve product by id
def get_specific_product():

    r = requests.get("https://2c45a4287c745e241ee4b9590b30fd3f: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@tegshop-6399.myshopify.com/admin/products/934425690169.json")

    print(r.json())


# update request: update product
def update_product():

    payload = {
      "product": {
        "product_id":8055147954432,
        "title": "updated title",
      }
    }

    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    r = requests.post("https://2c45a4287c745e241ee4b9590b30fd3f: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@tegshop-6399.myshopify.com/admin/products.json", json=payload,  headers=headers)


    print(r.json())


# delete request: delete product
def delete_product():

    r = requests.delete("https://2c45a4287c745e241ee4b9590b30fd3f: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@tegshop-6399.myshopify.com/admin/products/934425690169.json")

    print(r.status_code)



if __name__ == '__main__':

    # create_product()
    # get_all_products()
    # get_specific_product()
    update_product()
    # delete_product()