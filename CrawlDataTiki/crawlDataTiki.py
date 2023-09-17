import pandas as pd
import requests
import time
import random
from tqdm import tqdm
import json

cookies = {
    "_trackity": "b2ee50bb-3965-dd80-67b4-3f6b84ae3737",
    "delivery_zone": "Vk4wMzkwMDYwMDE=",
    "tiki_client_id": "300752126.1691425328",
    "_gcl_au": "1.1.1423128732.1691425335",
    "__iid": "749",
    "__su": "0",
    "_hjSessionUser_522327": "eyJpZCI6IjZmYzRjZjE5LTRmNDktNTQxZC1iNzE0LWU4ODc4M2JmODM0NyIsImNyZWF0ZWQiOjE2OTE0MjUzMzUzNzMsImV4aXN0aW5nIjp0cnVlfQ==",
    "G_ENABLED_IDPS": "google",
    "TIKI_ACCESS_TOKEN": "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI3ODQzMTUwIiwiaWF0IjoxNjkyODYwNTM1LCJleHAiOjE2OTI5NDY5MzUsImlzcyI6Imh0dHBzOi8vdGlraS52biIsImN1c3RvbWVyX2lkIjoiNzg0MzE1MCIsImVtYWlsIjoicXVvY2NodXl5NDI4QGdtYWlsLmNvbSIsImNsaWVudF9pZCI6InRpa2ktc3NvIiwibmFtZSI6Ijc4NDMxNTAiLCJzY29wZSI6InNzbyJ9.cXop7AQydNi1CJXlCbXO82p_XJb1w7CgpFxZFiCP34bV3O8zVhVpF3XZTwIEjO36Z_LvB3gUVSUMYE4XuNRPrcCOQtTdVpuUf1UKf6FGK1hpmU4_kP7jCxKN8B6-4T0Z1Sn0wGdWe1T2Q9vY7LFro3FbGM62F-N0xgxjC1IcB1bkil-NNxKfWAx0SP4QmvAoe2wdxznTZcyjxl8FDD2_xz9CePT0I5EXcAcZcWX8r4BDbGmwnx89vVi8R43_FG8FJ9gCpwk3ZKwjSVm8BDh3cl3woEVSUgaFf1RqCGpIve6IVXDqd-saz5YOtP3OVXLwCU_qOIKvuFXp_UpgVSDXXmccOxzhJ1Q0_cRPyPnKWgENaeUMkm0uPMry2QGAnsHw92HRQ8pMMo74qRDU98mCiUDRaFY0j_ZUPHO-Ead0f_m1f7J0cF2LGjU4zHR8wu6_03PHWoGhx2EsKpH38Pq0raItYkV1DdAjMUDxdWe7V20_ZWu1ekC7MA82y6Fb1gjEaqrH51i7FoJG3Dj8VxxCKo2vw7zV4Ys475ADiOZ6BkOFRgvqNNwSKN-nGBD4H0ZwZN8yZnYiEWNFIZOmuLdBJkV-jodHmX71r0SvPm5NdrqiHLwwlfdpvP4DXDmS22ol8KJPwcv-zEQa3AMFFELhGmaNKyCB_K-Gg28ThFx1rLQ",
    "TIKI_USER": "6ya%2FQq9rvDjeibm9k%2BugMP%2B8eFnwhNwXIkCPJ3b0liKRuwCQVUyGVx8eOsWYqUIYpFasXqoJ7fg%3D",
    "bnpl_whitelist_info": "{\"content\":\"Mua trước trả sau\",\"is_enabled\":true,\"icon\":\"https://salt.tikicdn.com/ts/tmp/95/15/2d/4b3d64b220f55f42885c86ac439d6d62.png\",\"deep_link\":\"https://tiki.vn/mua-truoc-tra-sau/dang-ky?src=account_page\"}",
    "_gid": "GA1.2.1796508843.1692860538",
    "TOKENS": "{\"access_token\":\"yBiwS9hoNQUL2E8rDz6nGHMqCkdAFsVT\",\"expires_in\":157680000,\"expires_at\":1850541747826,\"guest_token\":\"yBiwS9hoNQUL2E8rDz6nGHMqCkdAFsVT\"}",
    "_tuid": "7843150",
    "_hjSession_522327": "eyJpZCI6IjU4YTlmOTczLTBjODItNDQ3Yy1iMjQ4LWY4YTM0MjM4ODM4OCIsImNyZWF0ZWQiOjE2OTI5MzAxMTk2NjQsImluU2FtcGxlIjpmYWxzZX0=",
    "cto_bundle": "xjGzcV9jTVJXeW5EN2Z6alp3Q1JQSFRHazElMkZKS1pFdUdZdkpPNlhzN3N1MDcxaGpzQ1MzMko4JTJGdXpPUkxrN2xFdEVFeHJNMUREMVJFekMlMkZOZFhuV2tPWlRhSnBEdlBLM3clMkJ0NzdZVUFHcXJYUDNJOElRVGglMkZId1VsRjQ1NUVBJTJCUzJua09jR0JpbElndzFhTzhWSUJLJTJGcll6M0ZiRGhHSlNOR1JyekN2SU1Bc1dqVmpEcVc=",
    "_ga": "GA1.2.300752126.1691425328",
    "temp_client_id": "b2ee50bb-3965-dd80-67b4-3f6b84ae3737",
    "session_id": "7843150",
    "ascend_id": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRfaWQiOiIzMDA3NTIxMjYiLCJzZXNzaW9uX2lkIjoiNzg0MzE1MCIsIm5vbmNlIjoiYjJlZTUwYmItMzk2NS1kZDgwLTY3YjQtM2Y2Yjg0YWUzNzM3IiwiZXhwaXJlc19hdCI6IjE2OTMwMjEyMjUifQ.uy6ADzCWQAV7df6KiAfwPqGXNO-jVZAXjpp-bv7v0x0",
    "__cf_bm": "4c12f4ea3cf370d00e5a80cf4b067a2d56c5a4bb-1692930118-1800-AS+8vKMCzG4e2JohXxPI6+F02jHOCim1R6enl7rjXGjUo//gBQmLB0+7VW7Ip+2Ppe7ZbFBs/Z04OKFYJxZkX40=",
    "__cfduid": "d9f021bc5294ebf65a87fa9d5b9e0b3b21692930115",
    "device_id": "be12ef67-82df-415f-906f-4c9c12ab4910",
    "ascend": "token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRfaWQiOiIzMDA3NTIxMjYiLCJzZXNzaW9uX2lkIjoiNzg0MzE1MCIsIm5vbmNlIjoiYjJlZTUwYmItMzk2NS1kZDgwLTY3YjQtM2Y2Yjg0YWUzNzM3IiwiZXhwaXJlc19hdCI6IjE2OTMwMjEyMjUifQ.uy6ADzCWQAV7df6KiAfwPqGXNO-jVZAXjpp-bv7v0x0",
    "_hjFirstSeen": "1",
    "_gat_UA-52965901-5": "1",
    "_dc_gtm_UA-52965901-5": "1"
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Referer': 'https://tiki.vn/dien-thoai-oppo-a57-4gb-128gb-hang-chinh-hang-p205750556.html?src=category-page-1789&2hi=0',
    'x-guest-token': 'yBiwS9hoNQUL2E8rDz6nGHMqCkdAFsVT',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}


params = {
    'limit': '40',
    'include': 'advertisement',
    'aggregations': '2',
    'version': 'home-persionalized',
    'trackity_id': 'b2ee50bb-3965-dd80-67b4-3f6b84ae3737',
    'category': '1789',
    'page': '1',
    'urlKey': 'dien-thoai-may-tinh-bang'
}

products = []
for i in range(1, 28):
    params['page'] = i  # type: ignore
    response = requests.get('https://tiki.vn/api/personalish/v1/blocks/listings',
                            headers=headers, params=params)
    if response.status_code == 200:
        print('request success!!!')
        for record in response.json().get('data'):
            product_data = {
                'id': record.get('id'),
                'name': record.get('name'),
                'brand_name': record.get('brand_name'),
                'original_price': record.get('original_price'),
                'price': record.get('price'),
                'discount': record.get('discount_rate'),
                'thumbnail_url': record.get('thumbnail_url'),
                'quantity_sold': record.get('quantity_sold')
            }
            products.append(product_data)

        # Lưu sau mỗi lần gửi yêu cầu thành công
        with open('products_tiki.json', 'w', encoding='utf-8') as f:
            json.dump(products, f, ensure_ascii=False, indent=4)
    time.sleep(random.randrange(1, 3))
