from datetime import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List
import queue

class NotificationType(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass
class Notification:
    content: str
    type: NotificationType
    priority: Priority
    timestamp: datetime
    is_read: bool = False
1
class NotificationSystem:
    def __init__(self, low_priority_limit: int = 5):
        self.notifications = []
        self.low_priority_limit = low_priority_limit
        self.unread_count = 0

    def add_notification(self, content: str, type: NotificationType, priority: Priority):
        notification = Notification(
            content=content,
            type=type,
            priority=priority,
            timestamp=datetime.now()
        )
        
        if priority == Priority.HIGH:
            self.notifications.insert(0, notification)
        else:
            insert_index = 0
            for i, n in enumerate(self.notifications):
                if n.priority.value <= priority.value:
                    insert_index = i
                    break
                insert_index = i + 1
            self.notifications.insert(insert_index, notification)

        self.unread_count += 1

        low_priority_count = sum(1 for n in self.notifications 
                               if n.priority == Priority.LOW)
        if low_priority_count > self.low_priority_limit:
            for i, notification in enumerate(reversed(self.notifications)):
                if notification.priority == Priority.LOW:
                    del self.notifications[-(i+1)]
                    if not notification.is_read:
                        self.unread_count -= 1
                    break

    def get_next_notification(self) -> Notification:
        for notification in self.notifications:
            if not notification.is_read:
                notification.is_read = True
                self.unread_count -= 1
                return notification
        return None

    def get_all_notifications(self) -> List[Notification]:
        return self.notifications

    def get_unread_count(self) -> int:
        return self.unread_count

def main():
    notification_system = NotificationSystem(low_priority_limit=5)

    while True:
        print("\nSystem Powiadomień")
        print(f"Nieprzeczytane powiadomienia: {notification_system.get_unread_count()}")
        print("\nWybierz opcję:")
        print("1. Dodaj powiadomienie")
        print("2. Wyświetl następne powiadomienie")
        print("3. Wyświetl wszystkie powiadomienia")
        print("4. Wyjście")

        choice = input("\nWybór: ")

        if choice == "1":
            content = input("Treść powiadomienia: ")
            print("\nTyp powiadomienia:")
            print("1. Info")
            print("2. Warning")
            print("3. Error")
            type_choice = input("Wybór: ")
            type_map = {"1": NotificationType.INFO, 
                       "2": NotificationType.WARNING, 
                       "3": NotificationType.ERROR}
            
            print("\nPriorytet:")
            print("1. Niski")
            print("2. Średni")
            print("3. Wysoki")
            priority_choice = input("Wybór: ")
            priority_map = {"1": Priority.LOW, 
                          "2": Priority.MEDIUM, 
                          "3": Priority.HIGH}

            notification_system.add_notification(
                content,
                type_map.get(type_choice, NotificationType.INFO),
                priority_map.get(priority_choice, Priority.LOW)
            )

        elif choice == "2":
            notification = notification_system.get_next_notification()
            if notification:
                print("\nPowiadomienie:")
                print(f"Treść: {notification.content}")
                print(f"Typ: {notification.type.value}")
                print(f"Priorytet: {notification.priority.name}")
                print(f"Czas: {notification.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print("\nBrak nieprzeczytanych powiadomień!")

        elif choice == "3":
            notifications = notification_system.get_all_notifications()
            if notifications:
                print("\nWszystkie powiadomienia:")
                for i, notif in enumerate(notifications, 1):
                    print(f"\n{i}. {notif.content}")
                    print(f"   Typ: {notif.type.value}")
                    print(f"   Priorytet: {notif.priority.name}")
                    print(f"   Czas: {notif.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
                    print(f"   Status: {'Przeczytane' if notif.is_read else 'Nieprzeczytane'}")
            else:
                print("\nBrak powiadomień!")

        elif choice == "4":
            break

if __name__ == "__main__":
    main()