print("Привет, как дела")
answer = input()
if (("хорош" in answer or "прекрасн" in answer or "отличн" in answer) and
        ("плох" not in answer or "ужасно" not in answer)):
    print("Отлично, у меня тоже")
elif ("плох" in answer or "ужасн" in answer and
        ("хорош" not in answer or "прекрасн" not in answer or "отличн" not in answer)):
    print("Похоже вы не в настроение общаться")
else:
    print("Извините, но я вас не понимаю")
