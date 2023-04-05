import requests
from bs4 import BeautifulSoup

def get_cos(ancestor, selector=None, attribute=None, return_list=False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].text.strip()
        return ancestor.select_one(selector).text.strip()

    except AttributeError:
        return None


# product_code = input("Podaj kod produktu: ")
product_code = "103406739"
# url = "https://www.ceneo.pl/" + product_code + "#tab=reviews"
# url = "https://www.ceneo.pl/{}#tab=reviews".format(product_code)
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
page_dom = BeautifulSoup(response.text, "html.parser")
opinions = page_dom.select("div.js_product-review")
all_opinions = []

for opinion in opinions:
    print(opinion["data-entry-id"])
    single_option = {
        "opinion_id": opinion["data-entry-id"],
        "author": opinion.select_one("span.user-post__author-name").text.strip(),
        "recomendation": opinion.select_one("span.user-post__author-recomendation").text.strip(),
        "score": opinion.select_one("span.user-post__score-count").text.strip(),
        "purhased": opinion.select_one("div.review-pz").text.strip(),
        "published_at": opinion.select_one("span.user-post__published > time:nth-child(1)")['datetime'].strip(),
        "purhased_at": opinion.select_one("span.user-post__published > time:nth-child(2)")['datetime'].strip(),
        "thumbs_up": opinion.select_one("button.vote-yes > span").text.strip(),
        "thumbs_down": opinion.select_one("button.vote-no > span").text.strip(),
        'content': opinion.select_one('div.user-post__text').text.strip(),
        'pros' : [pros.text.strip() for pros in opinion.select("div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item")],
        'cons' : [cons.text.strip() for cons in opinion.select("div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item")],
        'new_cons' : get_cos(opinion, None, "data-entry-id")
    }
    all_opinions.append(single_option)

    print(all_opinions) 
    # print(single_option['recommendation'])

# print(all_opinions)