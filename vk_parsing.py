import csv

import requests


def take_posts(x):
    token = '2220a50a2220a50a2220a50ace224f8c02222202220a50a7c013f2fde27dfef5d076e67'
    version = 5.103
    domain = 'fit4life_official'
    count = 100
    offset = 0
    all_posts = []
    while offset < x:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset,
                                }
                                )
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def file_writer(data):
    with open('fit4life.csv', 'w') as f:
        a_pen = csv.writer(f)
        print("Количество словарей ", len(data))
        for p in data:
            print(type(p))
            print("Количество ключей в словаре ", len(p))
            print('Ключи: ', p.keys())
            print('-' * 30)
            for i in p.keys():
                print("{0} => {1}".format(i, p[i]))
            print(p)                # строка словарей   {
                                    # 'id': 1221903, 'from_id': -8204282, 'owner_id': -8204282, 'date': 1525705209, 'marked_as_ads': 0, 'post_type': 'post', 'text': 'А ЧТО Я ОДИН МОГУ СДЕЛАТЬ?',
                                    # 'attachments': [
                                    #                    {'type': 'photo', 'photo': {'id': 456243727, 'album_id': -7, 'owner_id': -8204282, 'user_id': 100,
                                    #                    'sizes': [  {'type': 'm', 'url': 'https://sun9-63.userapi.com/c824504/v824504554/12f945/HiV5HOa0WE0.jpg', 'width': 130, 'height': 98},
                                    #                                {'type': 'o', 'url': 'https://sun9-52.userapi.com/c824504/v824504554/12f947/AQMZDmTj920.jpg', 'width': 130, 'height': 98},
                                    #                                {'type': 'x', 'url': 'https://sun9-26.userapi.com/c824504/v824504554/12f946/yAN66foMF8Q.jpg', 'width': 604, 'height': 456}  ],
                                    # 'text': '', 'date': 1525665716, 'post_id': 1221903, 'access_key': '31f5965518d6df96ef'} } ],
                                    # 'post_source': {'type': 'vk'}, 'comments': {'count': 0, 'can_post': 1, 'groups_can_post': True},
                                    # 'likes': {'count': 49, 'user_likes': 0, 'can_like': 1, 'can_publish': 1}, 'reposts': {'count': 7, 'user_reposted': 0}, 'views': {'count': 5072}
                                    # }
            try:
                if p['attachments'][0]['type']:
                    img_url = p['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass
            print('-' * 14)
            a_pen.writerow(("Likes - ", p['likes']['count'], " url of img -> ",img_url))
            # a_pen.writerow((p.get('likes', 0).get('count', 0), img_url))


all_posts = take_posts(100)         # массив(список) словарей
file_writer(all_posts)
print(1)
