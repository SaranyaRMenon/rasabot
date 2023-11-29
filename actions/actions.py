# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk.events import UserUtteranceReverted
from typing import Any, Text, Dict, List, Union
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted
from rasa_sdk import Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action
import json
import os
import random
from datetime import datetime
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet


# Get the user's name.
class AskForName(Action):
    def name(self) -> Text:
        return "action_ask_userdetailsform_name"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[EventType]:
        presets = [
            "Could you please tell me your name to get started?",
            "Can you please tell me your name?",
            "May I know your name, please?",
            "Can you please tell me your good name?",
            "What name can I address you with?",
            "Could you please tell your name?"
        ]
        name_q = random.choice(presets)
        dispatcher.utter_message(text=name_q)
        return []

    def validate_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        if not value:
            dispatcher.utter_message(
                text="Sorry, without your name, I cannot proceed further."
            )
            # Set the slot to None to ask for the name again
            return [SlotSet("name", None)]
        else:
            return [SlotSet("name", value)]

# Get the user's email address.
# class AskForEmail(Action):
#     def name(self) -> Text:
#         return "action_ask_userdetailsform_email"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
#     ) -> List[EventType]:
#         name = tracker.get_slot("name")
#         presets = [
#             f"It's a pleasure to meet you, {name}. Please enter your email address.",
#             f"Nice to see you, {name}. Please provide your email address."
#         ]
#         mail_q = random.choice(presets)
#         dispatcher.utter_message(text=mail_q)
#         return []




class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        requested_slot = tracker.get_slot("requested_slot")
        if requested_slot:
            # A slot is being requested
            dispatcher.utter_message(text=f"I didn't quite understand that. Please provide your {requested_slot}.")
            return [UserUtteranceReverted(),SlotSet("requested_slot", requested_slot)]
        else:
            dispatcher.utter_message(text=f"I didn't quite understand that")
        return []
        # Revert user message which led to fallback.
       
    

class ActionUtterRephrase(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_utter_please_rephrase"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        requested_slot = tracker.get_slot("requested_slot")
        if requested_slot:
            # A slot is being requested
            dispatcher.utter_message(text=f"I'm sorry, I didn't quite understand that. Please provide your {requested_slot}.")
            return [UserUtteranceReverted(),SlotSet("requested_slot", requested_slot)]
        else:
            dispatcher.utter_message(text=f"I didn't quite understand that")
        return []
        # Revert user message which led to fallback.
        


