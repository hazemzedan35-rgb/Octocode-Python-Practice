class Message:
    def __init__(self, sender, receiver, content, date):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.date = date


def main():
    message_info = get_message()
    print(f'the sender is {message_info.sender} and the receiver is {message_info.receiver}')
    print(f"the content '{message_info.content}'")
    print(f'date of the message is {message_info.date}')


def get_message():
    sender = input("sender: ")
    receiver = input("receiver: ")
    content = input("content: ")
    date = input("date: ")
    message = Message(sender, receiver, content, date)

    return message


if __name__=="__main__":
    main()
    