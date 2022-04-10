import vk_api
import requests
import json
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload

vk_session = vk_api.VkApi(token='5e8e29ab0f34b3a2fb1d542dbd70ac31b6aef1b65d9f6fbc1330e9e79ffd57ffcd1facc2e9cf9bdd73004')
upload = VkUpload(vk_session)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'Привет':
            if event.from_user:
                # photo = upload.photo_messages("1.jpg")
                # attachment = 'photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Привет вездекодерам!'
                )
        elif event.text == 'Важный тест':
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Это психологичесий тест, который определит твой тип личности. Начнем с простого, '
                            'как настроение?',
                    keyboard=open("keyboards/questions/0.json", "r", encoding="UTF-8").read()
                )
            question = 1
            with open("question.json", encoding='utf-8') as read_file:
                question_titles = json.load(read_file)
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.from_user:
                        if question == 8:
                            vk.messages.send(
                                user_id=event.user_id,
                                random_id=get_random_id(),
                                message='Хахахаха а результат не скажу хахахах',
                                keyboard=open("keyboards/default.json", "r", encoding="UTF-8").read()
                            )
                            break
                        vk.messages.send(
                            user_id=event.user_id,
                            random_id=get_random_id(),
                            message=question_titles["{}".format(question)],
                            keyboard=open("keyboards/questions/{}.json".format(question), "r", encoding="UTF-8").read()
                        )
                        question = question + 1

        else:
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Выбирай',
                    keyboard=open("keyboards/default.json", "r", encoding="UTF-8").read()
                )