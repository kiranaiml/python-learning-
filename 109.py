#The Open/Closed Principle (OCP).
#Q1.
from abc import ABC, abstractmethod
class NotificationHandler(ABC):
    @abstractmethod
    def notify(self, message_text):
        pass
class JobOfferHandler(NotificationHandler):
    def notify(self, message_text):
        print(f"📱 TEXTING URGENTLY: {message_text}")

class GeneralQuestionHandler(NotificationHandler):
    def notify(self, message_text):
        print(f"📧 Emailing message: {message_text}")

class SpamHandler(NotificationHandler):
    def notify(self, message_text):
        print("🗑️ Deleting spam message silently.")
class ContactFormRouter:
    def send_notification(self, handler, message_text):
        handler.notify(message_text)
if __name__ == "__main__":
    router = ContactFormRouter()
    job_worker = JobOfferHandler()
    spam_worker = SpamHandler()
    
    print("--- Processing Portfolio Messages ---")
    
    router.send_notification(job_worker, "We want to hire you as a Senior Backend Dev!")
    router.send_notification(spam_worker, "Buy cheap sunglasses now!")