import shopify
from termcolor import colored
shop_url = "https://tegshop-6399.myshopify.com/"
api_version = "2022-07"
private_app_password = "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"
session = shopify.Session(shop_url, api_version, private_app_password)
shopify.ShopifyResource.activate_session(session)
# ...
# make collections -> save ids, add products to the ids (collections)
# could possibly also make it so it makes html 

# now just need to scrape through the csvs ?? 
# no don't use csvs, just scrape it from the direct website


# custom_collection = shopify.CustomCollection()
# custom_collection.title = "Macbooks"
# custom_collection.published = True
# custom_collection.id
# custom_collection.save()
# print(colored(f"Custom collection '{custom_collection.title}' created with the id {custom_collection.id}", "green"))


product = shopify.Product()
product.title = "Shopify Logo T-Shirt"
product.body_html = "Test description"
product.vendor = "TES"
product.status = "Draft"
product.id
product.save()
variant = shopify.Variant({'price': 9.99, 'requires_shipping': True, "inventory_management": "shopify", "inventory_tracker": "shopify", "inventory_quantity": 999})
product.variants = [variant]

product.save()
# shopify.InventoryLevel.set(location_id = 71666729216, inventory_item_id=8076701729024, available=999)


# image1 = shopify.Image({'src':'https://t2.gstatic.com/licensed-image?q=tbn:ANd9GcQ9oKQNXxgr-lTH1Z0o9ZaZjy6iN8Ccj8hiQN_zf0qM3aSxRsDNaYlALUh8Z1rQsD-KTme5L8Y2TcxJmjk'})
# image2 = shopify.Image({'src':'https://m.media-amazon.com/images/M/MV5BMTE5MjM5MzM3M15BMl5BanBnXkFtZTYwOTEzOTY0._V1_UY264_CR5,0,178,264_AL_.jpg'})
# product.images = [image1, image2]
# product.save()

print(f"Product '{product.title}' created with the id of {product.id}")

# collect = shopify.Collect({ 'product_id': product.id, 'collection_id': custom_collection.id })
# collect.save()

shopify.ShopifyResource.clear_session()