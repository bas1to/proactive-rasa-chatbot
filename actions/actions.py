# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


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

class ActionSayName(Action):

  def name(self) -> Text:
    return "action_say_name"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    name = tracker.get_slot("name")
    if not name:
      dispatcher.utter_message(text="I don't know your name.")
    else:
      dispatcher.utter_message(text=f"Your name is {name}.")
    return []

class ActionPracticeSOP(Action):

  def name(self) -> Text:
    return "action_check_reaction"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    name = tracker.get_slot("reaction")
    if not name:
      dispatcher.utter_message(text="You forgot to check if the person is showing no reaction and has no normal breathing.")
    else:
      dispatcher.utter_message(text="What do you do now?")
    return[]
