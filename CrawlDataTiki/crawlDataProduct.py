import pandas as pd
import requests
import time
import random
from tqdm import tqdm


cookies = {
    '_trackity': 'b2ee50bb-3965-dd80-67b4-3f6b84ae3737', 'delivery_zone': 'Vk4wMzkwMDYwMDE=', 'tiki_client_id': '300752126.1691425328', '_gcl_au': '1.1.1423128732.1691425335', '__iid': '749', '__su': '0', '_hjSessionUser_522327': 'eyJpZCI6IjZmYzRjZjE5LTRmNDktNTQxZC1iNzE0LWU4ODc4M2JmODM0NyIsImNyZWF0ZWQiOjE2OTE0MjUzMzUzNzMsImV4aXN0aW5nIjp0cnVlfQ==', 'G_ENABLED_IDPS': 'google', 'TIKI_ACCESS_TOKEN': 'eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI3ODQzMTUwIiwiaWF0IjoxNjkyODYwNTM1LCJleHAiOjE2OTI5NDY5MzUsImlzcyI6Imh0dHBzOi8vdGlraS52biIsImN1c3RvbWVyX2lkIjoiNzg0MzE1MCIsImVtYWlsIjoicXVvY2NodXl5NDI4QGdtYWlsLmNvbSIsImNsaWVudF9pZCI6InRpa2ktc3NvIiwibmFtZSI6Ijc4NDMxNTAiLCJzY29wZSI6InNzbyJ9.cXop7AQydNi1CJXlCbXO82p_XJb1w7CgpFxZFiCP34bV3O8zVhVpF3XZTwIEjO36Z_LvB3gUVSUMYE4XuNRPrcCOQtTdVpuUf1UKf6FGK1hpmU4_kP7jCxKN8B6-4T0Z1Sn0wGdWe1T2Q9vY7LFro3FbGM62F-N0xgxjC1IcB1bkil-NNxKfWAx0SP4QmvAoe2wdxznTZcyjxl8FDD2_xz9CePT0I5EXcAcZcWX8r4BDbGmwnx89vVi8R43_FG8FJ9gCpwk3ZKwjSVm8BDh3cl3woEVSUgaFf1RqCGpIve6IVXDqd-saz5YOtP3OVXLwCU_qOIKvuFXp_UpgVSDXXmccOxzhJ1Q0_cRPyPnKWgENaeUMkm0uPMry2QGAnsHw92HRQ8pMMo74qRDU98mCiUDRaFY0j_ZUPHO-Ead0f_m1f7J0cF2LGjU4zHR8wu6_03PHWoGhx2EsKpH38Pq0raItYkV1DdAjMUDxdWe7V20_ZWu1ekC7MA82y6Fb1gjEaqrH51i7FoJG3Dj8VxxCKo2vw7zV4Ys475ADiOZ6BkOFRgvqNNwSKN-nGBD4H0ZwZN8yZnYiEWNFIZOmuLdBJkV-jodHmX71r0SvPm5NdrqiHLwwlfdpvP4DXDmS22ol8KJPwcv-zEQa3AMFFELhGmaNKyCB_K-Gg28ThFx1rLQ',
    'TIKI_USER': '6ya%2FQq9rvDjeibm9k%2BugMP%2B8eFnwhNwXIkCPJ3b0liKRuwCQVUyGVx8eOsWYqUIYpFasXqoJ7fg%3D', 'bnpl_whitelist_info': '{%22content%22:%22Mua%20tr%C6%B0%E1%BB%9Bc%20tr%E1%BA%A3%20sau%22%2C%22is_enabled%22:true%2C%22icon%22:%22https://salt.tikicdn.com/ts/tmp/95/15/2d/4b3d64b220f55f42885c86ac439d6d62.png%22%2C%22deep_link%22:%22https://tiki.vn/mua-truoc-tra-sau/dang-ky?src=account_page%22}', '_gid': 'GA1.2.1796508843.1692860538', 'TOKENS': '{%22access_token%22:%22yBiwS9hoNQUL2E8rDz6nGHMqCkdAFsVT%22%2C%22expires_in%22:157680000%2C%22expires_at%22:1850541747826%2C%22guest_token%22:%22yBiwS9hoNQUL2E8rDz6nGHMqCkdAFsVT%22}', '_tuid': '7843150', '_gat': '1', '_hjIncludedInSessionSample_522327': '0', '_hjSession_522327': 'eyJpZCI6Ijc3MDMyYTljLTE0OGUtNDdiNy05ZmNhLTM2ZWVkNDg1YjE2NyIsImNyZWF0ZWQiOjE2OTI4NzUxMzcyMzAsImluU2FtcGxlIjpmYWxzZX0=', '_ga_GSD4ETCY1D': 'GS1.1.1692875137.5.1.1692875158.39.0.0', '_ga': 'GA1.1.300752126.1691425328', 'cto_bundle': 'SAER_l9jTVJXeW5EN2Z6alp3Q1JQSFRHazF4MkRCVHBqYzdPY2lURFJIeTNqb2QydFRSUW5lOHYlMkJ6NTRhUGpLMmZ2OEJYZmh0UzdyblFuUGZxNlZqY0lscTBrR2dLa1Z2MXpRRlZHRU9ubTJQazlMYWFTakNvSWs2MDFmU3EwV0xFbW5VU2x5bmw0WWFpUjNrYUduOUtxRzdlJTJCWnZGajNBNkRJd2RwQW5HaXV3QUU4TlRVZVRmRXdGd1RtQ0VPR1I1cDVLVllGd2liY2hjZk1YdDRQMHFHRyUyQjFRcEJETzVGTm5z'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Referer': 'https://tiki.vn/dien-thoai-samsung-galaxy-a34-5g-8gb-128gb-hang-chinh-hang-p247730209.html?src=category-page-1789&2hi=0',
    'x-guest-token': 'yBiwS9hoNQUL2E8rDz6nGHMqCkdAFsVT',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}


params = (
    ('platform', 'web'),
    ('spid', 247730217)
    # ('include', 'tag,images,gallery,promotions,badges,stock_item,variants,product_links,discount_tag,ranks,breadcrumbs,top_features,cta_desktop'),
)


def safe_encode(text, first_encoding="utf-8", fallback_encoding="latin-1", error_char="?"):
    try:
        return text.encode(first_encoding).decode(first_encoding)
    except UnicodeEncodeError as e:
        safe_text = text[:e.start] + error_char + text[e.end:]
        return safe_encode(safe_text, first_encoding, fallback_encoding, error_char)


def parser_product(json):
    d = dict()
    d['id'] = json.get('id')
    d['sku'] = json.get('sku')
    d['brand_name'] = json.get('brand_name')
    d['name'] = json.get('name')
    d['thumbnail_url'] = json.get('thumbnail_url')
    d['discount'] = json.get('discount')
    d['price'] = json.get('price')
    d['original_price'] = json.get('original_price')
    return d


df_id = pd.read_csv('product_id_tiki.csv')
p_ids = df_id.id.to_list()
print(p_ids)
result = []
for pid in tqdm(p_ids, total=len(p_ids)):
    try:
        response = requests.get('https://tiki.vn/api/v2/products/{}'.format(pid),
                                headers=headers, params=params, cookies=cookies)
        if response.status_code == 200:
            print('Crawl data {} success !!!'.format(pid))
            result.append(parser_product(response.json()))
        # Chúng ta sẽ di chuyển đoạn lưu CSV ra ngoài vòng lặp
    except Exception as e:
        print(f"Error when processing product ID {pid}. Error message: {e}")
    time.sleep(random.uniform(1, 3))

# Lưu dữ liệu vào CSV ở ngoài vòng lặp
try:
    df_product = pd.DataFrame(result)
    df_product.to_csv('crawled_product_tiki.csv',
                      index=False, encoding='utf-8-sig')

    print("Data has been saved to 'crawled_data_ncds.csv'")
except Exception as e:
    print(f"Error when saving data to CSV. Error message: {e}")
