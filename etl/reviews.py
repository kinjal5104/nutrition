# import os
# import requests
# from amazon_paapi import AmazonApi, AmazonApiException

# # --- AMAZON SETUP ---
# def search_amazon_products(keyword, max_results=1):
#     try:
#         amazon_api = AmazonApi(
#             os.getenv("AMAZON_ACCESS_KEY"),
#             os.getenv("AMAZON_SECRET_KEY"),
#             os.getenv("AMAZON_ASSOC_TAG"),
#             "IN"
#         )
#         result = amazon_api.search_items(keywords=keyword, item_count=max_results)
#         urls = []
#         for item in result.items:
#             urls.append({
#                 "url": item.detail_page_url,
#                 "title": item.item_info.title.display_value,
#                 "rating": item.customer_reviews.star_rating if item.customer_reviews else "N/A",
#                 "review": item.editorial_reviews[0].content if item.editorial_reviews else "No editorial review"
#             })
#         return urls
#     except AmazonApiException as e:
#         print("Amazon PA API error:", e)
#         return []

# # --- FLIPKART SETUP ---
# def search_flipkart_products(keyword, max_results=1):
#     affiliate_id = os.getenv("FLIPKART_AFFILIATE_ID")
#     token = os.getenv("FLIPKART_TOKEN")
#     headers = {
#         "Fk-Affiliate-Id": affiliate_id,
#         "Fk-Affiliate-Token": token
#     }
#     url = f"https://affiliate-api.flipkart.net/affiliate/search/json?query={keyword}&resultCount={max_results}"
#     resp = requests.get(url, headers=headers, timeout=30)
#     if resp.status_code == 200:
#         data = resp.json()
#         results = []
#         for product in data.get("products", []):
#             info = product.get("productBaseInfoV1", {})
#             results.append({
#                 "url": info.get("productUrl"),
#                 "title": info.get("title"),
#                 "rating": info.get("flipkartSpecialOffers", "N/A"),
#                 "review": info.get("productDescription", "No description available")
#             })
#         return results
#     else:
#         print("Flipkart API error:", resp.status_code)
#         return []

# # --- COMBINED WRAPPER FUNCTION ---
# def get_reviews_by_keyword(keyword):
#     all_reviews = []

#     # AMAZON
#     for product in search_amazon_products(keyword):
#         all_reviews.append({
#             "source": "Amazon",
#             "title": product["title"],
#             "rating": product["rating"],
#             "review": product["review"],
#             "url": product["url"]
#         })

#     # FLIPKART
#     for product in search_flipkart_products(keyword):
#         all_reviews.append({
#             "source": "Flipkart",
#             "title": product["title"],
#             "rating": product["rating"],
#             "review": product["review"],
#             "url": product["url"]
#         })

#     return all_reviews
